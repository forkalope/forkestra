# Forkestra

Forkestra is the synthetic infrastructure environment for Forkalope
development, integration testing, and SRE training. It owns the disposable
Containerlab/OrbStack experiments; the Forkalope product lives in the sibling
`forge` repository.

## Quick start on macOS

Prerequisites:

- Apple Silicon Mac
- [OrbStack](https://orbstack.dev/)
- this repository cloned somewhere under `/Users`

From the repository root:

```bash
bash scripts/bootstrap-macos.sh
```

The bootstrap is safe to re-run. It creates or starts the `ubuntu` ARM64 VM,
checks the VM-local Docker daemon, installs pinned Containerlab prerequisites,
and verifies the shared repository path. It does not deploy or destroy a lab.

## First lab

After bootstrapping, follow the three-node deployment and smoke-test commands
in [labs/containerlab/README.md](labs/containerlab/README.md). The topology is
[forkalope-3.clab.yml](labs/containerlab/forkalope-3.clab.yml).

The current progression is intentionally incremental:

1. Three native ARM64 Linux containers and point-to-point links.
2. Real Nebula overlay and disposable certificates.
3. Real latency/loss injection.
4. Generated multi-region topology.
5. One hundred nodes.

Generated Containerlab state stays under the lab directory and is ignored by
Git. Topology YAML, scripts, and documentation are the source of truth.

## Configuration

The bootstrap script accepts these environment overrides:

```bash
FORKALOPE_VM_NAME=ubuntu \
FORKALOPE_UBUNTU_VERSION=24.04 \
FORKALOPE_CONTAINERLAB_VERSION=0.79.0 \
  bash scripts/bootstrap-macos.sh
```

Keep version changes deliberate and update the reproducibility record in the
lab README when changing them.
