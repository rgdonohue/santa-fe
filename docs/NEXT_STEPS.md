# Next Steps Guide

After completing data download (`000_data_prep.ipynb`), here's what to tackle next.

## Immediate Next Steps

### 1. Complete First Analysis Notebook ✅

**File:** `notebooks/00_exploratory/001_who_lives_where.ipynb`

**Status:** Now functional! The notebook:
- ✅ Loads all 4 anchor datasets
- ✅ Creates overview map
- ✅ Calculates basic statistics (distance to river, zoning analysis)
- ⚠️ ACS demographic data joining still needs Census API key

**To do:**
- Run the notebook and verify it works with your data
- Adjust column names if your datasets have different field names
- Join ACS demographic data if you have Census API key
- Refine analysis based on what you discover

### 2. Generate Baseline Basemap ✅

**Script:** `scripts/create_basemap.py`

**Usage:**
```bash
python scripts/create_basemap.py
```

Or run in notebook:
```python
from scripts.create_basemap import create_baseline_basemap
create_baseline_basemap()
```

**Output:** `maps/static/baseline_basemap_santa_fe.png`

This creates a clean, reusable basemap template for future maps.

### 3. Write First Field Note 📝

**File:** `stories/drafts/field_note_01.md`

**Template is ready** - fill in:
- **Title:** Something specific and engaging
- **Date & Location:** Actual date and route of your walk/bike ride
- **The Question:** What you're investigating (from the notebook)
- **What I Found:** Use 1-2 maps/charts from the notebook
- **Reflection:** What this taught you about your environment
- **Data & Methods:** List datasets used
- **Next Steps:** What questions this raises

**Tips:**
- Anchor it in real experience (a walk, bike ride, observation)
- Use maps from `001_who_lives_where.ipynb`
- Keep it 800-1500 words (per PLAN_CORE.md)
- Don't worry about perfection - this is v0.1!

### 4. Fill Out Data Sources Documentation ✅

**File:** `docs/data_sources.md`

**Status:** Already pretty complete! Has:
- ✅ URLs for all datasets
- ✅ Download instructions
- ✅ Processing notes
- ✅ FIPS codes

**To do:**
- Add actual download dates when you get data
- Note any issues encountered
- Document any manual processing steps
- Add links to specific city GIS pages if found

### 5. Complete Ethics & Positionality 📝

**File:** `docs/ethics_positionality.md`

**Status:** Framework is there, needs your personal content

**To fill in:**
- **Positionality section:** Who are you in relation to Santa Fe?
  - Are you a resident? Visitor? Researcher?
  - What's your background/identity?
  - What assumptions do you bring?
  - How do you navigate privilege and power?
  
**Tips:**
- Be honest and reflective
- This is a living document - you can revise as you learn
- Consider: What does it mean to map a place you may or may not be from?

## Workflow Suggestions

### Week 1-2: Data & Analysis
1. ✅ Download all datasets (`000_data_prep.ipynb`)
2. ✅ Run exploratory analysis (`001_who_lives_where.ipynb`)
3. ✅ Generate baseline basemap
4. 📝 Start drafting first field note

### Week 3-4: Writing & Refinement
1. 📝 Complete first field note draft
2. 📝 Fill out ethics/positionality doc
3. 🔄 Refine analysis based on discoveries
4. 📤 Move field note to `stories/published/` when ready

## Questions to Guide Your Work

From `PLAN_CORE.md`, your first question is:
> **"Who lives where in relation to water and land-use constraints?"**

Consider:
- What patterns do you see in the maps?
- How does distance to water relate to demographics (if you have ACS data)?
- What does zoning tell you about land use?
- What questions does this raise about equity, access, history?

## Getting Unstuck

**If data doesn't load:**
- Check that `000_data_prep.ipynb` ran successfully
- Verify files exist in `data/processed/`
- Check CRS matches expectations

**If maps look wrong:**
- Verify CRS is set correctly
- Check that city limits clipping worked
- Try different basemap sources

**If analysis feels thin:**
- That's okay! This is exploratory.
- Focus on what you can observe, not what you can't prove
- Use the field note to reflect on limitations

**If writing feels hard:**
- Start with observations from your walk/ride
- Use the maps as prompts
- Don't worry about being "academic" - be honest

---

**Remember:** The goal is "small, finished artifacts that feel true, not exhaustive coverage." 
Start small, iterate, and let the work guide you.

