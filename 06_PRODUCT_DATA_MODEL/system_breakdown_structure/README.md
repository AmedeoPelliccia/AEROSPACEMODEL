---
model:
  id: SBS_MODEL
  title: System Breakdown Structure Model
  authority: ASIT
  schema_version: "1.0"
  status: ACTIVE
  scope: repository-wide
  description: >
    Canonical schema and validation model for the AEROSPACEMODEL
    System Breakdown Structure (SBS). The SBS provides the controlled
    hierarchical decomposition of an aerospace product from the
    top-level aircraft system down to subordinate system elements.

file_binding:
  path: 06_PRODUCT_DATA_MODEL/system_breakdown_structure/sbs_codes.csv
  format: csv
  encoding: UTF-8
  delimiter: ","
  header_required: true
  multi_value_delimiter: ";"

csv_schema:
  columns:
    - name: sbs_code
      type: string
      required: true
      description: Canonical controlled identifier of the SBS node
      pattern: '^SYS-[0-9]{3}$'

    - name: name
      type: string
      required: true
      description: Human-readable controlled name of the SBS node

    - name: level
      type: integer
      required: true
      description: Hierarchical level of the SBS node
      allowed_values: [0, 1, 2, 3, 4]

    - name: parent_code
      type: string
      required: false
      nullable: true
      description: Parent SBS code; empty only for the root node
      pattern: '^SYS-[0-9]{3}$'

    - name: domain
      type: string
      required: true
      description: Controlled domain classification of the SBS node

    - name: description
      type: string
      required: true
      description: Controlled description of the SBS node

    - name: ata_chapter
      type: string
      required: false
      nullable: true
      description: >
        ATA chapter cross-reference. Multiple values shall be separated
        by semicolons. ATA references are crosswalk values and are not
        the primary decomposition key.
      pattern: '^([0-9]{2})(;[0-9]{2})*$'

hierarchy:
  root:
    required: true
    level: 0
    cardinality: 1
    required_code: SYS-000
    required_name: Aircraft System
    parent_code_must_be_empty: true

  level_definitions:
    - level: 0
      label: ROOT
      purpose: Top-level governed aircraft or aerospace product system
    - level: 1
      label: SYSTEM
      purpose: Primary system decomposition
    - level: 2
      label: SUBSYSTEM
      purpose: Controlled subsystem decomposition
    - level: 3
      label: CONFIGURATION_ITEM
      purpose: Controlled item or major component decomposition
    - level: 4
      label: ELEMENT
      purpose: Optional fine-grained decomposition where needed

  parent_child_rules:
    - child_level: 1
      parent_level: 0
    - child_level: 2
      parent_level: 1
    - child_level: 3
      parent_level: 2
    - child_level: 4
      parent_level: 3

  level_progression_rule: >
    A child node shall have a level exactly one greater than its parent.

identifier_rules:
  uniqueness:
    sbs_code: global
    name_within_parent: true

  ordering:
    recommended_numeric_progression: true
    description: >
      Numeric series should reflect hierarchy blocks where practical,
      for example SYS-100, SYS-110, SYS-120.

domain_model:
  description: >
    Controlled domain vocabulary for SBS classification. Domains are
    organizational and semantic tags, not hierarchy drivers.

  allowed_domains:
    - ALL
    - A-AIRFRAME
    - P-PROPULSION
    - E-ELECTRICAL
    - V-AVIONICS
    - S-SOFTWARE
    - G-ENVIRONMENTAL
    - Q-SAFETY
    - M-MAINTAINABILITY
    - H-HUMAN_FACTORS
    - C-CERTIFICATION
    - L-LOGISTICS
    - O-OPERATIONS
    - I-INFRASTRUCTURES

  root_domain_rule:
    sbs_code: SYS-000
    required_domain: ALL

