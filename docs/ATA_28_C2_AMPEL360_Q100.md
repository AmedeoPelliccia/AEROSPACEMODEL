# ATA 28 – Fuel System Structure for AMPEL360 Q100

> **Circular Cryogenic Cells (C2) – LH₂ Focus**
>
> **Compliance:** S1000D Issue 5.0, EASA CS-25, SC-28-H2-001, SC-28-CRYO-002

---

## 1. Overview

This document defines the architecture, components, and governance for
the **cryogenic hydrogen fuel system** of the AMPEL360 Q100 aircraft,
using **Circular Cryogenic Cells (C2)** for liquid hydrogen storage.

**Scope:**
- LH₂ storage, distribution, boil-off management, and safety systems.
- Integration with ASIT/ASIGT for digital continuity and certification evidence.
- BREX governance via `KITDM-CTR-LM-CSDB_ATA28` contract.

**Key References:**
- KDB Requirements: `examples/ampel360_q100/KDB/requirements/ata28_c2_cryogenic_fuel.yaml`
- BREX Rules: `examples/ampel360_q100/ASIGT/brex/q100_c2_brex.yaml`
- Contract: `examples/ampel360_q100/ASIT/CONTRACTS/active/Q100-CTR-AMM-001.yaml`
- Pipeline: `pipelines/ata28_h2_pipeline.yaml`

---

## 2. Section Breakdown

### Section 00: Fuel System Description (28-00-xx)

| ATA Code | Subject | Info Code | Type |
|----------|---------|-----------|------|
| 28-00-00 | System Overview | 040 | Descriptive |
| 28-00-10 | System Safety | 040 | Descriptive |
| 28-00-20 | Regulatory Compliance | 040 | Descriptive |

- **Architecture:** 4 circular cryogenic cells, distribution lines,
  boil-off management, safety valves.
- **Integration:** Propulsion (ATA 71), electrical (ATA 24), fire
  protection (ATA 26).
- **BREX Rules:** SAFETY-002, SAFETY-H2-001.
- **Special Conditions:** SC-28-H2-001, SC-28-CRYO-002.

### Section 10: Fuel Storage — Circular Cryogenic Cells (28-10-xx)

| ATA Code | Subject | Info Code | Type |
|----------|---------|-----------|------|
| 28-10-00 | Cryogenic Cells Design | 040 | Descriptive |
| 28-10-10 | Boil-Off Management | 040 | Descriptive |
| 28-10-20 | Safety and Redundancy | 040 | Descriptive |

- **C2 Cell Specs:** 4 circular-section cells, 1200 kg total LH₂, -253°C,
  MLI insulation, vacuum < 0.001 mbar.
- **Boil-Off Thresholds:** Design < 0.5%/day, warning > 0.8%/day,
  alarm > 1.2%/day.
- **BREX Contract:** `KITDM-CTR-LM-CSDB_ATA28` for DM generation.
- **Escalation:** Mandatory HITL for hydrogen-related alerts.

### Section 20: Fuel Distribution (28-20-xx)

| ATA Code | Subject | Info Code | Type |
|----------|---------|-----------|------|
| 28-20-00 | Piping and Valves | 040 | Descriptive |
| 28-20-10 | Flow Control | 040 | Descriptive |
| 28-20-20 | Emergency Shutdown | 500 | Procedural |

- **DMC Constraints:** System Code `28`, Sub-system `20`.
- **Materials:** Stainless steel 316L, vacuum-jacketed MLI.
- **BREX Rule:** Validate safety content before publication.

### Section 30: Fuel Indication and Monitoring (28-30-xx)

| ATA Code | Subject | Info Code | Type |
|----------|---------|-----------|------|
| 28-30-00 | Sensors and Telemetry | 040 | Descriptive |
| 28-30-10 | AI/ML Monitoring | 040 | Descriptive |
| 28-30-20 | Crew Interfaces | 040 | Descriptive |

- **ASIT Integration:** Real-time data logging for digital twin.
- **EU AI Act:** Human oversight for critical alerts (high-risk category).
- **EICAS Messages:** Level, pressure, leak, boil-off, temperature alerts.

### Section 40: Maintenance and Operations (28-40-xx)

| ATA Code | Subject | Info Code | Type |
|----------|---------|-----------|------|
| 28-40-00 | Routine Inspections | 300 | Procedural |
| 28-40-10 | Refueling Procedures | 500 | Procedural |
| 28-40-20 | Troubleshooting | 700 | Procedural |

