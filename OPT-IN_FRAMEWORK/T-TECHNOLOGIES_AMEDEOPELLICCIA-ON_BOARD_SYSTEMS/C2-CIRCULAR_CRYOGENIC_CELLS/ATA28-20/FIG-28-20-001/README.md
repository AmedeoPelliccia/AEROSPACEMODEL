# FIG-28-20-001 — H₂ Cryogenic Shut-Off Valve Assembly Breakdown

**ATA:** 28-20-00  
**Figure:** FIG-28-20-001 REV A  
**DMC:** `DMC-AMPEL360-A-28-20-00-00A-040A-D`  
**Baseline:** BL-28-004  
**Lifecycle:** LC04 – Design Definition  
**SSOT:** SSOT-Q100-C2-004  
**DPP:** DPP-ATA28-20-001  
**Special Conditions:** ⭐ SC-28-H2-001 · SC-28-CRYO-002  
**Authority:** ASIT / Contract `KITDM-CTR-LM-CSDB_ATA28_H2`

---

## Overview

This directory contains all externalized data artifacts for the
**AMPEL360 Q100 ATA 28-20 Cryogenic H₂ Shut-Off Valve IPD module**
(FIG 28-20-001). The data has been extracted from the original
monolithic IPD Viewer component and refactored per the OPT-IN_FRAMEWORK
canonical architecture (TLI v2.1).

The shut-off valve is a **DAL A** safety-critical component in the
cryogenic hydrogen distribution system, providing fail-closed isolation
of LH₂ supply at –253 °C.

---

## Directory Contents

| File | Description | Validates Against |
|------|-------------|------------------|
| [`parts_list.json`](parts_list.json) | 14-item IPD parts list | `schemas/ipd/ipd_part_item.schema.json` |
| [`cross_references.json`](cross_references.json) | 8 AMM/CMM/TSM/SB/SRM/WDM/KNOT cross-refs | `schemas/ipd/ipd_cross_reference.schema.json` |
| [`source_data.json`](source_data.json) | 9 approved vendor source packages | `schemas/ipd/ipd_source_data.schema.json` |
| [`figure_metadata.json`](figure_metadata.json) | Figure title block + 14-hotspot map | `schemas/ipd/ipd_figure_metadata.schema.json` |
| [`drawing.svg`](drawing.svg) | Static SVG technical drawing (FIG-28-20-001 REV A) | — |
| [`viewer/IPDViewer.jsx`](viewer/IPDViewer.jsx) | Refactored React IPD Viewer component | — |

---

## Parts Summary (14 Items)

| Item | Hotspot | PN | Nomenclature | Category |
|------|---------|-----|--------------|----------|
| 0 | A | AMP-28-2001-000 | Shut-Off Valve Assembly – H₂ Cryogenic | assy |
| 2 | B | AMP-28-2001-010 | Valve Body – Cryogenic Grade SS 316L | detail |
| 4 | C | AMP-28-2001-020 | Valve Disc – LH₂ Service | detail |
| 6 | D | AMP-28-2001-030 | Valve Stem – Cryogenic | detail |
| 8 | E | AMP-28-2001-040 | Actuator Assembly – Pneumatic Cryogenic | assy |
| 10 | F | AMP-28-2001-050 | Actuator Piston – Cryogenic Service | detail |
| 12 | G | AMP-28-2001-060 | Solenoid Valve – Pilot 28VDC | detail |
| 14 | H | AMP-28-2001-070 | Position Sensor Assembly – LVDT Open/Closed | detail |
| 16 | I | AMP-28-2001-080 | Return Spring – Cryogenic Grade | detail |
| 18 | J | AMP-28-2001-090 | Seal Set – PTFE Cryogenic | consumable |
| 20 | K | AMP-28-2001-100 | Bearing Set – Cryogenic Journal | detail |
| 22 | L | AMP-28-2001-110 | Fastener Kit – Cryogenic Grade | standard |
| 24 | M | AMP-28-2001-120 | Heat Shield Assembly – Valve Interface | detail |
| 26 | N | AMP-28-2001-130 | Insulation Blanket – Multi-Layer (MLI) | consumable |

---

## Cross-References (8 Items)

| Type | Ref | Title |
|------|-----|-------|
| AMM | DMC-AMPEL360-A-28-20-00-00A-200A-D | Cryogenic H₂ Shut-Off Valve – Removal |
| AMM | DMC-AMPEL360-A-28-20-00-00A-400A-D | Cryogenic H₂ Shut-Off Valve – Installation |
| CMM | DMC-AMPEL360-A-28-20-10-00A-520A-D | Shut-Off Valve Assembly – Component Maintenance |
| TSM | DMC-AMPEL360-A-28-20-00-00A-700A-D | Cryogenic H₂ Shut-Off Valve – Fault Isolation |
| SB  | SB-AMPEL360-28-2001-REV-A | Cryogenic Seal Set Replacement |
| SRM | DMC-AMPEL360-A-28-20-00-00A-300A-D | Valve Body Structural Repair |
| WDM | DMC-AMPEL360-A-28-20-02-00A-040A-D | Solenoid Valve Wiring |
| KNOT | KNOT-ATA28-20-00-001 | LH₂ PTFE Seal Cryogenic Compatibility |

---

## Vendor Sources (9 Packages)

| ID | Vendor | Status |
|----|--------|--------|
| AMPEL-VP-2820-001 | Parker Hannifin Cryogenics Division | APPROVED |
| AMPEL-VP-2820-002 | Moog Aircraft Group | APPROVED |
| AMPEL-VP-2820-003 | Marotta Controls Inc. | APPROVED |
| AMPEL-VP-2820-004 | Curtiss-Wright Defense Solutions | APPROVED |
| AMPEL-VP-2820-005 | Associated Spring (Barnes Group) | APPROVED |
| AMPEL-VP-2820-006 | Trelleborg Sealing Solutions | APPROVED |
| AMPEL-VP-2820-007 | Garlock Bearings (EnPro Industries) | QUAL-TEST |
| AMPEL-VP-2820-008 | Lisi Aerospace | APPROVED |
| AMPEL-VP-2820-009 | Technifab Products Inc. | QUAL-TEST |

---

## ⚠️ Safety Notices

**DANGER — HYDROGEN HAZARD (SC-28-H2-001)**  
Hydrogen is extremely flammable. Concentrations of 4–75% in air are explosive.
Ensure adequate ventilation. No open flames or ignition sources within 15 metres.
Bonding and grounding required for all H₂ operations.

**DANGER — CRYOGENIC HAZARD (SC-28-CRYO-002)**  
Liquid hydrogen at –253 °C (–423 °F). Contact causes severe cryogenic burns.
Wear face shield, cryogenic gloves, and protective apron.
Emergency shower and eyewash must be accessible.

---

## Traceability

- **SSOT Registry:** `OPT-IN_FRAMEWORK/ENGINEERING_SSOT/00_SSOT_REGISTRY.yaml` → SSOT-Q100-C2-004
- **DPP Ledger:** `OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS/D-DIGITAL_THREAD_TRACEABILITY/ATA96/DPP-ATA28-20-001.yaml`
- **IPC Pipeline:** `pipelines/ipc_pipeline.yaml`
- **Parts Mapping:** `ASIGT/mapping/parts_to_ipd.yaml`

---

*Maintained by ASIT · Authority: KITDM-CTR-LM-CSDB_ATA28_H2 · Lifecycle: LC04*