top_level_structure:
  description: >
    Minimum expected level-1 systems for the baseline aerospace
    product model. Additional top-level systems may be added if
    approved by governance rules.

  required_nodes:
    - sbs_code: SYS-100
      name: Airframe
      domain: A-AIRFRAME
    - sbs_code: SYS-200
      name: Propulsion
      domain: P-PROPULSION
    - sbs_code: SYS-300
      name: Electrical
      domain: E-ELECTRICAL
    - sbs_code: SYS-400
      name: Avionics
      domain: V-AVIONICS
    - sbs_code: SYS-500
      name: Software
      domain: S-SOFTWARE

  optional_nodes:
    - sbs_code: SYS-600
      name: Environmental and Crew Systems
      domain: G-ENVIRONMENTAL
    - sbs_code: SYS-700
      name: Safety and Protection
      domain: Q-SAFETY
    - sbs_code: SYS-800
      name: Maintenance and Supportability
      domain: M-MAINTAINABILITY
    - sbs_code: SYS-900
      name: Human System Integration
      domain: H-HUMAN_FACTORS

ata_crosswalk_rules:
  semantics: cross_reference_only
  mandatory_for_levels: [1, 2]
  optional_for_levels: [0, 3, 4]
  normalization:
    fixed_width: 2
    separator: ";"
    no_spaces: true
  validation:
    regex: '^([0-9]{2})(;[0-9]{2})*$'

status_model:
  description: >
    Lifecycle state of the SBS node definition itself, not the product
    realization state.
  allowed_values:
    - ACTIVE
    - DRAFT
    - OBSOLETE
    - SUPERSEDED
  default: ACTIVE
  note: >
    The current sbs_codes.csv baseline does not yet expose a status
    column. If added, it shall use this controlled vocabulary.

semantic_rules:
  - id: SBS-RULE-001
    rule: Every row shall have a unique sbs_code.
  - id: SBS-RULE-002
    rule: Exactly one root node shall exist and it shall be SYS-000.
  - id: SBS-RULE-003
    rule: Root node parent_code shall be empty.
  - id: SBS-RULE-004
    rule: Every non-root node shall have a valid parent_code.
  - id: SBS-RULE-005
    rule: Every parent_code shall resolve to an existing sbs_code.
  - id: SBS-RULE-006
    rule: Child level shall equal parent level plus one.
  - id: SBS-RULE-007
    rule: Domain values shall be drawn from the controlled vocabulary.
  - id: SBS-RULE-008
    rule: ata_chapter values, if present, shall use semicolon-delimited two-digit ATA codes.
  - id: SBS-RULE-009
    rule: Duplicate name values are allowed only if they do not share the same parent_code.
  - id: SBS-RULE-010
    rule: Required top-level nodes shall be present unless formally exempted.
  - id: SBS-RULE-011
    rule: Empty description values are forbidden.
  - id: SBS-RULE-012
    rule: sbs_code values shall not be reused for different names across baselines.

validation_contract:
  validator_id: validate_sbs_model
  severity_levels:
    - ERROR
    - WARNING
    - INFO

  error_conditions:
    - Missing required column
    - Invalid sbs_code pattern
    - Duplicate sbs_code
    - Missing root node
    - Invalid parent reference
    - Invalid level progression
    - Invalid domain value
    - Invalid ata_chapter syntax
    - Missing required top-level node

  warning_conditions:
    - Missing ata_chapter on recommended levels
    - Non-sequential code grouping
    - Optional domain not used
    - Sparse hierarchy branch

integration_points:
  consumed_by:
    - 02_LIFECYCLE_OS/validators/
    - 04_PRODUCTS/<PRODUCT_FAMILY>/variants/<VARIANT>/
    - 06_PRODUCT_DATA_MODEL/configuration_management/
    - 07_TECHNICAL_PUBLICATIONS/
    - 08_AUTOMATION/scripts/

  related_files:
    - 06_PRODUCT_DATA_MODEL/system_breakdown_structure/sbs_codes.csv
    - 06_PRODUCT_DATA_MODEL/system_breakdown_structure/sbs_model.yaml
    - 00_META/glossary/controlled_vocabulary.yaml
    - 00_META/conventions/naming_convention.md

governance:
  change_control: required
  approval_authority: ASIT
  baseline_required: true
  interpretation_rule: >
    If local implementations introduce additional SBS levels, domains,
    or top-level systems, the schema version shall be updated or a local
    extension file shall be declared.

