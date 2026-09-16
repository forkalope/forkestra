#!/usr/bin/env python3
"""Build an offline, reproducible research handoff. No vendor APIs or purchases."""
from __future__ import annotations
import collections, copy, csv, datetime as dt, hashlib, json, pathlib, random, re, runpy, zipfile
from urllib.parse import urlparse
ROOT=pathlib.Path(__file__).resolve().parent
ctx=runpy.run_path(str(ROOT/'build_catalog.py'))
records=ctx['records']; by_id=ctx['by_id']
DATE='2026-09-16'
assets=[]
def asset(provider, slug, title, url, source, kind, status='web_rendered', rights='Permission not established; review before reuse', note=''):
    a=dict(id=f'{provider}-{slug}',provider_id=provider,title=title,url=url,source_page=source,kind=kind,
           retrieval_status=status,rights_status=rights,notes=note,checked_on=DATE,local_file=None,
           depicts_exact_rented_machine=False)
    assets.append(a);by_id[provider]['artwork'].append(a['id']);return a
press='https://www.hetzner.com/pressroom/'
hr='Press-kit terms: attribute Hetzner Online GmbH, use in a Hetzner-related context, notify press@hetzner.com; editing requires written consent. Reconfirm scope before public commercial UI use.'
het=[
('logo','Provider logo','hetzner_logo_server_cloud_hosting_thumbnail.webp','provider_logo'),
('hosted-by','Hosted-by badge','hetzner_logo_hosted_by_thumbnail-v2.webp','endorsement_badge'),
('fsn-exterior-1','Falkenstein exterior 1','Hetzner-Pressefotos-Falkenstein-DC-1.png','facility_photo'),
('fsn-exterior-2','Falkenstein exterior 2','Hetzner-Pressefotos-Falkenstein-DC-2.png','facility_photo'),
('fsn-exterior-3','Falkenstein exterior 3','Hetzner-Pressefotos-Falkenstein-DC-3.png','facility_photo'),
('fsn-exterior-4','Falkenstein exterior 4','Hetzner-Pressefotos-Falkenstein-DC-4.png','facility_photo'),
('fsn-flags','Falkenstein flags','Hetzner-Pressefotos-Falkenstein-DC-5.png','facility_photo'),
('fsn-aerial','Falkenstein campus aerial','Hetzner-Pressefotos-Falkenstein-DC-6-Print.png','facility_photo'),
('fsn-aisle','Falkenstein server aisle, portrait','Hetzner-Pressefotos-Falkenstein-DC-6.png','facility_photo'),
('technical','Technical workbench','Hetzner-Pressefotos-Technik.png','operations_photo'),
('trade-show','Trade-show photograph','Hetzner-Pressefotos-Messe.png','brand_photo'),
('server-tray','Technician and server tray','Hetzner-Pressefotos-Server.png','operations_photo')]
for slug,title,file,kind in het:
    note='Not an exact AX42 chassis photograph.'
    if slug=='hosted-by': note='Do not imply an actual hosting relationship in a future-network mockup.'
    asset('hetzner',slug,title,'https://cdn.hetzner.com/assets/Uploads/'+file,press,kind,rights=hr,note=note)
asset('hetzner','ax-family','AX family AMD processor illustration','https://cdn.hetzner.com/assets/Uploads/ax42_website_matrix.webp','https://www.hetzner.com/dedicated-rootserver/matrix-ax/','product_family_illustration',note='Marketing illustration, not a physical AX42 photograph. Press-kit permission does not automatically cover this marketing asset.')
asset('hetzner','sx-family','SX storage family illustration','https://cdn.hetzner.com/assets/Uploads/sx-line_website-matrix_big.jpg','https://www.hetzner.com/dedicated-rootserver/matrix-sx/','product_family_illustration',note='Storage hero, not an exact installed drive layout. Separate permission review.')
extra=[
('exabytes','dedicated-icon','Dedicated-server product icon','https://www.exabytes.my/wp-content/uploads/product-icon-dedicated-server.svg','https://www.exabytes.my/servers/dedicated-server','product_illustration','official_link_resolved_not_rendered',''),
('exabytes','hero','Server / operator marketing composite','https://www.exabytes.my/wp-content/uploads/1050x650-sidebanner-server-data-center.png','https://www.exabytes.my/servers/dedicated-server','marketing_composite','web_rendered','Do not label this a verified Exabytes facility photograph.'),
('gcore','server-stack','Server-stack illustration','https://assets.gcore.pro/site-media/uploads/fi_2_b0b2bfb9dd.png','https://gcore.com/hosting/dedicated/hong-kong','product_illustration','web_rendered','Generic illustration, not a chassis model.'),
('hosterion','racks','Dedicated-server rack photograph','https://hosterion.com/img-content/dedicated-servers.jpg','https://hosterion.com/dedicated-servers','hardware_photo','web_rendered','No claim that these chassis are the ds_IN!_v4 configuration.'),
('racknerd','server-icon','Server product icon','https://www.racknerd.com/images/service-icon-3.png','https://www.racknerd.com/','product_illustration','web_rendered',''),
('racknerd','logo-dark','Provider logo for dark background','https://www.racknerd.com/images/logo-footer.png','https://www.racknerd.com/','provider_logo','web_rendered','White wordmark needs dark background.'),
('sharktech','dedicated','Dedicated-server illustration','https://sharktech.net/wp-content/uploads/2023/04/what-are-dedicated-servers.svg','https://sharktech.net/dedicated-servers/','product_illustration','official_link_resolved_not_rendered',''),
('sharktech','benefits','Dedicated-hosting benefits illustration','https://sharktech.net/wp-content/uploads/2023/04/benefits-dedicated-hosted-servers.svg','https://sharktech.net/dedicated-servers/','product_illustration','official_link_resolved_not_rendered',''),
('bacloud','logo','Provider green logo','https://www.bacloud.com/templates/bc-twenty-one-qloud/assets/images/logo/bacloud_green.svg','https://www.bacloud.com/en/dedicated-servers','provider_logo','official_link_resolved_not_rendered',''),
('adentro-tecnologia','datacenter','Data-center operations photograph','https://adentro.com.br/wp-content/uploads/2025/05/datacenter-adentro.png','https://adentro.com.br/','operations_photo','web_rendered','No exact facility coordinates implied.'),
('adentro-tecnologia','mark','Institutional icon','https://adentro.com.br/wp-content/uploads/2025/06/adentro-icone-01.svg','https://adentro.com.br/','provider_logo','official_link_resolved_not_rendered',''),
('i3d-net','bare-metal-hero','Dedicated-server header illustration','https://www.i3d.net/wp-content/uploads/Header-Dedicated-Servers_Header.svg','https://www.i3d.net/bare-metal-servers/','product_illustration','official_link_resolved_not_rendered',''),
('huawei-cloud','bms','BMS product illustration','https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/yunying/BMS-2024/buy-zp_1.svg','https://www.huaweicloud.com/product/bms.html','product_illustration','official_link_resolved_not_rendered',''),
('interserver','dedicated','Dedicated-server illustration','https://www.interserver.net/dedicated/assets/images/dedi.webp','https://www.interserver.net/dedicated/','product_illustration','web_rendered',''),
('interserver','datacenter','Isometric data-center illustration','https://www.interserver.net/dedicated/assets/images/datac.webp','https://www.interserver.net/dedicated/','facility_illustration','web_rendered','Illustration, not a photograph.'),
('interserver','network','Global-network illustration','https://www.interserver.net/dedicated/assets/images/network.webp','https://www.interserver.net/dedicated/','network_illustration','web_rendered','Not evidence of InterServer worldwide physical sites.'),
('hostdime','logo','HostDime logo with slogan','https://www.hostdime.com/images/identity/HostDime_Logo_Slogan_420_100.png','https://www.hostdime.com/about/identity','provider_logo','web_rendered','Official identity page offers multiple formats; confirm current brand-use terms.'),
('hostdime','logo-no-slogan','HostDime logo without slogan','https://www.hostdime.com/images/identity/HostDime_Logo_390_80.png','https://www.hostdime.com/about/identity','provider_logo','official_link_fetch_failed','Official link extracted, but image fetch failed. Do not mark production-ready.'),
('digital-pacific','c6620','Dell PowerEdge C6620 node front','https://www.digitalpacific.com.au/wp-content/uploads/2024/05/image-2024-6-12_12-57-23.png','https://www.digitalpacific.com.au/dedicated/dedicated-servers/','chassis_model_photo','web_rendered','Shown with C6620 offers. Chassis/node family, not a photograph of the future rented unit.'),
('digital-pacific','m630','Dell PowerEdge M630 blade','https://www.digitalpacific.com.au/wp-content/uploads/2019/10/M630.jpg','https://www.digitalpacific.com.au/dedicated/dedicated-servers/','chassis_model_photo','web_rendered','Different model from the selected C6620 offer.'),
('digital-pacific','r620','Dell PowerEdge R620 rack server','https://www.digitalpacific.com.au/wp-content/uploads/2019/10/r620.jpg','https://www.digitalpacific.com.au/dedicated/dedicated-servers/','chassis_model_photo','web_rendered','Different model from the selected C6620 offer.')]
for p,s,t,u,src,k,status,note in extra: asset(p,s,t,u,src,k,status,note=note)

