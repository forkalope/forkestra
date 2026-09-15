# Forkalope Containerlab labs

This directory contains disposable three-node Forge labs. A single lab is one
autonomous Forkalope franchise: its own VM, Docker daemon, cluster identity,
node inventory, and local membership view. The two-franchise exercise uses
`forkalope-3.clab.yml` for Franchise 1 and
`forkalope-3-franchise-2.clab.yml` for Franchise 2.

Containerlab runs inside Linux because it needs Linux networking primitives
such as network namespaces, veth links, and netlink. On macOS, the supported
shape is one ARM64 Linux VM with Docker and Containerlab inside it.

## Prerequisites

The first lab host is the Ubuntu VM named `ubuntu` in OrbStack. The second
franchise uses `ubuntu-franchise-2`. Containerlab and Docker must be installed
inside each VM, and the repository must be somewhere under `/Users` so
OrbStack exposes the same path to both VMs.

The lab commands below intentionally use `-u root`. Containerlab creates
privileged links and namespaces, so this avoids hiding a Docker-group or
sudoers requirement while the lab is still being developed. The lab is
disposable; do not use this topology as a security boundary for untrusted
students.

## Automated bootstrap

From the `forkestra` repository root, run:

```bash
bash scripts/bootstrap-macos.sh
```

The bootstrap pauses before creating or preparing the VM. Approve each step;
use `--yes` only for a reviewed unattended run.

The script is safe to re-run. It creates the `ubuntu` VM only when it is
missing, starts it when stopped, installs the VM-local prerequisites at pinned
versions, checks Docker, and verifies that this repository is visible inside
the VM. It does not deploy or destroy a lab.

The defaults can be changed explicitly for another machine:

```bash
FORKALOPE_VM_NAME=ubuntu \
FORKALOPE_UBUNTU_VERSION=24.04 \
FORKALOPE_CONTAINERLAB_VERSION=0.79.0 \
  bash scripts/bootstrap-macos.sh
```

Prepare both franchise VMs with:

```bash
bash scripts/bootstrap-federation.sh
```

## Fresh Mac setup