extensions:
  local_extension_policy:
    allowed: true
    mechanism: companion_yaml
    description: >
      Product-specific SBS extensions may be declared in a companion file
      provided they do not violate canonical root, identifier, and
      hierarchy rules.

summary:
  principle: >
    The System Breakdown Structure is the canonical controlled hierarchy
    for aerospace product decomposition in AEROSPACEMODEL.
  invariant: >
    Every SBS node shall be uniquely identified, hierarchically valid,
    semantically classified, and machine-validated.
---
# System Breakdown Structure (SBS)

**Path:** `06_PRODUCT_DATA_MODEL/system_breakdown_structure/README.md`  
**Model ID:** `SBS_MODEL`  
**Authority:** ASIT  
**Schema version:** `1.0`  
**Status:** `ACTIVE`  
**Scope:** Repository-wide

---

## Purpose

This directory defines the **System Breakdown Structure (SBS)** for AEROSPACEMODEL.

The SBS is the canonical controlled hierarchy used to decompose an aerospace product from the **top-level aircraft system** down to subordinate system elements. It provides a stable structural model for:

- product decomposition,
- domain classification,
- ATA crosswalk mapping,
- configuration alignment,
- lifecycle traceability,
- and machine validation.

The SBS is a **controlled product structure**, not an informal classification list.

---

## Directory Contents

