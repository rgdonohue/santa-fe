# Santa Fe Field Notes

*A small, honest body of work about Santa Fe that combines maps, analysis, and lived experience.*

This is a geospatial investigation of Santa Fe, New Mexico—not a dissertation, not a data dump, but something in between. Think of it as field notes from someone trying to understand a place through the lens of where people live, how land is used, and where water flows.

![Santa Fe Field Notes](docs/santa-fe-masthead-3.png)

## What This Is

This project examines housing, displacement, and water in Santa Fe through critical geography. It focuses on:

- **Counter-mapping** that shows community alternatives to market-driven development
- **Power analysis** identifying who owns land and who gets displaced
- **Field notes** combining data analysis with walking and observation

Each piece includes maps, data analysis, and narrative—aiming for 800-1500 words that connect statistics to lived experience.

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

## The Questions We're Asking

**Focus areas:**

1. **Housing & Displacement** — Documenting both displacement pressures (96% of low-income renters are cost-burdened) and community alternatives (Housing Trust's 700+ affordable homes, Chainbreaker's organizing in Hopewell-Mann)

2. **Water Governance** — Mapping acequia infrastructure as commons management, Indigenous water rights settlements, and the gap between $68 million infrastructure needs and available funding

The work centers specific neighborhoods (Hopewell-Mann, Airport Road corridor) where community organizations are actively resisting displacement.

## Approach

- **Critical geography** — Using GIS to question power structures, not naturalize them
- **Community accountability** — Working with/learning from organizations like Chainbreaker Collective and NM Acequia Association
- **Counter-mapping** — Visualizing community land trusts, cooperative housing, and traditional water governance as alternatives
- **Partial and situated** — Maps as one perspective, not authoritative truth

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

## Ethics

This work takes place on Tewa homelands—specifically O'ga P'ogeh (White Shell Water Place). The project aims to support housing justice and Indigenous sovereignty rather than enable surveillance or displacement.

See `docs/ethics_positionality.md` for framework and `docs/COUNTER_MAPPING_STRATEGY.md` for approach.

## Getting Started

1. Read `PLAN_CORE.md` to understand the approach
2. Follow `SETUP.md` for environment setup
3. Run the data preparation notebook
4. Start your first field note

**Remember:** Better a small practice done consistently than a grand intention postponed indefinitely.

---

*A project examining displacement and resistance in Santa Fe through maps, data, and field observation.*
