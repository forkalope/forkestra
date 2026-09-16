# Forkalope — Worldwide Bare-Metal Research & Dashboard Handoff

**Research snapshot: 2026-09-16 · 90 provider entries · original UI proposal · synthetic fleet, not live infrastructure.**

This is a curated worldwide supplier longlist, not a defensible ranking of the 90 largest or best providers. It combines global operators, regional specialists, aggregators, managed dedicated services and hyperscaler physical-host products. The catalog is broad enough to design a convincing future Forkalope network, but it is not a completed procurement spreadsheet: some providers require sales quotes or dynamic configuration before a price and an exact physical machine can be matched.

**Coverage:** 48 entries have a specified example configuration; 67 have a numeric advertised price or starting rate; 56 have numerical memory; 49 have numerical raw local storage; 30 have a numerical public-port field. These are different completeness tests. A ‘specified example’ can still lack confirmed transit terms, a facility, tax basis or live stock. There are **35 direct artwork links**, including **14 for Hetzner**, plus official discovery pages for every provider. Image URLs are supplied, not image files; rights are not assumed.

The companion fixture contains **5,000 synthetic nodes across 20 countries/territories, 22 suppliers and 23 pools**. Its quantities, roles, health and topology are invented. Hardware points back to researched offers; missing hardware fields stay unknown. A real 5,000-node purchase would require availability, legal, network, operational and commercial diligence.

## Contents

