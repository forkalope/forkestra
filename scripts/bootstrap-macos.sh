#!/usr/bin/env bash

set -Eeuo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/bootstrap-macos.sh

Create or start the OrbStack Ubuntu VM used by the Forkalope Containerlab
experiments, install the VM-local Docker and Containerlab prerequisites, and
verify that this repository is visible inside the VM.

Environment overrides:
  FORKALOPE_VM_NAME             OrbStack machine name (default: ubuntu)
  FORKALOPE_UBUNTU_VERSION      Ubuntu version (default: 24.04)
  FORKALOPE_CONTAINERLAB_VERSION Containerlab version (default: 0.79.0)

The script does not deploy or destroy a lab.
USAGE
}

log() {
  printf '[bootstrap] %s\n' "$*"
}

die() {
  printf '[bootstrap] error: %s\n' "$*" >&2
  exit 1
}

if [[ $# -gt 0 ]]; then
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      exit 2
      ;;
  esac
fi

case "$(uname -s)" in
  Darwin) ;;
  *) die "this bootstrap script must run on macOS" ;;
esac

case "$(uname -m)" in
  arm64|aarch64) ;;
  *) die "this lab currently requires an Apple Silicon host" ;;
esac

command -v orb >/dev/null 2>&1 || die "OrbStack is not installed or orb is not on PATH"
command -v orbctl >/dev/null 2>&1 || die "OrbStack is not installed or orbctl is not on PATH"

vm_name="${FORKALOPE_VM_NAME:-ubuntu}"
ubuntu_version="${FORKALOPE_UBUNTU_VERSION:-24.04}"
containerlab_version="${FORKALOPE_CONTAINERLAB_VERSION:-0.79.0}"

[[ "$vm_name" != */* ]] || die "FORKALOPE_VM_NAME must be a simple machine name"
[[ "$ubuntu_version" =~ ^[0-9]+\.[0-9]+$ ]] || \
  die "FORKALOPE_UBUNTU_VERSION must look like 24.04"
[[ "$containerlab_version" =~ ^0\.[0-9]+\.[0-9]+$ ]] || \
  die "FORKALOPE_CONTAINERLAB_VERSION must look like 0.79.0"

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd -- "$script_dir/.." && pwd -P)"
topology="$repo_root/labs/containerlab/forkalope-3.clab.yml"

case "$repo_root" in
  /Users/*) ;;
  *)
    die "repository must be under /Users so OrbStack can share it with the VM: $repo_root"
    ;;
esac

[[ -f "$topology" ]] || die "topology not found: $topology"

if orbctl list -q | grep -Fxq -- "$vm_name"; then
  log "using existing OrbStack VM: $vm_name"
else
  log "creating OrbStack VM: $vm_name (Ubuntu $ubuntu_version, ARM64)"
  orbctl create -a arm64 "ubuntu:$ubuntu_version" "$vm_name"
fi

log "starting OrbStack VM: $vm_name"
orbctl start "$vm_name"

log "waiting for the VM to accept commands"
vm_ready=false
for _ in $(seq 1 30); do
  if orb -m "$vm_name" -u root true >/dev/null 2>&1; then
    vm_ready=true
    break
  fi
  sleep 1
done
$vm_ready || die "OrbStack VM did not become ready: $vm_name"

remote_prepare='set -eu
export DEBIAN_FRONTEND=noninteractive

policy_file=/usr/sbin/policy-rc.d
policy_created=false
cleanup_policy() {
  if [ "$policy_created" = true ]; then
    rm -f "$policy_file"
  fi
}
trap cleanup_policy EXIT HUP INT TERM

if ! command -v docker >/dev/null 2>&1 || ! command -v curl >/dev/null 2>&1 ||
   ! dpkg-query -W -f="\${Status}" ca-certificates 2>/dev/null | grep -q "install ok installed"; then
  if [ ! -e "$policy_file" ]; then
    printf "#!/bin/sh\nexit 101\n" > "$policy_file"
    chmod 755 "$policy_file"
    policy_created=true
  fi
  apt-get update
  apt-get install -y docker.io curl ca-certificates
fi

# OrbStack can leave networkd-wait-online pending while the VM is usable.
# Stop that transient wait before starting Docker, then leave its unit enabled
# for normal VM lifecycle behavior.
systemctl stop systemd-networkd-wait-online.service 2>/dev/null || true
systemctl enable docker.service
systemctl start docker.service
docker info >/dev/null

installed_version=""
if command -v containerlab >/dev/null 2>&1; then
  installed_version="$(containerlab version 2>/dev/null | awk '\''$1 == "version:" { print $2; exit }'\'')"
fi

if [ "$installed_version" != "$CONTAINERLAB_VERSION" ]; then
  bash -c "$(curl -fsSL https://get.containerlab.dev)" -- -v "$CONTAINERLAB_VERSION"
fi

test "$(containerlab version 2>/dev/null | awk '\''$1 == "version:" { print $2; exit }'\'')" = "$CONTAINERLAB_VERSION"
containerlab version >/dev/null
'

log "installing/checking Docker and Containerlab inside $vm_name"
orb -m "$vm_name" -u root env "CONTAINERLAB_VERSION=$containerlab_version" \
  sh -lc "$remote_prepare"

log "checking repository path inside $vm_name"
orb -m "$vm_name" -u root test -f "$topology" || \
  die "repository is not visible at the same path inside the VM: $topology"

log "bootstrap complete"
printf '  VM:           %s\n' "$vm_name"
printf '  Topology:     %s\n' "$topology"
printf '  Containerlab: %s\n' "$containerlab_version"
printf '\nNext: deploy the disposable lab with:\n'
printf '  orb -m %s -u root containerlab deploy -t %q\n' "$vm_name" "$topology"
