# Counter-Mapping Strategy for Santa Fe

## Overview

This document outlines a counter-mapping approach using community-generated data and critical analysis to challenge dominant narratives about Santa Fe. The focus is on supporting ongoing organizing efforts.

## Core Principle

Counter-mapping asks: "Who benefits from current arrangements?" and "What alternatives exist?"

## Mapping Projects

### 1. Housing: From Crisis to Transformation

**Traditional Narrative:** "Santa Fe has a housing affordability crisis"
**Counter-Narrative:** "Community organizations build alternatives while exposing extraction"

**Critical Context:**
- Housing deficit: 5,000+ units
- Median home price: $582,000 (double Albuquerque)
- 96% of low-income renters experience burden
- 37% of county workers commute (priced out)

**Data Layers:**
- Chainbreaker's Hopewell-Mann profiles (75% renters, $31,576 median)
- Housing Trust CLT: 700+ homes, 90-unit scattered site
- S3 Housing Initiative sites (122+ units)
- Princeton Eviction Lab data (block group level)
- Living wage geography ($15/hr zones)
- Acequia infrastructure as commons

**Key Visualizations:**
```python
# Map 1: "Creating Housing Outside the Market"
# Show S3 motel conversions (122+ units) vs luxury developments
# Highlight community investment vs private speculation

# Map 2: "Who Really Owns Santa Fe?"
# Corporate ownership concentration
# Anchorum, major nonprofits property holdings
# Empty/underused properties vs homeless counts

# Map 3: "Staying in Place"
# Living wage zones vs displacement pressure
# Where $15/hr makes housing affordable
```

**Key Questions:**
- How many units has community action created vs market development?
- Where does nonprofit property ownership concentrate?
- How does living wage geography overlap with affordable housing?

### 2. Carceral Geographies to Care Networks

**Traditional Narrative:** "Public safety through policing"
**Counter-Narrative:** "Community care prevents harm"

**Data Layers:**
- LEAD/Thrive diversion sites
- Crisis response locations (non-police)
- YouthWorks sites (1,000 youth/year)
- Communities in Schools (11 locations)
- Mental health/substance support sites

**Key Visualizations:**
```python
# Map 1: "Alternatives to Incarceration"
# LEAD diversion sites vs jail
# Success metrics (reduced arrests, better outcomes)

# Map 2: "Youth Support Ecosystem"
# YouthWorks, Communities in Schools locations
# Overlay with poverty/risk indicators
# Show protective factors vs punitive responses

# Map 3: "Crisis Care Not Cops"
# La Sala Crisis Center, behavioral health sites
# Compare response times/outcomes vs police
```

### 3. Indigenous Sovereignty vs Municipal Boundaries

**Traditional Narrative:** "Santa Fe city limits and service areas"
**Counter-Narrative:** "O'ga P'ogeh (White Shell Water Place) - ongoing Tewa homeland"

