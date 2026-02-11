# S1000D Template Examples

This directory contains complete, production-ready examples of S1000D Issue 5.0 XML files for the AEROSPACEMODEL project.

## Overview

These examples demonstrate proper S1000D structure and content for Aircraft Maintenance Manual (AMM) publications, covering ATA chapters 27 (Flight Controls) and 28 (Fuel).

## Files

### Data Modules (DM)

1. **DMC-AERO-A-27-00-00-00A-040A-A.xml**
   - **ATA Chapter:** 27 - Flight Controls
   - **Type:** Descriptive (Info Code 040A)
   - **Content:** Complete system overview including:
     - Primary flight controls (ailerons, elevators, rudder)
     - Secondary flight controls (flaps, slats, spoilers)
     - System architecture with quad-redundant computing
     - Safety features per ARP4761 requirements
     - Cross-references to maintenance procedures

2. **DMC-AERO-A-28-00-00-00A-040A-A.xml**
   - **ATA Chapter:** 28 - Fuel
   - **Type:** Descriptive (Info Code 040A)
   - **Content:** Complete system overview including:
     - Fuel storage (center tank, wing tanks, auxiliary tank)
     - Fuel distribution (pumps, lines, crossfeed system)
     - Fuel indication and temperature monitoring
     - Safety features and leak detection
     - Alternative fuel compatibility (SAF, H2)
     - Safety warnings for hydrogen systems

### Publication Module (PM)

3. **PM-AMM-001.xml**
   - **Publication Type:** Aircraft Maintenance Manual (AMM)
   - **Model:** AERO
   - **Content:** Publication structure organizing:
     - Front matter (title page, table of contents, introduction)
     - ATA 27 chapter with sub-system entries
     - ATA 28 chapter with sub-system entries
     - Hierarchical navigation structure
     - Data module references with proper addressing

### Data Module List (DML)

4. **DML-AMM-001.xml**
   - **Purpose:** Master list of all data modules in the AMM
   - **Type:** Publication DML (dmlType="p")
   - **Content:** Complete listing of:
     - All ATA 27 data modules (general + sub-systems)
     - All ATA 28 data modules (general + sub-systems)
     - Issue dates and security classifications
     - Cross-reference structure

## S1000D Compliance

All examples conform to:
- **S1000D Issue:** 5.0
- **Schema:** S1000D_5-0/xml_schema_flat/
- **Namespaces:** http://www.s1000d.org/S1000D_5-0
- **Business Rules:** BREX-compliant structure
- **Security:** Classification 01 (unclassified)

## Data Module Code (DMC) Structure

The DMC follows S1000D conventions:
```
DMC-[Model]-[SysDiff]-[ATA]-[SubSys]-[SubSubSys]-[Assy]-[DisAssy][Variant]-[InfoCode][Variant]-[ItemLoc]

Example: DMC-AERO-A-27-00-00-00A-040A-A
- AERO: Model Identification Code
- A: System Difference Code
- 27: ATA Chapter (Flight Controls)
- 00-00: Sub-system codes
- 00A: Assembly code
- 040: Disassembly code variant (description)
- A: Info code
- A: Info code variant
- A: Item location code
```

## ATA Chapter Reference

### ATA 27 - Flight Controls
- **27-00:** General
- **27-11:** Ailerons
- **27-21:** Rudder
- **27-31:** Elevator
- **27-40:** Horizontal Stabilizer
- **27-51:** Flaps
- **27-61:** Spoilers/Speedbrakes
- **27-81:** Lift Augmentation (Slats)

### ATA 28 - Fuel
- **28-00:** General
- **28-11:** Storage (Center Tank)
- **28-12:** Storage (Wing Tanks)
- **28-13:** Storage (Auxiliary Tank)
- **28-21:** Distribution (Pumps)
- **28-22:** Distribution (Lines)
- **28-23:** Crossfeed
- **28-30:** Dump
- **28-41:** Indicating (Quantity)
- **28-42:** Indicating (Temperature)

## Info Code Reference

Common info codes used:
- **040A:** Description - System overview
- **520A:** Maintenance Procedures - Removal/Installation
- **720A:** Troubleshooting
- **941A:** IPD - Illustrated Parts Data

## Usage in Content Pipeline

These examples are used by the ASIGT content pipeline (`src/aerospacemodel/asigt/pipeline.py`):

```python
from pathlib import Path
from aerospacemodel.asigt.pipeline import execute_pipeline

# Execute pipeline using these examples as templates
result = execute_pipeline(
    pipeline_yaml=Path("pipelines/amm_pipeline.yaml"),
    contract_id="KITDM-CTR-LM-CSDB_ATA27",
    baseline_id="FBL-2026-Q1-003",
    kdb_root=Path("KDB"),
    output_path=Path("output/CSDB")
)
```

## Validation

All XML files can be validated against S1000D schemas:

```bash
# Validate Data Module
xmllint --noout --schema S1000D_5-0/xml_schema_flat/descript.xsd DMC-AERO-A-27-00-00-00A-040A-A.xml

# Validate Publication Module
xmllint --noout --schema S1000D_5-0/xml_schema_flat/pm.xsd PM-AMM-001.xml

# Validate Data Module List
xmllint --noout --schema S1000D_5-0/xml_schema_flat/dml.xsd DML-AMM-001.xml
```

## Safety Considerations

### ATA 27 - Flight Controls
- All flight control systems are **DAL A** (Design Assurance Level A)
- Catastrophic failure probability < 1E-9 per flight hour
- Requires redundant actuation and monitoring
- Subject to ARP4761 safety assessment

### ATA 28 - Fuel
- Fuel system failures can be **DAL A** (feed systems) or **DAL B** (indication)
- Leak detection and isolation are critical safety features
- Hydrogen systems require special handling procedures
- All maintenance requires proper bonding and grounding

## Related Documentation

- [Content Pipeline Documentation](../../../docs/CONTENT_PIPELINE.md)
- [S1000D Template Guide](../README.md)
- [ASIGT Pipeline Implementation](../../../src/aerospacemodel/asigt/pipeline.py)
- [ATA 27 BREX Instructions](../../../.github/agents/ata27_brex_instructions.md)
- [ATA 28 BREX Instructions](../../../.github/agents/ata28_brex_instructions.md)

## Modification

When creating new data modules based on these examples:

1. **Update DMC codes** - Ensure proper ATA chapter and sub-system codes
2. **Update content** - Replace example content with actual technical data
3. **Update references** - Ensure all dmRef elements point to existing modules
4. **Update dates** - Use current issue dates
5. **Validate** - Run through S1000D schema validation
6. **BREX check** - Verify compliance with project BREX rules

## License

These templates are part of the AEROSPACEMODEL project and follow the project license (Apache 2.0).

---
*Generated by ASIGT Content Pipeline*
*Version: 1.0.0*
*Last Updated: 2026-02-11*
