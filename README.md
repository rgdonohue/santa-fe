# Santa Fe Field Notes

*A small, honest body of work about Santa Fe that combines maps, analysis, and lived experience.*

This is a geospatial investigation of Santa Fe, New Mexico—not a dissertation, not a data dump, but something in between. Think of it as field notes from someone trying to understand a place through the lens of where people live, how land is used, and where water flows.

## What This Is

This project asks questions like: *Who lives where in relation to water and land-use constraints?* It combines:

- **Maps** that tell spatial stories
- **Analysis** that reveals patterns
- **Narrative** that grounds numbers in lived experience

Each "field note" is a small, finished piece—800–1500 words, at least one map, one chart, and a reflection on what the data reveals about this place.

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

**Anchor themes for v0.1:**

1. **Land & Housing** — Who lives where? How does zoning shape the city?
2. **Water & Watershed** — Where does water flow? How does proximity to water relate to where people live?

These aren't abstract questions. They're grounded in walks through neighborhoods, observations of daily life, and curiosity about how this place works.

## What Makes This Different

- **Small and finished** — We prioritize completed field notes over exhaustive coverage
- **Ethical and reflective** — Maps are partial views, not neutral truths. We ask "who could be harmed?" before publishing
- **Reproducible** — Clean data pipelines, documented sources, version-controlled code
- **Honest** — Acknowledges limitations, lived experience, and the complexity of mapping a place

## Data Sources

We work with five anchor datasets:
- Census tracts + ACS demographics
- City parcels + zoning
- Hydrology (rivers, streams, arroyos)
- OSM roads + POIs
- City limits boundary

See `docs/data_sources.md` for detailed sources, download instructions, and processing notes.

## Ethical Stance

This work happens on Tewa homelands, in a complex colonial city. We avoid maps that expose vulnerable people or sensationalize suffering. We prioritize context, care, and questions that matter beyond our own curiosity.

See `docs/ethics_positionality.md` for the full framework.

## Getting Started

1. Read `PLAN_CORE.md` to understand the approach
2. Follow `SETUP.md` for environment setup
3. Run the data preparation notebook
4. Start your first field note

**Remember:** Better a small practice done consistently than a grand intention postponed indefinitely.

---

*"Who lives where in relation to water and land-use constraints?"* — That's where we start.

