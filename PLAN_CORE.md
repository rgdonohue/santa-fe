# Santa Fe Field Notes – Core Plan (v0.1)

Timebox: **Nov–Feb (12–16 weeks)**  

Goal: A small, honest body of work about Santa Fe that combines **maps, analysis, and lived experience** — not a dissertation.

---

## 1. v0.1 Outcomes (By End of January)

By ~end of January, I want:

1. **3 published "field notes"**  

   - Each with at least 1 map + 1 chart + 800–1500 words.

2. **1 baseline basemap** for Santa Fe  

   - Reusable for future projects (simple, legible, documented style).

3. **2 "anchor themes" chosen for deeper work**  

   - e.g., (a) Land & Housing, (b) Water & Watershed.

4. **1 clean, reproducible data pipeline**  

   - From raw downloads → processed tables/shapes → analysis-ready layers.

Success = small, finished artifacts that feel true, not exhaustive coverage.

---

## 2. What I'll Do First (Next 2 Weeks)

The first question I care about:

> **"Who lives where in relation to water and land-use constraints?"**

To answer a first, rough version of that, I'll:

1. **Set up repo + minimal structure**

   - Create `data/`, `notebooks/`, `src/`, `maps/`, `stories/`, `docs/`.

   - Add this file as `PLAN_CORE.md`.

2. **Create Python environment**

   - Pin: `python`, `geopandas`, `pandas`, `duckdb`, `jupyter`, `contextily` (or similar).

3. **Download 4 anchor datasets (on purpose):**

   - **City parcels + zoning (city GIS)**  

     → Where are the legal containers for land + how are they classified?

   - **Census tracts + ACS demographics**  

     → Who lives where: income, race/ethnicity, housing tenure, etc.

   - **Santa Fe River + arroyos / hydrology layer**  

     → Where water and flow paths actually sit in space.

   - **OSM roads + POIs**  

     → Everyday infrastructure: streets, services, landmarks.

   Together, these let me make a first map of **people + parcels + zoning + water + roads** — a structural snapshot touching at least **3 themes** (land/housing, water, mobility).

4. **Make one exploratory notebook**

   - `notebooks/00_exploratory/001_who_lives_where.ipynb`

   - Tasks:

     - Load the 4 datasets.

     - Clip to Santa Fe city limits.

     - Simple maps: parcels over census tracts, river, and main roads.

     - 2–3 quick stats (e.g., median income by distance to river, % renters by zoning category).

5. **Draft first field note (even if rough)**

   - `stories/drafts/field_note_01.md`

   - Anchor it in a real walk or bike ride through my neighborhood.

   - Use 1–2 figures from the notebook, even if they're imperfect.

I can refine later. The point is to establish the full pipeline **once**.

---

## 3. How I Choose What to Work On (Prioritization Rules)

When I'm staring at 15 themes and 40 datasets, I'll prioritize work that:

1. **Matters beyond my own curiosity**

   - Would a neighbor, planner, organizer, or friend care about this question?

2. **Is tractable in 1–2 weeks**

   - Can I get from question → draft map → draft note in that timeframe?

3. **Has accessible, trustworthy data**

   - At least one decent public dataset; I'm not stuck in scraping hell.

4. **Connects to my anchor themes**

   - Land & housing; water & watershed; mobility & access; health & equity.

5. **Teaches me something about my immediate lived environment**

   - Bonus points if it changes how I walk, ride, or relate to the city.

If a project doesn't hit at least **3/5** of these, it goes in the backlog, not the active queue.

---

## 4. Tools: When to Use What

Short, opinionated rules so I don't thrash:

- **Python + Notebooks (Jupyter/Quarto)**

  - Use when:

    - I might repeat the analysis.

    - I'll publish the result or reuse the code.

    - I need joins, aggregations, or model-y stuff.

  - Default for: data cleaning, ESDA, charts, and "story-ready" figures.

- **QGIS**

  - Use when:

    - I need quick visual QA (projection weirdness, topology issues).

    - I'm experimenting with symbology before encoding it in code.

    - I want a one-off high-polish static map.

  - Treat as: **drafting table & eyeball check**, not the core pipeline.

- **MapLibre (web maps)**

  - Use only when:

    - Interactivity truly adds insight (hover, zoom, temporal slider, etc.).

    - There's a concrete use case (story map, shareable demo).

  - Do **not** default to web maps. Earn the interactivity.

- **Writing tools (Markdown, maybe a blog engine later)**

  - All narrative is drafted in plain text (`stories/drafts`).

  - Figures from notebooks/QGIS are exported and linked here.

---

## 5. Minimal Directory Structure (v0.1)

Keep this small to start; I can always elaborate.

```text
data/
  raw/
  processed/

notebooks/
  00_exploratory/
  10_analysis/

src/
  data/
  analysis/
  viz/

maps/
  static/

stories/
  drafts/
  published/

docs/
  data_sources.md
  ethics_positionality.md
```

* This file lives at repo root as `PLAN_CORE.md`.

* Deeper detail (full data catalog, extended ethics, methods) go into `docs/`.

---

## 6. Themes & Ethics (Short Version)

**Anchor themes for v0.1 (pick two):**

* Land, housing, and displacement
* Water and watershed
* Mobility, access, and daily life
* Health, environment, and equity
* Culture, history, and memory

For now I'll lean toward:

1. **Land & Housing**
2. **Water & Watershed**

**Ethical stance (summary):**

* This work happens on Tewa homelands and in a complex colonial city; my maps are partial views, not neutral truths.

* I will avoid maps that:

  * Expose specific vulnerable people or locations (e.g., encampments, treatment centers).

  * Sensationalize suffering (addiction, houselessness, crime).

* I'll prioritize:

  * Context: numbers + history + lived experience.

  * Care: asking "who could be harmed if this map circulates?"

Extended reflection and land acknowledgment live in `docs/ethics_positionality.md`.

---

## 7. Maintenance Ritual

Once every 2–3 weeks:

1. Re-read this plan.

2. Update:

   * v0.1 outcomes (if they've shifted).

   * Anchor themes (if they've clarified).

   * Next 2–3 concrete steps.

3. Move at least one thing from `stories/drafts` → `stories/published`.

Goal: keep this document short enough that I actually revise it.

