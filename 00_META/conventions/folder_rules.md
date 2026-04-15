# Folder Rules — AEROSPACEMODEL

**Path:** `00_META/conventions/folder_rules.md`  
**Authority:** ASIT  
**Status:** ACTIVE

---

## Rules

1. Folder names are controlled vocabulary. New folders must be registered before use.
2. Every active lifecycle phase folder must contain `KNOTS.csv` and `KNU_PLAN.csv`.
3. Every lifecycle phase folder must contain a `README.md`.
4. The `evidence/` subfolder is mandatory in every active lifecycle phase.
5. Empty directories must contain a `.gitkeep` file to preserve structure.
6. Product variant folders must follow the canonical structure defined in `04_PRODUCTS/<PRODUCT_FAMILY>/variants/<VARIANT>/`.
7. Programmes must be organized by craft class and family: `04_PRODUCTS/<PRODUCT_FAMILY>/<CRAFT_CLASS>/<FAMILY>/programmes/<PROGRAMME>/`.
8. Valid craft classes are: `CRAFT_CREWED`, `CRAFT_UNCREWED`, `STATIONS`.
9. Valid family identities are: `AMPEL` (crewed), `ROBBBO-T` (uncrewed), `GAIA` (stations).
