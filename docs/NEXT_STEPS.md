# Next Steps Guide

Prioritize counter-mapping displacement and water governance, using the updated sources and guardrails.

## Immediate Tasks (this week)

1. **Prep data (colonial + community layers)**
   - Run `notebooks/00_exploratory/000_data_prep.ipynb` for parcels/tracts/OSM/hydrology/city limits.
   - Manually add counter-mapping layers: S3 motel conversions (Santa Fe Suites 122 units; Lamplighter acquisition), Housing Trust CLT parcels, acequia linework, Princeton Eviction Lab block-group CSV (aggregate only), Chainbreaker displacement profile attributes.
   - Record download dates and sources in `docs/data_sources.md`.

2. **Exploratory notebook: housing power & alternatives**
   - Use `notebooks/00_exploratory/001_who_lives_where.ipynb` as a base or clone to `001_housing_power_alternatives.ipynb`.
   - Tasks: join cost-burden + living-wage geography, map S3/CLT sites vs. displacement pressure, overlay acequia commons, compute community-created units vs. recent market-rate units (approximate if needed).
   - Export 1–2 maps to `maps/static/` for use in the first field note.

3. **Field note draft**
   - File: `stories/drafts/field_note_01_hopewell_mann_resistance.md` (or similar).
   - Anchor in a walk/ride through Hopewell-Mann or Airport Road corridor; pair narrative with maps from the exploratory notebook.

## Guardrails (apply to all mapping)
- No point-level sensitive data (evictions, crisis calls, domestic violence shelters, unhoused encampments). Aggregate/blur and get partner consent for care-related sites.
- Indigenous/acequia data: use public acequia lines; anything else requires permission from Pueblo partners.
- Share drafts and maps with Chainbreaker/NMAA/S3 partners before publishing.

## Documentation to update
- `docs/data_sources.md`: fill URLs, dates, processing notes for each added layer; mark anything withheld for sensitivity.
- `docs/ethics_positionality.md`: add your own positionality statement.
- `docs/COUNTER_MAPPING_STRATEGY.md`: log which partners reviewed the latest maps.

## If stuck
- CRS issues: ensure layers are in EPSG:32113 for analysis; use EPSG:3857 only for web tiles.
- Data gaps: note them in `docs/data_sources.md` and proceed with placeholders; do not improvise with unverified data.
- Analysis feels thin: add power analysis (ownership concentration, AHTF allocation geography) rather than more choropleths.

**Remember:** Small, finished artifacts that partners can use beat broad-but-incomplete analyses.
