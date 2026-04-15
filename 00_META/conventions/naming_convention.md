# Naming Convention — AEROSPACEMODEL

**Path:** `00_META/conventions/naming_convention.md`  
**Authority:** ASIT  
**Status:** ACTIVE

---

## Folder Naming

- Folder names use UPPERCASE with underscores for top-level controlled directories.
- Product family folders use UPPERCASE: `PRODUCT_FAMILY`.
- Craft class folders use UPPERCASE: `CRAFT_CREWED`, `CRAFT_UNCREWED`, `STATIONS`.
- Family identity folders use UPPERCASE: `AMPEL`, `ROBBBO-T`, `GAIA`.
- Programme folders are lowercase: `programmes/`.
- Variant folders use UPPERCASE: `VARIANT`.
- Lifecycle phase folders follow the pattern: `LC<NN>_<PHASE_NAME>`.

## File Naming

- Controlled YAML files: `lowercase_with_underscores.yaml`
- Controlled CSV files: `UPPERCASE_WITH_UNDERSCORES.csv`
- Markdown documents: `UPPERCASE_WITH_UNDERSCORES.md` for system documents, `lowercase_with_underscores.md` for supporting content.

## ID Formats

- KNOT ID: `KNOT-<PRODUCT>-<LCCODE>-<SEQ:04d>` (e.g., `KNOT-PROD-LC01-0001`)
- KNU ID: `KNU-<PRODUCT>-<LCCODE>-<SEQ:04d>` (e.g., `KNU-PROD-LC01-0001`)
- Evidence OID: `OID-<PRODUCT>-<LCCODE>-<SEQ:04d>` (e.g., `OID-PROD-LC01-0001`)
- Audit ID: `AUD-<PRODUCT>-<SEQ:04d>` (e.g., `AUD-PROD-0001`)
- Mapping ID: `MAP-<STANDARD>-<SEQ:04d>` (e.g., `MAP-AS9100-0001`)

## Multi-Value Fields

Multi-value fields in CSV files use semicolon (`;`) as delimiter.