# Metadata enrichments; do not manufacture unknown facts.
for r in records:
    r['normalized_status']='specified_example' if r['evidence']=='configured' else 'partial_or_quote_required'
    r['artwork_ready']=bool(r['artwork'])
    r['artwork_note']='Direct official-source URLs available; reuse rights and delivery statuses vary.' if r['artwork'] else 'No direct image URL established in this pass. Use the linked official product page for discovery, or a Forkalope-owned generic illustration plus the provider name.'
    r['source_provenance']={'kind':'first_party_public_pages_or_first_party_search_index','date':DATE,'checkout_verified':False,'sources':r['source_urls']}
    for k in ['service_rate_mbps','committed_mbps','egress_overage_per_tb','private_port_mbps']:
        r['network'].setdefault(k,None)
    r['price']['currency_conversion_applied']=False
    r['price']['monthly_equivalent_amount']=round(r['price']['amount']*730,4) if r['price']['period']=='hour' and r['price']['amount'] is not None else r['price']['amount']
    r['price']['monthly_equivalent_basis']='730-hour illustration, not a billing guarantee' if r['price']['period']=='hour' else 'See term, promotion and tax notes'

# This is an original, expressly hypothetical deployment mix, not vendor inventory.
pool_specs=[
 ('hetzner','DE',1450,'build-runner','Falkenstein'),('hetzner','FI',900,'build-runner','Helsinki'),
 ('ovhcloud','US',400,'git-replica',None),('interserver','US',250,'artifact-store','NYC metro'),
 ('reliablesite','US',250,'build-runner','Miami'),('clouvider','GB',160,'regional-edge','London'),
 ('nforce','NL',150,'cold-artifact-cache',None),('ikoula','FR',180,'git-replica',None),
 ('aruba','IT',120,'regional-edge',None),('glesys','SE',80,'git-replica',None),
 ('lumadock','ES',100,'build-runner','Madrid'),('gcore','HK',80,'regional-edge','Hong Kong'),
 ('exabytes','MY',100,'regional-edge','Cyberjaya'),('voyager','NZ',60,'regional-edge','Auckland'),
 ('xneelo','ZA',80,'regional-edge',None),('idc-frontier','JP',100,'memory-pool','Fukushima / Shirakawa'),
 ('gabia','KR',60,'regional-edge',None),('vinahost','VN',50,'regional-edge',None),
 ('turhost','TR',100,'regional-edge',None),('adentro-tecnologia','BR',140,'git-replica',None),
 ('hivelocity','NL',80,'regional-edge','Amsterdam'),('latitude-sh','SG',60,'regional-edge','Singapore'),
 ('ransomit','AU',50,'regional-edge','Melbourne')]
assert sum(s[2] for s in pool_specs)==5000
# Approximate display anchors, deliberately not exact facility coordinates.
anchors={
'DE':(51.0,10.0),'FI':(64.0,26.0),'US':(39.0,-98.0),'GB':(54.0,-2.0),'NL':(52.2,5.3),
'FR':(46.6,2.3),'IT':(42.8,12.8),'SE':(62.0,15.0),'ES':(40.2,-3.7),'HK':(22.3,114.2),
'MY':(4.5,109.0),'NZ':(-41.0,174.0),'ZA':(-29.0,24.0),'JP':(37.0,138.0),'KR':(36.0,128.0),
'VN':(16.0,107.0),'TR':(39.0,35.0),'BR':(-12.0,-52.0),'SG':(1.35,103.82),'AU':(-25.0,134.0)}
# Illustrative country-level anchors may fall away from a populated region; never render as site pins.
name_overrides={'GB':'United Kingdom','KR':'South Korea','TW':'Taiwan','RU':'Russia','VN':'Vietnam','TR':'Türkiye','HK':'Hong Kong','US':'United States','CZ':'Czechia'}
try:
    import pycountry
    def country_name(code): return name_overrides.get(code) or pycountry.countries.get(alpha_2=code).name
except ImportError:
    def country_name(code): return name_overrides.get(code,code)