Install [OrbStack](https://orbstack.dev/) first. Then run these commands from
the repository root. The Ubuntu 24.04 VM is the conservative reproducible
baseline; the current development VM is Ubuntu 26.04.1 ARM64 and also works.

```bash
orbctl create -a arm64 ubuntu:24.04 ubuntu
orbctl start ubuntu

orb -m ubuntu -u root sh -lc \
  'apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y docker.io curl ca-certificates'
orb -m ubuntu -u root systemctl enable --now docker

# Pin this while reproducing the lab. Change deliberately when upgrading.
orb -m ubuntu -u root sh -lc \
  'bash -c "$(curl -fsSL https://get.containerlab.dev)" -- -v 0.79.0'
```

If the VM already exists, use `orbctl list` and `orbctl start ubuntu`, then
skip the `create` command. Verify the VM-local tools before deploying:

```bash
orb -m ubuntu -u root sh -lc \
  'docker info --format "{{.ServerVersion}} {{.Architecture}}" && containerlab version'
```

The macOS `docker` command and the VM-local `docker` command can refer to
different daemons. Use the `orb -m ubuntu ...` form for this lab.

## Deploy

Build the Forge image and deploy Franchise 1:

```bash
bash scripts/deploy-lab.sh
```

To practice the first-run wizard before launching the full three-node lab:

```bash
bash scripts/deploy-lab.sh --bootstrap-only
```

This publishes one node at `http://localhost:8080/forklift`. After reviewing
the wizard, run the normal deployment command to replace it with the full
three-node topology.

Deployment also pauses before building and replacing the disposable lab. The
Forklift Networking page is the live operator checkpoint: while fewer than
three nodes are present it shows a setup wizard, then it settles into the node
inventory once the lab is complete.

Deploy both isolated franchise labs:

```bash
bash scripts/deploy-lab.sh --all --reconfigure
```

Franchise 1 is served at `http://localhost:8080/forklift`; Franchise 2 is
served at `http://localhost:8180/forklift`. Their Docker networks, cluster IDs,
node IDs, and VM-local Docker daemons are distinct. Use the Networking view in
each Forklift to run the explicit two-sided federation contract. Networking
does not become active merely because both labs are running:

1. In Franchise 1, click **Send proposal**.
2. In Franchise 2, verify the peer fingerprint and click **Approve proposal**.
3. In Franchise 1, click **Approve proposal**; its probe runs after the peer
   approval arrives.
4. In Franchise 2, click **Probe gateway** and confirm every checklist step is
   complete.

If the disposable lab is already running and the image or topology changed:

```bash
bash scripts/deploy-lab.sh --reconfigure
```

Then open [http://localhost:8080/forklift](http://localhost:8080/forklift).
The page is served from `node-001`, not from a separate frontend process.

Set the topology path for the remaining direct Containerlab commands:

```bash
REPO_ROOT="$(pwd)"
TOPOLOGY="$REPO_ROOT/labs/containerlab/forkalope-3.clab.yml"
```

Inspect the lab:

```bash
orb -m ubuntu -u root containerlab inspect -t "$TOPOLOGY"
```

Check the interfaces and peer-to-peer links:

```bash
orb -m ubuntu -u root containerlab exec -t "$TOPOLOGY" --cmd 'ip addr show'

orb -m ubuntu -u root docker exec clab-forkalope-3-node-001 \
  ping -c 3 -W 1 10.240.0.2
orb -m ubuntu -u root docker exec clab-forkalope-3-node-002 \
  ping -c 3 -W 1 10.240.0.6
orb -m ubuntu -u root docker exec clab-forkalope-3-node-003 \
  ping -c 3 -W 1 10.240.0.10
```

Expected data-link addresses are:

| Link | Endpoint A | Endpoint B |
| --- | --- | --- |
| 1 | node-001 `eth1` / `10.240.0.1` | node-002 `eth1` / `10.240.0.2` |
| 2 | node-002 `eth2` / `10.240.0.5` | node-003 `eth1` / `10.240.0.6` |
| 3 | node-003 `eth2` / `10.240.0.9` | node-001 `eth2` / `10.240.0.10` |

## Troubleshooting

Check the VM, Docker daemon, and lab containers independently:

```bash
orbctl list
orb -m ubuntu -u root systemctl status docker --no-pager
orb -m ubuntu -u root docker ps
orb -m ubuntu -u root containerlab inspect -t "$TOPOLOGY"
```

If the VM-local Docker daemon is unavailable, start it with
`orb -m ubuntu -u root systemctl start docker`. If the topology definition
changed and the generated lab state is stale, use `--reconfigure`; it destroys
and recreates only this named lab:

```bash
orb -m ubuntu -u root containerlab deploy \
  --reconfigure -t "$TOPOLOGY"
```

Containerlab writes generated inventories and state under the corresponding
`labs/containerlab/clab-*` directory. Those directories are intentionally
ignored by Git. The topology YAML and this README are the source of truth.

Remove the disposable lab when finished:

```bash
orb -m ubuntu -u root containerlab destroy -t "$TOPOLOGY"

# For the second franchise, use its VM and topology explicitly.
orb -m ubuntu-franchise-2 -u root containerlab destroy \
  -t "$REPO_ROOT/labs/containerlab/forkalope-3-franchise-2.clab.yml"
```

## Reproducibility record

The first successful run was on 2026-09-14 with:

- Apple Silicon macOS host
- OrbStack Ubuntu `26.04.1` ARM64 VM named `ubuntu`
- Docker `29.1.3` inside the VM
- Containerlab `0.79.0`
- `forkalope/forge:lab` node image

The next networking step is to run this same membership traffic over a pinned
Nebula deployment with disposable CA/certificate generation. The current HTTP
gossip endpoint is intentionally lab-only and unauthenticated; Nebula identity
and a Forkalope enrollment policy must protect it before non-lab use.

## Bootstrap script plan

When this setup is scripted, keep the responsibilities explicit:

1. Check that the host is Apple Silicon and that OrbStack is installed.
2. Create or start the named Ubuntu VM without replacing an existing VM.
3. Check Docker and Containerlab versions inside that VM; install only when
   missing, using pinned versions.
4. Check that the repository path is visible inside the VM.
5. Run `containerlab deploy`, `inspect`, and the smoke tests for an explicit
   topology path.
6. Make cleanup accept only the known lab topology/name; never delete a broad
   directory as part of reset.

A likely future layout is:

```text
scripts/
  bootstrap-containerlab-macos.sh  # host + Ubuntu VM prerequisites
  lab-3.sh                          # deploy, inspect, test, destroy
```

Until then, this README is the manual bootstrap contract.
