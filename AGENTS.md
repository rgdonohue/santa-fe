# Repository Guidelines

## Critical Note for AI Assistants

This project engages with critical geography and counter-mapping approaches. When working on this codebase:
- Recognize that spatial categories (parcels, census tracts) are not neutral but carry colonial histories
- Prioritize analyses that make power visible rather than just documenting inequality
- Consider alternative methodologies beyond pure quantitative analysis
- See `docs/CRITICAL_REFLECTIONS.md` for epistemological framework

## Project Structure & Module Organization
- `src/` holds Python modules (`data/` loaders for parcels/census/hydrology/OSM, `analysis/` transforms, `viz/` mapping helpers).
- `notebooks/` is split into `00_exploratory/` for quick passes and `10_analysis/` for refined runs.
- `data/raw/` keeps downloads; `data/processed/` holds cleaned layers consumed by loaders; keep both out of version control.
- Outputs live in `maps/static/` (figures) and `stories/` (drafts and published notes). Documentation sits in `docs/`.

## Build, Test, and Development Commands
- Environment setup:
  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
- Optional kernel registration:
  ```bash
  python -m ipykernel install --user --name santa-fe --display-name "Python (santa-fe)"
  ```
- Launch the main exploratory notebook:
  ```bash
  jupyter lab notebooks/00_exploratory/001_who_lives_where.ipynb
  ```
- Quick dependency check:
  ```bash
  python -c "import geopandas, pandas, duckdb; print('ok')"
  ```

## Coding Style & Naming Conventions
- Follow PEP 8 with 4-space indentation; snake_case for files/functions; type hints where helpful.
- Keep shared logic in `src/`; notebooks should call helpers instead of duplicating code.
- Use docstrings that note CRS, column expectations, and required file locations.
- Notebook names stay zero-padded (`001_topic.ipynb`) to preserve order.

## Testing & Validation Guidelines
- No formal automated suite yet; validate changes by running affected notebooks or a short script that loads processed layers and renders a sample map.
- If you add tests, prefer `pytest` under `tests/` with tiny GeoJSON fixtures rather than bulky raw data.
- Re-run notebooks touched by code changes to confirm clean execution.

## Commit & Pull Request Guidelines
- Commit subjects are concise and present-tense (`data: add hydrology loader guard`, `viz: tweak basemap alpha`).
- PRs should cover purpose, modules/notebooks touched, data sources, and before/after visuals when maps change.
- Link plan items from `PLAN_CORE.md` when relevant and log new datasets in `docs/data_sources.md`.
- Do not commit large raw or processed files; document download and processing steps instead.

## Data Handling & Configuration
- Keep secrets in environment variables or a `.env` file loaded via `python-dotenv`; never hardcode credentials.
- Preserve the separation between `data/raw/` and `data/processed/`; regenerate processed layers rather than editing in place.
- Export maps via `src/viz/maps.save_map` at 300 dpi and store under `maps/static/` with descriptive names (`river_corridor_v1.png`).
- Be aware that data categories themselves encode power relations; document these in analysis.

## Alternative Methodologies

Beyond traditional GIS/Python workflows, consider integrating:

### Participatory Methods
- **Community mapping sessions:** Involve residents in defining spatial questions
- **Oral history collection:** Document lived experience of place
- **Photo-voice:** Visual documentation by community members
- **Walking interviews:** Mobile methods that reveal embodied knowledge

### Contemplative Approaches
- **Sitting practice with maps:** What arises from sustained attention?
- **Walking meditation routes:** Data collection as contemplative practice
- **Deep listening sessions:** Attending to place without extraction

### Counter-Mapping Techniques
- **Power mapping:** Visualize ownership networks, corporate entities
- **Inverse analysis:** Map what's absent, hidden, or erased
- **Temporal layers:** Show displacement and change over time
- **Uncertainty visualization:** Make visible what we don't know

### Implementation Notes
- These methods complement but don't replace quantitative analysis
- Document alternative methods in field notes alongside code
- Consider mixed-method notebooks that combine computation with reflection
- Acknowledge when technical methods reach their limits