def flag(code): return ''.join(chr(127397+ord(c)) for c in code)
pools=[];nodes=[];rng=random.Random(20260916)
scenario_time='2026-09-16T12:00:00Z'
for index,(pid,cc,count,role,city) in enumerate(pool_specs,1):
    r=by_id[pid]
    assert cc in r['locations']['country_codes'] or pid=='latitude-sh'
    pool_id=f'concept-{cc.lower()}-{pid}-{index:02}'
    price=copy.deepcopy(r['price'])
    if pid=='hivelocity': price.update(amount=130,monthly_equivalent_amount=130,kind='computed_75_plus_55_AMS1_selector_verify_checkout')
    if pid=='latitude-sh': price.update(amount=350,monthly_equivalent_amount=350,kind='Singapore_monthly_display_verify_checkout')
    pool=dict(id=pool_id,provider_id=pid,offer_id=r['offer_id'],country_code=cc,city_label=city,
              node_count=count,proposed_role=role,synthetic=True,bulk_stock_verified=False,
              hypothetical_site_id=pool_id+'-site',actual_facility_id=None,
              country_display_anchor={'lat':anchors[cc][0],'lon':anchors[cc][1],'precision':'illustrative_country_anchor_not_facility'},
              location_evidence=r['locations']['scope'],modeled_unit_price=price,
              assumptions='Quantity, workload assignment and topology are invented for UI design; price snapshot is not a bulk quote or a future-price forecast.')
    pools.append(pool)
    for i in range(1,count+1):
        u=rng.random()
        state='healthy' if u<.94 else 'draining' if u<.96 else 'maintenance' if u<.98 else 'degraded' if u<.995 else 'unreachable'
        # One deliberately correlated, invented pool incident; no real vendor outage implied.
        incident='concept-incident-01' if pid=='interserver' and i<=12 else None
        if incident: state='degraded'
        observed=None if state=='unreachable' else scenario_time
        cpu_pct=round(rng.uniform(7,84),1) if observed else None
        if role=='build-runner' and observed: cpu_pct=round(rng.uniform(28,92),1)
        memory_pct=round(rng.uniform(18,81),1) if observed else None
        service_cap=r['network'].get('service_rate_mbps') or r['network']['public_port_mbps']
        egress=round(rng.uniform(.005,.12)*service_cap,2) if observed and service_cap else None
        monthly_transfer=round(rng.uniform(.10,.55)*r['network']['included_transfer_tb'],3) if observed and r['network']['included_transfer_tb'] else None
        storage_pct=round(rng.uniform(18,76),1) if observed and (r['storage']['raw_capacity_vendor_gb'] is not None or pid=='idc-frontier') else None
        ram=r['memory']['capacity_vendor_gb']
        if ram is None and r['memory'].get('capacity_gib') is None: raise AssertionError(pid)
        nodes.append(dict(id=f'{cc.lower()}-{pid}-{i:05}',pool_id=pool_id,provider_id=pid,offer_id=r['offer_id'],
            country_code=cc,city_label=city,proposed_role=role,synthetic=True,
            status=state,incident_id=incident,actual_facility_id=None,actual_rack_id=None,
            enrollment={'state':'enrolled' if observed else 'last_seen_stale','fabric_address':None,'provider_instance_id':None},
            telemetry={'synthetic':True,'observed_at':observed,'last_seen_at':scenario_time if observed else '2026-09-16T11:46:00Z',
                'cpu_utilization_pct':cpu_pct,'memory_utilization_pct':memory_pct,'storage_utilization_pct':storage_pct,
                'public_egress_mbps':egress,'month_to_date_transfer_tb':monthly_transfer,
                'overlay_health':'degraded' if incident else ('connected' if observed else 'unknown'),
                'hardware_health':'unknown' if not observed else 'nominal',
                'request_latency_ms':None,'power_watts':None},
            illustration_key='forkalope-generic-storage' if role in ('artifact-store','cold-artifact-cache') else 'forkalope-generic-compute'))

cc_counts=collections.Counter(n['country_code'] for n in nodes)
provider_counts=collections.Counter(n['provider_id'] for n in nodes)
role_counts=collections.Counter(n['proposed_role'] for n in nodes)
status_counts=collections.Counter(n['status'] for n in nodes)
costs=collections.defaultdict(float)
known_cores=known_core_nodes=known_ram=known_ram_nodes=known_storage=known_storage_nodes=0
for p in pools:
    r=by_id[p['provider_id']];n=p['node_count']
    costs[p['modeled_unit_price']['currency']]+=p['modeled_unit_price']['monthly_equivalent_amount']*n
    if r['cpu']['physical_cores_total'] is not None: known_cores+=r['cpu']['physical_cores_total']*n;known_core_nodes+=n
    if r['memory']['capacity_vendor_gb'] is not None: known_ram+=r['memory']['capacity_vendor_gb']*n;known_ram_nodes+=n
    if r['storage']['raw_capacity_vendor_gb'] is not None: known_storage+=r['storage']['raw_capacity_vendor_gb']*n;known_storage_nodes+=n
summary=dict(synthetic=True,nodes=len(nodes),providers=len(provider_counts),countries_or_territories=len(cc_counts),pools=len(pools),
    country_counts=dict(cc_counts),provider_counts=dict(provider_counts),role_counts=dict(role_counts),status_counts=dict(status_counts),
    known_physical_cores=known_cores,physical_core_coverage_nodes=known_core_nodes,
    known_memory_vendor_gb=known_ram,memory_coverage_nodes=known_ram_nodes,
    known_local_raw_storage_vendor_gb=known_storage,local_raw_storage_coverage_nodes=known_storage_nodes,
    modeled_monthly_base_cost_by_native_currency={k:round(v,2) for k,v in sorted(costs.items())},
    cost_caveat='Illustrative multiplication of retail snapshots. Mixed tax/term bases; no FX, bulk discount, network overage, software, operations or setup amortization. Not a procurement budget.')
coverage=dict(providers=len(records),specified_examples=sum(r['evidence']=='configured' for r in records),
    numeric_advertised_prices=sum(r['price']['amount'] is not None for r in records),
    numeric_memory_records=sum(r['memory']['capacity_vendor_gb'] is not None or r['memory'].get('capacity_gib') is not None for r in records),
    numeric_raw_local_storage_records=sum(r['storage']['raw_capacity_vendor_gb'] is not None for r in records),
    numeric_physical_core_records=sum(r['cpu']['physical_cores_total'] is not None for r in records),
    numeric_public_port_records=sum(r['network']['public_port_mbps'] is not None for r in records),
    explicit_country_records=sum(bool(r['locations']['country_codes']) for r in records),
    direct_artwork_links=len(assets),providers_with_direct_artwork=len({a['provider_id'] for a in assets}),
    hetzner_artwork_links=sum(a['provider_id']=='hetzner' for a in assets),
    rendered_artwork_links=sum(a['retrieval_status']=='web_rendered' for a in assets))
allcc=sorted({cc for r in records for cc in r['locations']['country_codes']}|set(cc_counts))
countries=[{'code':cc,'name':country_name(cc),'emoji':flag(cc),
    'flag_svg_url':f'https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.3.2/flags/4x3/{cc.lower()}.svg',
    'flag_source':'https://flagicons.lipis.dev/','flag_license':'MIT; retain upstream license',
    'flag_link_status':'constructed_from_documented_pinned_library_path; individual URLs not fetched',
    'synthetic_node_count':cc_counts.get(cc,0),
    'display_anchor': {'lat':anchors[cc][0],'lon':anchors[cc][1],'precision':'illustrative_country_anchor_not_facility'} if cc in anchors else None}
    for cc in allcc]
metadata={'schema_version':'1.0.0','research_date':DATE,'purpose':'Forkalope worldwide bare-metal catalog and UI concept; not active inventory',
 'ranking':'curated longlist; ordinal numbers are identifiers, not quality or size rankings',
 'coverage':coverage,'unknown_values':'null means unknown or not established, never zero',
 'source_scope':'Official provider pages/docs and their indexed public descriptions; stock/checkout not transaction-verified',
 'no_reuse_license_granted_for_third_party_assets':True}

