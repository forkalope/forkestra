#!/usr/bin/env bash

set -Eeuo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/deploy-lab.sh [--franchise franchise-1|franchise-2|all] [--all] [--bootstrap-only] [--reconfigure] [--yes]

Build the sibling Forge repository as forkalope/forge:lab inside one or both
OrbStack Ubuntu VMs, deploy the selected three-node franchise topology, and
print the Forklift URL. Use --reconfigure to replace an already-running
disposable lab. By default, the script pauses before building and deploying;
use --yes only for an explicitly unattended run.
USAGE
}

reconfigure=false
franchise="franchise-1"
assume_yes=false
bootstrap_only=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --reconfigure) reconfigure=true ;;
    --yes) assume_yes=true ;;
    --bootstrap-only) bootstrap_only=true; franchise="franchise-1" ;;
    --all) franchise="all" ;;
    --franchise)
      [[ $# -ge 2 ]] || { usage >&2; exit 2; }
      franchise="$2"
      shift
      ;;
    -h|--help) usage; exit 0 ;;
    *) usage >&2; exit 2 ;;
  esac
  shift
done

command -v orb >/dev/null 2>&1 || { printf 'error: orb is not available\n' >&2; exit 1; }

confirm() {
  $assume_yes && return 0
  [[ -t 0 ]] || { printf 'error: interactive confirmation required; rerun with --yes\n' >&2; exit 1; }
  local answer
  read -r -p "$1 [y/N] " answer
  [[ "$answer" == "y" || "$answer" == "Y" ]]
}

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd -- "$script_dir/.." && pwd -P)"
forge_root="$(cd -- "$repo_root/../forge" && pwd -P)"

[[ -f "$forge_root/Dockerfile" ]] || { printf 'error: sibling Forge repository not found at %s\n' "$forge_root" >&2; exit 1; }

deploy_franchise() {
  local name="$1"
  local vm_name
  local topology
  local host_port
  local peer_vm_name
  local local_host
  local peer_host
  case "$name" in
    franchise-1)
      vm_name="${FORKALOPE_FRANCHISE_1_VM:-ubuntu}"
      topology="$repo_root/labs/containerlab/$([[ "$bootstrap_only" == true ]] && printf '%s' forkalope-1.clab.yml || printf '%s' forkalope-3.clab.yml)"
      host_port="8080"
      peer_vm_name="${FORKALOPE_FRANCHISE_2_VM:-ubuntu-franchise-2}"
      ;;
    franchise-2)
      vm_name="${FORKALOPE_FRANCHISE_2_VM:-ubuntu-franchise-2}"
      topology="$repo_root/labs/containerlab/forkalope-3-franchise-2.clab.yml"
      host_port="8180"
      peer_vm_name="${FORKALOPE_FRANCHISE_1_VM:-ubuntu}"
      ;;
    *)
      printf 'error: unknown franchise %s (use franchise-1, franchise-2, or all)\n' "$name" >&2
      exit 2
      ;;
  esac

  [[ -f "$topology" ]] || { printf 'error: topology not found: %s\n' "$topology" >&2; exit 1; }
  local_host="$(orbctl list 2>/dev/null | awk -v vm="$vm_name" '$1 == vm {print $NF; exit}')"
  if $bootstrap_only; then
    peer_host="127.0.0.1"
  else
    peer_host="$(orbctl list 2>/dev/null | awk -v vm="$peer_vm_name" '$1 == vm {print $NF; exit}')"
  fi
  [[ "$local_host" =~ ^[0-9a-fA-F:.]+$ ]] || { printf 'error: could not determine IP for VM %s\n' "$vm_name" >&2; exit 1; }
  [[ "$peer_host" =~ ^[0-9a-fA-F:.]+$ ]] || { printf 'error: could not determine IP for VM %s\n' "$peer_vm_name" >&2; exit 1; }
  confirm "Build and deploy $name on $vm_name?" || { printf '[lab] skipped %s\n' "$name"; return 0; }
  printf '[lab] building forkalope/forge:lab in %s\n' "$vm_name"
  orb -m "$vm_name" -u root docker build -t forkalope/forge:lab "$forge_root"

  if $bootstrap_only && $reconfigure; then
    full_topology="$repo_root/labs/containerlab/forkalope-3.clab.yml"
    printf '[lab] replacing the full lab with the one-node bootstrap\n'
    orb -m "$vm_name" -u root containerlab destroy -t "$full_topology" >/dev/null 2>&1 || true
  elif ! $bootstrap_only && $reconfigure && [[ "$name" == franchise-1 ]]; then
    bootstrap_topology="$repo_root/labs/containerlab/forkalope-1.clab.yml"
    printf '[lab] replacing the one-node bootstrap with the full lab\n'
    orb -m "$vm_name" -u root containerlab destroy -t "$bootstrap_topology" >/dev/null 2>&1 || true
  fi

  local deploy_args=(deploy -t "$topology")
  if $reconfigure; then
    deploy_args+=(--reconfigure)
  fi

  printf '[lab] deploying %s\n' "$name"
  orb -m "$vm_name" -u root env \
    "FORKALOPE_FRANCHISE_1_HOST=$([[ "$name" == franchise-1 ]] && printf '%s' "$local_host" || printf '%s' "$peer_host")" \
    "FORKALOPE_FRANCHISE_2_HOST=$([[ "$name" == franchise-2 ]] && printf '%s' "$local_host" || printf '%s' "$peer_host")" \
    containerlab "${deploy_args[@]}"
  printf 'Forklift %s: http://localhost:%s/forklift\n' "$name" "$host_port"
}

case "$franchise" in
  all)
    $bootstrap_only && { printf 'error: --bootstrap-only cannot be combined with --all\n' >&2; exit 2; }
    deploy_franchise franchise-1
    deploy_franchise franchise-2
    ;;
  franchise-1|franchise-2)
    if $bootstrap_only && [[ "$franchise" != franchise-1 ]]; then
      printf 'error: --bootstrap-only is only available for franchise-1\n' >&2
      exit 2
    fi
    deploy_franchise "$franchise"
    ;;
  *)
    printf 'error: unknown franchise %s (use franchise-1, franchise-2, or all)\n' "$franchise" >&2
    exit 2
    ;;
esac
