# TDMS — Total Document Management System

## Overview

The **Total Document Management System (TDMS)** provides a hybrid human + machine document representation architecture for the AEROSPACEMODEL framework. It enables efficient collaboration between human authors/reviewers and AI agents by maintaining two complementary views of the same data.

## Core Concept: Dual-Plane Architecture

TDMS operates on two planes:

### 1. Human Plane (Source of Truth)
- **Purpose**: Authoritative, editable, auditable representation
- **Formats**: YAML, JSON, XML (S1000D where applicable)
- **Audience**: Human authors, reviewers, auditors, certification teams
- **Characteristics**:
  - Fully readable and reviewable
  - Version-controlled
  - Schema-validated
  - Contains full context and descriptions

### 2. Machine Plane (Derived View)
- **Purpose**: Token-efficient, compact representation for AI agents
- **Formats**: TSV, CSV, Line Protocol
- **Audience**: AI agents, automated loops, runtime systems
- **Characteristics**:
  - Minimized token count (~4x reduction)
  - Deterministic serialization
  - ID-based disambiguation via dictionaries
  - Fast parsing and processing

```
Human Plane ←──[source of truth]
     │
     ▼
Converter (bidirectional with validation)
     │
     ▼  
Machine Plane ←──[derived view for agents]
```

**Key Principle**: The planes do not compete. The Human Plane is always the source of truth; the Machine Plane is a derived view optimized for AI context windows.

## Quick Start

### Python API

```python
from aerospacemodel.tdms import (
    HumanPlane,
    MachinePlane,
    TDMSConverter,
    TDMSDictionary,
    DictionaryRegistry,
)

# Load from human-readable YAML (source of truth)
human = HumanPlane.load("contract.yaml")

# Convert to token-efficient format for AI agents
converter = TDMSConverter()
machine = converter.to_machine_plane(human)

# Export compact TSV for agent consumption
machine.to_tsv("contract_compact.tsv")
print(f"Token estimate: ~{machine.token_count_estimate()} tokens")

# After AI processing, convert back with validation
modified_machine = MachinePlane.from_tsv("agent_output.tsv")
result = converter.to_human_plane(modified_machine, validate=True)

if result.success:
    result.human_plane.save("contract_updated.yaml")
```

### CLI Commands

```bash
# Convert Human → Machine (YAML → TSV)
aerospacemodel tdms convert -i contract.yaml -o contract.tsv

# Convert Machine → Human (TSV → YAML)
aerospacemodel tdms convert -i agent_output.tsv -o updated.yaml

# Show file information
aerospacemodel tdms info contract.yaml

# List available dictionaries
aerospacemodel tdms dict list

# Show specific dictionary
aerospacemodel tdms dict show --type ata

# Create default dictionaries
aerospacemodel tdms dict create --output ./dictionaries/
```

## Components

### HumanPlane

The human-readable representation using nested YAML/JSON structures.

```python
human = HumanPlane(data={
    "header": {
        "contract_id": "CTR-001",
        "title": "Fuel System CSDB Generation",
        "status": "DRAFT"
    },
    "source": {
        "ata_chapters": ["28", "28-10"],
        "baseline": {"type": "FBL", "id": "FBL-2026-Q1"}
    }
})

# Access via dot notation
title = human.get("header.title")
human.set("header.status", "APPROVED")

# Flatten for analysis
flat = human.flatten()  # {"header.title": "...", "header.status": "..."}

# Save/Load
human.save("contract.yaml")
loaded = HumanPlane.load("contract.yaml")
```

### MachinePlane

The token-efficient representation using flat tabular records.

```python
# From TSV
machine = MachinePlane.from_tsv("contracts.tsv")

# Access records
for record in machine:
    print(record["header.contract_id"])

# Filter records
approved = machine.filter(status="APV")

# Export formats
tsv_content = machine.to_tsv()
csv_content = machine.to_csv()
lp_content = machine.to_line_protocol()

# Token estimation
tokens = machine.token_count_estimate()
```

### TDMSConverter

Bidirectional converter with validation and provenance tracking.