def dump(name,obj):
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
dump('providers-and-offers.json',{'metadata':metadata,'providers':records})
dump('artwork-manifest.json',{'metadata':{'research_date':DATE,'downloads_included':False,'rights':'Per-asset review required'},'assets':assets})
dump('countries-and-flags.json',{'metadata':{'research_date':DATE,'boundaries':'Use geographic labels neutrally; hosting location is not citizenship or provider ownership'},'countries':countries})
dump('fleet-5000.synthetic.json',{'metadata':{'schema_version':'1.0.0','synthetic':True,'scenario_id':'forkalope-future-5000-v1','random_seed':20260916,'scenario_time':scenario_time,
 'warning':'All nodes, telemetry, incidents, allocation counts and operational relationships are synthetic. Offers point to real 2026 research; fleet does not exist. No credentials or live endpoints.'},
 'summary':summary,'pools':pools,'incidents':[{'id':'concept-incident-01','synthetic':True,'summary':'Invented packet-loss incident affecting 12 nodes in a hypothetical storage pool','actual_provider_incident':False}], 'nodes':nodes})
dump('research-coverage.json',{'coverage':coverage,'fixture':summary})

# Flat export for direct UI prototyping; price qualification fields must stay visible.
with (ROOT/'provider-offers.csv').open('w',newline='',encoding='utf-8-sig') as f:
    cols=['provider_id','provider','product','price_amount','currency','period','price_kind','price_display','physical_cores','hardware_threads','memory_vendor_gb','memory_gib','raw_local_storage_gb','public_port_mbps','service_rate_mbps','transfer_tb','unmetered','country_codes','location_scope','product_url','artwork_count','notes']
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
    for r in records:
        w.writerow(dict(provider_id=r['id'],provider=r['name'],product=r['product'],price_amount=r['price']['amount'],currency=r['price']['currency'],period=r['price']['period'],price_kind=r['price']['kind'],price_display=r['price_display'],physical_cores=r['cpu']['physical_cores_total'],hardware_threads=r['cpu']['hardware_threads_total'],memory_vendor_gb=r['memory']['capacity_vendor_gb'],memory_gib=r['memory'].get('capacity_gib'),raw_local_storage_gb=r['storage']['raw_capacity_vendor_gb'],public_port_mbps=r['network']['public_port_mbps'],service_rate_mbps=r['network']['service_rate_mbps'],transfer_tb=r['network']['included_transfer_tb'],unmetered=r['network']['unmetered'],country_codes=';'.join(r['locations']['country_codes']),location_scope=r['locations']['scope'],product_url=r['source_urls'][0],artwork_count=len(r['artwork']),notes=r['notes']))