1. [How to use this handoff](#how-to-use)
2. [Dashboard direction and six screens](#dashboard)
3. [Normalization and data model](#normalization)
4. [Synthetic 5,000-node deployment](#synthetic-fleet)
5. [Provider index](#provider-index)
6. [All 90 provider cards](#provider-cards)
7. [Artwork, flags and map assets](#artwork)
8. [Procurement gaps and refresh checklist](#diligence)

<a id="how-to-use"></a>
## 1. How to use this handoff

Start the UI with the synthetic fleet, not the 90-entry supplier catalog. Join each node’s `offer_id` to `providers-and-offers.json`; join its `pool_id` to the fixture’s pools. The 90 suppliers belong in the discovery/expansion catalog. Showing thousands of active hosts from all 90 would add operational fragmentation without making the mockup more credible.

Keep three independently labeled layers: **researched offer** (what a provider advertises), **contracted asset** (what Forkalope has actually ordered and pays for), and **telemetry** (what the agent currently observes). This package has the first, and synthetic examples of the second and third. Never turn a product maximum into an installed specification or a provider’s world map into a deployed-node map.

| File | Use |
|---|---|
| `forkalope-bare-metal-worldwide.md` | This self-contained research and design specification |
| `providers-and-offers.json` | 90 nested provider/example-offer records with native units, pricing qualifiers, source URLs and asset references |
| `provider-offers.csv` | Flat comparison export; empty numeric fields mean unknown |
| `artwork-manifest.json` | Direct image URLs, classifications, retrieval status and rights notes |
| `countries-and-flags.json` | Country/territory codes, display labels, pinned flag-library paths and synthetic counts |
| `fleet-5000.synthetic.json` | Deterministic 5,000-node fixture, pools, invented telemetry and one invented correlated incident |
| `research-coverage.json` | Completeness counts and computed fixture totals |
| `build_catalog.py`, `make_deliverables.py` | Rebuild the handoff offline with Python; no provider API calls |

### Evidence labels

`specified_example` means a named offer/configuration was captured, not that every field is verified. `partial_or_quote_required` includes sales-only providers, uncaptured dynamic baskets, and known hardware with unresolved pricing. Price `kind` must remain attached to the number: family minimum, promotion, commitment equivalent, regional base and live configured price are not interchangeable. Individual notes identify contradictory or stale-looking source material. Research was read from public pages and first-party indexed snippets; there were no authenticated checkouts, purchase transactions, throughput tests or independent uptime measurements.

<a id="dashboard"></a>
## 2. Dashboard direction — “Forkalope Fabric”

**Design proposal:** make it feel like one professionally operated cloud with a visible supply chain, not a collection of unrelated hosting control panels. Use a quiet dark-navy canvas, flat surfaces, compact white typography, restrained coral selection states and status colors that are always paired with text/icons. Avoid neon globes, animated particle clouds and a full-screen tangle of arcs. Rich provider photography belongs in regional headers and expanded cards; normalized server silhouettes belong in dense inventories. These are proposed design choices, not assertions about the existing repository.

### Screen A — World overview

A 1440–1728 px desktop composition: compact left navigation, 64 px top bar, six concise aggregate tiles, then a large map beside an incident/saturation rail and a virtualized inventory table below. Top-level tiles: enrolled nodes; schedulable CPU; allocatable memory; usable storage; current external egress; recurring cost. Each tile carries coverage and freshness, not just a spectacular total. The research fixture can honestly show “known physical cores” and “raw local storage”; it cannot supply real schedulable CPU or usable replicated storage.

Map markers aggregate by country at world zoom. Their size encodes a single selected metric such as node count, and their status ring encodes the worst material state, with affected/total counts on hover. Clicking a country zooms into its available regions/pools. The map always has a table alternative. Separate toggles switch between **Physical fleet**, **Fabric connectivity**, **Workload placement**, and **Supplier footprint**; these are different layers and must not be merged. Physical underlay links are not the same as overlay reachability.

Use a persistent breadcrumb such as `World / Europe / Germany / Hetzner / AX42`. MapLibre GL JS provides a documented point-clustering pattern; use it as the initial map implementation rather than writing a globe engine. See the [official clustering example](https://maplibre.org/maplibre-gl-js/docs/examples/create-and-style-clusters/). Application state, not the map widget, should own filters and selections.

### Screen B — Country / regional operations

A country outline, small flag plus readable country name, and a short row of local metrics replace the world header. Show provider distribution, CPU-generation mix, pool health, transfer budget and workloads currently served. The inventory below groups by provider, product or role. Present smaller suppliers as real first-class infrastructure, but keep any unknown city at country level rather than creating a fake data-center pin. A country’s legal jurisdiction, cloud region name and data residency policy are distinct fields requiring separate validation.

### Screen C — Fleet inventory: table and card modes

The table is the primary operating view: node ID, health, provider, location, offer/CPU, physical cores, RAM, disks, usable storage, port, traffic allowance, current utilization, role and cost qualification. Users can pin identity and status columns, save views and compare two to four hosts. Card mode uses a consistent illustrated server form, provider name/approved logo, country label and just five or six headline facts. Full facts appear in a side panel. No retail “Buy now” controls in the operator inventory; procurement is a separate workflow.

Filters should cover country/territory, city, supplier, upstream/operator when known, CPU vendor/model/generation, physical-core count, RAM size/unit, actual ECC status, storage medium, raw/usable capacity, port rate, committed service rate, transfer model, currency, contract term, role, health, enrollment status, reimage/KVM support and evidence freshness. Include **Unknown** explicitly. Multiple selections within one facet are OR; different facets are AND. Price comparisons require a currency and comparable tax/term basis, or an explicitly dated FX conversion.

### Screen D — One machine

The side-panel header shows immutable Forkalope node ID, hostname, provider, confirmed location, health and the best available artwork. Tabs: Overview; Hardware; Storage; Network; Workloads; Events; Contract & provenance. Include BIOS/firmware, disk health and serials only when actually obtained. Artwork must state `actual model`, `provider illustration` or `generic depiction`; never suggest a stock image is a photograph of that physical unit.

Network details separate public interface, provider-private interface and Forkalope overlay. Show observed handshake freshness, direct/relayed route state, loss and latency only when collected. An overlay failure should not automatically turn hardware health red. Store actions behind RBAC: drain, cordon, restart agent, open console, reboot and reimage. Destructive actions need target-specific confirmation and audit trails; simulation actions must never reach real provider APIs.

### Screen E — Hardware / supplier comparison

Compare configurations, not brand slogans. Put price conditions directly under the price: “annual equivalent”, “setup extra”, “regional surcharge”, “quote required”, or “promotion until verified”. Keep cores and hardware threads separate; do not normalize every machine to a fictional common vCPU benchmark. The table should reveal useful contrasts: a legacy four-core Xeon, a modern desktop Ryzen, a memory-heavy dual-socket node, a storage chassis and a cloud bare-metal host with external block storage.

### Screen F — Network capacity and cost

Separate instantaneous bits per second from cumulative transferred bytes. Plot traffic budget consumed and projected exhaustion only where the billing rules and reset date are known. Unmetered machines still have finite links and policies. Costs should split base rent, setup amortization, extra disks, IPv4, licenses, managed support, transfer overage and reserved commitments. Show spending concentration by supplier, country and underlying facility, but count reseller and shared-parent risk separately where known. No global dollar total should appear until an explicit FX dataset and timestamp exist.

### Navigation, performance and honest empty states

Use level-of-detail: world aggregates → country aggregates → actual site/pool → nodes. Cluster points instead of mounting thousands of HTML markers; virtualize rows and cards; fetch thumbnail artwork only for visible items. Draw overlay edges for a selected node or aggregated region pair, not every theoretical node pair. On a 5,000-node view, a physical rack rendering is inappropriate unless actual rack assignments exist. The fixture’s pools are logical groups, not evidence of contiguous rented racks.

Recommended screenshot set: global overview; Germany/Finland supply concentration; Brazil expanded supplier card; Australia traffic-limited node detail; storage pool with the invented correlated incident; cross-provider comparison. Add a restrained “Preview / synthetic data” designation to public mockups and exported screenshots. Keep preview actions isolated from production at the backend and credential boundary. Do not publish invented provider failures as real incidents.

Unknown values render `Not established`, stale telemetry shows its age, and a failed image uses a neutral glyph rather than a broken-image box. Respect reduced motion, keyboard traversal, focus visibility, readable contrast and a non-color status representation. Empty filters must show which constraint removed the results and offer a clear reset. Never silently drop unknown rows from an “all hosts” total.

<a id="normalization"></a>
## 3. Normalization and production data model

### What the supplied JSON does—and does not—normalize

The catalog uses common field names and explicit numeric fields where the source permits them. It preserves raw vendor wording alongside each number. It does **not** silently convert vaguely labeled RAM GB to GiB, calculate a physical-core count from a cloud vCPU label, interpret a missing field as zero, or invent disk redundancy. This is intentionally safer than a deceptively complete matrix.

| Concern | Rule for Forkalope |
|---|---|
| CPU | Preserve full model, socket count when known, total physical cores, hardware threads, and separately vendor vCPU/OCPU counts. Record heterogeneous core types when relevant. |
| Memory | Preserve vendor value and unit. Explicit GiB can be multiplied by 2^30 for bytes; ambiguous GB remains vendor-GB until confirmed. Memory capacity does not establish ECC. |
| Local disks | Keep count, per-drive size, medium/interface and raw sum separately. Additional empty bays are not installed storage. |
| Usable storage | RAID 1 is approximately one mirror member’s size; RAID 10 and distributed replication need their own accounting. Filesystem overhead and reserves are additional. |
| Remote storage | External block/SAN allocation is not local raw disk capacity. Cloud-backed hosts may have no included local data disk. |
| Link speed | Store physical NIC, public port, guaranteed/committed rate and private rate separately. Two NICs do not prove a doubled Internet entitlement. |
| Traffic | Preserve allowance, period, direction, scope and policy: metered, unmetered, shared pool, 95th percentile or quote. |
| Price | Amount + ISO currency + billing period + commitment + tax basis + setup + promotion/renewal. Family minima are not configured baskets. |
| Geography | Country/territory code, city, facility, confidence/precision and supporting source. Provider HQ and generic cloud region maps are not a physical-host address. |
| Artwork | Provider logo, chassis-model photo, facility photo, generic illustration and permission status are independent metadata. |
| Health | Provider reachability, hardware health, OS-agent health, overlay health and workload health are separate signals. |
| Unknown | JSON `null`; distinguish not collected, not published, contradictory and not applicable in a production implementation. |

Arithmetic examples: 2 × 512 GB disks sum to 1,024 vendor GB raw, not 1,024 GB safely usable after mirroring. A 10 Gbps port with 20 TB/month remains a traffic-limited plan; the port is not a promise of 10 Gbps continuous free transit. An hourly rate × 730 is only a comparison convention. Native-currency subtotals remain separate. These are accounting rules, not performance guarantees.

### Recommended entities

**Provider** owns name, domains, brand assets and support/API capabilities. **Offer revision** is an immutable researched or quoted configuration with regional and price qualifications. **Offer-location availability** binds a specific revision to a real region, stock state and observation time. **Contracted node** owns the real provider instance ID, actual hardware snapshot, fixed contract details and independently verified location. **Telemetry sample** owns measurements and timestamps. **Artwork asset** owns source, permission, hash and rendering purpose. **Failure-domain relation** models shared upstream, parent, chassis, facility and network dependence without assuming different brands are independent.

The supplied `providers-and-offers.json` deliberately denormalizes one example offer into each provider entry for convenient UI ingestion. Its `offer_id` provides a stable join. Split those entities when you move to production; do not overwrite an old contracted host when the public price page changes. Keep the offer source URL, research timestamp and contracted quote artifact separately.

### Example join in plain JavaScript

```js
const [catalog, fleet] = await Promise.all([
  fetch("/fixtures/providers-and-offers.json").then(r => {
    if (!r.ok) throw new Error(`Catalog HTTP ${r.status}`);
    return r.json();
  }),
  fetch("/fixtures/fleet-5000.synthetic.json").then(r => {
    if (!r.ok) throw new Error(`Fleet HTTP ${r.status}`);
    return r.json();
  })
]);
if (fleet.metadata.synthetic !== true) throw new Error("Expected isolated fixture");
const offerById = new Map(catalog.providers.map(p => [p.offer_id, p]));
const poolById = new Map(fleet.pools.map(p => [p.id, p]));
const rows = fleet.nodes.map(node => {
  const offer = offerById.get(node.offer_id);
  const pool = poolById.get(node.pool_id);
  if (!offer || !pool) throw new Error(`Broken fixture join: ${node.id}`);
  return { ...node, offer, pool };
});
// Explicit null checks: zero is not a safe substitute for unknown.
const withKnownRam = rows.filter(r => r.offer.memory.capacity_vendor_gb !== null);
const germany = rows.filter(r => r.country_code === "DE");
// Display the pool price plus its kind; never show only an unqualified number.
```

### Aggregation rules

Totals must carry known/unknown counts. Sum raw local storage only across fields that really mean raw local storage; do not add remote volume capacity to a raw-drive headline. Do not sum private and public port rates as if they were independent external throughput. Count a pooled transfer allowance once per billing pool, not once per server. A global p95 latency cannot be obtained by averaging each node’s p95; aggregate the underlying histogram or define a different explicitly named statistic. Observed usable capacity, filesystem free bytes and scheduler allocatable resources should ultimately supersede sales-page capacities in operations.

<a id="synthetic-fleet"></a>
## 4. A plausible 5,000-node concept fleet

**All quantities and operational assignments below are synthetic design assumptions.** This is a heterogeneous fleet with large inexpensive European pools, US Git/build/storage capacity, and smaller regional pools. It is not a recommendation to use tiny legacy hosts as primary build machines or to run synchronous worldwide consensus across all regions. A substantial concentration at Hetzner is intentional for a readable scenario, not an assertion of optimal resilience. Stock, capacity reservations and policy compatibility have not been secured.

| Supplier | Country/territory | Example offer | Nodes | Proposed role |
|---|---|---|---:|---|
| [Hetzner](#provider-hetzner) | 🇩🇪 Germany | AX42 | 1,450 | build-runner |
| [Hetzner](#provider-hetzner) | 🇫🇮 Finland | AX42 | 900 | build-runner |
| [OVHcloud](#provider-ovhcloud) | 🇺🇸 United States | Eco RISE-1 (US catalog) | 400 | git-replica |
| [InterServer](#provider-interserver) | 🇺🇸 United States | Buy It Now — 2 × Xeon E5-2680 v4 8SFF, SATA storage | 250 | artifact-store |
| [ReliableSite](#provider-reliablesite) | 🇺🇸 United States | AMD Ryzen 5600X 64GB Rapid Deploy | 250 | build-runner |
| [Clouvider](#provider-clouvider) | 🇬🇧 United Kingdom | Preconfigured E3-1240 v5, London — SSD | 160 | regional-edge |
| [NFOrce](#provider-nforce) | 🇳🇱 Netherlands | HP DL320e v2 Budget 1 | 150 | cold-artifact-cache |
| [IKOULA](#provider-ikoula) | 🇫🇷 France | Regen S1 | 180 | git-replica |
| [Aruba](#provider-aruba) | 🇮🇹 Italy | AV-A205.1 | 120 | regional-edge |
| [GleSYS](#provider-glesys) | 🇸🇪 Sweden | X11-1 | 80 | git-replica |
| [LumaDock](#provider-lumadock) | 🇪🇸 Spain | BM.E1 / HPE ProLiant DL360 Gen9 | 100 | build-runner |
| [Gcore](#provider-gcore) | 🇭🇰 Hong Kong | Hong Kong Xeon E-2136 dedicated | 80 | regional-edge |
| [Exabytes](#provider-exabytes) | 🇲🇾 Malaysia | Economy Self-Managed Dedicated | 100 | regional-edge |
| [Voyager](#provider-voyager) | 🇳🇿 New Zealand | Low dedicated — 32 GB | 60 | regional-edge |
| [xneelo](#provider-xneelo) | 🇿🇦 South Africa | TruServ Plus 2336 | 80 | regional-edge |
| [IDC Frontier](#provider-idc-frontier) | 🇯🇵 Japan | Standard 2P32C256GB | 100 | memory-pool |
| [Gabia](#provider-gabia) | 🇰🇷 South Korea | One-minute rental — HP DL160 Gen10 SSD | 60 | regional-edge |
| [VinaHost](#provider-vinahost) | 🇻🇳 Vietnam | Xeon Quad Core E3 v1-2-3 Series Basic | 50 | regional-edge |
| [Turhost](#provider-turhost) | 🇹🇷 Türkiye | E65 Sunucu | 100 | regional-edge |
| [Adentro Tecnologia](#provider-adentro-tecnologia) | 🇧🇷 Brazil | Dedicado Light | 140 | git-replica |
| [Hivelocity](#provider-hivelocity) | 🇳🇱 Netherlands | Intel Xeon E-2336 | 80 | regional-edge |
| [Latitude.sh](#provider-latitude-sh) | 🇸🇬 Singapore | m4.metal.small | 60 | regional-edge |
| [RansomIT](#provider-ransomit) | 🇦🇺 Australia | ME2-E-2136-64GB-2x500GBNVME-10G | 50 | regional-edge |

**Computed fixture totals:** 5,000 nodes; 22 providers; 20 countries/territories; 23 logical pools. Known physical cores: **51,360 across 4,920 nodes**. Known memory: **310,960 vendor GB across 5,000 nodes**. Known raw local disk: **17,953,200 vendor GB across 4,900 nodes**. These are capacity sums, not equivalent compute performance or safe usable storage.

Status counts are generated deterministically rather than copied from any live provider: healthy: 4,710, degraded: 77, maintenance: 97, unreachable: 21, draining: 95. The invented incident affects 12 members of one hypothetical storage pool. Unknown timestamps and health remain unknown on unreachable hosts; no live endpoints, IP assignments or credentials are included.

### Native-currency base-rent arithmetic

The following subtotals multiply snapshot display rates by invented quantities. They deliberately mix no currencies. Tax/commitment bases still vary within currencies, and setup, staffing, egress overage, private networking, software and bulk discounts are excluded. **Do not use these as a purchase budget.** Hetzner’s indexed rate remains provisional; Hivelocity AMS1 uses 75 + 55 = USD 130; Latitude Singapore uses its separate USD 350 display rather than the global minimum.

| Currency | Modeled monthly base subtotal |
|---|---:|
| BRL | 124,600.00 |
| EUR | 260,030.10 |
| JPY | 11,500,000.00 |
| KRW | 9,000,000.00 |
| MYR | 51,590.00 |
| NZD | 21,900.00 |
| USD | 221,958.50 |
| ZAR | 159,600.00 |

### Geography and expansion

The fixture supplies approximate **country display anchors**, not facility coordinates. A country marker can support a map drill-down, but the client must never relabel it a data center. City labels appear only where the offer/site material supports them; some country pools intentionally have no city. Malaysia’s country anchor is a schematic label position, not a physical site. Geocoding verified sites is a separate task.

India, additional Latin American countries, the Middle East, more African markets and additional Asia-Pacific metros are expansion candidates in the longlist. Do not fill those gaps by assigning a provider’s cheapest global offer to every advertised location. Quote-only candidates belong in a planned-capacity layer until a physical SKU, country, price and network package are tied together.

<a id="provider-index"></a>
## 5. Provider index

Numbers identify entries; they are not rankings. `S` = specified example, `P` = partial/quote/configurator. Countries shown are the scope captured for the example or explicitly qualified footprint, not an exhaustive inventory guarantee.

| # | Provider | Example / family | Advertised price | Location codes | Evidence |
|---:|---|---|---|---|:---:|
| 1 | [Hetzner](#provider-hetzner) | AX42 | EUR 79/mo — indexed starting price unconfirmed checkout | FI, DE | S |
| 2 | [OVHcloud](#provider-ovhcloud) | Eco RISE-1 (US catalog) | USD 70/mo — advertised | US | S |
| 3 | [Leaseweb](#provider-leaseweb) | Dedicated Servers / configurable bare metal | Quote / not captured — configurator not captured | See scope / unknown | P |
| 4 | [Scaleway](#provider-scaleway) | Dedibox Core-10-XS | EUR 114.74/mo — 36 month commitment | See scope / unknown | S |
| 5 | [IONOS](#provider-ionos) | L-16 HDD | USD 47/mo — advertised | See scope / unknown | S |
| 6 | [Contabo](#provider-contabo) | AMD Ryzen 12 Cores | USD 131.75/mo — promotion terms unverified | See scope / unknown | P |
| 7 | [Worldstream](#provider-worldstream) | Dedicated Servers / Deals | Quote / not captured — configurator not captured | NL | P |
| 8 | [DataPacket](#provider-datapacket) | Berlin AMD EPYC 4245P | USD 230/mo — starting price configuration incomplete | DE | P |
| 9 | [Cherry Servers](#provider-cherry-servers) | Instant Dedicated Servers | EUR 0.084/hr — family minimum not a configured offer | See scope / unknown | P |
| 10 | [Servers.com](#provider-servers-com) | Enterprise Bare Metal | Quote / not captured — quote only | See scope / unknown | P |
| 11 | [Latitude.sh](#provider-latitude-sh) | m4.metal.small | USD 296/mo — global starting price not location quote | See scope / unknown | S |
| 12 | [Vultr](#provider-vultr) | Bare Metal | Quote / not captured — configurator not captured | See scope / unknown | P |
| 13 | [phoenixNAP](#provider-phoenixnap) | Bare Metal Cloud s0.d1.small | USD 0.08/hr — advertised | See scope / unknown | S |
| 14 | [Hivelocity](#provider-hivelocity) | Intel Xeon E-2336 | USD 75/mo — base before regional surcharge | NL | S |
| 15 | [IBM Cloud](#provider-ibm-cloud) | Bare Metal Servers — Classic / VPC | Quote / not captured — configurator not captured | See scope / unknown | P |
| 16 | [OneProvider](#provider-oneprovider) | Paris Atom C2350 dedicated | EUR 7.99/mo — promotion | FR | S |
| 17 | [Clouvider](#provider-clouvider) | Preconfigured E3-1240 v5, London — SSD | USD 74/mo — advertised configuration | GB | S |
| 18 | [RedSwitches](#provider-redswitches) | Dedicated / Bare Metal Servers | Quote / not captured — quote or configurator | See scope / unknown | P |
| 19 | [Velia](#provider-velia) | AMD Ryzen 9 7950X3D | EUR 139/mo — sale | DE, US, SG | S |
| 20 | [IP-Projects](#provider-ip-projects) | Performance Server Ryzen 5 8400F | EUR 101.46/mo — starting price with spec conflict | DE | P |
| 21 | [Avoro](#provider-avoro) | Ryzen 9000 Dedicated / Instant Dedicated | EUR 141.92/mo — family minimum not a configured offer | DE | P |
| 22 | [Keyweb](#provider-keyweb) | Keymachine KM i7 \| 32 GB | EUR 74/mo — advertised configuration | DE | S |
| 23 | [myLoc / servdiscount](#provider-myloc-servdiscount) | servdiscount dedicated inventory | Quote / not captured — configurator not captured | DE | P |
| 24 | [Fasthosts](#provider-fasthosts) | Xeon-E-32-NVMe | GBP 100/mo — discounted configuration terms unverified | GB | S |
| 25 | [UKServers](#provider-ukservers) | cPanel 270 | GBP 124/mo — starting price configuration incomplete | GB | P |
| 26 | [RapidSwitch](#provider-rapidswitch) | AMD dedicated family | GBP 47.95/mo — family minimum not a configured offer | GB, US | P |
| 27 | [Namecheap](#provider-namecheap) | Dedicated Server catalog | USD 44.88/mo — family minimum not a configured offer | US | P |
| 28 | [NovoServe](#provider-novoserve) | Dedicated / unmetered servers | Quote / not captured — quote or configurator | NL, DK, US | P |
| 29 | [NFOrce](#provider-nforce) | HP DL320e v2 Budget 1 | EUR 49.99/mo — 12 month contract | NL | S |
| 30 | [AltusHost](#provider-altushost) | Dedicated Servers | Quote / not captured — quote or configurator | See scope / unknown | P |
| 31 | [HOSTKEY](#provider-hostkey) | AMD EPYC 9354 dedicated offer | EUR 299/mo — starting price | See scope / unknown | S |
| 32 | [FDCServers](#provider-fdcservers) | Unmetered Dedicated Servers | USD 129/mo — family minimum not a configured offer | See scope / unknown | P |
| 33 | [Aruba](#provider-aruba) | AV-A205.1 | EUR 110.68/mo — advertised | IT | S |
| 34 | [IKOULA](#provider-ikoula) | Regen S1 | EUR 180/mo — advertised | FR | S |
| 35 | [Nine](#provider-nine) | Root Dedicated Server | CHF 233/mo — advertised | CH | P |
| 36 | [GleSYS](#provider-glesys) | X11-1 | EUR 265/mo — advertised | SE | S |
| 37 | [M247 Global](#provider-m247-global) | Dedicated Servers | Quote / not captured — quote only | See scope / unknown | P |
| 38 | [GTHost](#provider-gthost) | Supermicro Blade Xeon D-1531 | USD 59/mo — advertised | US | S |
| 39 | [ServerMania](#provider-servermania) | AMD EPYC 4124P entry configuration | USD 139/mo — provider guide example not checkout | See scope / unknown | S |
| 40 | [ReliableSite](#provider-reliablesite) | AMD Ryzen 5600X 64GB Rapid Deploy | USD 129/mo — advertised configuration | US | S |
| 41 | [InterServer](#provider-interserver) | Buy It Now — 2 × Xeon E5-2680 v4 8SFF, SATA storage | USD 236/mo — advertised configuration | US | S |
| 42 | [Liquid Web](#provider-liquid-web) | Managed Dedicated Servers | Quote / not captured — quote or configurator | See scope / unknown | P |
| 43 | [OpenMetal](#provider-openmetal) | Bare Metal | Quote / not captured — configurator not captured | See scope / unknown | P |
| 44 | [Wholesale Internet](#provider-wholesale-internet) | Dual Xeon E5-2660 custom dedicated | USD 64/mo — advertised | US | S |
| 45 | [Dacentec](#provider-dacentec) | Supermicro 8-bay dual E5-2650 v2 | USD 80/mo — advertised | US | S |
| 46 | [Database Mart / Server Mart](#provider-database-mart-server-mart) | Lite Dedicated SSD | USD 41/mo — recurring promotion | US | S |
| 47 | [Colocation America](#provider-colocation-america) | Intel Xeon E3-1270 v6 dedicated | USD 135/mo — advertised | US | P |
| 48 | [Tier.Net](#provider-tier-net) | Single Intel E3-1270 v6 dedicated | Quote / not captured — configurator not captured | US | P |
| 49 | [HostDime](#provider-hostdime) | Self-managed Xeon E3-1230 v5 | USD 129/mo — advertised | US, BR, MX, GB, CO, IN | S |
| 50 | [RackNerd](#provider-racknerd) | Intel Xeon E3-1230 v2 bare metal | USD 139/mo — advertised | US | S |
| 51 | [LumaDock](#provider-lumadock) | BM.E1 / HPE ProLiant DL360 Gen9 | USD 119/mo — promotion billing term needs confirmation | GB, DE, US, NL, FR, ES | S |
| 52 | [Gcore](#provider-gcore) | Hong Kong Xeon E-2136 dedicated | USD 158/mo — advertised | HK | S |
| 53 | [Zenlayer](#provider-zenlayer) | S-Series Bare Metal Cloud | USD 0.587/hr — family minimum not a configured offer | See scope / unknown | P |
| 54 | [Exabytes](#provider-exabytes) | Economy Self-Managed Dedicated | MYR 515.9/mo — advertised | MY | S |
| 55 | [IP ServerOne](#provider-ip-serverone) | Single NVIDIA RTX 4090 dedicated GPU server | MYR 2,099/mo — starting price | MY | S |
| 56 | [E2E Networks](#provider-e2e-networks) | Dedicated / Bare Metal Servers | Quote / not captured — quote only | IN | P |
| 57 | [Voyager](#provider-voyager) | Low dedicated — 32 GB | NZD 365/mo — advertised | NZ | S |
| 58 | [xneelo](#provider-xneelo) | TruServ Plus 2336 | ZAR 1,995/mo — advertised | ZA | S |
| 59 | [HOSTAFRICA](#provider-hostafrica) | Metal Core Linux 8 | USD 140.84/mo — advertised | See scope / unknown | P |
| 60 | [EdgeUno](#provider-edgeuno) | Bare Metal | USD 695/mo — family minimum not a configured offer | AR, BR, CL, CO, EC, MX, PE | P |
| 61 | [Bacloud](#provider-bacloud) | Epyc U33 customizable dedicated | EUR 187/mo — starting price configuration incomplete | LT, NL | P |
| 62 | [Arsys](#provider-arsys) | Dedicated Servers | Quote / not captured — quote or configurator | ES | P |
| 63 | [Sakura Internet](#provider-sakura-internet) | Sakura PHY dedicated servers | Quote / not captured — configurator not captured | JP | P |
| 64 | [Kagoya](#provider-kagoya) | KAGOYA FLEX Bare Metal | Quote / not captured — quote only | JP | P |
| 65 | [IDC Frontier](#provider-idc-frontier) | Standard 2P32C256GB | JPY 115,000/mo — advertised configuration | JP | S |
| 66 | [Servers Australia](#provider-servers-australia) | Value Dedicated / Enterprise HPE ProLiant DL365 Gen11 | AUD 99/mo — family minimum not a configured offer | AU | P |
| 67 | [Digital Pacific](#provider-digital-pacific) | X-C6620-2 — Dell PowerEdge C6620 node | AUD 473/mo — displayed rate billing widget discrepancy | AU | S |
| 68 | [RansomIT](#provider-ransomit) | ME2-E-2136-64GB-2x500GBNVME-10G | USD 165/mo — advertised configuration | AU | S |
| 69 | [DonWeb](#provider-donweb) | Servidores Dedicados | Quote / not captured — configurator not captured | See scope / unknown | P |
| 70 | [Afrihost](#provider-afrihost) | Bronze Self-Managed Dedicated | ZAR 1,350/mo — advertised | ZA | S |
| 71 | [Amazon Web Services](#provider-amazon-web-services) | EC2 m7i.metal-24xl | Quote / not captured — regional rate not captured | See scope / unknown | P |
| 72 | [Oracle Cloud](#provider-oracle-cloud) | BM.Standard.E5.192 | Quote / not captured — current rate not captured | See scope / unknown | P |
| 73 | [Alibaba Cloud](#provider-alibaba-cloud) | Elastic Bare Metal ecs.ebmg7.32xlarge | Quote / not captured — configurator not captured | See scope / unknown | P |
| 74 | [Tencent Cloud](#provider-tencent-cloud) | Cloud Bare Metal (CBM) | Quote / not captured — configurator not captured | See scope / unknown | P |
| 75 | [Huawei Cloud](#provider-huawei-cloud) | BMS physical.s4.xlarge (China pricing) | CNY 6,560/mo — estimated configuration | CN | P |
| 76 | [Shinjiru](#provider-shinjiru) | E3 Premium — Malaysia | USD 119.9/mo — starting price | MY | S |
| 77 | [i3D.net](#provider-i3d-net) | bm9.hmm.12 | USD 213/mo — global starting price not location quote | See scope / unknown | S |
| 78 | [Gabia](#provider-gabia) | One-minute rental — HP DL160 Gen10 SSD | KRW 150,000/mo — advertised | KR | S |
| 79 | [IDCloudHost](#provider-idcloudhost) | Bare Metal Dedicated Server | IDR 2,500,000/mo — family minimum not a configured offer | ID, SG | P |
| 80 | [VinaHost](#provider-vinahost) | Xeon Quad Core E3 v1-2-3 Series Basic | USD 94.03/mo — 36 month equivalent verify checkout | VN | S |
| 81 | [Radore](#provider-radore) | Dell R630 — 64 GB | USD 259/mo — advertised | TR | S |
| 82 | [Turhost](#provider-turhost) | E65 Sunucu | USD 219.77/mo — regular rate promotion separate | TR | S |
| 83 | [Hosterion](#provider-hosterion) | ds_IN!_v4 | EUR 229/mo — advertised | See scope / unknown | S |
| 84 | [InMotion Hosting](#provider-inmotion-hosting) | Advanced Dedicated | USD 149.99/mo — 12 month commitment | US | S |
| 85 | [DreamHost](#provider-dreamhost) | Standard Dedicated — 16 GB | USD 165/mo — annual prepaid equivalent | US | S |
| 86 | [ServerPoint](#provider-serverpoint) | Xeon E3-1275 v6 | USD 79/mo — advertised | US | S |
| 87 | [Psychz Networks](#provider-psychz-networks) | cMetal / Single CPU Xeon Dedicated | Quote / not captured — configurator not captured | US, BR, GB, NL, RU, ES, ZA, IN, SG, TW, KR, JP, AU | P |
| 88 | [Sharktech](#provider-sharktech) | Dedicated Servers | USD 219/mo — family minimum not a configured offer | See scope / unknown | P |
| 89 | [Adentro Tecnologia](#provider-adentro-tecnologia) | Dedicado Light | BRL 890/mo — advertised configuration with page discrepancy | BR | S |
| 90 | [ServerPronto](#provider-serverpronto) | Power — Xeon E3-1230 v2 | USD 59.95/mo — advertised | US | S |

Every price above must be read with its full card. Many price points are starting rates, long-term equivalents or promotions, not cancel-anytime monthly quotes.

<a id="provider-cards"></a>
## 6. All 90 provider cards

<a id="provider-hetzner"></a>
### 01. Hetzner

**Example:** AX42 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 79/month indexed starting price; dynamic checkout not captured |
| CPU | AMD Ryzen 7 PRO 8700GE; 8 cores / SMT |
| Memory | 64 GB DDR5 ECC |
| Disk / storage | 2 × 512 GB NVMe SSD |
| Network / transfer | 1 Gbps public port and guaranteed bandwidth; unlimited traffic. Optional 10 Gbps uplink has a different 20 TB outgoing allowance. |
| Physical location scope | HEL1 Helsinki, FI; FSN1 Falkenstein, DE |
| Location confidence | Named AX42 locations on product page |

**Caveats:** Do not put this physical SKU in Hetzner US/Singapore cloud regions. IPv4 can be an extra. Price is provisional, not a firm quotation.

**First-party sources:** [Source 1](https://www.hetzner.com/dedicated-rootserver/ax42/) · [Source 2](https://www.hetzner.com/dedicated-rootserver/matrix-ax/).

**Artwork:** [hetzner-logo](#asset-hetzner-logo), [hetzner-hosted-by](#asset-hetzner-hosted-by), [hetzner-fsn-exterior-1](#asset-hetzner-fsn-exterior-1), [hetzner-fsn-exterior-2](#asset-hetzner-fsn-exterior-2), [hetzner-fsn-exterior-3](#asset-hetzner-fsn-exterior-3), [hetzner-fsn-exterior-4](#asset-hetzner-fsn-exterior-4), [hetzner-fsn-flags](#asset-hetzner-fsn-flags), [hetzner-fsn-aerial](#asset-hetzner-fsn-aerial), [hetzner-fsn-aisle](#asset-hetzner-fsn-aisle), [hetzner-technical](#asset-hetzner-technical), [hetzner-trade-show](#asset-hetzner-trade-show), [hetzner-server-tray](#asset-hetzner-server-tray), [hetzner-ax-family](#asset-hetzner-ax-family), [hetzner-sx-family](#asset-hetzner-sx-family). Classifications and permissions are below.

<a id="provider-ovhcloud"></a>
### 02. OVHcloud

**Example:** Eco RISE-1 (US catalog) · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 70/month + USD 70 setup |
| CPU | Intel Xeon E-2386G; 6 cores / 12 threads |
| Memory | 32 GB base; up to 128 GB |
| Disk / storage | 2 × 512 GB NVMe base; configurable |
| Network / transfer | 1 Gbps public; 1 Gbps private. Transfer policy must be checked against selected country. |
| Physical location scope | US catalog; choose a supported US region in the regional availability matrix |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Kimsufi and So you Start/Eco are product families, not independent providers. Page may show coming-soon or limited availability. Do not apply EU/US traffic rules to APAC blindly.

**Supply-chain note:** OVHcloud / Eco / Kimsufi / So you Start. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://eco.us.ovhcloud.com/rise/) · [Source 2](https://us.ovhcloud.com/bare-metal/regions-availability/).

**Artwork discovery:** [Official product/brand page](https://eco.us.ovhcloud.com/rise/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-leaseweb"></a>
### 03. Leaseweb

**Example:** Dedicated Servers / configurable bare metal · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Configurator or sales quotation; exact basket not captured |
| CPU | Intel Xeon / AMD configurations; select exact SKU |
| Memory | Configuration dependent |
| Disk / storage | HDD, SSD and NVMe options; quote required |
| Network / transfer | High-bandwidth line: 10/25/40/100 Gbps ports; commit packages can use 95th-percentile billing. Do not treat port as free transit. |
| Physical location scope | Global dedicated-server regions; verify the chosen SKU against country selector |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** One provider with many regions. Private interconnect and Internet transit are separate products.

**First-party sources:** [Source 1](https://www.leaseweb.com/en/products-services/dedicated-servers) · [Source 2](https://www.leaseweb.com/en/products-services/dedicated-servers/high-bandwidth-server) · [Source 3](https://kb.leaseweb.com/kb/dedicated-server/dedicated-server-overview/).

**Artwork discovery:** [Official product/brand page](https://www.leaseweb.com/en/products-services/dedicated-servers). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-scaleway"></a>
### 04. Scaleway

**Example:** Dedibox Core-10-XS · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 114.74/month equivalent on 36-month commitment |
| CPU | AMD EPYC 8024P; 8 cores / 16 threads; 2.4 GHz |
| Memory | 64 GB |
| Disk / storage | 2 × 960 GB NVMe |
| Network / transfer | Product family advertises up to 25 Gbps; exact included public/private split requires configuration. |
| Physical location scope | Dedibox locations in France/Europe; select SKU location before mapping |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not mix Dedibox commitment pricing with hourly Elastic Metal. Online.net and Dedibox are not independent suppliers.

**Supply-chain note:** Scaleway / Dedibox / Online.net. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://www.scaleway.com/en/dedicated-server/dedicated-power/) · [Source 2](https://www.scaleway.com/en/pricing/dedibox/).

**Artwork discovery:** [Official product/brand page](https://www.scaleway.com/en/dedicated-server/dedicated-power/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-ionos"></a>
### 05. IONOS

**Example:** L-16 HDD · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 47/month; cancel anytime |
| CPU | Intel Xeon E3-1230 v6; 4 cores; 3.5–3.9 GHz |
| Memory | 16 GB DDR4 ECC |
| Disk / storage | 2 × 1 TB SATA HDD; software RAID 1 |
| Network / transfer | Unlimited traffic advertised; exact port/region to verify. |
| Physical location scope | Country chosen at order; do not assume every IONOS Cloud region carries this SKU |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** RAID 1 yields approximately 1 TB before filesystem overhead, not 2 TB usable. IONOS dedicated-core Cloud VMs are excluded.

**Supply-chain note:** IONOS. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://www.ionos.com/servers/cheap-dedicated-servers) · [Source 2](https://www.ionos.com/servers/dedicated-servers).

**Artwork discovery:** [Official product/brand page](https://www.ionos.com/servers/cheap-dedicated-servers). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-contabo"></a>
### 06. Contabo

**Example:** AMD Ryzen 12 Cores · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 131.75/month promotional; displayed regular USD 179 |
| CPU | AMD Ryzen 9 7900; 12 physical cores; 3.7 GHz |
| Memory | 64 GB base; up to 128 GB as an upgrade |
| Disk / storage | 1 TB NVMe base; upgrades separate |
| Network / transfer | Port, transfer/FUP and regional surcharge require exact-order confirmation. |
| Physical location scope | Dedicated-server region selector; not the same as VPS region availability |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not substitute RAM/storage figures from third-party review tables or combine this price with Genoa/Turin configurations. First-party indexed product card identifies Ryzen 9 7900, 64 GB and 1 TB NVMe; final direct fetch was HTTP 403. Revalidate the complete promotional basket.

**First-party sources:** [Source 1](https://contabo.com/en-us/dedicated-servers/) · [Source 2](https://contabo.com/).

**Artwork discovery:** [Official product/brand page](https://contabo.com/en-us/dedicated-servers/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-worldstream"></a>
### 07. Worldstream

**Example:** Dedicated Servers / Deals · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Live inventory or custom quote; exact offer price not captured |
| CPU | Intel/AMD bare-metal configurations |
| Memory | Configuration dependent |
| Disk / storage | Configuration dependent |
| Network / transfer | Port and transit commitment are configurable; capture exact traffic package. |
| Physical location scope | Netherlands dedicated facilities; exact site/SKU to confirm |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Separate Worldstream customer network/private services from Internet allowance.

**First-party sources:** [Source 1](https://www.worldstream.com/en/dedicated-servers/) · [Source 2](https://www.worldstream.com/en/dedicated-servers/deals/).

**Artwork discovery:** [Official product/brand page](https://www.worldstream.com/en/dedicated-servers/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-datapacket"></a>
### 08. DataPacket

**Example:** Berlin AMD EPYC 4245P · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 230/month starting price |
| CPU | AMD EPYC 4245P |
| Memory | Not fixed in retrieved starting-price card |
| Disk / storage | Not fixed in retrieved starting-price card |
| Network / transfer | Dedicated-server family offers unshared 10–200 Gbps; quote binds port, commit and transfer. |
| Physical location scope | Berlin, DE for this price; extensive separate worldwide location catalog |
| Location confidence | Price specifically Berlin; worldwide footprint is separate |

**Caveats:** Other cities have different prices. Tel Aviv offering is physically described in Petah Tikva; do not use city marketing centroid as verified facility coordinates.

**First-party sources:** [Source 1](https://www.datapacket.com/datacenters/berlin) · [Source 2](https://www.datapacket.com/dedicated-servers) · [Source 3](https://www.datapacket.com/datacenters).

**Artwork discovery:** [Official product/brand page](https://www.datapacket.com/datacenters/berlin). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-cherry-servers"></a>
### 09. Cherry Servers

**Example:** Instant Dedicated Servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From EUR 0.084/hour advertised family minimum; exact SKU not captured |
| CPU | Physical dedicated CPU; select catalog SKU |
| Memory | Configuration dependent |
| Disk / storage | Configuration dependent |
| Network / transfer | Traffic package depends on plan and region. Spot is a separate preemptible product. |
| Physical location scope | Verify bare-metal location selector, not virtual-server availability |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** A family maximum of 128 cores / 768 GB must not be paired with the minimum hourly price.

**First-party sources:** [Source 1](https://www.cherryservers.com/) · [Source 2](https://www.cherryservers.com/bare-metal-dedicated-servers).

**Artwork discovery:** [Official product/brand page](https://www.cherryservers.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-servers-com"></a>
### 10. Servers.com

**Example:** Enterprise Bare Metal · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Sales quotation |
| CPU | Enterprise Intel/AMD configurations; custom |
| Memory | Custom |
| Disk / storage | Custom |
| Network / transfer | Contract-specific connectivity and private networking |
| Physical location scope | Global location catalog; order-specific validation required |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Current site identifies Servers.com by Nexcess. Do not assume independent corporate failure domain from other Nexcess-branded services.

**Supply-chain note:** Nexcess branding shown; investigate shared parent with Liquid Web. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://www.servers.com/products/enterprise-bare-metal) · [Source 2](https://www.servers.com/).

**Artwork discovery:** [Official product/brand page](https://www.servers.com/products/enterprise-bare-metal). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-latitude-sh"></a>
### 11. Latitude.sh

**Example:** m4.metal.small · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From USD 296/month; regional/billing-mode prices differ |
| CPU | AMD EPYC 4244P; 6 cores; 3.8 GHz |
| Memory | 48 GB |
| Disk / storage | 2 × 960 GB NVMe |
| Network / transfer | 2 × 10 Gbps NIC; 20 TB outbound; incoming unmetered. NIC sum is not guaranteed Internet throughput. |
| Physical location scope | Location-specific pricing selector; Singapore listed separately from global minimum |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Current product page says 48 GB; an older launch article said 64 GB. Singapore monthly display USD 350 is not the global minimum; annual and hourly modes differ.

**First-party sources:** [Source 1](https://www.latitude.sh/pricing/m4-metal-small) · [Source 2](https://www.latitude.sh/pricing).

**Artwork discovery:** [Official product/brand page](https://www.latitude.sh/pricing/m4-metal-small). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-vultr"></a>
### 12. Vultr

**Example:** Bare Metal · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Live pricing selector; exact CPU-only offer not captured |
| CPU | Physical CPU SKU; GPU Bare Metal is a separate family |
| Memory | SKU dependent |
| Disk / storage | SKU dependent |
| Network / transfer | Included transfer/port vary by SKU and region. |
| Physical location scope | Bare-metal availability is a subset of Vultr regions |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not substitute Cloud Compute dedicated-vCPU plans for bare metal.

**First-party sources:** [Source 1](https://www.vultr.com/products/bare-metal/) · [Source 2](https://www.vultr.com/pricing/).

**Artwork discovery:** [Official product/brand page](https://www.vultr.com/products/bare-metal/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-phoenixnap"></a>
### 13. phoenixNAP

**Example:** Bare Metal Cloud s0.d1.small · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 0.08/hour; USD 58.40 for a modeled 730-hour month |
| CPU | Intel Xeon E3-1240 v3; 4 cores; 3.4 GHz |
| Memory | 16 GB DDR3 |
| Disk / storage | 2 × 240 GB SSD |
| Network / transfer | 2 × 1 Gbps NIC. Initial bandwidth allocation is 15 TB per location pool, 5 TB in Singapore; not per server. |
| Physical location scope | Location must be checked in BMC instance catalog |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not multiply the initial location bandwidth pool by node count. 730-hour monthly value is arithmetic, not a vendor monthly commitment.

**First-party sources:** [Source 1](https://phoenixnap.com/bare-metal-cloud) · [Source 2](https://phoenixnap.com/bare-metal-cloud/instances) · [Source 3](https://phoenixnap.com/kb/phoenixnap-bare-metal-cloud-billing-models).

**Artwork discovery:** [Official product/brand page](https://phoenixnap.com/bare-metal-cloud). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-hivelocity"></a>
### 14. Hivelocity

**Example:** Intel Xeon E-2336 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 75/month base; AMS1 selector displays +USD 55 (USD 130 arithmetic total; verify basket) |
| CPU | Intel Xeon E-2336; 6 cores / 12 threads; 2.9 GHz |
| Memory | 32 GB |
| Disk / storage | 480 GB SSD |
| Network / transfer | 1 Gbps; 20 TB transfer |
| Physical location scope | AMS1 Amsterdam, NL has explicit surcharge; other regions priced separately |
| Location confidence | Example selector AMS1; base price is not Amsterdam total |

**Caveats:** Avoid showing Amsterdam at USD 75. Outlet stock is separate and can disappear.

**First-party sources:** [Source 1](https://www.hivelocity.net/pricing) · [Source 2](https://www.hivelocity.net/data-centers/).

**Artwork discovery:** [Official product/brand page](https://www.hivelocity.net/pricing). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-ibm-cloud"></a>
### 15. IBM Cloud

**Example:** Bare Metal Servers — Classic / VPC · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Region/configuration calculator; quotation |
| CPU | Intel Xeon / AMD EPYC, product-dependent |
| Memory | Configuration dependent |
| Disk / storage | Configuration dependent |
| Network / transfer | Classic advertises 20 TB included bandwidth; VPC networking/billing is separate. |
| Physical location scope | Classic and VPC region matrices differ |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** 20 TB applies to Classic description; do not apply automatically to VPC. Procurement and provisioning APIs differ.

**First-party sources:** [Source 1](https://www.ibm.com/products/bare-metal-servers/pricing) · [Source 2](https://www.ibm.com/products/bare-metal-servers) · [Source 3](https://cloud.ibm.com/catalog/infrastructure/bare-metal).

**Artwork discovery:** [Official product/brand page](https://www.ibm.com/products/bare-metal-servers/pricing). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-oneprovider"></a>
### 16. OneProvider

**Example:** Paris Atom C2350 dedicated · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 7.99/month promotional; displayed regular EUR 11.99; setup promo EUR 0 vs EUR 4.99 |
| CPU | Intel Atom C2350; 2 cores / 2 threads; 1.7 GHz |
| Memory | 4 GB DDR3 |
| Disk / storage | 1 × 128 GB SATA SSD |
| Network / transfer | 1 Gbps unmetered, subject to fair-use policy |
| Physical location scope | Paris, FR |
| Location confidence | Advertised dedicated offer location |

**Caveats:** Aggregator/reseller: record actual upstream when known. Other virtual 1-vCPU products on the same page are not physical boxes. Tiny legacy offer is unsuitable as a primary modern build runner.

**Supply-chain note:** Reseller / upstream operator unknown. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://oneprovider.com/).

**Artwork discovery:** [Official product/brand page](https://oneprovider.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-clouvider"></a>
### 17. Clouvider

**Example:** Preconfigured E3-1240 v5, London — SSD · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 74/month in the final USD locale; earlier EUR locale displayed EUR 64 |
| CPU | Intel Xeon E3-1240 v5; 4 cores / 8 threads; 3.5 GHz |
| Memory | 16 GB DDR4 ECC |
| Disk / storage | 1 × 240 GB SSD |
| Network / transfer | 1 Gbps NIC; 50 TB monthly data transfer |
| Physical location scope | London, United Kingdom |
| Location confidence | Preconfigured offer explicitly names London |

**Caveats:** Price is locale/currency-specific, not a USD-to-EUR conversion. The 50 TB allowance is not unmetered. Other dedicated regions include Manchester, Amsterdam, Frankfurt and seven US metros; this price/configuration is London.

**First-party sources:** [Source 1](https://www.clouvider.com/dedicated-servers/).

**Artwork discovery:** [Official product/brand page](https://www.clouvider.com/dedicated-servers/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-redswitches"></a>
### 18. RedSwitches

**Example:** Dedicated / Bare Metal Servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Sales or configurator quotation |
| CPU | Intel/AMD configurable |
| Memory | Configurable |
| Disk / storage | Configurable |
| Network / transfer | 25 Gbps+ and unmetered options advertised; exact included service requires quote |
| Physical location scope | 20+ locations advertised; validate dedicated stock for each city |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Month-to-month and zero-setup claims are product/contract dependent. Record actual facility and upstream separately.

**First-party sources:** [Source 1](https://www.redswitches.com/).

**Artwork discovery:** [Official product/brand page](https://www.redswitches.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-velia"></a>
### 19. Velia

**Example:** AMD Ryzen 9 7950X3D · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 139/month advertised sale |
| CPU | AMD Ryzen 9 7950X3D; 16 cores / 32 threads; 4.2 GHz |
| Memory | 128 GB DDR5; vendor memory labeling needs confirmation |
| Disk / storage | 2 × 960 GB NVMe |
| Network / transfer | Traffic/port depend on order; not established in retrieved sale card |
| Physical location scope | Germany / US / Singapore offered by provider; selected SKU stock needs confirmation |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Vendor listing refers to DDR5 ECC REG; verify the actual memory implementation on this consumer CPU rather than normalizing it as registered ECC.

**First-party sources:** [Source 1](https://www.velia.net/gaming/) · [Source 2](https://www.velia.net/amd-ryzen-dedicated-server/) · [Source 3](https://www.velia.net/dedicated-server/).

**Artwork discovery:** [Official product/brand page](https://www.velia.net/gaming/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-ip-projects"></a>
### 20. IP-Projects

**Example:** Performance Server Ryzen 5 8400F · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From EUR 101.46/month |
| CPU | AMD Ryzen 5 8400F |
| Memory | Page conflict: 32 GB in offer body vs 64 GB in another summary |
| Disk / storage | 2 × 1 TB NVMe |
| Network / transfer | IPMI advertised; port/traffic not established |
| Physical location scope | German dedicated offering; exact facility/stock requires quote |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Keep RAM numeric field null until checkout resolves the 32/64 GB discrepancy.

**First-party sources:** [Source 1](https://www.ip-projects.de/).

**Artwork discovery:** [Official product/brand page](https://www.ip-projects.de/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-avoro"></a>
### 21. Avoro

**Example:** Ryzen 9000 Dedicated / Instant Dedicated · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From EUR 141.92/month excluding VAT for Ryzen 9000 family |
| CPU | Ryzen 9000 family; up to 16 cores / 32 threads, not a fixed base SKU |
| Memory | Up to 256 GB; base not established |
| Disk / storage | Configuration dependent |
| Network / transfer | Instant inventory includes 1 Gbps and 10 Gbps variants; do not combine them. |
| Physical location scope | Frankfurt, DE facility information; exact server selector required |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Avoro Rootserver/Power Rootserver is not the same as this physical Dedicated line.

**First-party sources:** [Source 1](https://avoro.eu/dedicated-server) · [Source 2](https://avoro.eu/en/instant-dedicated) · [Source 3](https://avoro.eu/en/datacenter).

**Artwork discovery:** [Official product/brand page](https://avoro.eu/dedicated-server). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-keyweb"></a>
### 22. Keyweb

**Example:** Keymachine KM i7 | 32 GB · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 74/month + EUR 119 setup; German consumer prices include 19% VAT |
| CPU | Intel Core i7-8700; 6 physical cores; up to 4.6 GHz |
| Memory | 32 GB DDR4 |
| Disk / storage | 2 × 250 GB SATA SSD; software RAID 1 |
| Network / transfer | 1 Gbps switch port; 1 IPv4 and 1 IPv6; transfer allowance unresolved |
| Physical location scope | Germany; exact facility must be confirmed |
| Location confidence | Dedicated physical service explicitly in Germany |

**Caveats:** Minimum contract one month; 14-day end-of-term notice. RAM/drive upgrades are separate charges. Dedicated VPS is not this physical product. RAID 1 usable capacity is about 250 GB before overhead. Transfer row is blank in parsed comparison; do not silently call it unlimited.

**First-party sources:** [Source 1](https://www.keyweb.de/en/server/dedicated-root-server/dedicated-basic-server).

**Artwork discovery:** [Official product/brand page](https://www.keyweb.de/en/server/dedicated-root-server/dedicated-basic-server). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-myloc-servdiscount"></a>
### 23. myLoc / servdiscount

**Example:** servdiscount dedicated inventory · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Live inventory price; exact basket not captured |
| CPU | Fixed physical configurations |
| Memory | Fixed per offer |
| Disk / storage | Fixed per offer |
| Network / transfer | Network conditions require exact inventory row |
| Physical location scope | Düsseldorf, DE |
| Location confidence | Provider identifies Düsseldorf for these servers |

**Caveats:** Group myLoc, servdiscount and webtropia for supplier concentration analysis; do not count them as three unrelated networks.

**Supply-chain note:** myLoc / servdiscount / webtropia. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://servdiscount.com/).

**Artwork discovery:** [Official product/brand page](https://servdiscount.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-fasthosts"></a>
### 24. Fasthosts

**Example:** Xeon-E-32-NVMe · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | GBP 100/month discounted; displayed regular GBP 115; promotion term needs checkout |
| CPU | Intel Xeon E-2356G; 6 cores; 3.2 GHz |
| Memory | 32 GB DDR4 ECC |
| Disk / storage | 2 × 512 GB NVMe; software RAID 1 |
| Network / transfer | Unlimited transfers; exact included public port speed requires order confirmation |
| Physical location scope | United Kingdom; exact dedicated data center to confirm |
| Location confidence | UK dedicated service |

**Caveats:** Landing-page “from GBP 25” is not the selected configuration. Limited-stock message displayed. Port hardware family supports dual GbE/10GbE variants; no included per-SKU Internet speed inferred. RAM/storage are not family maximums.

**First-party sources:** [Source 1](https://www.fasthosts.co.uk/dedicated-servers/cheap) · [Source 2](https://www.fasthosts.co.uk/dedicated-servers).

**Artwork discovery:** [Official product/brand page](https://www.fasthosts.co.uk/dedicated-servers/cheap). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-ukservers"></a>
### 25. UKServers

**Example:** cPanel 270 · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From GBP 124/month |
| CPU | Intel Xeon E-2488; 8 cores; 3.2 GHz |
| Memory | 32–128 GB ECC; base tier 32 GB |
| Disk / storage | Up to 2 SSD/HDD + 2 M.2 NVMe; installed base drives not specified |
| Network / transfer | 1 Gbps or 10 Gbps options; included transfer not captured; IPMI |
| Physical location scope | UK facilities; exact location via order |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** cPanel-focused offering may include licensing/management. Ask for an unmanaged Linux equivalent rather than assuming identical price.

**First-party sources:** [Source 1](https://www.ukservers.com/baremetal-server/cpanel-servers/).

**Artwork discovery:** [Official product/brand page](https://www.ukservers.com/baremetal-server/cpanel-servers/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-rapidswitch"></a>
### 26. RapidSwitch

**Example:** AMD dedicated family · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From GBP 47.95/month; specific SKU not captured |
| CPU | AMD dedicated; configurable |
| Memory | Configuration dependent |
| Disk / storage | Configuration dependent |
| Network / transfer | Contract/order-specific port and transfer |
| Physical location scope | UK locations advertised include Maidenhead, Gosport, Glasgow; separate Dallas US offer starts GBP 160 |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not use the UK family minimum as a Dallas quote.

**First-party sources:** [Source 1](https://www.rapidswitch.com/).

**Artwork discovery:** [Official product/brand page](https://www.rapidswitch.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-namecheap"></a>
### 27. Namecheap

**Example:** Dedicated Server catalog · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Advertises from USD 44.88/month; promotions and annual equivalents vary |
| CPU | Physical dedicated configurations; exact SKU needed |
| Memory | SKU dependent |
| Disk / storage | SKU dependent |
| Network / transfer | Bandwidth varies by chosen fixed plan |
| Physical location scope | US dedicated offering; confirm exact order location |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Full root requires User-Responsible or Basic management. Hardware upgrades mean changing plan, not arbitrary live RAM additions.

**First-party sources:** [Source 1](https://www.namecheap.com/hosting/dedicated-servers/our-prices/).

**Artwork discovery:** [Official product/brand page](https://www.namecheap.com/hosting/dedicated-servers/our-prices/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-novoserve"></a>
### 28. NovoServe

**Example:** Dedicated / unmetered servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | 1 Gbps unmetered configurations advertised above EUR 100/month; exact SKU quote |
| CPU | Intel Xeon / AMD EPYC; configurable |
| Memory | Configurable |
| Disk / storage | NVMe / SSD / HDD options |
| Network / transfer | Standard 25 TB outbound with free incoming; unmetered 1–50 Gbps alternatives are different packages |
| Physical location scope | Netherlands, Denmark, US advertised; verify SKU location |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not conflate 25 TB metered standard with separately priced unmetered transit.

**First-party sources:** [Source 1](https://novoserve.com/dedicated-servers) · [Source 2](https://novoserve.com/dedicated-server) · [Source 3](https://novoserve.com/blog/ai-dedicated-servers-with-fixed-monthly-pricing).

**Artwork discovery:** [Official product/brand page](https://novoserve.com/dedicated-servers). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-nforce"></a>
### 29. NFOrce

**Example:** HP DL320e v2 Budget 1 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 49.99/month excluding VAT; standard 12-month auto-renewing contract |
| CPU | Intel Xeon E3-1240 v3; 4 cores / 8 threads; 3.4–3.8 GHz |
| Memory | 16 GB |
| Disk / storage | 2 × 2 TB SATA HDD |
| Network / transfer | 1 Gbps dedicated; 10 TB outgoing; incoming unmetered/free |
| Physical location scope | NL-1 Databarn Amsterdam; NL-3 Nedzone Steenbergen, NL |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Site states own hardware, not reseller. Exact stock/site must still be selected.

**First-party sources:** [Source 1](https://www.nforce.com/).

**Artwork discovery:** [Official product/brand page](https://www.nforce.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-altushost"></a>
### 30. AltusHost

**Example:** Dedicated Servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Sales/configurator quotation |
| CPU | Configuration dependent |
| Memory | Configuration dependent |
| Disk / storage | Configuration dependent |
| Network / transfer | Quote required |
| Physical location scope | European provider; physical location must be verified for selected server |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** 

**First-party sources:** [Source 1](https://altushost.com/).

**Artwork discovery:** [Official product/brand page](https://altushost.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-hostkey"></a>
### 31. HOSTKEY

**Example:** AMD EPYC 9354 dedicated offer · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From EUR 299/month advertised |
| CPU | AMD EPYC 9354; 32 cores; 3.25 GHz |
| Memory | 192 GB |
| Disk / storage | 2 × 1 TB NVMe |
| Network / transfer | 10 Gbps; 50 TB transfer |
| Physical location scope | Location selection required; provider advertises NL, FI, US and additional markets |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not use bm.v/vCPU-marked products as evidence of a complete physical host. Confirm the selected EPYC listing is single-tenant full hardware.

**First-party sources:** [Source 1](https://hostkey.com/).

**Artwork discovery:** [Official product/brand page](https://hostkey.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-fdcservers"></a>
### 32. FDCServers

**Example:** Unmetered Dedicated Servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From USD 129/month; base hardware not captured |
| CPU | AMD EPYC / Intel Xeon options |
| Memory | Configuration dependent |
| Disk / storage | Configuration dependent |
| Network / transfer | 10–200 Gbps unmetered family; advertised no data cap, throttling or FUP. Exact port must be priced. |
| Physical location scope | 23 locations advertised; dedicated selector needed |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not infer physical-server locations from FDC VPS availability.

**First-party sources:** [Source 1](https://fdcservers.net/product/unmetered-dedicated-servers) · [Source 2](https://fdcservers.net/).

**Artwork discovery:** [Official product/brand page](https://fdcservers.net/product/unmetered-dedicated-servers). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-aruba"></a>
### 33. Aruba

**Example:** AV-A205.1 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 110.68/month + VAT |
| CPU | AMD Ryzen 5 9600X; 6 cores; 3.9–5.4 GHz |
| Memory | 32 GB DDR5 on-die ECC |
| Disk / storage | 2 × 500 GB NVMe |
| Network / transfer | 1 Gbps; unlimited traffic |
| Physical location scope | Arezzo and Bergamo, IT |
| Location confidence | Product row lists these locations |

**Caveats:** DDR5 on-die ECC is not proof of end-to-end server ECC. SeFlow is another Aruba line, not independent. Lower-priced RD-I101 has 25 TB/month, not unlimited.

**Supply-chain note:** Aruba / SeFlow. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://www.arubacloud.com/dedicated-servers-range/) · [Source 2](https://aruba.it/en/server-price-list.aspx).

**Artwork discovery:** [Official product/brand page](https://www.arubacloud.com/dedicated-servers-range/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-ikoula"></a>
### 34. IKOULA

**Example:** Regen S1 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 180/month regular; EUR 150/month promotion code IKREGEN30; excluding VAT |
| CPU | 2 × Intel Xeon Silver 4214R; total 24 cores / 48 threads |
| Memory | 128 GB DDR4 ECC REG |
| Disk / storage | 2 × 960 GB enterprise NVMe; software RAID |
| Network / transfer | Shared 1 Gbps public; 100 Mbps guaranteed; unlimited traffic |
| Physical location scope | France |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Use EUR 180 for non-promotional cost scenarios; code price may expire. Do not count 1 Gbps as committed bandwidth.

**First-party sources:** [Source 1](https://www.ikoula.com/en/dedicated-server/regen) · [Source 2](https://www.ikoula.com/en/dedicated-server).

**Artwork discovery:** [Official product/brand page](https://www.ikoula.com/en/dedicated-server/regen). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-nine"></a>
### 35. Nine

**Example:** Root Dedicated Server · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | CHF 233/month + CHF 250 setup |
| CPU | AMD EPYC 7313P; 16 cores |
| Memory | 32 GB base; expandable |
| Disk / storage | Disk details require full configuration |
| Network / transfer | Included transit details require confirmation |
| Physical location scope | Zurich, CH; provider describes two independent data centres |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Managed Dedicated is a different, higher-priced service; do not substitute managed price or disks without validating the root configuration.

**First-party sources:** [Source 1](https://docs.nine.ch/docs/root-server/) · [Source 2](https://nine.ch/en/price-calculator/).

**Artwork discovery:** [Official product/brand page](https://docs.nine.ch/docs/root-server/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-glesys"></a>
### 36. GleSYS

**Example:** X11-1 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 265/month (also SEK 2,665 listed), excluding VAT |
| CPU | Intel Xeon Gold 6132; 14 cores / 28 threads |
| Memory | 64 GB |
| Disk / storage | 2 × 480 GB SATA SSD |
| Network / transfer | 10 Gbps port; transfer entitlement must be confirmed separately |
| Physical location scope | Falkenberg and Stockholm, SE |
| Location confidence | Exact X11-1 row locations |

**Caveats:** Other GleSYS SKUs offer Oulu FI or Oslo NO, but do not propagate those locations to X11-1.

**First-party sources:** [Source 1](https://glesys.com/pricing/) · [Source 2](https://glesys.com/products/bare-metal/dedicated-servers/).

**Artwork discovery:** [Official product/brand page](https://glesys.com/pricing/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-m247-global"></a>
### 37. M247 Global

**Example:** Dedicated Servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Sales quotation |
| CPU | Enterprise configurable bare metal |
| Memory | Custom |
| Disk / storage | Custom |
| Network / transfer | Custom connectivity/commit |
| Physical location scope | Global footprint; facility and SKU need sales confirmation |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** 

**First-party sources:** [Source 1](https://www.m247global.com/dedicated-server).

**Artwork discovery:** [Official product/brand page](https://www.m247global.com/dedicated-server). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-gthost"></a>
### 38. GTHost

**Example:** Supermicro Blade Xeon D-1531 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 59/month; USD 5/day trial is separate |
| CPU | Intel Xeon D-1531; 6 cores / 12 threads; 2.2–2.7 GHz |
| Memory | 16 GB DDR4-2133 |
| Disk / storage | 480 GB SSD |
| Network / transfer | 300 Mbps unmetered; IPMI |
| Physical location scope | US catalog; exact city selected at order |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not confuse daily trial pricing with a daily production billing plan.

**First-party sources:** [Source 1](https://gthost.com/dedicated-server-usa/).

**Artwork discovery:** [Official product/brand page](https://gthost.com/dedicated-server-usa/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-servermania"></a>
### 39. ServerMania

**Example:** AMD EPYC 4124P entry configuration · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 139/month in provider pricing guide dated July 14, 2026 |
| CPU | AMD EPYC 4124P |
| Memory | 32 GB |
| Disk / storage | 1 TB NVMe M.2 |
| Network / transfer | 1 Gbps port; 100 TB transfer in provider pricing guide example |
| Physical location scope | Location must be selected; article price is not a regional inventory guarantee |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Linux example. Treat the article as a published example, not a guaranteed purchasable basket.

**First-party sources:** [Source 1](https://www.servermania.com/kb/articles/dedicated-server-hosting-pricing) · [Source 2](https://www.servermania.com/kb/articles/dedicated-server-hosting-pricing).

**Artwork discovery:** [Official product/brand page](https://www.servermania.com/kb/articles/dedicated-server-hosting-pricing). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-reliablesite"></a>
### 40. ReliableSite

**Example:** AMD Ryzen 5600X 64GB Rapid Deploy · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 129/month |
| CPU | AMD Ryzen 5600X; 6 cores / 12 threads; 3.7 GHz |
| Memory | 64 GB DDR4; non-ECC |
| Disk / storage | 1 × 512 GB NVMe; no RAID |
| Network / transfer | 1 Gbps unmetered service; up-to-10-Gbps port wording depends on Metal+ and is inconsistent |
| Physical location scope | Miami, Florida, US in selected inventory row |
| Location confidence | Inventory row for selected configuration |

**Caveats:** Inventory snapshot names Miami for this exact configuration. Provider also lists NYC, Los Angeles, Dallas, Amsterdam and Querétaro, but that is not universal SKU stock. Port wording conflicts: free 10 Gbps versus Metal+ conditional; retain the clear 1 Gbps service entitlement, leave physical port unknown. Ignore erroneous DDR5 upsell text for Ryzen 5600X.

**First-party sources:** [Source 1](https://www.reliablesite.net/dedicated-servers/) · [Source 2](https://www.reliablesite.net/dedicated-servers/6-core-server/amd-ryzen-5600x-64GB).

**Artwork discovery:** [Official product/brand page](https://www.reliablesite.net/dedicated-servers/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-interserver"></a>
### 41. InterServer

**Example:** Buy It Now — 2 × Xeon E5-2680 v4 8SFF, SATA storage · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 236/month; zero setup fees advertised |
| CPU | 2 × Intel Xeon E5-2680 v4; 28 total physical cores |
| Memory | 128 GB |
| Disk / storage | 2 × 24 TB SATA HDD |
| Network / transfer | 1 Gbps unmetered; 1 VLAN IP (/30) advertised |
| Physical location scope | NYC metro region, US |
| Location confidence | Selected stocked offer names NYC region, not an exact facility |

**Caveats:** NYC-region stocked offer, not the USD 213 NVMe variant. Other dedicated metros are Dallas and Los Angeles; hardware varies. Stock listings and a generic sold-out notice coexist, so availability is not guaranteed.

**First-party sources:** [Source 1](https://www.interserver.net/dedicated/).

**Artwork:** [interserver-dedicated](#asset-interserver-dedicated), [interserver-datacenter](#asset-interserver-datacenter), [interserver-network](#asset-interserver-network). Classifications and permissions are below.

<a id="provider-liquid-web"></a>
### 42. Liquid Web

**Example:** Managed Dedicated Servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Sales/configurator quotation |
| CPU | Physical managed dedicated hardware |
| Memory | Configuration dependent |
| Disk / storage | Configuration dependent |
| Network / transfer | Managed-service network package depends on contract |
| Physical location scope | Dedicated region selector; not all cloud locations apply |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Managed software/support can inflate comparisons against unmanaged Hetzner. Quote an equivalent Linux-only configuration.

**Supply-chain note:** Nexcess branding shown; check relation to Servers.com. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://www.liquidweb.com/).

**Artwork discovery:** [Official product/brand page](https://www.liquidweb.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-openmetal"></a>
### 43. OpenMetal

**Example:** Bare Metal · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Pricing table/configurator; exact basket not captured |
| CPU | Enterprise bare metal; select hardware class |
| Memory | Configuration dependent |
| Disk / storage | Configuration dependent |
| Network / transfer | Network package depends on hardware/contract |
| Physical location scope | US East, US West and Europe listed |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Bare-metal rental and multi-node hosted private cloud are different units of purchase; do not divide a cluster price by an assumed node count.

**First-party sources:** [Source 1](https://openmetal.io/bare-metal-pricing/) · [Source 2](https://openmetal.io/).

**Artwork discovery:** [Official product/brand page](https://openmetal.io/bare-metal-pricing/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-wholesale-internet"></a>
### 44. Wholesale Internet

**Example:** Dual Xeon E5-2660 custom dedicated · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 64/month; free setup |
| CPU | 2 × Xeon E5-2660; total 16 cores / 32 threads |
| Memory | 32 GB ECC |
| Disk / storage | 480 GB SSD |
| Network / transfer | 1 Gbps unmetered; 5 IPv4; IPv6 /64 |
| Physical location scope | Kansas City, Missouri, US |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Legacy hardware; power efficiency and single-thread performance differ substantially from modern EPYC/Ryzen.

**First-party sources:** [Source 1](https://www.wholesaleinternet.net/custom_dedicated/) · [Source 2](https://www.wholesaleinternet.net/).

**Artwork discovery:** [Official product/brand page](https://www.wholesaleinternet.net/custom_dedicated/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-dacentec"></a>
### 45. Dacentec

**Example:** Supermicro 8-bay dual E5-2650 v2 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 80/month in current billing inventory |
| CPU | 2 × Intel Xeon E5-2650 v2 |
| Memory | 128 GB |
| Disk / storage | 240 GB SSD + 2 × 3 TB HDD |
| Network / transfer | 1 Gbps dedicated family; included transfer not captured |
| Physical location scope | Lenoir, North Carolina, US; exact inventory facility must be confirmed |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** The billing URL contains an unavailable older selected item but also current inventory rows; this record describes the listed Supermicro offer, not that unavailable Opteron. Some other plans are rent-to-own.

**First-party sources:** [Source 1](https://dacentec.com/hostbill/) · [Source 2](https://billing.dacentec.com/hostbill/index.php?%2Fcart=&action=add&cat_id=3&id=428).

**Artwork discovery:** [Official product/brand page](https://dacentec.com/hostbill/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-database-mart-server-mart"></a>
### 46. Database Mart / Server Mart

**Example:** Lite Dedicated SSD · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 41/month recurring promotion; regular USD 49 |
| CPU | Intel Xeon E3-1220; 4 cores |
| Memory | 16 GB |
| Disk / storage | 480 GB SSD + 500 GB SATA disk |
| Network / transfer | 100 Mbps unmetered; 1 IPv4 |
| Physical location scope | US; Dallas advertised, exact order facility to verify |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not confuse server-mart.com with unrelated similarly named providers. SSD plus SATA auxiliary disk is not a mirrored pair.

**Supply-chain note:** Database Mart / Server Mart. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://www.databasemart.com/pricing) · [Source 2](https://www.databasemart.com/dedicated-hosting).

**Artwork discovery:** [Official product/brand page](https://www.databasemart.com/pricing). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-colocation-america"></a>
### 47. Colocation America

**Example:** Intel Xeon E3-1270 v6 dedicated · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 135/month |
| CPU | Xeon E3-1270 v6; 4 cores / 8 threads; 3.8 GHz |
| Memory | Up to 64 GB; base allocation not established |
| Disk / storage | Up to 4 drives; base drives not established |
| Network / transfer | 1 Gbps; 15 TB transfer; free setup |
| Physical location scope | Los Angeles, California, US |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** The catalog reports maxima, not necessarily included RAM or disk. A separate E3-1220 row has a suspicious thread count; that row is not normalized here.

**First-party sources:** [Source 1](https://www.colocationamerica.com/dedicated-servers-all) · [Source 2](https://www.colocationamerica.com/dedicated-servers).

**Artwork discovery:** [Official product/brand page](https://www.colocationamerica.com/dedicated-servers-all). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-tier-net"></a>
### 48. Tier.Net

**Example:** Single Intel E3-1270 v6 dedicated · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Exact SKU price requires order; family from USD 49.95 is not this configuration |
| CPU | Xeon E3-1270 v6; 4 cores; 3.8–4.2 GHz |
| Memory | 64 GB DDR4 |
| Disk / storage | 500 GB SSD |
| Network / transfer | 10 Gbps port; 20 TB transfer |
| Physical location scope | Ashburn VA; Bend OR; Binghamton NY; Charlotte NC; Dallas TX; New York NY, US |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Managed support is a separate add-on. Do not equate 10 Gbps access with 10 Gbps sustained unmetered Internet.

**First-party sources:** [Source 1](https://www.tier.net/dedicated-server-hosting).

**Artwork discovery:** [Official product/brand page](https://www.tier.net/dedicated-server-hosting). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-hostdime"></a>
### 49. HostDime

**Example:** Self-managed Xeon E3-1230 v5 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 129/month |
| CPU | Xeon E3-1230 v5; 4 cores / 8 threads; 3.4 GHz |
| Memory | 16 GB |
| Disk / storage | 480 GB SSD OR 1 TB SATA3 HDD |
| Network / transfer | 1 Gbps burstable uplink; advertised 75 Mbps (~25 TB) monthly bandwidth; verify measurement/billing method |
| Physical location scope | US offer; separate dedicated catalogs in Brazil, Mexico, UK, Colombia and India |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Normalized disk selects the SSD option. Do not interpret the approximate 25 TB as an independently verified metered allowance. Do not count announced Mexico 2028 facility as operating.

**First-party sources:** [Source 1](https://www.hostdime.com/self-managed-dedicated-servers).

**Artwork:** [hostdime-logo](#asset-hostdime-logo), [hostdime-logo-no-slogan](#asset-hostdime-logo-no-slogan). Classifications and permissions are below.

<a id="provider-racknerd"></a>
### 50. RackNerd

**Example:** Intel Xeon E3-1230 v2 bare metal · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 139/month; optional 15OFFDEDI promotion requires checkout |
| CPU | Intel Xeon E3-1230 v2 |
| Memory | 16 GB |
| Disk / storage | 480 GB SSD |
| Network / transfer | 1 Gbps; 35 TB; 5 IPv4; IPMI/KVM |
| Physical location scope | US table; choose exact city in order form |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Hybrid Dedicated is a different virtualized product and excluded. Separate 160 TB storage special is USD 479/month in Los Angeles DC-02.

**First-party sources:** [Source 1](https://www.racknerd.com/dedicated-servers).

**Artwork:** [racknerd-server-icon](#asset-racknerd-server-icon), [racknerd-logo-dark](#asset-racknerd-logo-dark). Classifications and permissions are below.

<a id="provider-lumadock"></a>
### 51. LumaDock

**Example:** BM.E1 / HPE ProLiant DL360 Gen9 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 119/month promotional; displayed regular USD 159; billing selector/commitment must be checked |
| CPU | 2 × Xeon E5-2680 v3; total 24 cores / 48 threads; 2.5 GHz |
| Memory | 64 GB DDR4 ECC |
| Disk / storage | 3 × 2 TB SSD |
| Network / transfer | 1 Gbps unmetered; IPv4/IPv6; iLO |
| Physical location scope | London GB; Frankfurt DE; New York US; Amsterdam NL; Paris FR; Madrid ES |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Milan marked SOON is not included. Exact city/SKU availability and annual selector effect must be verified.

**First-party sources:** [Source 1](https://lumadock.com/dedicated-servers).

**Artwork discovery:** [Official product/brand page](https://lumadock.com/dedicated-servers). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-gcore"></a>
### 52. Gcore

**Example:** Hong Kong Xeon E-2136 dedicated · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 158/month |
| CPU | Intel Xeon E-2136 |
| Memory | 32 GB |
| Disk / storage | 2 × 2 TB SATA; hardware RAID |
| Network / transfer | 1 Gbps; 5 TB/month |
| Physical location scope | Hong Kong, HK |
| Location confidence | Exact regional product page |

**Caveats:** Gcore Cloud minute-billed bare metal is a separate purchase path; do not combine its EUR prices with this hosting offer.

**First-party sources:** [Source 1](https://gcore.com/hosting/dedicated/hong-kong).

**Artwork:** [gcore-server-stack](#asset-gcore-server-stack). Classifications and permissions are below.

<a id="provider-zenlayer"></a>
### 53. Zenlayer

**Example:** S-Series Bare Metal Cloud · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From USD 0.587/hour; selected monthly promotional locations from USD 77 are separate |
| CPU | Intel Xeon E-series range; 4–8 cores; 3.5–3.9 GHz |
| Memory | 16–32 GB range; exact base not captured |
| Disk / storage | SATA or SSD; exact capacity requires selected SKU |
| Network / transfer | Monthly plans may include 10–50 Mbps flat or 1.5–7.5 TB by location; 95th-percentile plans also exist |
| Physical location scope | Global edge locations; order-specific bare-metal location selector |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not pair all maximum hardware/network values with the minimum price. Cloud USD 8.03 offerings are VMs, not these physical servers.

**First-party sources:** [Source 1](https://www.zenlayer.com/bare-metal/) · [Source 2](https://docs.console.zenlayer.com/welcome/pricing/bare-metal-cloud-pricing).

**Artwork discovery:** [Official product/brand page](https://www.zenlayer.com/bare-metal/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-exabytes"></a>
### 54. Exabytes

**Example:** Economy Self-Managed Dedicated · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | MYR 515.90/month + MYR 500 setup |
| CPU | Single Intel Xeon E3; 4 cores; exact model not specified |
| Memory | 16 GB |
| Disk / storage | 2 × 1 TB NL-SAS; RAID 1 |
| Network / transfer | 100 Mbps unmetered; shared/constant wording differs on page; 2 IPv4 |
| Physical location scope | Cyberjaya, Malaysia |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not assume a 100 Mbps committed dedicated circuit from the shared-port wording. Managed tiers and larger setup fees are different offers.

**First-party sources:** [Source 1](https://www.exabytes.my/servers/dedicated-server).

**Artwork:** [exabytes-dedicated-icon](#asset-exabytes-dedicated-icon), [exabytes-hero](#asset-exabytes-hero). Classifications and permissions are below.

<a id="provider-ip-serverone"></a>
### 55. IP ServerOne

**Example:** Single NVIDIA RTX 4090 dedicated GPU server · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From MYR 2,099/month + 8% SST |
| CPU | AMD EPYC 7313; 16 cores; 3 GHz; 1 × RTX 4090 24 GB GPU |
| Memory | 64 GB |
| Disk / storage | 1 × 3.8 TB NVMe / SSD; exact interface to confirm |
| Network / transfer | 300 Mbps; transfer allowance not established |
| Physical location scope | Malaysia offering; confirm GPU facility; general bare metal also has Singapore locations |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Page says software RAID 1 while listing a single disk: treat RAID/usable capacity as unresolved. Use MYR, not the illustrative USD conversion at 4.4 MYR/USD. Nova GPU VM is excluded.

**First-party sources:** [Source 1](https://www.ipserverone.com/pricing/) · [Source 2](https://www.ipserverone.com/gpu-servers/) · [Source 3](https://www.ipserverone.com/bare-metal/).

**Artwork discovery:** [Official product/brand page](https://www.ipserverone.com/pricing/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-e2e-networks"></a>
### 56. E2E Networks

**Example:** Dedicated / Bare Metal Servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Current quote required after July/August 2026 pricing changes |
| CPU | Physical CPU/GPU configurations; quote exact host |
| Memory | Quote |
| Disk / storage | Quote |
| Network / transfer | Quote port, egress and cross-region charges |
| Physical location scope | India; selected dedicated region must be quoted |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Provider pricing-change notice directs dedicated/bare-metal customers to account managers. Do not use pre-change rates or VM prices.

**First-party sources:** [Source 1](https://docs.e2enetworks.com/docs/myaccount/billing/pricing-update-july-2026/).

**Artwork discovery:** [Official product/brand page](https://docs.e2enetworks.com/docs/myaccount/billing/pricing-update-july-2026/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-voyager"></a>
### 57. Voyager

**Example:** Low dedicated — 32 GB · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | NZD 365/month + GST |
| CPU | 2 CPUs; 16 total cores; exact model not given |
| Memory | 32 GB |
| Disk / storage | 2 × 1 TB SSD |
| Network / transfer | Unmetered subject to fair-use policy; port speed not specified |
| Physical location scope | Auckland, New Zealand |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** 64 GB variant is NZD 375/month. This is the physical dedicated service, not the cloud-server line.

**First-party sources:** [Source 1](https://voyager.nz/business/hosting/dedicated-servers).

**Artwork discovery:** [Official product/brand page](https://voyager.nz/business/hosting/dedicated-servers). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-xneelo"></a>
### 58. xneelo

**Example:** TruServ Plus 2336 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | ZAR 1,995/month + ZAR 695 setup; VAT inclusive |
| CPU | Xeon E-2336; 6 cores / 12 threads; 2.9–4.8 GHz |
| Memory | 32 GB ECC |
| Disk / storage | 2 × 1 TB enterprise SSD; software RAID 1 |
| Network / transfer | Unlimited subject to AUP; exact public port must be confirmed |
| Physical location scope | South Africa; selected TruServ facility must be confirmed |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Use self-managed TruServ for full control. Do not mislabel old Hetzner South Africa/xneelo photographs as the German Hetzner fleet.

**First-party sources:** [Source 1](https://xneelo.co.za/dedicated-servers/).

**Artwork discovery:** [Official product/brand page](https://xneelo.co.za/dedicated-servers/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-hostafrica"></a>
### 59. HOSTAFRICA

**Example:** Metal Core Linux 8 · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 140.84/month advertised; confirm billing currency |
| CPU | 8 physical cores / 16 threads; exact CPU model not captured |
| Memory | Requires product configuration |
| Disk / storage | Requires product configuration |
| Network / transfer | Requires product configuration |
| Physical location scope | African dedicated service; exact country/SKU needs order confirmation |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** VDS rows on the same page are virtual and excluded. Do not infer dedicated locations from the entire VPS footprint.

**First-party sources:** [Source 1](https://www.hostafrica.com/servers/dedicated-servers/).

**Artwork discovery:** [Official product/brand page](https://www.hostafrica.com/servers/dedicated-servers/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-edgeuno"></a>
### 60. EdgeUno

**Example:** Bare Metal · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From USD 695/month; custom host configuration |
| CPU | Custom Intel / AMD physical hardware |
| Memory | Custom |
| Disk / storage | Custom |
| Network / transfer | Custom bandwidth/commit; exact allowance needs quote |
| Physical location scope | Dedicated/cloud footprint includes Argentina, Brazil, Chile, Colombia, Ecuador, Mexico and Peru; additional US/Europe locations |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** 45+ sites is a provider network claim, not 45 confirmed locations for every bare-metal configuration. VPS prices are not dedicated prices.

**First-party sources:** [Source 1](https://edgeuno.cloud/) · [Source 2](https://edgeuno.com/bare-metal/) · [Source 3](https://edgeuno.com/the-enterprise-guide-to-edge-data-centers-for-latin-america-enterprises/).

**Artwork discovery:** [Official product/brand page](https://edgeuno.cloud/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-bacloud"></a>
### 61. Bacloud

**Example:** Epyc U33 customizable dedicated · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 187/month; minimum one month |
| CPU | AMD EPYC 7002 series; exact processor selected in configurator |
| Memory | Up to 2 TB; base RAM unknown |
| Disk / storage | Chassis supports 4 NVMe + 3 HDD/SSD positions; included drives unknown |
| Network / transfer | Up to 10 Gbps; exact port and transfer package require configuration |
| Physical location scope | Lithuania for this dedicated page; separate Netherlands bare-metal offerings |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Capacity maxima and chassis drive bays are not included RAM/disks. Free setup advertised. Own Lithuanian facility provides useful real data-centre artwork.

**First-party sources:** [Source 1](https://www.bacloud.com/en/dedicated-servers) · [Source 2](https://www.bacloud.com/en/our-datacenter/lithuania).

**Artwork:** [bacloud-logo](#asset-bacloud-logo). Classifications and permissions are below.

<a id="provider-arsys"></a>
### 62. Arsys

**Example:** Dedicated Servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Pay-per-use/configurator quotation |
| CPU | Configurable physical dedicated hardware |
| Memory | Configurable |
| Disk / storage | Configurable |
| Network / transfer | 1 Gbps; unlimited traffic advertised |
| Physical location scope | Spain; exact site and selected configuration to confirm |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not treat a provider landing-page starting price as a priced configuration. Investigate corporate affiliation before counting as independent from IONOS.

**First-party sources:** [Source 1](https://www.arsys.net/servers/dedicated) · [Source 2](https://www.arsys.net/).

**Artwork discovery:** [Official product/brand page](https://www.arsys.net/servers/dedicated). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-sakura-internet"></a>
### 63. Sakura Internet

**Example:** Sakura PHY dedicated servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Current PHY configurator/quotation; no reliable matched price captured |
| CPU | Current PHY physical-server configurations |
| Memory | Configure |
| Disk / storage | Configure |
| Network / transfer | Configure bandwidth and transfer |
| Physical location scope | Japan; exact PHY site must be selected |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Older Sakura dedicated generations have separate end-of-sale/end-of-service notices. Do not assume they describe current PHY availability, or use old-generation prices.

**First-party sources:** [Source 1](https://server.sakura.ad.jp/).

**Artwork discovery:** [Official product/brand page](https://server.sakura.ad.jp/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-kagoya"></a>
### 64. Kagoya

**Example:** KAGOYA FLEX Bare Metal · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Sales/configurator quotation |
| CPU | Physical dedicated KAGOYA FLEX configurations |
| Memory | Configure |
| Disk / storage | Configure |
| Network / transfer | Contract-specific network package |
| Physical location scope | Japan; facility and SLA to confirm |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** KAGOYA FLEX bare metal is the relevant family. Old managed-hosting campaign prices are not used as a physical-server quotation.

**First-party sources:** [Source 1](https://www.kagoya.jp/).

**Artwork discovery:** [Official product/brand page](https://www.kagoya.jp/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-idc-frontier"></a>
### 65. IDC Frontier

**Example:** Standard 2P32C256GB · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | JPY 115,000/month; setup JPY 0; excluding tax |
| CPU | 2 × 16-core processors; exact CPU model not stated |
| Memory | 256 GB |
| Disk / storage | 400 GB RAID 1 or 2,400 GB RAID 5 internal SAS SSD; raw disk count not established |
| Network / transfer | Redundant 1 Gbps (East Japan 1) or 10 Gbps (East Japan 2/3); best-effort shared network; transfer billing not established |
| Physical location scope | Fukushima Shirakawa Data Center, Japan; East Japan 1/2/3 service regions |
| Location confidence | Bare-metal pricing page identifies the facility; region-specific interfaces |

**Caveats:** East Japan 1 has redundant 1 Gbps interfaces; East Japan 2/3 redundant 10 Gbps. Internal storage options are 400 GB RAID 1 or 2,400 GB RAID 5 using SAS SSDs and hot spare; exact included selection must be checked. 21+ nodes requires sales consultation. Hardware and stock may vary; no CPU/RAM/disk changes after order.

**First-party sources:** [Source 1](https://www.idcf.jp/cloud/baremetal/price/).

**Artwork discovery:** [Official product/brand page](https://www.idcf.jp/cloud/baremetal/price/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-servers-australia"></a>
### 66. Servers Australia

**Example:** Value Dedicated / Enterprise HPE ProLiant DL365 Gen11 · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Value family from AUD 99/month ex GST; selected hardware and other landing pages differ |
| CPU | Value: SKU dependent; Enterprise includes HPE ProLiant DL365 Gen11 options |
| Memory | Configuration dependent |
| Disk / storage | Configuration dependent |
| Network / transfer | Family advertises 2 × 10 Gbps switch ports; Internet entitlement is separate |
| Physical location scope | Sydney SY3/SY4; Brisbane BR1; Melbourne ME1; Perth PE2, AU |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not pair the AUD 99 Value minimum with the Enterprise Gen11 hardware. Other site pages show different starting prices; marketplace basket controls.

**First-party sources:** [Source 1](https://www.serversaustralia.com.au/products-services/dedicated-servers) · [Source 2](https://www.serversaustralia.com.au/marketplace/buy-dedicated-servers).

**Artwork discovery:** [Official product/brand page](https://www.serversaustralia.com.au/products-services/dedicated-servers). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-digital-pacific"></a>
### 67. Digital Pacific

**Example:** X-C6620-2 — Dell PowerEdge C6620 node · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | AUD 473/month displayed; billing-cycle widget contains inconsistent equivalent figures, so checkout must confirm |
| CPU | 2 × Intel Xeon Gold 5415+; 16 total physical cores; 2.9 GHz |
| Memory | 64 GB DDR5 |
| Disk / storage | 4 × 480 GB SSD; RAID 10; advertised usable 960 GB |
| Network / transfer | 5 TB monthly transfer; public port speed requires confirmation |
| Physical location scope | Sydney, Australia |
| Location confidence | Dedicated page explicitly locates its server fleet in Sydney |

**Caveats:** Australian storefront; confirm currency and tax. Use the primary displayed rate, not the contradictory half/third-price widget equivalents. Dedicated physical compute node in shared blade chassis; shared chassis remains a failure domain. Stock is only a snapshot.

**First-party sources:** [Source 1](https://www.digitalpacific.com.au/dedicated/dedicated-servers/).

**Artwork:** [digital-pacific-c6620](#asset-digital-pacific-c6620), [digital-pacific-m630](#asset-digital-pacific-m630), [digital-pacific-r620](#asset-digital-pacific-r620). Classifications and permissions are below.

<a id="provider-ransomit"></a>
### 68. RansomIT

**Example:** ME2-E-2136-64GB-2x500GBNVME-10G · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 165/month in selected USD storefront |
| CPU | Intel Xeon E-2136; 6 cores; 3.3 GHz |
| Memory | 64 GB |
| Disk / storage | 2 × 500 GB NVMe |
| Network / transfer | 10 Gbps port; 20 TB monthly data; 1 IPv4 and IPv6 /64 |
| Physical location scope | Melbourne, Australia; selected product says Equinix ME2 |
| Location confidence | Product-row site; category-header ME1 discrepancy recorded |

**Caveats:** Product row explicitly says Equinix ME2 although the category heading says ME1; selected row wins provisionally and must be confirmed. USD is explicit; do not assume AUD. One unit shown available, not a bulk reservation. Other city catalogs have separate hardware and prices.

**First-party sources:** [Source 1](https://secure.ransomit.com.au/index.php?rp=/store/melbourne-dedicated-servers) · [Source 2](https://www.ransomit.com.au/).

**Artwork discovery:** [Official product/brand page](https://secure.ransomit.com.au/index.php?rp=/store/melbourne-dedicated-servers). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-donweb"></a>
### 69. DonWeb

**Example:** Servidores Dedicados · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Current catalog/configurator; exact basket not captured |
| CPU | Physical dedicated servers; exact configuration required |
| Memory | Configure |
| Disk / storage | Configure |
| Network / transfer | Verify included transfer, port and international connectivity |
| Physical location scope | Latin American service; exact physical site must be confirmed, not inferred from customer country |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Keep physical dedicated offers separate from cloud/VPS and Proxmox virtual packages. Country remains unknown until the dedicated order location is verified.

**First-party sources:** [Source 1](https://donweb.com/en-int/servidores-dedicados) · [Source 2](https://donweb.com/).

**Artwork discovery:** [Official product/brand page](https://donweb.com/en-int/servidores-dedicados). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-afrihost"></a>
### 70. Afrihost

**Example:** Bronze Self-Managed Dedicated · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | ZAR 1,350/month; free setup |
| CPU | Intel Xeon E3-1230; 4 cores; 3.2 GHz |
| Memory | 8 GB DDR3 1333 MHz |
| Disk / storage | 2 × 1 TB enterprise disks; RAID 1 |
| Network / transfer | 1 Gbps; unlimited traffic subject to terms |
| Physical location scope | South Africa; exact hosting facility to confirm |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Month-to-month. Provider retains hardware ownership; this is rental, not colocation or purchased hardware.

**First-party sources:** [Source 1](https://www.afrihost.com/dedicated-hosting).

**Artwork discovery:** [Official product/brand page](https://www.afrihost.com/dedicated-hosting). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-amazon-web-services"></a>
### 71. Amazon Web Services

**Example:** EC2 m7i.metal-24xl · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Region-specific hourly On-Demand price; exact primary-source price not captured |
| CPU | 4th-generation Intel Xeon Scalable; 96 vendor vCPUs, not 96 physical cores |
| Memory | 384 GiB |
| Disk / storage | EBS-only; no included local instance store |
| Network / transfer | 37.5 Gbps instance network; 30 Gbps EBS bandwidth. Internet egress and EBS are separately billed. |
| Physical location scope | Only regions offering this exact .metal instance type |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Only the .metal SKU is physical bare metal. Ordinary EC2 instances, dedicated tenancy and Dedicated Hosts are different products. Never treat internal network bandwidth as included Internet transit.

**First-party sources:** [Source 1](https://aws.amazon.com/ec2/instance-types/m7i/) · [Source 2](https://docs.aws.amazon.com/ec2/latest/instancetypes/gp.html) · [Source 3](https://aws.amazon.com/ec2/pricing/on-demand/).

**Artwork discovery:** [Official product/brand page](https://aws.amazon.com/ec2/instance-types/m7i/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-oracle-cloud"></a>
### 72. Oracle Cloud

**Example:** BM.Standard.E5.192 · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Current compute, memory and network rate quotation required |
| CPU | AMD EPYC 9J14; 192 vendor OCPUs; 2.4–3.7 GHz |
| Memory | 2,304 GB |
| Disk / storage | Remote block storage; no local data disk in this shape |
| Network / transfer | 1 × 100 Gbps NIC; Internet egress and block storage priced separately |
| Physical location scope | Select a region and availability domain that supports E5 bare metal |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** A 2023 launch price was not assumed current in September 2026. OCPU meaning is shape/architecture dependent: preserve the vendor unit rather than imposing one universal conversion.

**First-party sources:** [Source 1](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm) · [Source 2](https://www.oracle.com/cloud/compute/pricing/).

**Artwork discovery:** [Official product/brand page](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-alibaba-cloud"></a>
### 73. Alibaba Cloud

**Example:** Elastic Bare Metal ecs.ebmg7.32xlarge · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Regional ECS calculator / console pricing |
| CPU | Intel Xeon Platinum 8369B; 128 vendor vCPUs; 2.9 GHz / 3.5 GHz all-core turbo |
| Memory | 512 GiB |
| Disk / storage | Cloud ESSD storage, separately configured |
| Network / transfer | 64 Gbps instance network; 32 Gbps disk bandwidth; public Internet charging is separate |
| Physical location scope | Exact region and zone must support this EBM instance family |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Physical single-tenant Elastic Bare Metal, not normal ECS VMs. Source overview updated August 17, 2026. Do not translate 128 vCPUs into 128 physical cores.

**First-party sources:** [Source 1](https://www.alibabacloud.com/help/en/ecs/user-guide/elastic-bare-metal-server-overview) · [Source 2](https://www.alibabacloud.com/help/en/ecs/user-guide/create-an-ecs-bare-metal-instance).

**Artwork discovery:** [Official product/brand page](https://www.alibabacloud.com/help/en/ecs/user-guide/elastic-bare-metal-server-overview). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-tencent-cloud"></a>
### 74. Tencent Cloud

**Example:** Cloud Bare Metal (CBM) · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Compute + system/data disks + network charged separately; console quote |
| CPU | Exact CBM physical-server model must be selected |
| Memory | Configure |
| Disk / storage | Configure system/data disks |
| Network / transfer | Separately billed networking; exact port and allowance not captured |
| Physical location scope | Select a CBM-supported region; generic Tencent Cloud region map is not SKU availability |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Physical bare-metal product confirmed; no matched current public configuration/price was captured. Do not seed invented host specifications.

**First-party sources:** [Source 1](https://www.tencentcloud.com/product/cbm) · [Source 2](https://www.tencentcloud.com/document/product/1171/52407) · [Source 3](https://www.tencentcloud.com/document/product/1171/52409).

**Artwork discovery:** [Official product/brand page](https://www.tencentcloud.com/product/cbm). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-huawei-cloud"></a>
### 75. Huawei Cloud

**Example:** BMS physical.s4.xlarge (China pricing) · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | CNY 6,560/month estimated configuration price; checkout controls |
| CPU | Intel Skylake V5; 28 physical cores |
| Memory | 192 GB |
| Disk / storage | Cloud-disk capable; included disk capacity not established |
| Network / transfer | 10 Gigabit Ethernet NIC; public EIP/Internet bandwidth is a separate charge |
| Physical location scope | China product catalog; exact region/zone must be selected |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not combine China CNY rates with international USD configurations. The 10 GE interface does not imply a free 10 Gbps public Internet connection.

**First-party sources:** [Source 1](https://www.huaweicloud.com/product/bms.html) · [Source 2](https://www.huaweicloud.com/intl/en-us/product/bms.html) · [Source 3](https://support.huaweicloud.com/intl/en-us/productdesc-bms/bms_01_0001.html).

**Artwork:** [huawei-cloud-bms](#asset-huawei-cloud-bms). Classifications and permissions are below.

<a id="provider-shinjiru"></a>
### 76. Shinjiru

**Example:** E3 Premium — Malaysia · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From USD 119.90/month |
| CPU | Intel Xeon E3; 4 cores; exact E3 model not stated |
| Memory | 32 GB DDR4 |
| Disk / storage | 2 × 2 TB enterprise HDD |
| Network / transfer | Advertised 1 Gbps unmetered but plan lists Speed 300 Mbps; T&C apply |
| Physical location scope | Malaysia |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Keep the 1 Gbps headline and 300 Mbps plan speed as distinct unresolved fields. No-setup wording includes a 12-month condition; do not assume monthly orders have no setup charge.

**First-party sources:** [Source 1](https://www.shinjiru.com/offshore-web-hosting/offshore-dedicated-server-business/).

**Artwork discovery:** [Official product/brand page](https://www.shinjiru.com/offshore-web-hosting/offshore-dedicated-server-business/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-i3d-net"></a>
### 77. i3D.net

**Example:** bm9.hmm.12 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From USD 213/month; varies by region |
| CPU | AMD EPYC 4464P; 12 cores / 24 threads; 3.75–5.40 GHz |
| Memory | 128 GB DDR5 |
| Disk / storage | 1.92 TB NVMe |
| Network / transfer | Egress billed per GB: Europe USD 0.0021; North America 0.0030; Latin America 0.0107; APAC 0.0118; Oceania 0.0176; Middle East 0.0334; Africa 0.0468. Exact public port/commit requires order. |
| Physical location scope | 60+ advertised global sites; supported SKU/stock and rate differ by region |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Physical single tenant explicitly confirmed. Committed dedicated and hourly Bare Metal Cloud have different pricing modes. Provider backbone capacity is not per-server bandwidth.

**First-party sources:** [Source 1](https://www.i3d.net/bare-metal-servers/) · [Source 2](https://www.i3d.net/global-bare-metal-servers/) · [Source 3](https://www.i3d.net/bare-metal-cloud/).

**Artwork:** [i3d-net-bare-metal-hero](#asset-i3d-net-bare-metal-hero). Classifications and permissions are below.

<a id="provider-gabia"></a>
### 78. Gabia

**Example:** One-minute rental — HP DL160 Gen10 SSD · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | KRW 150,000/month, excluding VAT |
| CPU | Intel Xeon Bronze 3204; 6 cores; 1.9 GHz |
| Memory | 16 GB DDR4 |
| Disk / storage | 480 GB SSD + 1 TB SATA 7,200 RPM HDD |
| Network / transfer | 10 Mbps included circuit in plan; generic feature says 1 Gbps uplink. Extra contracted network/power/backup usage is billed. |
| Physical location scope | South Korea; exact Gabia IDC site must be confirmed |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Pure hardware rental without term commitment or purchase requirement. Preserve 10 Mbps contracted allowance separately from 1 Gbps uplink; do not advertise 1 Gbps unlimited.

**First-party sources:** [Source 1](https://idc.gabiacloud.com/server/onemin).

**Artwork discovery:** [Official product/brand page](https://idc.gabiacloud.com/server/onemin). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-idcloudhost"></a>
### 79. IDCloudHost

**Example:** Bare Metal Dedicated Server · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From IDR 2,500,000/month |
| CPU | Exact physical-server SKU requires sales/configurator |
| Memory | Configure |
| Disk / storage | Configure |
| Network / transfer | Quote port, domestic/international transfer and overages |
| Physical location scope | Provider footprint includes Bogor, Jakarta and Cibitung ID, plus Singapore; dedicated SKU location must be quoted |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Homepage lists physical bare metal but retrieved minimum is not paired with a complete host configuration. Do not import third-party Xeon/RAM claims into this price.

**First-party sources:** [Source 1](https://idcloudhost.com/).

**Artwork discovery:** [Official product/brand page](https://idcloudhost.com/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-vinahost"></a>
### 80. VinaHost

**Example:** Xeon Quad Core E3 v1-2-3 Series Basic · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 94.03/month advertised with 36-month selection; verify prepaid total |
| CPU | Intel Xeon E3-1230 v2; 4 cores / 8 threads; 3.3–3.7 GHz |
| Memory | 8 GB DDR3 |
| Disk / storage | 240 GB SSD OR 500 GB HDD; SSD selected for catalog example |
| Network / transfer | Shared 100/10 Mbps displayed; unlimited transfer. Meaning of the two speed components must be confirmed. |
| Physical location scope | Vietnam; exact physical city/facility to confirm |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not present the long-term equivalent as cancel-anytime monthly pricing. Preserve the split network label rather than silently assuming a 100 Mbps international circuit.

**First-party sources:** [Source 1](https://vinahost.vn/en/server/).

**Artwork discovery:** [Official product/brand page](https://vinahost.vn/en/server/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-radore"></a>
### 81. Radore

**Example:** Dell R630 — 64 GB · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 259/month |
| CPU | 2 × Intel Xeon E5-2680 v4 |
| Memory | 64 GB |
| Disk / storage | 2 × 960 GB SSD |
| Network / transfer | 100 Mbps–1 Gbps unlimited Internet options; exact included selected port to confirm; 10 Gbps optional |
| Physical location scope | Turkey; physical facility must be confirmed for the order |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not treat the top of a configurable 100 Mbps–1 Gbps range as a guaranteed included port. /29 IP block advertised.

**First-party sources:** [Source 1](https://radore.com/services/dedicated).

**Artwork discovery:** [Official product/brand page](https://radore.com/services/dedicated). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-turhost"></a>
### 82. Turhost

**Example:** E65 Sunucu · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Regular USD 219.77/month; first 3 months promotion USD 79.99/month |
| CPU | Intel Xeon Silver 4214R; 12 cores / 24 threads; 2.4–3.5 GHz |
| Memory | 32 GB ECC |
| Disk / storage | 2 × 480 GB enterprise SSD; hardware RAID 1 |
| Network / transfer | 1 Gbps exclusive port; 5,000 GB monthly transfer |
| Physical location scope | Turkey; exact dedicated facility to confirm |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Budget the regular rate, not the 3-month incentive forever. RAID 1 is approximately 480 GB usable before filesystem overhead.

**First-party sources:** [Source 1](https://www.turhost.com/sunucu/dedicated-server/).

**Artwork discovery:** [Official product/brand page](https://www.turhost.com/sunucu/dedicated-server/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-hosterion"></a>
### 83. Hosterion

**Example:** ds_IN!_v4 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | EUR 229/month unmanaged |
| CPU | Intel Xeon Gold; 44 cores / 88 threads; exact model not stated |
| Memory | 64 GB |
| Disk / storage | 2 × 1 TB SSD |
| Network / transfer | Public IPv4 and IPv6 /64; exact port and transfer allowance require quote |
| Physical location scope | Dedicated facility not established by the retrieved product page; do not infer from Romanian headquarters |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Management is an additional EUR 125/month, not included. Country intentionally unknown until dedicated site confirmed.

**First-party sources:** [Source 1](https://hosterion.com/dedicated-servers).

**Artwork:** [hosterion-racks](#asset-hosterion-racks). Classifications and permissions are below.

<a id="provider-inmotion-hosting"></a>
### 84. InMotion Hosting

**Example:** Advanced Dedicated · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 149.99/month on 12-month term; shown renewal USD 149.99 |
| CPU | Intel Xeon E-2176G or specified equivalent; 6 cores / 12 threads |
| Memory | 64 GB DDR4 |
| Disk / storage | 2 × 1.92 TB SSD; software RAID 1 |
| Network / transfer | 1 Gbps unmetered; 10 IPv4 addresses |
| Physical location scope | Select available dedicated region; US offering used for this catalog example |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Region and management mode can change pricing; some selections show USD 179.99. CPU asterisk permits equivalent hardware. Verify root/reimage policy before using as a runner pool.

**Supply-chain note:** Investigate supply/company relationship with OpenMetal; do not assume independent. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://www.inmotionhosting.com/dedicated-servers).

**Artwork discovery:** [Official product/brand page](https://www.inmotionhosting.com/dedicated-servers). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-dreamhost"></a>
### 85. DreamHost

**Example:** Standard Dedicated — 16 GB · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 165/month annual equivalent; annual prepayment |
| CPU | AMD EPYC; 6 physical cores; exact model unspecified |
| Memory | 16 GB |
| Disk / storage | 480 GB SSD advertised, with RAID 1; drive count and raw-versus-usable capacity unresolved |
| Network / transfer | Unmetered subject to policy; port speed not published in captured plan |
| Physical location scope | US data centers; exact site must be confirmed |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Managed physical server, not DreamCompute VM. Do not assume 480 GB raw when RAID display may describe usable capacity. Reimage can incur USD 100; verify current service terms.

**First-party sources:** [Source 1](https://www.dreamhost.com/hosting/dedicated/) · [Source 2](https://help.dreamhost.com/hc/en-us/articles/215279658-Dedicated-server-overview).

**Artwork discovery:** [Official product/brand page](https://www.dreamhost.com/hosting/dedicated/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-serverpoint"></a>
### 86. ServerPoint

**Example:** Xeon E3-1275 v6 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 79/month |
| CPU | Intel Xeon E3-1275 v6; 4 cores / 8 threads |
| Memory | 32 GB DDR4 |
| Disk / storage | 1 × 960 GB SSD |
| Network / transfer | 2 × 1 Gbps NIC; 70 TB monthly transfer; aggregated public throughput not assumed |
| Physical location scope | Nevada and Texas US dedicated footprint; select SKU-specific site |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** VDS products are excluded. Two NICs do not establish a 2 Gbps Internet entitlement.

**First-party sources:** [Source 1](https://www.serverpoint.com/en/bare-metal-dedicated-server/all-dedicated-servers/) · [Source 2](https://www.serverpoint.com/).

**Artwork discovery:** [Official product/brand page](https://www.serverpoint.com/en/bare-metal-dedicated-server/all-dedicated-servers/). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-psychz-networks"></a>
### 87. Psychz Networks

**Example:** cMetal / Single CPU Xeon Dedicated · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | Live inventory / custom quote |
| CPU | Single/dual Xeon physical server; exact SKU required |
| Memory | Single-CPU family 16/32 GB options; selected configuration required |
| Disk / storage | Up to 4 drive positions; installed drive capacity requires order |
| Network / transfer | 100 Mbps to 40 Gbps options; metered or unmetered; exact traffic package must be selected |
| Physical location scope | Los Angeles, Dallas, Chicago, Atlanta, Ashburn US; São Paulo BR; London GB; Amsterdam NL; Moscow RU; Barcelona ES; Johannesburg ZA; Mumbai IN; Singapore SG; Taipei TW; Seoul KR; Tokyo JP; Sydney AU |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** These are dedicated-service location listings, not guaranteed inventory for every SKU. cVirtual is excluded; cMetal supports physical provisioning. Vendor private network and public transit are distinct.

**Supply-chain note:** Profuse Solutions / Psychz. This is not a fully audited ownership graph.

**First-party sources:** [Source 1](https://www.psychz.net/dedicated-hosting.html).

**Artwork discovery:** [Official product/brand page](https://www.psychz.net/dedicated-hosting.html). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="provider-sharktech"></a>
### 88. Sharktech

**Example:** Dedicated Servers · **Evidence:** partial or quote required · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | From USD 219/month; exact configured basket not captured |
| CPU | Physical dedicated hardware; select current inventory |
| Memory | Configure |
| Disk / storage | Configure |
| Network / transfer | 1–40 Gbps family options; metered/unmetered terms depend on order |
| Physical location scope | Provider location selector; exact dedicated sites must be verified |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Do not confuse 40/100 Gbps backbone links with each server public port. Dynamic inventory did not expose a matched current configuration.

**First-party sources:** [Source 1](https://sharktech.net/) · [Source 2](https://sharktech.net/dedicated-servers/).

**Artwork:** [sharktech-dedicated](#asset-sharktech-dedicated), [sharktech-benefits](#asset-sharktech-benefits). Classifications and permissions are below.

<a id="provider-adentro-tecnologia"></a>
### 89. Adentro Tecnologia

**Example:** Dedicado Light · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | BRL 890/month on product page; older homepage minimum BRL 1,490 differs |
| CPU | 2 × Xeon E5-2680 v4; 28 cores / 56 threads |
| Memory | 64 GB DDR4 |
| Disk / storage | 2 × 100 GB SSD RAID 1 for OS, plus 250 GB Pure Storage all-flash allocation |
| Network / transfer | Literal “1 GB com tráfego ilimitado”; unlimited transfer, speed unit requires confirmation |
| Physical location scope | Brazil; product confirms national data centers, not an exact selected city |
| Location confidence | Country-only physical-service confirmation |

**Caveats:** Brazilian Adentro, not adentro.com. Selected product price supersedes homepage family minimum for this record; confirm commercial terms. Pure Storage all-flash allocation is remote/shared storage capacity, not another local physical disk. Network page says “1 GB”; its speed unit is ambiguous.

**First-party sources:** [Source 1](https://adentro.com.br/solucoes/servidor-dedicado/) · [Source 2](https://adentro.com.br/).

**Artwork:** [adentro-tecnologia-datacenter](#asset-adentro-tecnologia-datacenter), [adentro-tecnologia-mark](#asset-adentro-tecnologia-mark). Classifications and permissions are below.

<a id="provider-serverpronto"></a>
### 90. ServerPronto

**Example:** Power — Xeon E3-1230 v2 · **Evidence:** specified example · **Observed:** 2026-09-16

| Field | Researched value / qualification |
|---|---|
| Price | USD 59.95/month |
| CPU | Intel Xeon E3-1230 v2; 4 cores / 8 threads; 3.3 GHz |
| Memory | 16 GB DDR3 |
| Disk / storage | 240 GB SSD |
| Network / transfer | 10 TB transfer; selected public port requires confirmation |
| Physical location scope | US dedicated service; exact physical facility must be confirmed |
| Location confidence | provider footprint; confirm SKU availability |

**Caveats:** Legacy CPU intentionally retained as a real low-cost class; do not equate its four cores with modern EPYC cores.

**First-party sources:** [Source 1](https://www.serverpronto.com/dedicated).

**Artwork discovery:** [Official product/brand page](https://www.serverpronto.com/dedicated). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.

<a id="artwork"></a>
## 7. Artwork, flags and maps

### Direct artwork manifest — 35 links

These URLs were extracted from official provider pages or their official asset hosts. `web_rendered` means the image was actually rendered during research; SVG links marked `official_link_resolved_not_rendered` were identified but not raster-rendered. One HostDime link failed to fetch and is retained only as an explicitly flagged lead. No local copies, hashes, universal reuse rights or long-term CDN availability are claimed.

**Hetzner is the strongest starting set in this handoff:** 12 press-kit images/badges plus two dedicated-product illustrations. The [official pressroom](https://www.hetzner.com/pressroom/) gives conditions: attribute Hetzner Online GmbH; keep usage related to Hetzner; notify its press contact; obtain written approval for edits. Those press-kit terms must not be automatically extended to marketing assets elsewhere on the site. A “hosted by” badge could imply a real commercial relationship, so omit it from a future-network concept unless the context is unmistakable.

**Recommended asset treatment:** large facility photos for supplier/country headers; model photos on expanded cards where the actual model matches; provider logos as small secondary identity marks; a consistent Forkalope-owned generic chassis illustration for all other node cards. A CPU model does not identify the chassis. Cropping, recoloring or removing logos may require separate permission. Do not hotlink unapproved third-party assets in production; after approval, retain original/source metadata, sanitize SVG and publish controlled derivatives on your own asset host.

<a id="asset-hetzner-logo"></a>
#### Hetzner — Provider logo

[Direct image](https://cdn.hetzner.com/assets/Uploads/hetzner_logo_server_cloud_hosting_thumbnail.webp) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `provider_logo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-hosted-by"></a>
#### Hetzner — Hosted-by badge

[Direct image](https://cdn.hetzner.com/assets/Uploads/hetzner_logo_hosted_by_thumbnail-v2.webp) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `endorsement_badge` · Retrieval: `web_rendered`. Do not imply an actual hosting relationship in a future-network mockup.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-fsn-exterior-1"></a>
#### Hetzner — Falkenstein exterior 1

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Falkenstein-DC-1.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `facility_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-fsn-exterior-2"></a>
#### Hetzner — Falkenstein exterior 2

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Falkenstein-DC-2.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `facility_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-fsn-exterior-3"></a>
#### Hetzner — Falkenstein exterior 3

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Falkenstein-DC-3.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `facility_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-fsn-exterior-4"></a>
#### Hetzner — Falkenstein exterior 4

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Falkenstein-DC-4.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `facility_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-fsn-flags"></a>
#### Hetzner — Falkenstein flags

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Falkenstein-DC-5.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `facility_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-fsn-aerial"></a>
#### Hetzner — Falkenstein campus aerial

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Falkenstein-DC-6-Print.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `facility_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-fsn-aisle"></a>
#### Hetzner — Falkenstein server aisle, portrait

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Falkenstein-DC-6.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `facility_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-technical"></a>
#### Hetzner — Technical workbench

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Technik.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `operations_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-trade-show"></a>
#### Hetzner — Trade-show photograph

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Messe.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `brand_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-server-tray"></a>
#### Hetzner — Technician and server tray

[Direct image](https://cdn.hetzner.com/assets/Uploads/Hetzner-Pressefotos-Server.png) · [Official source page](https://www.hetzner.com/pressroom/)

Type: `operations_photo` · Retrieval: `web_rendered`. Not an exact AX42 chassis photograph.

Rights: Hetzner press-kit conditions described above; not an unrestricted license.

<a id="asset-hetzner-ax-family"></a>
#### Hetzner — AX family AMD processor illustration

[Direct image](https://cdn.hetzner.com/assets/Uploads/ax42_website_matrix.webp) · [Official source page](https://www.hetzner.com/dedicated-rootserver/matrix-ax/)

Type: `product_family_illustration` · Retrieval: `web_rendered`. Marketing illustration, not a physical AX42 photograph. Press-kit permission does not automatically cover this marketing asset.

Rights: Permission not established; review before reuse.

<a id="asset-hetzner-sx-family"></a>
#### Hetzner — SX storage family illustration

[Direct image](https://cdn.hetzner.com/assets/Uploads/sx-line_website-matrix_big.jpg) · [Official source page](https://www.hetzner.com/dedicated-rootserver/matrix-sx/)

Type: `product_family_illustration` · Retrieval: `web_rendered`. Storage hero, not an exact installed drive layout. Separate permission review.

Rights: Permission not established; review before reuse.

<a id="asset-exabytes-dedicated-icon"></a>
#### Exabytes — Dedicated-server product icon

[Direct image](https://www.exabytes.my/wp-content/uploads/product-icon-dedicated-server.svg) · [Official source page](https://www.exabytes.my/servers/dedicated-server)

Type: `product_illustration` · Retrieval: `official_link_resolved_not_rendered`. 

Rights: Permission not established; review before reuse.

<a id="asset-exabytes-hero"></a>
#### Exabytes — Server / operator marketing composite

[Direct image](https://www.exabytes.my/wp-content/uploads/1050x650-sidebanner-server-data-center.png) · [Official source page](https://www.exabytes.my/servers/dedicated-server)

Type: `marketing_composite` · Retrieval: `web_rendered`. Do not label this a verified Exabytes facility photograph.

Rights: Permission not established; review before reuse.

<a id="asset-gcore-server-stack"></a>
#### Gcore — Server-stack illustration

[Direct image](https://assets.gcore.pro/site-media/uploads/fi_2_b0b2bfb9dd.png) · [Official source page](https://gcore.com/hosting/dedicated/hong-kong)

Type: `product_illustration` · Retrieval: `web_rendered`. Generic illustration, not a chassis model.

Rights: Permission not established; review before reuse.

<a id="asset-hosterion-racks"></a>
#### Hosterion — Dedicated-server rack photograph

[Direct image](https://hosterion.com/img-content/dedicated-servers.jpg) · [Official source page](https://hosterion.com/dedicated-servers)

Type: `hardware_photo` · Retrieval: `web_rendered`. No claim that these chassis are the ds_IN!_v4 configuration.

Rights: Permission not established; review before reuse.

<a id="asset-racknerd-server-icon"></a>
#### RackNerd — Server product icon

[Direct image](https://www.racknerd.com/images/service-icon-3.png) · [Official source page](https://www.racknerd.com/)

Type: `product_illustration` · Retrieval: `web_rendered`. 

Rights: Permission not established; review before reuse.

<a id="asset-racknerd-logo-dark"></a>
#### RackNerd — Provider logo for dark background

[Direct image](https://www.racknerd.com/images/logo-footer.png) · [Official source page](https://www.racknerd.com/)

Type: `provider_logo` · Retrieval: `web_rendered`. White wordmark needs dark background.

Rights: Permission not established; review before reuse.

<a id="asset-sharktech-dedicated"></a>
#### Sharktech — Dedicated-server illustration

[Direct image](https://sharktech.net/wp-content/uploads/2023/04/what-are-dedicated-servers.svg) · [Official source page](https://sharktech.net/dedicated-servers/)

Type: `product_illustration` · Retrieval: `official_link_resolved_not_rendered`. 

Rights: Permission not established; review before reuse.

<a id="asset-sharktech-benefits"></a>
#### Sharktech — Dedicated-hosting benefits illustration

[Direct image](https://sharktech.net/wp-content/uploads/2023/04/benefits-dedicated-hosted-servers.svg) · [Official source page](https://sharktech.net/dedicated-servers/)

Type: `product_illustration` · Retrieval: `official_link_resolved_not_rendered`. 

Rights: Permission not established; review before reuse.

<a id="asset-bacloud-logo"></a>
#### Bacloud — Provider green logo

[Direct image](https://www.bacloud.com/templates/bc-twenty-one-qloud/assets/images/logo/bacloud_green.svg) · [Official source page](https://www.bacloud.com/en/dedicated-servers)

Type: `provider_logo` · Retrieval: `official_link_resolved_not_rendered`. 

Rights: Permission not established; review before reuse.

<a id="asset-adentro-tecnologia-datacenter"></a>
#### Adentro Tecnologia — Data-center operations photograph

[Direct image](https://adentro.com.br/wp-content/uploads/2025/05/datacenter-adentro.png) · [Official source page](https://adentro.com.br/)

Type: `operations_photo` · Retrieval: `web_rendered`. No exact facility coordinates implied.

Rights: Permission not established; review before reuse.

<a id="asset-adentro-tecnologia-mark"></a>
#### Adentro Tecnologia — Institutional icon

[Direct image](https://adentro.com.br/wp-content/uploads/2025/06/adentro-icone-01.svg) · [Official source page](https://adentro.com.br/)

Type: `provider_logo` · Retrieval: `official_link_resolved_not_rendered`. 

Rights: Permission not established; review before reuse.

<a id="asset-i3d-net-bare-metal-hero"></a>
#### i3D.net — Dedicated-server header illustration

[Direct image](https://www.i3d.net/wp-content/uploads/Header-Dedicated-Servers_Header.svg) · [Official source page](https://www.i3d.net/bare-metal-servers/)

Type: `product_illustration` · Retrieval: `official_link_resolved_not_rendered`. 

Rights: Permission not established; review before reuse.

<a id="asset-huawei-cloud-bms"></a>
#### Huawei Cloud — BMS product illustration

[Direct image](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/yunying/BMS-2024/buy-zp_1.svg) · [Official source page](https://www.huaweicloud.com/product/bms.html)

Type: `product_illustration` · Retrieval: `official_link_resolved_not_rendered`. 

Rights: Permission not established; review before reuse.

<a id="asset-interserver-dedicated"></a>
#### InterServer — Dedicated-server illustration

[Direct image](https://www.interserver.net/dedicated/assets/images/dedi.webp) · [Official source page](https://www.interserver.net/dedicated/)

Type: `product_illustration` · Retrieval: `web_rendered`. 

Rights: Permission not established; review before reuse.

<a id="asset-interserver-datacenter"></a>
#### InterServer — Isometric data-center illustration

[Direct image](https://www.interserver.net/dedicated/assets/images/datac.webp) · [Official source page](https://www.interserver.net/dedicated/)

Type: `facility_illustration` · Retrieval: `web_rendered`. Illustration, not a photograph.

Rights: Permission not established; review before reuse.

<a id="asset-interserver-network"></a>
#### InterServer — Global-network illustration

[Direct image](https://www.interserver.net/dedicated/assets/images/network.webp) · [Official source page](https://www.interserver.net/dedicated/)

Type: `network_illustration` · Retrieval: `web_rendered`. Not evidence of InterServer worldwide physical sites.

Rights: Permission not established; review before reuse.

<a id="asset-hostdime-logo"></a>
#### HostDime — HostDime logo with slogan

[Direct image](https://www.hostdime.com/images/identity/HostDime_Logo_Slogan_420_100.png) · [Official source page](https://www.hostdime.com/about/identity)

Type: `provider_logo` · Retrieval: `web_rendered`. Official identity page offers multiple formats; confirm current brand-use terms.

Rights: Permission not established; review before reuse.

<a id="asset-hostdime-logo-no-slogan"></a>
#### HostDime — HostDime logo without slogan

[Direct image](https://www.hostdime.com/images/identity/HostDime_Logo_390_80.png) · [Official source page](https://www.hostdime.com/about/identity)

Type: `provider_logo` · Retrieval: `official_link_fetch_failed`. Official link extracted, but image fetch failed. Do not mark production-ready.

Rights: Permission not established; review before reuse.

<a id="asset-digital-pacific-c6620"></a>
#### Digital Pacific — Dell PowerEdge C6620 node front

[Direct image](https://www.digitalpacific.com.au/wp-content/uploads/2024/05/image-2024-6-12_12-57-23.png) · [Official source page](https://www.digitalpacific.com.au/dedicated/dedicated-servers/)

Type: `chassis_model_photo` · Retrieval: `web_rendered`. Shown with C6620 offers. Chassis/node family, not a photograph of the future rented unit.

Rights: Permission not established; review before reuse.

<a id="asset-digital-pacific-m630"></a>
#### Digital Pacific — Dell PowerEdge M630 blade

[Direct image](https://www.digitalpacific.com.au/wp-content/uploads/2019/10/M630.jpg) · [Official source page](https://www.digitalpacific.com.au/dedicated/dedicated-servers/)

Type: `chassis_model_photo` · Retrieval: `web_rendered`. Different model from the selected C6620 offer.

Rights: Permission not established; review before reuse.

<a id="asset-digital-pacific-r620"></a>
#### Digital Pacific — Dell PowerEdge R620 rack server

[Direct image](https://www.digitalpacific.com.au/wp-content/uploads/2019/10/r620.jpg) · [Official source page](https://www.digitalpacific.com.au/dedicated/dedicated-servers/)

Type: `chassis_model_photo` · Retrieval: `web_rendered`. Different model from the selected C6620 offer.

Rights: Permission not established; review before reuse.

### Country flags

Use [flag-icons](https://flagicons.lipis.dev/), which supplies ISO 3166-1 alpha-2 flags in SVG and publishes its MIT licensing and integration instructions. The companion country file uses the documented version `7.3.2` as a pinned example; inspect and retain the upstream license when vendoring. A generated flag URL is a path derived from the library convention, not an individually fetched/verified file. Prefer local package imports or a controlled CDN copy for production.

```html
<!-- With the flag-icons package CSS loaded -->
<span class="fi fi-de" aria-hidden="true"></span> Germany
<span class="fi fi-gb" aria-hidden="true"></span> United Kingdom
```

Show a readable country/territory name next to the flag. Use `GB`, not `UK`, as the alpha-2 key; do not use country flags as a substitute for interface language. Geographic market labels do not imply a position on sovereignty. The map and tables should handle country/territory categories consistently.

### Maps

[Natural Earth](https://www.naturalearthdata.com/) provides cartographic data, and its [terms](https://www.naturalearthdata.com/about/terms-of-use/) place its raster and vector data in the public domain. Start with a simplified world boundary layer for the globe/overview and a more detailed scale at country zoom. Version and document the chosen boundary treatment. Its generalized boundaries are not a data-center geocoder.

Use [MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/) for the interactive map and its [clustering example](https://maplibre.org/maplibre-gl-js/docs/examples/create-and-style-clusters/) as the first implementation reference. Basemap data, rendering library and tile-hosting service are separate dependencies with separate terms. Natural Earth assets and flag assets are links in this package, not downloaded map/flag files.

### Original illustration library to commission or generate

Create a cohesive set of 10–12 Forkalope-owned depictions: compact compute node; high-memory compute; NVMe-heavy server; HDD storage chassis; GPU server; blade node; remote-block-backed host; regional edge node; logical server pool; maintenance state; empty/unknown inventory. Use the same front/three-quarter angle, silhouette scale, lighting and neutral enclosure; overlay operational metadata in HTML rather than burning text into artwork. These are briefs, not generated assets delivered here.

For each reusable illustration, provide transparent 256/512 px variants and an SVG only when a real vector master exists. Never derive physical rack height, drive-bay count or chassis branding from an unknown model. A generic “storage node” drawing is honest; a very specific Dell chassis under an unrelated provider’s unverified product is not. The direct Digital Pacific photos are useful visual references for how genuinely different node/blade/rack families look, subject to rights review.

<a id="diligence"></a>
## 8. Procurement gaps, exclusions and refresh checklist

### Deliberate exclusions / qualification

Equinix Metal is not an active future supplier: its [official documentation](https://docs.equinix.com/metal/) records the June 30, 2026 sunset. Equinix data-center facilities used by other operators are a different matter; an operator renting colocation there is not selling the retired Metal product. VPS/VDS, dedicated-core VMs and shared GPU slices are not counted as physical servers simply because a page says “dedicated resources.” Hyperscaler `.metal`/bare-metal products are included with their cloud storage/network charging caveats.

Kimsufi/So you Start/Eco are represented under OVHcloud; Dedibox/Online under Scaleway; myLoc/servdiscount under one entry; SeFlow under Aruba; Database Mart/Server Mart under one entry. Brand counts are not independent ownership or failure-domain counts. Some other parent/supply relationships remain explicitly unverified. An aggregator can rent genuine physical hardware while still sharing an upstream site/operator with another brand in the catalog.

A managed dedicated service may be unsuitable for arbitrary reimaging or a Forkalope runner despite being a real physical server. A dedicated blade/node may still share enclosure power/network with neighbors. Access, supported operating systems, console/recovery API, secure boot, TPM, firmware control and provider abuse policies must be assessed before onboarding. Do not put tenant CI secrets on untrusted or unmanaged enrollment paths. These are proposed diligence requirements, not guarantees about any listed supplier.

### What still needs a quote or deeper verification

The `partial_or_quote_required` records remain research leads, not complete buyable baskets. The largest gaps are authenticated/dynamic enterprise pricing, exact facility availability, public-vs-private bandwidth detail, traffic direction/scope, promotion renewals, tax, setup, control-plane automation, and approved image licensing for most brands. Some specified offers also contain these gaps. Do not hide those limitations in the UI.

Before a real order, capture a dated quote for one exact SKU in one exact site: CPU/socket/core details; installed RAM and genuine ECC; each disk and RAID; remote storage; public/private ports and commit; transfer allowance and overage; IPv4/IPv6; DDoS policy; management/KVM/reimage; replacement and escalation; currency, tax, setup, commitment and renewal. Then confirm batch quantity and lead time. A webpage showing one unit in stock is not evidence of 500 available units.

For a refresh pipeline, retain source URL, retrieval method, fetched timestamp, content hash, parsed units and change diff. Monitor changed price/spec/location fields for review rather than overwriting trusted contract data. Respect provider site/API policies. Recheck asset delivery and permission independently of server pricing. Keep legacy/retired offers for historical node snapshots but remove them from an active procurement filter.

### Acceptance checks for the UI implementation

The fixture must load exactly 5,000 unique node IDs and 90 unique supplier records. Every node must join to an existing pool and offer. Country filters must retain correct counts; cleared filters restore the whole fleet. Aggregate tiles must expose unknown coverage. Limited-transfer and unmetered plans must remain distinguishable. Raw and usable storage cannot be swapped. Annual/committed prices cannot be relabeled month-to-month. Synthetic data must never be mistaken for actual production telemetry, and no destructive action may reach a live provider from the simulator.

The companion scripts run offline and rebuild the data deterministically. They do not automatically refresh prices or verify live URLs. To refresh, update the researched records and their source qualifications deliberately, then rebuild.