- **ASIGT Pipeline:** Generate AMM/SRM tasks via `ata28_h2_pipeline.yaml`.
- **BREX Escalation:** Mandatory for hydrogen-related anomalies.

---

## 3. Lifecycle Phase Integration

| Phase | Key Subjects | BREX/ASIT Action |
|-------|-------------|------------------|
| LC01–LC04 (Design) | Tank sizing, material selection, safety analysis | Generate DMs, validate with `KITDM-CTR-LM-CSDB_ATA28` |
| LC05–LC07 (Verification) | Prototyping, boil-off tests, failure mode analysis | Transform test data to certification evidence |
| LC08–LC10 (Production) | Manufacturing, quality control, as-built docs | Produce IPC/DT documentation |
| LC11–LC14 (Operations) | Maintenance logs, real-time monitoring, analytics | Update IDB, trigger HITL for anomalies |

---

## 4. BREX Governance

### C2-Specific Rules (q100_c2_brex.yaml)

| Rule ID | Name | Category | Enforcement |
|---------|------|----------|-------------|
| C2-STRUCT-001 | Domain classification | Structure | Block |
| C2-STRUCT-002 | Novel technology tag | Structure | Block |
| C2-CTR-001 | Contract required | Authority | Require contract |
| C2-SAFETY-001 | H₂ explosion warning | Safety | Block |
| C2-SAFETY-002 | Cryogenic warning | Safety | Block |
| C2-SAFETY-003 | Leak detection docs | Safety | Block |
| C2-SAFETY-004 | Asphyxiation warning | Safety | Block |
| C2-BOG-001 | Boil-off monitoring | Operational | Block |
| C2-BOG-002 | Boil-off escalation | Operational | Escalate |
| C2-ESC-001 | H₂ anomaly escalation | Escalation | Escalate |
| C2-ESC-002 | Cell repair recert | Escalation | Escalate |
| C2-LC-001 | Lifecycle state | Lifecycle | Block |
| C2-AI-001 | AI human oversight | AI Governance | Escalate |
| C2-AI-002 | AI explainability | AI Governance | Block |
| C2-MAT-001 | Material compatibility | Design | Block |

---

## 5. Example: BREX-Governed Workflow

```python
from aerospacemodel.asigt.brex_governance import (
    BREXGovernedValidator,
    OperationContext,
)

# Validate a fuel system maintenance procedure
validator = BREXGovernedValidator(
    contract_id="KITDM-CTR-LM-CSDB_ATA28",
    baseline_id="DBL-Q100-2026-Q2",
)

result = validator.validate_operation(
    operation="generate_srm_task",
    context=OperationContext(
        contract_id="KITDM-CTR-LM-CSDB_ATA28",
        ata_domain="ATA 28",
        sub_system="40",  # Maintenance
        safety_impact=True,
    ),
)

if result.allowed:
    print("Generate SRM task for LH₂ tank inspection.")
elif result.escalation_required:
    print(f"Escalate to: {result.escalation_target}")
else:
    print(f"Blocked by: {result.blocked_by}")
```

---

## 6. Documentation Outputs

| Document Type | Purpose | Pipeline |
|---------------|---------|----------|
| AMM | Maintenance procedures | `ata28_h2_pipeline.yaml` |
| SRM | Structural repairs | `srm_pipeline.yaml` |
| IPC | Illustrated parts catalog | `ipc_pipeline.yaml` |
| DT Documentation | Digital twin integration | `dt_documentation_pipeline.yaml` |

---

## 7. Special Conditions

- **SC-28-H2-001:** Hydrogen Storage and Distribution — covers LH₂ tank
  design, pressure systems, leak detection, and emergency procedures.
- **SC-28-CRYO-002:** Cryogenic Temperature Handling — covers material
  selection, thermal management, insulation integrity, and personnel safety.

---

## 8. Related Documents

| Document | Reference |
|----------|-----------|
| Program Config | `examples/ampel360_q100/program_config.yaml` |
| KDB Requirements | `examples/ampel360_q100/KDB/requirements/ata28_c2_cryogenic_fuel.yaml` |
| BREX Rules | `examples/ampel360_q100/ASIGT/brex/q100_c2_brex.yaml` |
| Contract | `examples/ampel360_q100/ASIT/CONTRACTS/active/Q100-CTR-AMM-001.yaml` |
| H2 Pipeline | `pipelines/ata28_h2_pipeline.yaml` |
| Lifecycle Activation | `lifecycle/T_SUBDOMAIN_LC_ACTIVATION.yaml` |
| Master BREX Authority | `ASIT/GOVERNANCE/master_brex_authority.yaml` |
