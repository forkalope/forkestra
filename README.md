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

The bootstrap is safe to re-run. It creates or starts the selected ARM64 VM,
checks that VM's Docker daemon, installs pinned Containerlab prerequisites, and
verifies the shared repository path. It does not deploy or destroy a lab.

## First lab

After bootstrapping, follow the three-node deployment and smoke-test commands
in [labs/containerlab/README.md](labs/containerlab/README.md). The topology is
[forkalope-3.clab.yml](labs/containerlab/forkalope-3.clab.yml). This is
Franchise 1: one autonomous control domain with three disposable Forge nodes.

To create the two-franchise exercise, use two independent OrbStack VMs:

```bash
bash scripts/bootstrap-federation.sh
bash scripts/deploy-lab.sh --all --reconfigure
```

Franchise 1 is served at [http://localhost:8080/forklift](http://localhost:8080/forklift)
and Franchise 2 at [http://localhost:8180/forklift](http://localhost:8180/forklift).
Each VM has its own Docker daemon and three-node Containerlab domain. The
domains are intentionally isolated until an explicit federation contract is
implemented and approved by both sides.

The authority boundary and federation exercise are described in
[`forge/docs/franchises.md`](../forge/docs/franchises.md).

The current progression is intentionally incremental:

1. One franchise: three native ARM64 Linux containers and point-to-point links.
2. Two franchises: independent VMs, control domains, and node inventories.
3. Bilateral federation contract and gateway between the franchises.
4. Real Nebula overlay and disposable certificates.
5. Real latency/loss injection and generated multi-region topology.
6. One hundred nodes across many independently operated franchises.

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

The second exercise VM uses the same bootstrap contract with a different name:

```bash
FORKALOPE_VM_NAME=ubuntu-franchise-2 \
FORKALOPE_FRANCHISE=franchise-2 \
  bash scripts/bootstrap-macos.sh
```

Keep version changes deliberate and update the reproducibility record in the
lab README when changing them.