# Markdown assembly: designed to remain useful as a single standalone text file.
def esc(v): return str(v).replace('|','\\|').replace('\n',' ')
def fmt(v): return 'Unknown' if v is None else f'{v:,}' if isinstance(v,(int,float)) else str(v)
md=[]
def put(s=''): md.append(s)
put('# Forkalope — Worldwide Bare-Metal Research & Dashboard Handoff')
put(f'\n**Research snapshot: {DATE} · 90 provider entries · original UI proposal · synthetic fleet, not live infrastructure.**\n')
put('This is a curated worldwide supplier longlist, not a defensible ranking of the 90 largest or best providers. It combines global operators, regional specialists, aggregators, managed dedicated services and hyperscaler physical-host products. The catalog is broad enough to design a convincing future Forkalope network, but it is not a completed procurement spreadsheet: some providers require sales quotes or dynamic configuration before a price and an exact physical machine can be matched.\n')
put(f"**Coverage:** {coverage['specified_examples']} entries have a specified example configuration; {coverage['numeric_advertised_prices']} have a numeric advertised price or starting rate; {coverage['numeric_memory_records']} have numerical memory; {coverage['numeric_raw_local_storage_records']} have numerical raw local storage; {coverage['numeric_public_port_records']} have a numerical public-port field. These are different completeness tests. A ‘specified example’ can still lack confirmed transit terms, a facility, tax basis or live stock. There are **{len(assets)} direct artwork links**, including **{coverage['hetzner_artwork_links']} for Hetzner**, plus official discovery pages for every provider. Image URLs are supplied, not image files; rights are not assumed.\n")
put(f"The companion fixture contains **5,000 synthetic nodes across {summary['countries_or_territories']} countries/territories, {summary['providers']} suppliers and {summary['pools']} pools**. Its quantities, roles, health and topology are invented. Hardware points back to researched offers; missing hardware fields stay unknown. A real 5,000-node purchase would require availability, legal, network, operational and commercial diligence.\n")
put('## Contents\n\n1. [How to use this handoff](#how-to-use)\n2. [Dashboard direction and six screens](#dashboard)\n3. [Normalization and data model](#normalization)\n4. [Synthetic 5,000-node deployment](#synthetic-fleet)\n5. [Provider index](#provider-index)\n6. [All 90 provider cards](#provider-cards)\n7. [Artwork, flags and map assets](#artwork)\n8. [Procurement gaps and refresh checklist](#diligence)\n')
put('<a id="how-to-use"></a>\n## 1. How to use this handoff\n')
put('Start the UI with the synthetic fleet, not the 90-entry supplier catalog. Join each node’s `offer_id` to `providers-and-offers.json`; join its `pool_id` to the fixture’s pools. The 90 suppliers belong in the discovery/expansion catalog. Showing thousands of active hosts from all 90 would add operational fragmentation without making the mockup more credible.\n')
put('Keep three independently labeled layers: **researched offer** (what a provider advertises), **contracted asset** (what Forkalope has actually ordered and pays for), and **telemetry** (what the agent currently observes). This package has the first, and synthetic examples of the second and third. Never turn a product maximum into an installed specification or a provider’s world map into a deployed-node map.\n')
put('| File | Use |\n|---|---|\n| `forkalope-bare-metal-worldwide.md` | This self-contained research and design specification |\n| `providers-and-offers.json` | 90 nested provider/example-offer records with native units, pricing qualifiers, source URLs and asset references |\n| `provider-offers.csv` | Flat comparison export; empty numeric fields mean unknown |\n| `artwork-manifest.json` | Direct image URLs, classifications, retrieval status and rights notes |\n| `countries-and-flags.json` | Country/territory codes, display labels, pinned flag-library paths and synthetic counts |\n| `fleet-5000.synthetic.json` | Deterministic 5,000-node fixture, pools, invented telemetry and one invented correlated incident |\n| `research-coverage.json` | Completeness counts and computed fixture totals |\n| `build_catalog.py`, `make_deliverables.py` | Rebuild the handoff offline with Python; no provider API calls |\n')
put('### Evidence labels\n\n`specified_example` means a named offer/configuration was captured, not that every field is verified. `partial_or_quote_required` includes sales-only providers, uncaptured dynamic baskets, and known hardware with unresolved pricing. Price `kind` must remain attached to the number: family minimum, promotion, commitment equivalent, regional base and live configured price are not interchangeable. Individual notes identify contradictory or stale-looking source material. Research was read from public pages and first-party indexed snippets; there were no authenticated checkouts, purchase transactions, throughput tests or independent uptime measurements.\n')
put('<a id="dashboard"></a>\n## 2. Dashboard direction — “Forkalope Fabric”\n')
put('**Design proposal:** make it feel like one professionally operated cloud with a visible supply chain, not a collection of unrelated hosting control panels. Use a quiet dark-navy canvas, flat surfaces, compact white typography, restrained coral selection states and status colors that are always paired with text/icons. Avoid neon globes, animated particle clouds and a full-screen tangle of arcs. Rich provider photography belongs in regional headers and expanded cards; normalized server silhouettes belong in dense inventories. These are proposed design choices, not assertions about the existing repository.\n')
put('### Screen A — World overview\n\nA 1440–1728 px desktop composition: compact left navigation, 64 px top bar, six concise aggregate tiles, then a large map beside an incident/saturation rail and a virtualized inventory table below. Top-level tiles: enrolled nodes; schedulable CPU; allocatable memory; usable storage; current external egress; recurring cost. Each tile carries coverage and freshness, not just a spectacular total. The research fixture can honestly show “known physical cores” and “raw local storage”; it cannot supply real schedulable CPU or usable replicated storage.\n')
put('Map markers aggregate by country at world zoom. Their size encodes a single selected metric such as node count, and their status ring encodes the worst material state, with affected/total counts on hover. Clicking a country zooms into its available regions/pools. The map always has a table alternative. Separate toggles switch between **Physical fleet**, **Fabric connectivity**, **Workload placement**, and **Supplier footprint**; these are different layers and must not be merged. Physical underlay links are not the same as overlay reachability.\n')
put('Use a persistent breadcrumb such as `World / Europe / Germany / Hetzner / AX42`. MapLibre GL JS provides a documented point-clustering pattern; use it as the initial map implementation rather than writing a globe engine. See the [official clustering example](https://maplibre.org/maplibre-gl-js/docs/examples/create-and-style-clusters/). Application state, not the map widget, should own filters and selections.\n')
put('### Screen B — Country / regional operations\n\nA country outline, small flag plus readable country name, and a short row of local metrics replace the world header. Show provider distribution, CPU-generation mix, pool health, transfer budget and workloads currently served. The inventory below groups by provider, product or role. Present smaller suppliers as real first-class infrastructure, but keep any unknown city at country level rather than creating a fake data-center pin. A country’s legal jurisdiction, cloud region name and data residency policy are distinct fields requiring separate validation.\n')
put('### Screen C — Fleet inventory: table and card modes\n\nThe table is the primary operating view: node ID, health, provider, location, offer/CPU, physical cores, RAM, disks, usable storage, port, traffic allowance, current utilization, role and cost qualification. Users can pin identity and status columns, save views and compare two to four hosts. Card mode uses a consistent illustrated server form, provider name/approved logo, country label and just five or six headline facts. Full facts appear in a side panel. No retail “Buy now” controls in the operator inventory; procurement is a separate workflow.\n')
put('Filters should cover country/territory, city, supplier, upstream/operator when known, CPU vendor/model/generation, physical-core count, RAM size/unit, actual ECC status, storage medium, raw/usable capacity, port rate, committed service rate, transfer model, currency, contract term, role, health, enrollment status, reimage/KVM support and evidence freshness. Include **Unknown** explicitly. Multiple selections within one facet are OR; different facets are AND. Price comparisons require a currency and comparable tax/term basis, or an explicitly dated FX conversion.\n')
put('### Screen D — One machine\n\nThe side-panel header shows immutable Forkalope node ID, hostname, provider, confirmed location, health and the best available artwork. Tabs: Overview; Hardware; Storage; Network; Workloads; Events; Contract & provenance. Include BIOS/firmware, disk health and serials only when actually obtained. Artwork must state `actual model`, `provider illustration` or `generic depiction`; never suggest a stock image is a photograph of that physical unit.\n')
put('Network details separate public interface, provider-private interface and Forkalope overlay. Show observed handshake freshness, direct/relayed route state, loss and latency only when collected. An overlay failure should not automatically turn hardware health red. Store actions behind RBAC: drain, cordon, restart agent, open console, reboot and reimage. Destructive actions need target-specific confirmation and audit trails; simulation actions must never reach real provider APIs.\n')
put('### Screen E — Hardware / supplier comparison\n\nCompare configurations, not brand slogans. Put price conditions directly under the price: “annual equivalent”, “setup extra”, “regional surcharge”, “quote required”, or “promotion until verified”. Keep cores and hardware threads separate; do not normalize every machine to a fictional common vCPU benchmark. The table should reveal useful contrasts: a legacy four-core Xeon, a modern desktop Ryzen, a memory-heavy dual-socket node, a storage chassis and a cloud bare-metal host with external block storage.\n')
put('### Screen F — Network capacity and cost\n\nSeparate instantaneous bits per second from cumulative transferred bytes. Plot traffic budget consumed and projected exhaustion only where the billing rules and reset date are known. Unmetered machines still have finite links and policies. Costs should split base rent, setup amortization, extra disks, IPv4, licenses, managed support, transfer overage and reserved commitments. Show spending concentration by supplier, country and underlying facility, but count reseller and shared-parent risk separately where known. No global dollar total should appear until an explicit FX dataset and timestamp exist.\n')
put('### Navigation, performance and honest empty states\n\nUse level-of-detail: world aggregates → country aggregates → actual site/pool → nodes. Cluster points instead of mounting thousands of HTML markers; virtualize rows and cards; fetch thumbnail artwork only for visible items. Draw overlay edges for a selected node or aggregated region pair, not every theoretical node pair. On a 5,000-node view, a physical rack rendering is inappropriate unless actual rack assignments exist. The fixture’s pools are logical groups, not evidence of contiguous rented racks.\n')
put('Recommended screenshot set: global overview; Germany/Finland supply concentration; Brazil expanded supplier card; Australia traffic-limited node detail; storage pool with the invented correlated incident; cross-provider comparison. Add a restrained “Preview / synthetic data” designation to public mockups and exported screenshots. Keep preview actions isolated from production at the backend and credential boundary. Do not publish invented provider failures as real incidents.\n')
put('Unknown values render `Not established`, stale telemetry shows its age, and a failed image uses a neutral glyph rather than a broken-image box. Respect reduced motion, keyboard traversal, focus visibility, readable contrast and a non-color status representation. Empty filters must show which constraint removed the results and offer a clear reset. Never silently drop unknown rows from an “all hosts” total.\n')
put('<a id="normalization"></a>\n## 3. Normalization and production data model\n')
put('### What the supplied JSON does—and does not—normalize\n\nThe catalog uses common field names and explicit numeric fields where the source permits them. It preserves raw vendor wording alongside each number. It does **not** silently convert vaguely labeled RAM GB to GiB, calculate a physical-core count from a cloud vCPU label, interpret a missing field as zero, or invent disk redundancy. This is intentionally safer than a deceptively complete matrix.\n')
put('| Concern | Rule for Forkalope |\n|---|---|\n| CPU | Preserve full model, socket count when known, total physical cores, hardware threads, and separately vendor vCPU/OCPU counts. Record heterogeneous core types when relevant. |\n| Memory | Preserve vendor value and unit. Explicit GiB can be multiplied by 2^30 for bytes; ambiguous GB remains vendor-GB until confirmed. Memory capacity does not establish ECC. |\n| Local disks | Keep count, per-drive size, medium/interface and raw sum separately. Additional empty bays are not installed storage. |\n| Usable storage | RAID 1 is approximately one mirror member’s size; RAID 10 and distributed replication need their own accounting. Filesystem overhead and reserves are additional. |\n| Remote storage | External block/SAN allocation is not local raw disk capacity. Cloud-backed hosts may have no included local data disk. |\n| Link speed | Store physical NIC, public port, guaranteed/committed rate and private rate separately. Two NICs do not prove a doubled Internet entitlement. |\n| Traffic | Preserve allowance, period, direction, scope and policy: metered, unmetered, shared pool, 95th percentile or quote. |\n| Price | Amount + ISO currency + billing period + commitment + tax basis + setup + promotion/renewal. Family minima are not configured baskets. |\n| Geography | Country/territory code, city, facility, confidence/precision and supporting source. Provider HQ and generic cloud region maps are not a physical-host address. |\n| Artwork | Provider logo, chassis-model photo, facility photo, generic illustration and permission status are independent metadata. |\n| Health | Provider reachability, hardware health, OS-agent health, overlay health and workload health are separate signals. |\n| Unknown | JSON `null`; distinguish not collected, not published, contradictory and not applicable in a production implementation. |\n')
put('Arithmetic examples: 2 × 512 GB disks sum to 1,024 vendor GB raw, not 1,024 GB safely usable after mirroring. A 10 Gbps port with 20 TB/month remains a traffic-limited plan; the port is not a promise of 10 Gbps continuous free transit. An hourly rate × 730 is only a comparison convention. Native-currency subtotals remain separate. These are accounting rules, not performance guarantees.\n')
put('### Recommended entities\n\n**Provider** owns name, domains, brand assets and support/API capabilities. **Offer revision** is an immutable researched or quoted configuration with regional and price qualifications. **Offer-location availability** binds a specific revision to a real region, stock state and observation time. **Contracted node** owns the real provider instance ID, actual hardware snapshot, fixed contract details and independently verified location. **Telemetry sample** owns measurements and timestamps. **Artwork asset** owns source, permission, hash and rendering purpose. **Failure-domain relation** models shared upstream, parent, chassis, facility and network dependence without assuming different brands are independent.\n')
put('The supplied `providers-and-offers.json` deliberately denormalizes one example offer into each provider entry for convenient UI ingestion. Its `offer_id` provides a stable join. Split those entities when you move to production; do not overwrite an old contracted host when the public price page changes. Keep the offer source URL, research timestamp and contracted quote artifact separately.\n')
put('### Example join in plain JavaScript\n\n```js\nconst [catalog, fleet] = await Promise.all([\n  fetch("/fixtures/providers-and-offers.json").then(r => {\n    if (!r.ok) throw new Error(`Catalog HTTP ${r.status}`);\n    return r.json();\n  }),\n  fetch("/fixtures/fleet-5000.synthetic.json").then(r => {\n    if (!r.ok) throw new Error(`Fleet HTTP ${r.status}`);\n    return r.json();\n  })\n]);\nif (fleet.metadata.synthetic !== true) throw new Error("Expected isolated fixture");\nconst offerById = new Map(catalog.providers.map(p => [p.offer_id, p]));\nconst poolById = new Map(fleet.pools.map(p => [p.id, p]));\nconst rows = fleet.nodes.map(node => {\n  const offer = offerById.get(node.offer_id);\n  const pool = poolById.get(node.pool_id);\n  if (!offer || !pool) throw new Error(`Broken fixture join: ${node.id}`);\n  return { ...node, offer, pool };\n});\n// Explicit null checks: zero is not a safe substitute for unknown.\nconst withKnownRam = rows.filter(r => r.offer.memory.capacity_vendor_gb !== null);\nconst germany = rows.filter(r => r.country_code === "DE");\n// Display the pool price plus its kind; never show only an unqualified number.\n```\n')
put('### Aggregation rules\n\nTotals must carry known/unknown counts. Sum raw local storage only across fields that really mean raw local storage; do not add remote volume capacity to a raw-drive headline. Do not sum private and public port rates as if they were independent external throughput. Count a pooled transfer allowance once per billing pool, not once per server. A global p95 latency cannot be obtained by averaging each node’s p95; aggregate the underlying histogram or define a different explicitly named statistic. Observed usable capacity, filesystem free bytes and scheduler allocatable resources should ultimately supersede sales-page capacities in operations.\n')
put('<a id="synthetic-fleet"></a>\n## 4. A plausible 5,000-node concept fleet\n')
put('**All quantities and operational assignments below are synthetic design assumptions.** This is a heterogeneous fleet with large inexpensive European pools, US Git/build/storage capacity, and smaller regional pools. It is not a recommendation to use tiny legacy hosts as primary build machines or to run synchronous worldwide consensus across all regions. A substantial concentration at Hetzner is intentional for a readable scenario, not an assertion of optimal resilience. Stock, capacity reservations and policy compatibility have not been secured.\n')
put('| Supplier | Country/territory | Example offer | Nodes | Proposed role |\n|---|---|---|---:|---|')
for p in pools:
    r=by_id[p['provider_id']]
    put(f"| [{r['name']}](#provider-{r['id']}) | {flag(p['country_code'])} {country_name(p['country_code'])} | {esc(r['product'])} | {p['node_count']:,} | {p['proposed_role']} |")
