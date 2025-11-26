# Data Sources

Lightweight catalog of datasets used in this project, with provenance for key stats and guidance on what to map (and what not to map).

## Critical Note on Data Categories

The core datasets rely on colonial spatial categories—parcels, census tracts, zoning districts—that encode private property regimes and state surveillance. Use them critically. See `CRITICAL_REFLECTIONS.md` for epistemological concerns.

## Provenance for Frequently Cited Numbers

- **96% rent burden (low-income renters):** Human Impact Partners + Chainbreaker, "Evictions in the COVID-19 Era" (2021)
- **5,000+ unit housing gap / $582k median home price:** City housing needs assessments (2024 market studies; Realtors Assoc. of NM reports)
- **$3M+ Affordable Housing Trust Fund annual allocation:** City of Santa Fe AHTF ordinance and FY2024 award docs
- **122-unit Santa Fe Suites motel conversion / Lamplighter acquisition:** S3 Santa Fe Housing Initiative press releases (2020–2022)
- **$68M acequia infrastructure need:** NMAA legislative priorities (2025)
- **Living wage $15/hr (2025):** City of Santa Fe Living Wage Ordinance

## Anchor Datasets (v0.1)

### Parcels + Zoning
- **Source:** City of Santa Fe GIS Portal (ArcGIS Online)
- **URL:** https://santafenm.gov/gis (search "Parcels" / "Zoning")
- **Format:** Shapefile/GeoPackage; CRS often EPSG:2257; reproject to project CRS
- **Notes:** Legal land containers; use for joins with ownership/zoning analysis

### Census Tracts + ACS Demographics
- **Source:** U.S. Census TIGER/Line + ACS 5-year
- **URLs:** https://www2.census.gov/geo/tiger/TIGER2022/TRACT/ and https://api.census.gov/data/
- **Format:** Shapefile + API CSV/JSON
- **Notes:** Income, tenure, rent burden; requires API key

### Hydrology (Santa Fe River + Arroyos)
- **Source:** USGS 3D Hydrography Program (replaces NHD) + city water layers where available
- **URL:** https://www.usgs.gov/3d-hydrography-program/access-3dhp-data-products
- **Format:** GDB/Shapefile/GeoPackage
- **Notes:** Use for river/arroyo context; clip to city limits

### Roads + POIs
- **Source:** OpenStreetMap (GeoFabrik Southwest extract or Overpass API)
- **URL:** https://download.geofabrik.de/north-america/us/southwest.html
- **Format:** PBF → GeoPackage/GeoJSON
- **Notes:** Streets, services, landmarks; refresh as needed

### City Limits
- **Source:** TIGER/Line Places (PLACEFP=70490) or City GIS boundary
- **URL:** https://www2.census.gov/geo/tiger/TIGER2022/PLACE/
- **Format:** Shapefile/GeoPackage
- **Notes:** Used for clipping/extent

## Counter-Mapping Layers

### Housing / Displacement
- **Eviction burden:** Princeton Eviction Lab block-group CSV (https://evictionlab.org/) — aggregate only; no point-level filings
- **Community-created housing:** S3 motel conversions (Santa Fe Suites 122 units; Lamplighter acquisition) and Housing Trust CLT parcels — manual geocoding from press releases/AHTF awards
- **Cost burden & living wage:** ACS cost-burden tables + City Living Wage Ordinance geography ($15/hr in 2025)
- **Chainbreaker profiles:** Hopewell-Mann and Airport Road displacement profiles (HIP/Chainbreaker 2021)

### Water & Commons
- **Acequia network:** NM OSE Acequia Mapping Project (2017–2019) from https://gis.ose.state.nm.us/
- **Water rights settlements:** Aamodt Settlement (2017), Ohkay Owingeh Settlement (2023) — court/legislative records for summary attributes
- **Indigenous lands:** BIA Tract Viewer (respect data sensitivity; use only with permission)

### Care Networks (from QOL survey)
- **Diversion and crisis response:** LEAD/Thrive sites; La Sala Crisis Center (Santa Fe County); CONNECT network nodes (aggregate to neighborhoods or grid)
- **Youth support:** YouthWorks sites; Communities in Schools (11 schools) — map as area/cluster, not individuals
- **Health safety net:** La Familia Medical Center, FQHCs; use facility points only if partners agree

## What to Map vs. What to Avoid (from QOL report)

| Category | Map | Avoid |
| --- | --- | --- |
| Housing | S3 sites, CLT parcels, AHTF-funded projects (aggregated) | Point-level eviction filings or individual addresses of unhoused residents |
| Public health/care | Facility locations (clinics, crisis centers) with partner consent; CONNECT coverage areas | Individual patient/service data; any identifiable crisis locations |
| Education/youth | School sites (Communities in Schools), YouthWorks hubs | Individual student-level data or sensitive program addresses (domestic violence shelters) |
| Public safety | LEAD/Thrive service zones, non-police crisis response coverage | Crime hotspotting that could stigmatize neighborhoods |
| Indigenous/acequia | Acequia lines (public), settlement footprints with context | Sacred/ceremonial sites without explicit permission |

## Processing & Storage

- Raw downloads → `data/raw/`; processed GeoPackages → `data/processed/`
- Standard CRS: EPSG:32113 (analysis) and EPSG:3857 (web map tiles); document CRS per layer
- Sensitive data: keep out of repo; aggregate/blurring required for any person-level data

## Community Return & Citation

- Share finished layers/maps with Chainbreaker, NMAA, Pueblo partners, and S3 coalition before publication.
- Cite community sources (HIP/Chainbreaker profiles, acequia linework credits, S3 press releases) alongside official datasets in notebooks and stories.

**Last updated:** 2025-02-11
