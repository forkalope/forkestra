#!/usr/bin/env bash

set -Eeuo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/deploy-lab.sh [--reconfigure]

Build the sibling Forge repository as forkalope/forge:lab inside the OrbStack
Ubuntu VM, deploy the three-node Containerlab topology, and print the Forklift
URL. Use --reconfigure to replace an already-running disposable lab.
USAGE
}

reconfigure=false
if [[ $# -gt 1 ]]; then
  usage >&2
  exit 2
fi
if [[ $# -eq 1 ]]; then
  case "$1" in
    --reconfigure) reconfigure=true ;;
    -h|--help) usage; exit 0 ;;
    *) usage >&2; exit 2 ;;
  esac
fi

command -v orb >/dev/null 2>&1 || { printf 'error: orb is not available\n' >&2; exit 1; }

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd -- "$script_dir/.." && pwd -P)"
forge_root="$(cd -- "$repo_root/../forge" && pwd -P)"
topology="$repo_root/labs/containerlab/forkalope-3.clab.yml"
vm_name="${FORKALOPE_VM_NAME:-ubuntu}"

[[ -f "$forge_root/Dockerfile" ]] || { printf 'error: sibling Forge repository not found at %s\n' "$forge_root" >&2; exit 1; }

printf '[lab] building forkalope/forge:lab\n'
orb -m "$vm_name" -u root docker build -t forkalope/forge:lab "$forge_root"

deploy_args=(deploy -t "$topology")
if $reconfigure; then
  deploy_args+=(--reconfigure)
fi

printf '[lab] deploying forkalope-3\n'
orb -m "$vm_name" -u root containerlab "${deploy_args[@]}"

printf '\nForklift is served by node-001 at http://localhost:8080/forklift\n'