put(f"\n**Computed fixture totals:** {len(nodes):,} nodes; {len(provider_counts)} providers; {len(cc_counts)} countries/territories; {len(pools)} logical pools. Known physical cores: **{known_cores:,} across {known_core_nodes:,} nodes**. Known memory: **{known_ram:,} vendor GB across {known_ram_nodes:,} nodes**. Known raw local disk: **{known_storage:,} vendor GB across {known_storage_nodes:,} nodes**. These are capacity sums, not equivalent compute performance or safe usable storage.\n")
put('Status counts are generated deterministically rather than copied from any live provider: '+', '.join(f'{k}: {v:,}' for k,v in status_counts.items())+'. The invented incident affects 12 members of one hypothetical storage pool. Unknown timestamps and health remain unknown on unreachable hosts; no live endpoints, IP assignments or credentials are included.\n')
put('### Native-currency base-rent arithmetic\n\nThe following subtotals multiply snapshot display rates by invented quantities. They deliberately mix no currencies. Tax/commitment bases still vary within currencies, and setup, staffing, egress overage, private networking, software and bulk discounts are excluded. **Do not use these as a purchase budget.** Hetzner’s indexed rate remains provisional; Hivelocity AMS1 uses 75 + 55 = USD 130; Latitude Singapore uses its separate USD 350 display rather than the global minimum.\n')
put('| Currency | Modeled monthly base subtotal |\n|---|---:|')
for curr,total in sorted(costs.items()): put(f'| {curr} | {total:,.2f} |')
put('\n### Geography and expansion\n\nThe fixture supplies approximate **country display anchors**, not facility coordinates. A country marker can support a map drill-down, but the client must never relabel it a data center. City labels appear only where the offer/site material supports them; some country pools intentionally have no city. Malaysia’s country anchor is a schematic label position, not a physical site. Geocoding verified sites is a separate task.\n')
put('India, additional Latin American countries, the Middle East, more African markets and additional Asia-Pacific metros are expansion candidates in the longlist. Do not fill those gaps by assigning a provider’s cheapest global offer to every advertised location. Quote-only candidates belong in a planned-capacity layer until a physical SKU, country, price and network package are tied together.\n')
put('<a id="provider-index"></a>\n## 5. Provider index\n\nNumbers identify entries; they are not rankings. `S` = specified example, `P` = partial/quote/configurator. Countries shown are the scope captured for the example or explicitly qualified footprint, not an exhaustive inventory guarantee.\n')
put('| # | Provider | Example / family | Advertised price | Location codes | Evidence |\n|---:|---|---|---|---|:---:|')
for i,r in enumerate(records,1):
    p=r['price'];price=f"{p['currency']} {p['amount']:,.4f}".rstrip('0').rstrip('.')+f"/{'hr' if p['period']=='hour' else 'mo'}" if p['amount'] is not None else 'Quote / not captured'
    # repr formatting of amounts ending in integer zeros is handled by the decimal portion above.
    put(f"| {i} | [{r['name']}](#provider-{r['id']}) | {esc(r['product'])} | {price} — {esc(p['kind'].replace('_',' '))} | {', '.join(r['locations']['country_codes']) or 'See scope / unknown'} | {'S' if r['evidence']=='configured' else 'P'} |")