**Organizations Leading:**
- Tewa Women United (*wi don gi mu* - "we are one")
- Pueblo Action Alliance (#WaterBack campaign)
- Three Sisters Collective (Indigenous women/femme space)
- Santa Fe Indigenous Center

**Data Layers (with permission only):**
- O'ga P'ogeh vs "Santa Fe" place names
- Aamodt Settlement water rights (2017)
- Ohkay Owingeh Settlement ($818.3M federal)
- BIA Tract Viewer (tribal/allotted lands)
- Historic Pueblo Revolt (1680) sites

**Approach:**
- Center #LandBack and #WaterBack frameworks
- Partner directly with Pueblo governments
- Visualize water as relation, not resource
- Show continuous 10,000+ year presence

### 4. Wealth Extraction vs Community Wealth

**Traditional Narrative:** "Economic development creates prosperity"
**Counter-Narrative:** "Concentrated wealth extracts from community"

**Data Layers:**
- Foundation assets vs community needs
- Nonprofit executive salaries vs living wage
- STR concentration vs long-term rentals
- Art market wealth vs artist displacement
- Tourism infrastructure vs resident services

**Key Visualizations:**
```python
# Map 1: "Following the Money"
# Foundation headquarters vs funded programs
# Show extraction (where wealth accumulates)
# vs distribution (where programs operate)

# Map 2: "Two Santa Fes"
# Tourist Santa Fe (galleries, hotels, STRs)
# vs Resident Santa Fe (schools, clinics, groceries)
# Price differentials and access barriers

# Map 3: "Making a Living vs Making a Killing"
# Living wage employers
# Worker centers and union sites
# Wage theft hotspots
```

## Data Collection Strategy

### Critical Community-Generated Data

1. **Chainbreaker-Human Impact Partners Research**
   - "Equitable Development & Risk of Displacement" profiles
   - Hopewell-Mann, Airport Road, Canyon Road, Downtown
   - Most granular displacement data available
   - 96% rent burden documentation

2. **Princeton Eviction Lab**
   - 80+ million records nationally
   - Census block group level for Santa Fe
   - Track displacement in real-time

3. **Acequia Infrastructure Mapping**
   - NM OSE Acequia Mapping Project (2017-2019)
   - Traditional governance visualization
   - $68 million infrastructure need documented
   - NMAA Congreso de Las Acequias data

4. **Indigenous Water Rights Data**
   - Aamodt Settlement (2017) quantifications
   - Ohkay Owingeh Settlement (2023) - $818.3M
   - BIA Tract Viewer for tribal lands
   - Pueblo Action Alliance #WaterBack research

### Participatory Methods

1. **Community Mapping Sessions**
   - Partner with organizations
   - Use local knowledge to define boundaries
   - Identify assets not in official data

2. **Walking Interviews**
   - Document displacement stories
   - Map desire paths vs official routes
   - Record sensory/emotional geographies

3. **Youth Mapping**
   - Partner with Mayor's Youth Advisory Board
   - Map youth-defined safe/unsafe spaces
   - Document youth vision for Santa Fe

## Technical Implementation

### Phase 1: Critical Data Assembly
```python
# Load QOL report datasets
qol_data = {
    's3_housing': load_s3_sites(),
    'living_wage': calculate_wage_zones(),
    'lead_thrive': map_diversion_program(),
    'youth_programs': load_youthworks_sites()
}

# Add power analysis layers
power_data = {
    'corporate_owners': load_assessor_data(),
    'nonprofit_property': load_990_data(),
    'foundation_flows': track_funding()
}

# Critically examine colonial categories
colonial_critique = {
    'census_tracts': add_redlining_history(),
    'parcels': show_commons_enclosure(),
    'zoning': reveal_segregation_origins()
}
```

### Phase 2: Counter-Visualization
- Use color to show community vs corporate
- Animate temporal changes (displacement over time)
- Create "view from below" perspectives
- Show uncertainty and contested boundaries

### Phase 3: Community Return
- Share maps with partner organizations (Chainbreaker, NMAA, Pueblo partners, S3 coalition) before publishing
- Create accessible formats (print handouts, PNGs, low-bandwidth web)
- Support active campaigns (AHTF allocations, #WaterBack, Hopewell-Mann stabilization) with tailored views
- Document usage (meetings informed, campaigns supported) and iterate

### What to Map vs. Avoid (from QOL survey + displacement focus)
- **Map (aggregate/consented):** S3 sites, CLT parcels, LEAD/Thrive coverage areas, CONNECT service zones, Communities in Schools locations, YouthWorks hubs, acequia lines, AHTF-funded projects
- **Avoid/blur:** Point-level eviction filings, individual unhoused locations, domestic violence shelters, sacred/ceremonial sites without permission, person-level health data
- **Mitigations:** Aggregate to neighborhood/grid, remove exact addresses, confirm with partners before release

## Ethical Commitments

1. **No Surveillance:** Never create maps that could be used to surveil or displace vulnerable communities

2. **Community Consent:** Always get permission before mapping community assets or Indigenous sites

3. **Power Analysis:** Every map should ask "who benefits?"

4. **Action Orientation:** Maps should support concrete campaigns for justice

5. **Accessibility:** Ensure maps are available to those without technical expertise

## Success Metrics

Rather than traditional GIS metrics, evaluate based on:
- Maps used in community campaigns
- Policy changes influenced by visualizations
- Community members trained in counter-mapping
- Dominant narratives challenged
- Power structures made visible

## Limitations and Ongoing Questions

- Can master's tools (GIS) dismantle master's house?
- How to avoid co-optation of counter-maps?
- What responsibilities come with making power visible?
- How to ensure community control of their data?
- When should we refuse to map?

## Resources and Partnerships

### Essential Community Partners

**Housing Justice & Anti-Displacement:**
- **Chainbreaker Collective** (700 members)
  - Contact: 505-577-5481 (eviction hotline)
  - Hopewell-Mann Stabilization Plan lead
- **Santa Fe Housing Action Coalition**
  - Secured $3M annual Housing Trust Fund
- **The Housing Trust** (formerly SF Community Housing Trust)
  - 700+ affordable homes, CLT model

**Indigenous Sovereignty:**
- **Tewa Women United** (since 1989)
  - Six northern Pueblos collaboration
  - Environmental justice & reproductive justice
- **Pueblo Action Alliance**
  - #WaterBack campaign leadership
- **Three Sisters Collective**
  - Dr. Christina Castro (Taos/Jemez Pueblo)

**Water & Environmental Justice:**
- **NM Acequia Association** (NMAA)
  - Congreso de Las Acequias federation
  - Acequia mapping and governance
- **Earth Care New Mexico**
  - Southside environmental justice
  - YUCCA youth climate organizing
- **Communities for Clean Water Coalition**
  - LANL contamination response

**Worker & Immigrant Rights:**
- **Somos Un Pueblo Unido** (3,500+ members)
  - Worker center, wage theft prevention
  - Living wage campaign victory

### Technical Resources
- Santa Fe Data Platform API
- QGIS for collaborative mapping
- Leaflet for web-based story maps
- Observable for interactive visualizations

### Inspirations
- Anti-Eviction Mapping Project
- Design Studio for Social Intervention
- Counter Cartographies Collective
- Indigenous Mapping Network

---

*This strategy is a living document. It should evolve based on community needs and feedback.*
