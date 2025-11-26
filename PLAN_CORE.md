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

Success = completed work that's useful to community organizations, not comprehensive coverage.

---

## 2. What I'll Do First (Next 2 Weeks)

The first question I care about:

> **"How do community-led initiatives create alternatives to displacement, and what power structures shape housing access?"**

To explore this, I'll:

1. **Set up repo + minimal structure**

   - Create `data/`, `notebooks/`, `src/`, `maps/`, `stories/`, `docs/`.

   - Add this file as `PLAN_CORE.md`.

2. **Create Python environment**

   - Pin: `python`, `geopandas`, `pandas`, `duckdb`, `jupyter`, `contextily` (or similar).

3. **Download anchor datasets + power structure data:**

   **Colonial Categories (use critically):**
   - **City parcels + zoning** → Legal containers for land
   - **Census tracts + ACS demographics** → Official demographics
   - **Santa Fe River + hydrology** → Water as mapped resource
   - **OSM roads + POIs** → Infrastructure networks

   **Counter-Mapping Data (from community research):**
   - **S3 Housing Initiative sites** → Motel conversions (Santa Fe Suites, Lamplighter)
   - **Chainbreaker displacement profiles** → Hopewell-Mann (75% renters, $31,576 median income)
   - **Housing Trust CLT properties** → 90-unit scattered-site preserving affordability
   - **Acequia infrastructure** → NM OSE Acequia Mapping Project linework
   - **Living wage geography** → $15/hr minimum wage impact zones
   - **Princeton Eviction Lab data** → 80+ million records at block group level

   These datasets let me compare official categories with community-generated data.

4. **Make one exploratory notebook**

   - `notebooks/00_exploratory/001_housing_power_alternatives.ipynb`

   - Tasks:

     - Load both colonial categories AND counter-mapping data
     - Map S3 housing sites against displacement pressure zones
     - Visualize living wage impact vs. housing cost burden
     - Calculate: units created through community action vs. market rate development
     - Identify: Major nonprofit/foundation property holdings

5. **Draft first field note (even if rough)**

   - `stories/drafts/field_note_01_hopewell_mann_resistance.md`

   - Walk the Hopewell-Mann corridor (Chainbreaker's focus area)
   - Document O'ga P'ogeh (White Shell Water Place) - Tewa name for Santa Fe
   - Interview Chainbreaker member about Neighborhood Stabilization Plan
   - Contrast community vision with developer pressure
   - Map acequia networks as alternative governance structures

I can refine later. The point is to establish the full pipeline **once**.

---

## 3. How I Choose What to Work On (Prioritization Rules)

When I'm staring at 15 themes and 40 datasets, I'll prioritize work that:

1. **Challenges power rather than documenting inequality**

   - Does this make visible the mechanisms of displacement (corporate ownership, STRs, speculation)?
   - Could this analysis support housing justice movements or Indigenous sovereignty?

2. **Matters beyond my own curiosity**

   - Would a neighbor, planner, organizer, or friend care about this question?
   - Can community organizations use this for advocacy?

3. **Questions the categories themselves**

   - Am I interrogating colonial spatial units (parcels, census tracts)?
   - Can I layer alternative geographies (watersheds, walking distances, ceremonial landscapes)?

4. **Is tractable in 1–2 weeks**

   - Can I get from question → draft map → draft note in that timeframe?
   - But also: does "tractable" mean avoiding harder questions about power?

5. **Has accessible, trustworthy data**

   - At least one decent public dataset; I'm not stuck in scraping hell.
   - But also: whose data is this? Who decided what to count?

6. **Connects to my anchor themes**

   - Land & housing; water & watershed; mobility & access; health & equity.
   - With explicit attention to: displacement, sovereignty, reciprocity

7. **Teaches me something about my immediate lived environment**

   - Changes how I walk, ride, or relate to the city
   - Reveals power structures in familiar places

If a project doesn't hit at least **4/7** of these, it goes in the backlog, not the active queue.

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

1. **Land & Housing** — with focus on displacement mechanisms and resistance
2. **Water & Watershed** — understanding water as relation, not resource

**Counter-Mapping Approaches (Informed by QOL Report):**

Instead of just documenting what is, actively map:

* **Power structures to expose:**
  - 37% of county workers commute (can't afford local housing)
  - 96% of low-income renters experience rent burden
  - Corporate/STR ownership vs community land trusts
  - $68 million acequia infrastructure need vs funding gaps

* **Community-controlled alternatives:**
  - Chainbreaker's Hopewell-Mann Stabilization Plan (700 members)
  - Housing Trust CLT: 700+ homes, 90-unit scattered site
  - Acequia governance: Traditional *repartimiento* water sharing
  - Tewa Women United: *wi don gi mu* ("we are one")
  - Pueblo Action Alliance: #WaterBack campaign

* **Resistance networks & mutual aid:**
  - Somos Un Pueblo Unido: 3,500+ members, worker center
  - Three Sisters Collective: Indigenous women/femme space
  - Food Depot: 28.3 million pounds distributed
  - Earth Care: Southside environmental justice
  - NMAA: Congreso de Las Acequias federation

* **Data sovereignty & counter-knowledge:**
  - Chainbreaker-Human Impact Partners displacement profiles
  - Princeton Eviction Lab: 80+ million records
  - OSE Acequia Mapping: Traditional governance visualization
  - Indigenous place names: O'ga P'ogeh vs "Santa Fe"

**Ethical stance (summary):**

* This work happens on Tewa homelands and in a complex colonial city; my maps are partial views, not neutral truths.

* I will avoid maps that:

  * Expose specific vulnerable people or locations (e.g., encampments, treatment centers).
  * Enable surveillance or displacement through "who lives where" mapping.
  * Sensationalize suffering (addiction, houselessness, crime).
  * Naturalize colonial categories without critique.

* I'll prioritize:

  * **Counter-narratives:** Maps that challenge dominant stories about Santa Fe.
  * **Power analysis:** Making visible the mechanisms of inequality.
  * **Context:** Numbers + history + lived experience + structural analysis.
  * **Care:** Asking "who could be harmed?" AND "who benefits from this analysis?"
  * **Reciprocity:** How does this work give back to affected communities?

Extended reflection, critical framework, and ongoing questions live in:
- `docs/ethics_positionality.md`
- `docs/CRITICAL_REFLECTIONS.md`

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

