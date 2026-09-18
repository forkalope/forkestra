# Forkalope current state

Updated 2026-09-18.

The developer simulator uses a deterministic synthetic topology generated from
the 90-provider research catalog in `forkalope-bare-metal-research/`. The
current scenario is `forkalope-global-8134-v3-90-providers`:

- 8,134 nodes across 48 countries
- 131 metro anchors, 307 candidate facilities, 399 provider-site assignments
- 481 simulated failure domains and 517 logical pools
- 3,658 U.S. nodes across 26 U.S. metros, including Northern California and
  the Pacific Northwest
- 3,496 nodes in the modeled European region
- deterministic synthetic public-looking IPv4 and IPv6 identities for every
  node, generated from a separate stable network seed

All deployment quantities, locations, hardware assignments, telemetry, health
states and incidents remain synthetic. The provider files are researched offer
references, not reservations, verified availability or a deployment map.
Displayed addresses are simulation identifiers and are never used for real
network traffic.

Fleet rows expose and search both addresses. Selecting a node opens a dedicated
server detail screen with placement, hardware, telemetry and network identity.
From there a student can create an isolated Flight School session through the
backend HTTP API and run commands in the deterministic `ops01` shell. The UI
uses `http://localhost:8787` during local development and
`https://api.forkalope.com` elsewhere. Cross-node `ssh` resolution remains a
backend milestone; the selected machine is staged as a target but is not yet
reported as connected.

The `/` entry screen requires agreement to Forkalope's Terms of Service and
Privacy Policy before opening Flight School. That entry screen is the sole
out-of-world disclosure boundary; the `/simulator/` UI and shell output stay
fully in-world.
