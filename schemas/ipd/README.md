# IPD Schema Suite

**Domain:** `schemas/ipd/`  
**Authority:** ASIT  
**Version:** 1.0.0  
**Standard:** S1000D Issue 5.0 · ATA iSpec 2200 · AMPEL360 Q100

---

## Overview

The `schemas/ipd/` directory contains JSON Schema (draft-07) definitions for
the **Illustrated Parts Data (IPD)** module suite used in the AMPEL360 Q100
program. These schemas validate all externalized IPD data artifacts produced
under the **OPT-IN_FRAMEWORK** canonical architecture per TLI v2.1 patterns.

IPD modules correspond to S1000D Info Code `940A`–`942A` (Parts Data / IPD /
Illustrated Parts Data Supplementary). They are consumed by the IPC pipeline
(`pipelines/ipc_pipeline.yaml`) and the `ASIGT/mapping/parts_to_ipd.yaml`
transformation.

---

## Schema Files

| File | Purpose | S1000D Reference |
|------|---------|-----------------|
| [`ipd_part_item.schema.json`](ipd_part_item.schema.json) | Validates each row in a `parts_list.json` file | Info Code 941 |
| [`ipd_cross_reference.schema.json`](ipd_cross_reference.schema.json) | Validates entries in `cross_references.json` | Info Code 040 (cross-reference element) |
| [`ipd_source_data.schema.json`](ipd_source_data.schema.json) | Validates vendor source package entries in `source_data.json` | Approved Source List (AVL) |
| [`ipd_figure_metadata.schema.json`](ipd_figure_metadata.schema.json) | Validates figure title block and hotspot map in `figure_metadata.json` | Info Code 040 (figure element) |

---

## Schema Relationships

```
FIG-xx-xx-xxx/
├── parts_list.json          ← array of ipd_part_item.schema.json objects
├── cross_references.json    ← array of ipd_cross_reference.schema.json objects
├── source_data.json         ← array of ipd_source_data.schema.json objects
└── figure_metadata.json     ← single ipd_figure_metadata.schema.json object
```

Each JSON data file also carries:
- A `$schema` reference pointing to the corresponding schema file
- A `_metadata` object with `dmc`, `baseline_ref`, `issue_date`, `authority`

---

## Field Reference

### `ipd_part_item.schema.json`

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `fig` | ✅ | string | Figure ID (pattern `FIG-##-##-###`) |
| `item` | ✅ | integer | Item number (even, ≥ 0) |
| `hotspot` | — | string | Hotspot letter A–Z |
| `pn` | ✅ | string | Part number |
| `nomenclature` | ✅ | string | Part description (title case) |
| `qty` | ✅ | int/string | Quantity or `"AR"` |
| `unit` | ✅ | enum | Unit of measure (EA, SET, IN, …) |
| `smr` | ✅ | string | SMR code (MIL-STD-1552) |
| `csn` | — | string | Catalog Sequence Number |
| `ata` | ✅ | string | ATA chapter-section-subject |
| `effectivity` | — | string | MSN effectivity range |
| `source` | — | string | Vendor package ID (`AMPEL-VP-xxxx-xxx`) |
| `cage` | — | string | 5-char CAGE code |
| `ipc_ref` | — | string | Vendor IPC/CMM cross-reference |
| `note` | — | string | Supplementary note |
| `category` | — | enum | `assy`, `detail`, `consumable`, `standard` |

### `ipd_cross_reference.schema.json`

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `type` | ✅ | enum | `AMM`, `CMM`, `TSM`, `SB`, `SRM`, `WDM`, `KNOT` |
| `ref` | ✅ | string | DMC or publication reference |
| `title` | ✅ | string | Document title |
| `ata` | — | string | ATA chapter-section-subject |

### `ipd_source_data.schema.json`

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `id` | ✅ | string | Package ID (`AMPEL-VP-xxxx-xxx`) |
| `title` | ✅ | string | Package descriptive title |
| `vendor` | ✅ | string | Vendor/manufacturer name |
| `status` | ✅ | enum | `APPROVED`, `QUAL-TEST`, `DRAFT`, `REJECTED` |
| `date` | ✅ | string | ISO 8601 date (YYYY-MM-DD) |

### `ipd_figure_metadata.schema.json`

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `figure_id` | ✅ | string | Figure ID (pattern `FIG-##-##-###`) |
| `revision` | ✅ | string | Revision letter A–Z |
| `issue_date` | ✅ | string | ISO 8601 date |
| `title` | ✅ | string | Drawing title |
| `dmc` | ✅ | string | S1000D DMC |
| `ata_chapter` | ✅ | string | ATA chapter-section-subject |
| `sheet` | — | string | Sheet number |
| `scale` | — | string | Drawing scale |
| `drawn_by` | — | string | Drafter ID |
| `checked_by` | — | string | Reviewer ID |
| `hotspot_map` | ✅ | object | Map of letter → `{item, x_pct, y_pct}` |
| `baseline_ref` | — | string | Engineering baseline reference |
| `provenance` | — | object | `{source_hash, generation_contract}` |

---

## SMR Code Reference (MIL-STD-1552)

SMR codes follow the format `XBZA0`:

| Position | Field | Values |
|----------|-------|--------|
| 1 | Source | `X` Manufacturer, `A`–`P` Procurable, `O` One-time buy |
| 2 | Maintainability | `B` Repair at organizational level, `O` Depot only, `D` No repair |
| 3 | Recoverability | `Z` Non-reparable (discard), `F` Reparable |
| 4 | Unit | `A` Each, `D` Depot |
| 5 | Quantity | `0`–`9` |

---

## Related Documents

| Document | Path |
|----------|------|
| IPC Pipeline | `pipelines/ipc_pipeline.yaml` |
| Parts-to-IPD Mapping | `ASIGT/mapping/parts_to_ipd.yaml` |
| Artifact Types | `schemas/ampel360_artifact_types.yaml` |
| Metadata Record Schema | `schemas/ampel360_metadata_record.schema.json` |
| S1000D IPD DM Template | `ASIGT/s1000d_templates/dm_ipd.xml` |

---

*Maintained by ASIT · Authority: KITDM-CTR-LM-CSDB_ATA28_H2 · Lifecycle: LC04*