```python
converter = TDMSConverter()

# Human → Machine
machine = converter.to_machine_plane(human)

# Machine → Human (with validation)
result = converter.to_human_plane(machine, validate=True)
if result.success:
    human = result.human_plane
else:
    print(result.errors)

# Round-trip validation
result = converter.validate_round_trip(human)
print(f"Lossless: {result.status}")
```

### TDMSDictionary

ID-based disambiguation for compact representation.

```python
# Create standard dictionaries
dict_ata = TDMSDictionary.create_ata_dictionary()
dict_pub = TDMSDictionary.create_publication_dictionary()
dict_status = TDMSDictionary.create_status_dictionary()

# Lookup operations
print(dict_ata.get_value("28"))      # "Fuel"
print(dict_ata.get_id("Fuel"))        # "28"

# Use with registry
registry = DictionaryRegistry.create_with_defaults()
value = registry.resolve("AMM", DictionaryType.PUBLICATION)
# "Aircraft Maintenance Manual"
```

## Format Details

### TSV Output Example

Human Plane (YAML):
```yaml
header:
  contract_id: KITDM-CTR-LM-CSDB_ATA28
  title: ATA 28 Fuel System CSDB Generation
  status: APPROVED
  category: LM
source:
  baseline:
    type: FBL
    id: FBL-2026-Q1-003
```

Machine Plane (TSV):
```
header.contract_id	header.title	header.status	header.category	source.baseline.type	source.baseline.id
KITDM-CTR-LM-CSDB_ATA28	ATA 28 Fuel System CSDB Generation	APV	LM	FBL	FBL-2026-Q1-003
```

**Note**: Status "APPROVED" is compacted to "APV" using the status dictionary.

### Supported Formats

| Format | Extension | Use Case |
|--------|-----------|----------|
| TSV | `.tsv` | Recommended for AI agents (tabs are single tokens) |
| CSV | `.csv` | Excel compatibility, when commas in values are rare |
| Line Protocol | `.lp` | Sequential processing, streaming |

## Standard Dictionaries

TDMS includes pre-built dictionaries for aerospace domain:

| Type | Entries | Example |
|------|---------|---------|
| ATA | 48 | `28` → `Fuel` |
| Publication | 13 | `AMM` → `Aircraft Maintenance Manual` |
| Status | 12 | `APV` → `Approved` |
| Stakeholder | 8 | `ENG` → `Engineering` |
| Baseline | 5 | `FBL` → `Functional Baseline` |

## Integration with ASIT/ASIGT

TDMS integrates seamlessly with the AEROSPACEMODEL governance architecture:

```python
from aerospacemodel import Contract
from aerospacemodel.tdms import HumanPlane, TDMSConverter

# Load ASIT contract as HumanPlane
human = HumanPlane.load("ASIT/CONTRACTS/active/my_contract.yaml")

# Convert for AI agent processing
converter = TDMSConverter()
machine = converter.to_machine_plane(human)

# Agent processes compact representation...
# ... then converts back for governance review

result = converter.to_human_plane(modified_machine, validate=True)
if result.success:
    result.human_plane.save("contract_for_review.yaml")
```

## Best Practices

1. **Human Plane is Source of Truth**: Never directly edit Machine Plane outputs. Make changes in Human Plane and re-convert.

2. **Version Control Human Plane**: Store YAML/JSON in git. Machine Plane is regenerated as needed.

3. **Validate Round-Trips**: When AI agents modify data, always validate the conversion back to Human Plane.

4. **Use Dictionaries Consistently**: Register all dictionaries before conversion to ensure consistent ID compaction.

5. **Track Provenance**: Use metadata hashes to verify data integrity across conversions.

## Architecture Benefits

| Benefit | Human Plane | Machine Plane |
|---------|-------------|---------------|
| Readability | ✓ Excellent | - Compact |
| Token Efficiency | - Verbose | ✓ ~4x reduction |
| Auditability | ✓ Full context | - IDs only |
| AI Processing | - High token cost | ✓ Optimized |
| Version Control | ✓ Diff-friendly | - Binary-like |
| Schema Validation | ✓ Full validation | ✓ Basic validation |
