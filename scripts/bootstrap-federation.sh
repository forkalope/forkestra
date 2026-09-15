#!/usr/bin/env bash

set -Eeuo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
bootstrap="$script_dir/bootstrap-macos.sh"

printf '[federation] bootstrapping Franchise 1 VM: %s\n' "${FORKALOPE_FRANCHISE_1_VM:-ubuntu}"
FORKALOPE_VM_NAME="${FORKALOPE_FRANCHISE_1_VM:-ubuntu}" \
FORKALOPE_FRANCHISE=franchise-1 \
  bash "$bootstrap"

printf '\n[federation] bootstrapping Franchise 2 VM: %s\n' "${FORKALOPE_FRANCHISE_2_VM:-ubuntu-franchise-2}"
FORKALOPE_VM_NAME="${FORKALOPE_FRANCHISE_2_VM:-ubuntu-franchise-2}" \
FORKALOPE_FRANCHISE=franchise-2 \
  bash "$bootstrap"

printf '\nBoth franchise VMs are ready. Deploy their isolated labs with:\n'
printf '  bash scripts/deploy-lab.sh --all --reconfigure\n'
printf '\nFranchise 1 Forklift: http://localhost:8080/forklift\n'
printf 'Franchise 2 Forklift: http://localhost:8180/forklift\n'
