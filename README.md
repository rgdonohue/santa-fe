# Santa Fe Field Notes

A geospatial analysis project documenting housing displacement and community responses in Santa Fe, New Mexico.

![Santa Fe Field Notes](docs/santa-fe-masthead-3.png)

## Purpose

Santa Fe faces a housing crisis: 96% of low-income renters are cost-burdened, median home prices have reached $582,000 (double Albuquerque's), and 37% of county workers commute because they can't afford to live where they work. This project maps both the crisis and community-led solutions.

The work focuses on two neighborhoods experiencing intense displacement pressure—Hopewell-Mann and the Airport Road corridor—where grassroots organizations are actively organizing for housing justice. By combining public datasets with community-generated research, the project aims to produce maps and analysis useful for ongoing advocacy efforts.

## Quick Start

1. **Set up your environment:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Download the data:**
   Run `notebooks/00_exploratory/000_data_prep.ipynb` to download and process the core datasets (census tracts, parcels, hydrology, OSM, city limits).

3. **Start exploring:**
   Open `notebooks/00_exploratory/001_who_lives_where.ipynb` to begin your first analysis.

4. **Read the plan:**
   See `PLAN_CORE.md` for the full strategy, prioritization rules, and v0.1 outcomes.

## Project Structure

```
santa-fe/
├── data/           # Raw downloads and processed GeoPackages
├── notebooks/       # Exploratory (00_) and analysis (10_) notebooks
├── src/            # Reusable Python modules (loaders, viz, analysis)
├── maps/           # Static map outputs
├── stories/        # Field notes (drafts → published)
└── docs/           # Data sources, ethics, methods
```

## Key Research Questions

1. **Housing**: How many affordable units have community organizations created compared to market-rate development? Where are eviction pressures highest?

2. **Ownership**: Who owns Santa Fe's rental properties? How concentrated is ownership among corporate landlords?

3. **Alternatives**: Where are community land trusts, cooperative housing, and other non-market models succeeding?

4. **Water**: How do traditional acequia systems challenge privatized water management? What's the gap between infrastructure needs and funding?

## Methodology

The project uses GIS to analyze spatial patterns while recognizing that standard geographic categories (census tracts, parcels) encode colonial histories. Key approaches:

- Compare official data with community-generated research (Chainbreaker's displacement profiles, Princeton Eviction Lab data)
- Aggregate sensitive data to protect privacy (no point-level evictions or individual addresses)
- Partner with local organizations before publishing maps that could affect their work
- Document both problems and solutions—not just mapping crisis but highlighting alternatives

## Data Sources

Colonial spatial categories (used critically):
- Census tracts, parcels, zoning districts
- Official hydrology layers

Community-generated research:
- Chainbreaker displacement profiles (Hopewell-Mann)
- Princeton Eviction Lab data (block group level)
- NM OSE Acequia Mapping Project
- Housing Trust CLT properties
- S3 motel conversions (Santa Fe Suites 122 units; Lamplighter acquisition)

See `docs/data_sources.md` for sources and `docs/CRITICAL_REFLECTIONS.md` for epistemological concerns about these categories.

**Source notes for key stats:** 96% rent burden from Human Impact Partners/Chainbreaker COVID-era research (2021); 5,000+ unit deficit and $582k median price from recent city housing needs assessments (2024); $3M+ AHTF allocation from city ordinance/FY2024 awards; $68M acequia need from NMAA legislative priorities (2025).

## Ethics & Privacy

This work takes place on unceded Tewa homelands. Key commitments:

- **No surveillance mapping**: No point-level evictions, individual addresses, or unhoused encampment locations
- **Partner consent**: Share maps with affected organizations before publication
- **Aggregate sensitive data**: Blur locations of crisis services, domestic violence shelters, and care networks
- **Support organizing**: Prioritize analysis that helps community campaigns

See `docs/ethics_positionality.md` for detailed framework.

## Contributing

This project welcomes contributions that:
- Add community-generated data sources
- Improve analysis methods
- Document housing victories
- Connect findings to organizing campaigns

Contact information for key community partners:
- **Chainbreaker Collective**: 505-577-5481 (eviction prevention hotline)
- **NM Acequia Association**: Research on traditional water governance
- **S3 Housing Coalition**: Motel conversion projects

## Setup

See `SETUP.md` for detailed environment setup. Basic requirements:
- Python 3.11+
- GeoPandas, DuckDB, Jupyter
- 2GB disk space for processed data

---

*Supporting housing justice and water sovereignty in Santa Fe through careful data analysis.*