put('\nEvery price above must be read with its full card. Many price points are starting rates, long-term equivalents or promotions, not cancel-anytime monthly quotes.\n')
put('<a id="provider-cards"></a>\n## 6. All 90 provider cards\n')
for i,r in enumerate(records,1):
    put(f"<a id=\"provider-{r['id']}\"></a>\n### {i:02}. {r['name']}\n")
    put(f"**Example:** {r['product']} · **Evidence:** {r['normalized_status'].replace('_',' ')} · **Observed:** {DATE}\n")
    put('| Field | Researched value / qualification |\n|---|---|')
    fields=[('Price',r['price_display']),('CPU',r['cpu']['display']),('Memory',r['memory']['display']),('Disk / storage',r['storage']['display']),('Network / transfer',r['network']['display']),('Physical location scope',r['locations']['display']),('Location confidence',r['locations']['scope'])]
    for title,val in fields: put(f'| {title} | {esc(val)} |')
    put('\n**Caveats:** '+r['notes']+'\n')
    if r['corporate_or_supply_group']: put('**Supply-chain note:** '+r['corporate_or_supply_group']+'. This is not a fully audited ownership graph.\n')
    put('**First-party sources:** '+' · '.join(f'[Source {j}]({u})' for j,u in enumerate(r['source_urls'],1))+'.\n')
    if r['artwork']:
        put('**Artwork:** '+', '.join(f'[{a}](#asset-{a})' for a in r['artwork'])+'. Classifications and permissions are below.\n')
    else:
        put(f"**Artwork discovery:** [Official product/brand page]({r['art_source_page']}). No direct image URL verified for this provider in this pass; use a neutral Forkalope illustration until an approved asset is acquired.\n")
put('<a id="artwork"></a>\n## 7. Artwork, flags and maps\n')
put(f'### Direct artwork manifest — {len(assets)} links\n\nThese URLs were extracted from official provider pages or their official asset hosts. `web_rendered` means the image was actually rendered during research; SVG links marked `official_link_resolved_not_rendered` were identified but not raster-rendered. One HostDime link failed to fetch and is retained only as an explicitly flagged lead. No local copies, hashes, universal reuse rights or long-term CDN availability are claimed.\n')
put('**Hetzner is the strongest starting set in this handoff:** 12 press-kit images/badges plus two dedicated-product illustrations. The [official pressroom](https://www.hetzner.com/pressroom/) gives conditions: attribute Hetzner Online GmbH; keep usage related to Hetzner; notify its press contact; obtain written approval for edits. Those press-kit terms must not be automatically extended to marketing assets elsewhere on the site. A “hosted by” badge could imply a real commercial relationship, so omit it from a future-network concept unless the context is unmistakable.\n')
put('**Recommended asset treatment:** large facility photos for supplier/country headers; model photos on expanded cards where the actual model matches; provider logos as small secondary identity marks; a consistent Forkalope-owned generic chassis illustration for all other node cards. A CPU model does not identify the chassis. Cropping, recoloring or removing logos may require separate permission. Do not hotlink unapproved third-party assets in production; after approval, retain original/source metadata, sanitize SVG and publish controlled derivatives on your own asset host.\n')
for a in assets:
    put(f"<a id=\"asset-{a['id']}\"></a>\n#### {by_id[a['provider_id']]['name']} — {a['title']}\n")
    put(f"[Direct image]({a['url']}) · [Official source page]({a['source_page']})\n")
    put(f"Type: `{a['kind']}` · Retrieval: `{a['retrieval_status']}`. {a['notes']}\n")
    if a['provider_id']=='hetzner' and a['source_page']==press: put('Rights: Hetzner press-kit conditions described above; not an unrestricted license.\n')
    else: put('Rights: '+a['rights_status']+'.\n')