```text
06_PRODUCT_DATA_MODEL/system_breakdown_structure/
├── README.md
├── sbs_codes.csv
└── sbs_model.yaml
````

### File roles

| File             | Role                                            |
| ---------------- | ----------------------------------------------- |
| `README.md`      | Human-readable operating definition of the SBS  |
| `sbs_codes.csv`  | Controlled SBS node register                    |
| `sbs_model.yaml` | Machine-readable schema and validation contract |

---

## Operating Principle

Every SBS node shall be:

1. **uniquely identified**,
2. **hierarchically valid**,
3. **semantically classified**,
4. **crosswalk-capable to ATA where relevant**,
5. and **machine-validated** against the SBS schema.

The SBS is therefore a **canonical decomposition model**, not a free-form taxonomy.

---

## File Binding

The authoritative SBS register is:

```text
06_PRODUCT_DATA_MODEL/system_breakdown_structure/sbs_codes.csv
```

### File binding rules

| Attribute             | Value    |
| --------------------- | -------- |
| Format                | `csv`    |
| Encoding              | `UTF-8`  |
| Delimiter             | `,`      |
| Header row            | required |
| Multi-value delimiter | `;`      |

---

## CSV Schema

The SBS register uses the following column schema.

| Column        | Type    | Required | Description                                                    |
| ------------- | ------- | -------: | -------------------------------------------------------------- |
| `sbs_code`    | string  |      Yes | Canonical controlled identifier of the SBS node                |
| `name`        | string  |      Yes | Human-readable controlled name of the SBS node                 |
| `level`       | integer |      Yes | Hierarchical level of the SBS node                             |
| `parent_code` | string  |       No | Parent SBS code; empty only for the root node                  |
| `domain`      | string  |      Yes | Controlled domain classification                               |
| `description` | string  |      Yes | Controlled description of the SBS node                         |
| `ata_chapter` | string  |       No | ATA chapter cross-reference; semicolon-delimited when multiple |

### Field constraints

#### `sbs_code`

* Pattern: `^SYS-[0-9]{3}$`
* Must be globally unique

#### `level`

* Allowed values: `0`, `1`, `2`, `3`, `4`

#### `parent_code`

* Empty only for the root node
* When present, must match: `^SYS-[0-9]{3}$`
* Must resolve to an existing parent in the same file

#### `ata_chapter`

* Pattern: `^([0-9]{2})(;[0-9]{2})*$`
* ATA values are **cross-reference values**
* ATA does **not** define the hierarchy itself

---

## Hierarchy Model

The SBS hierarchy is strictly controlled.

### Root node

Exactly one root node is required:

| Attribute     | Required value    |
| ------------- | ----------------- |
| `sbs_code`    | `SYS-000`         |
| `name`        | `Aircraft System` |
| `level`       | `0`               |
| `parent_code` | empty             |
| `domain`      | `ALL`             |

### Level definitions

| Level | Label                | Purpose                                                 |
| ----: | -------------------- | ------------------------------------------------------- |
|   `0` | `ROOT`               | Top-level governed aircraft or aerospace product system |
|   `1` | `SYSTEM`             | Primary system decomposition                            |
|   `2` | `SUBSYSTEM`          | Controlled subsystem decomposition                      |
|   `3` | `CONFIGURATION_ITEM` | Controlled item or major component decomposition        |
|   `4` | `ELEMENT`            | Optional fine-grained decomposition                     |

### Parent-child rules

| Child level | Parent level |
| ----------: | -----------: |
|         `1` |          `0` |
|         `2` |          `1` |
|         `3` |          `2` |
|         `4` |          `3` |

### Hierarchy invariant

A child node shall have a level **exactly one greater** than its parent.

---

## Identifier Rules

### Uniqueness

* `sbs_code` must be globally unique
* `name` may repeat only if it does **not** share the same `parent_code`

### Ordering

Numeric grouping should reflect structure blocks where practical.
Recommended pattern:

```text
SYS-100
SYS-110
SYS-120
```

This is a recommendation, not a semantic substitute for hierarchy validation.

---

## Domain Model

Domains are **controlled semantic tags**, not hierarchy drivers.

### Allowed domains

* `ALL`
* `A-AIRFRAME`
* `P-PROPULSION`
* `E-ELECTRICAL`
* `V-AVIONICS`
* `S-SOFTWARE`
* `G-ENVIRONMENTAL`
* `Q-SAFETY`
* `M-MAINTAINABILITY`
* `H-HUMAN_FACTORS`
* `C-CERTIFICATION`
* `L-LOGISTICS`
* `O-OPERATIONS`
* `I-INFRASTRUCTURES`

### Root domain rule

The root node `SYS-000` shall use:

```text
ALL
```

---

## Top-Level Baseline Structure

The minimum expected level-1 structure for the baseline aerospace product model is:

| SBS code  | Name                           | Domain              | Status   |
| --------- | ------------------------------ | ------------------- | -------- |
| `SYS-100` | Airframe                       | `A-AIRFRAME`        | Required |
| `SYS-200` | Propulsion                     | `P-PROPULSION`      | Required |
| `SYS-300` | Electrical                     | `E-ELECTRICAL`      | Required |
| `SYS-400` | Avionics                       | `V-AVIONICS`        | Required |
| `SYS-500` | Software                       | `S-SOFTWARE`        | Required |
| `SYS-600` | Environmental and Crew Systems | `G-ENVIRONMENTAL`   | Optional |
| `SYS-700` | Safety and Protection          | `Q-SAFETY`          | Optional |
| `SYS-800` | Maintenance and Supportability | `M-MAINTAINABILITY` | Optional |
| `SYS-900` | Human System Integration       | `H-HUMAN_FACTORS`   | Optional |

Additional top-level systems may be introduced only under controlled governance.

---

## ATA Crosswalk Rules

ATA values are used as a **cross-reference layer**.

### Semantics

* ATA is **cross-reference only**
* ATA does **not** define parent-child SBS structure
* Multiple ATA chapters shall be semicolon-delimited
* No spaces are permitted inside multi-value ATA fields

### ATA applicability by level

| Level class          | ATA rule                             |
| -------------------- | ------------------------------------ |
| Levels `1`, `2`      | ATA reference recommended / expected |
| Levels `0`, `3`, `4` | ATA reference optional               |

### Normalization rules

| Attribute | Value     |
| --------- | --------- |
| Width     | 2 digits  |
| Separator | `;`       |
| Spaces    | forbidden |

Valid examples:

```text
24
27;31
51;52;53
```

---

## Status Model

The SBS node definition may use the following status vocabulary if a status column is added in future baselines:

* `ACTIVE`
* `DRAFT`
* `OBSOLETE`
* `SUPERSEDED`

Default status:

```text
ACTIVE
```

Note: the current `sbs_codes.csv` baseline does **not** yet expose a `status` column.

---

## Validation Rules

The SBS validator shall enforce the following semantic rules.

| Rule ID        | Rule                                                                                |
| -------------- | ----------------------------------------------------------------------------------- |
| `SBS-RULE-001` | Every row shall have a unique `sbs_code`                                            |
| `SBS-RULE-002` | Exactly one root node shall exist and it shall be `SYS-000`                         |
| `SBS-RULE-003` | Root node `parent_code` shall be empty                                              |
| `SBS-RULE-004` | Every non-root node shall have a valid `parent_code`                                |
| `SBS-RULE-005` | Every `parent_code` shall resolve to an existing `sbs_code`                         |
| `SBS-RULE-006` | Child `level` shall equal parent `level + 1`                                        |
| `SBS-RULE-007` | `domain` values shall come from the controlled vocabulary                           |
| `SBS-RULE-008` | `ata_chapter` values, if present, shall use semicolon-delimited two-digit ATA codes |
| `SBS-RULE-009` | Duplicate `name` values are allowed only when parent differs                        |
| `SBS-RULE-010` | Required top-level nodes shall be present unless formally exempted                  |
| `SBS-RULE-011` | Empty `description` values are forbidden                                            |
| `SBS-RULE-012` | `sbs_code` values shall not be reused for different names across baselines          |

---

## Validation Contract

### Validator identifier

```text
validate_sbs_model
```

### Severity levels

* `ERROR`
* `WARNING`
* `INFO`

### Error conditions

* Missing required column
* Invalid `sbs_code` pattern
* Duplicate `sbs_code`
* Missing root node
* Invalid parent reference
* Invalid level progression
* Invalid domain value
* Invalid `ata_chapter` syntax
* Missing required top-level node

### Warning conditions

* Missing `ata_chapter` on recommended levels
* Non-sequential code grouping
* Optional domain not used
* Sparse hierarchy branch

---

## Integration Points

The SBS model is consumed by:

* `02_LIFECYCLE_OS/validators/`
* `04_PRODUCTS/<PRODUCT_FAMILY>/variants/<VARIANT>/`
* `06_PRODUCT_DATA_MODEL/configuration_management/`
* `07_TECHNICAL_PUBLICATIONS/`
* `08_AUTOMATION/scripts/`

### Related files

* `06_PRODUCT_DATA_MODEL/system_breakdown_structure/sbs_codes.csv`
* `06_PRODUCT_DATA_MODEL/system_breakdown_structure/sbs_model.yaml`
* `00_META/glossary/controlled_vocabulary.yaml`
* `00_META/conventions/naming_convention.md`

---

## Governance

| Attribute          | Value    |
| ------------------ | -------- |
| Change control     | required |
| Approval authority | `ASIT`   |
| Baseline required  | `true`   |

### Interpretation rule

If a local implementation introduces:

* additional SBS levels,
* additional domains,
* or additional top-level systems,

then the schema version shall be updated or a local extension file shall be declared.

---

## Extensions

Local extensions are permitted under controlled conditions.

### Extension policy

| Attribute | Value            |
| --------- | ---------------- |
| Allowed   | `true`           |
| Mechanism | `companion_yaml` |

### Constraint

Product-specific SBS extensions may be declared only if they do not violate:

* canonical root rules,
* identifier rules,
* hierarchy rules,
* and controlled validation semantics.

---

## Example CSV Header

```csv
sbs_code,name,level,parent_code,domain,description,ata_chapter
```

---

## Example Root Record

```csv
SYS-000,Aircraft System,0,,ALL,Top-level aircraft system,
```

---

## Design Principle

The System Breakdown Structure is the **canonical controlled hierarchy** for aerospace product decomposition in AEROSPACEMODEL.

### Invariant

Every SBS node shall be:

* uniquely identified,
* hierarchically valid,
* semantically classified,
* and machine-validated.

---

## Summary

The SBS layer provides the structural decomposition needed to align:

```text
product architecture
→ controlled hierarchy
→ domain classification
→ ATA crosswalk
→ lifecycle traceability
→ validation
```

It shall therefore be treated as a controlled product data model, not as an informal system list.

---



