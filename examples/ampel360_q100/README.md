# AMPEL360 Q100 — Circular Cryogenic Cells (C2) Example

> **Program:** AMPEL360 Q100  
> **Novel Technology:** C2 — Circular Cryogenic Cells  
> **ATA Chapter:** 28 — Fuel System (LH₂)

## Overview

This example demonstrates the AEROSPACEMODEL framework applied to the
**AMPEL360 Q100** aircraft's **Circular Cryogenic Cells (C2)** fuel system.
The C2 system uses four circular-section cryogenic cells to store liquid
hydrogen (LH₂) at -253°C for fuel cell propulsion.

## Directory Structure

```
ampel360_q100/
├── program_config.yaml          # Aircraft program configuration
├── KDB/
│   └── requirements/
│       └── ata28_c2_cryogenic_fuel.yaml  # C2 fuel system requirements
├── ASIT/
│   └── CONTRACTS/
│       └── active/
│           └── Q100-CTR-AMM-001.yaml     # AMM generation contract
├── ASIGT/
│   └── brex/
│       └── q100_c2_brex.yaml             # C2-specific BREX rules
├── IDB/                         # Generated output (CSDB)
└── output/                      # Rendered publications
```

## Key Features

### Circular Cryogenic Cells (C2)
- 4 circular-section LH₂ cells (1200 kg total capacity)
- Vacuum-jacketed MLI insulation
- Boil-off rate < 0.5% per day (design target)

### BREX Governance
- 16 C2-specific rules covering safety, boil-off, AI governance, and materials
- Mandatory hydrogen and cryogenic hazard warnings
- Escalation to STK_SAF for all hydrogen anomalies

### Compliance
- EASA CS-25 with Special Conditions SC-28-H2-001 and SC-28-CRYO-002
- EU AI Act (high-risk category for AI monitoring)
- ISO 14687-2 hydrogen fuel quality

## Running the Pipeline

```bash
# Generate AMM using the ATA 28 H2 pipeline
aerospacemodel pipeline run \
  --config program_config.yaml \
  --pipeline ata28_h2_pipeline \
  --contract ASIT/CONTRACTS/active/Q100-CTR-AMM-001.yaml
```

## Related Documentation

| Document | Path |
|----------|------|
| ATA 28 BREX Instructions | `docs/ATA_28_BREX_INSTRUCTIONS.md` |
| ATA 28 C2 Structure | `docs/ATA_28_C2_AMPEL360_Q100.md` |
| H2 Pipeline | `pipelines/ata28_h2_pipeline.yaml` |
| Lifecycle Activation | `lifecycle/T_SUBDOMAIN_LC_ACTIVATION.yaml` |