put('### Country flags\n\nUse [flag-icons](https://flagicons.lipis.dev/), which supplies ISO 3166-1 alpha-2 flags in SVG and publishes its MIT licensing and integration instructions. The companion country file uses the documented version `7.3.2` as a pinned example; inspect and retain the upstream license when vendoring. A generated flag URL is a path derived from the library convention, not an individually fetched/verified file. Prefer local package imports or a controlled CDN copy for production.\n')
put('```html\n<!-- With the flag-icons package CSS loaded -->\n<span class="fi fi-de" aria-hidden="true"></span> Germany\n<span class="fi fi-gb" aria-hidden="true"></span> United Kingdom\n```\n')
put('Show a readable country/territory name next to the flag. Use `GB`, not `UK`, as the alpha-2 key; do not use country flags as a substitute for interface language. Geographic market labels do not imply a position on sovereignty. The map and tables should handle country/territory categories consistently.\n')
put('### Maps\n\n[Natural Earth](https://www.naturalearthdata.com/) provides cartographic data, and its [terms](https://www.naturalearthdata.com/about/terms-of-use/) place its raster and vector data in the public domain. Start with a simplified world boundary layer for the globe/overview and a more detailed scale at country zoom. Version and document the chosen boundary treatment. Its generalized boundaries are not a data-center geocoder.\n')
put('Use [MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/) for the interactive map and its [clustering example](https://maplibre.org/maplibre-gl-js/docs/examples/create-and-style-clusters/) as the first implementation reference. Basemap data, rendering library and tile-hosting service are separate dependencies with separate terms. Natural Earth assets and flag assets are links in this package, not downloaded map/flag files.\n')
put('### Original illustration library to commission or generate\n\nCreate a cohesive set of 10–12 Forkalope-owned depictions: compact compute node; high-memory compute; NVMe-heavy server; HDD storage chassis; GPU server; blade node; remote-block-backed host; regional edge node; logical server pool; maintenance state; empty/unknown inventory. Use the same front/three-quarter angle, silhouette scale, lighting and neutral enclosure; overlay operational metadata in HTML rather than burning text into artwork. These are briefs, not generated assets delivered here.\n')
put('For each reusable illustration, provide transparent 256/512 px variants and an SVG only when a real vector master exists. Never derive physical rack height, drive-bay count or chassis branding from an unknown model. A generic “storage node” drawing is honest; a very specific Dell chassis under an unrelated provider’s unverified product is not. The direct Digital Pacific photos are useful visual references for how genuinely different node/blade/rack families look, subject to rights review.\n')
put('<a id="diligence"></a>\n## 8. Procurement gaps, exclusions and refresh checklist\n')
put('### Deliberate exclusions / qualification\n\nEquinix Metal is not an active future supplier: its [official documentation](https://docs.equinix.com/metal/) records the June 30, 2026 sunset. Equinix data-center facilities used by other operators are a different matter; an operator renting colocation there is not selling the retired Metal product. VPS/VDS, dedicated-core VMs and shared GPU slices are not counted as physical servers simply because a page says “dedicated resources.” Hyperscaler `.metal`/bare-metal products are included with their cloud storage/network charging caveats.\n')
put('Kimsufi/So you Start/Eco are represented under OVHcloud; Dedibox/Online under Scaleway; myLoc/servdiscount under one entry; SeFlow under Aruba; Database Mart/Server Mart under one entry. Brand counts are not independent ownership or failure-domain counts. Some other parent/supply relationships remain explicitly unverified. An aggregator can rent genuine physical hardware while still sharing an upstream site/operator with another brand in the catalog.\n')
put('A managed dedicated service may be unsuitable for arbitrary reimaging or a Forkalope runner despite being a real physical server. A dedicated blade/node may still share enclosure power/network with neighbors. Access, supported operating systems, console/recovery API, secure boot, TPM, firmware control and provider abuse policies must be assessed before onboarding. Do not put tenant CI secrets on untrusted or unmanaged enrollment paths. These are proposed diligence requirements, not guarantees about any listed supplier.\n')
put('### What still needs a quote or deeper verification\n\nThe `partial_or_quote_required` records remain research leads, not complete buyable baskets. The largest gaps are authenticated/dynamic enterprise pricing, exact facility availability, public-vs-private bandwidth detail, traffic direction/scope, promotion renewals, tax, setup, control-plane automation, and approved image licensing for most brands. Some specified offers also contain these gaps. Do not hide those limitations in the UI.\n')
put('Before a real order, capture a dated quote for one exact SKU in one exact site: CPU/socket/core details; installed RAM and genuine ECC; each disk and RAID; remote storage; public/private ports and commit; transfer allowance and overage; IPv4/IPv6; DDoS policy; management/KVM/reimage; replacement and escalation; currency, tax, setup, commitment and renewal. Then confirm batch quantity and lead time. A webpage showing one unit in stock is not evidence of 500 available units.\n')
put('For a refresh pipeline, retain source URL, retrieval method, fetched timestamp, content hash, parsed units and change diff. Monitor changed price/spec/location fields for review rather than overwriting trusted contract data. Respect provider site/API policies. Recheck asset delivery and permission independently of server pricing. Keep legacy/retired offers for historical node snapshots but remove them from an active procurement filter.\n')
put('### Acceptance checks for the UI implementation\n\nThe fixture must load exactly 5,000 unique node IDs and 90 unique supplier records. Every node must join to an existing pool and offer. Country filters must retain correct counts; cleared filters restore the whole fleet. Aggregate tiles must expose unknown coverage. Limited-transfer and unmetered plans must remain distinguishable. Raw and usable storage cannot be swapped. Annual/committed prices cannot be relabeled month-to-month. Synthetic data must never be mistaken for actual production telemetry, and no destructive action may reach a live provider from the simulator.\n')
put('The companion scripts run offline and rebuild the data deterministically. They do not automatically refresh prices or verify live URLs. To refresh, update the researched records and their source qualifications deliberately, then rebuild.\n')
text='\n'.join(md)
(ROOT/'forkalope-bare-metal-worldwide.md').write_text(text,encoding='utf-8')

# Package-level README and validations.
readme=f'''# Forkalope bare-metal research bundle\n\nOpen `forkalope-bare-metal-worldwide.md` first. Research date: {DATE}.\n\n90 curated providers; {coverage['specified_examples']} specified examples; {coverage['numeric_advertised_prices']} numeric advertised prices/starting rates. Missing data is explicit. {len(assets)} direct artwork URLs, not downloaded image files. 5,000 invented nodes across {len(cc_counts)} countries/territories. No real deployment, purchasing or provider API calls are represented.\n\nRebuild with Python 3.10+: `python make_deliverables.py`. Optional `pycountry` improves country names; generated files are already included. The scripts use only standard-library dependencies otherwise.\n\nAll third-party image rights remain with their owners. Verify permission before production reuse. Source links and limits are in the Markdown and JSON.\n'''
(ROOT/'README.md').write_text(readme,encoding='utf-8')
assert len(records)==90
assert len(nodes)==5000 and len({n['id'] for n in nodes})==5000
assert len({a['id'] for a in assets})==len(assets)
assert all(n['offer_id'] in {r['offer_id'] for r in records} for n in nodes)
assert all(n['pool_id'] in {p['id'] for p in pools} for n in nodes)
assert all(p['node_count']==sum(n['pool_id']==p['id'] for n in nodes) for p in pools)
assert len(re.findall(r'^### \d\d\. ',text,re.M))==90
assert sum(status_counts.values())==5000
for r in records:
    for u in r['source_urls']:
        assert urlparse(u).scheme in ('https','http') and urlparse(u).netloc, u
for a in assets: assert urlparse(a['url']).scheme=='https' and a['source_page']
# Verify all internally generated fragment links target anchors or heading IDs explicitly included.
anchors_in=set(re.findall(r'<a id="([^"]+)"></a>',text))
for link in re.findall(r'\]\(#([^\)]+)\)',text): assert link in anchors_in,link
for f in ROOT.glob('*.json'): json.loads(f.read_text())
manifest={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in ROOT.iterdir() if f.is_file() and f.suffix in ('.md','.json','.csv','.py') and f.name!='checksums.sha256'}
(ROOT/'checksums.sha256').write_text(''.join(f'{h}  {name}\n' for name,h in sorted(manifest.items())))
zip_path=ROOT.parent/'forkalope-bare-metal-research-bundle.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for f in sorted(ROOT.iterdir()):
        if f.is_file() and f.suffix in ('.md','.json','.csv','.py','.sha256'): z.write(f,'forkalope-bare-metal-research/'+f.name)
print(json.dumps({'coverage':coverage,'fixture_summary':summary,'markdown_words':len(text.split()),'markdown_bytes':len(text.encode()),'zip_bytes':zip_path.stat().st_size},indent=2))
