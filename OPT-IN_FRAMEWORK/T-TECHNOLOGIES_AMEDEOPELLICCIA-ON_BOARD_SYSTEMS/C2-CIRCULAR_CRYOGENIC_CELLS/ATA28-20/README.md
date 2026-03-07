# ATA 28-20 — Cryogenic H₂ Distribution (Shut-Off Valves)

**Aircraft:** AMPEL360 Q100 Hydrogen-Electric  
**ATA Chapter:** 28-20 – Fuel Distribution (Cryogenic H₂)  
**Technology Domain:** C2-CIRCULAR_CRYOGENIC_CELLS ⭐ Novel Technology  
**Lifecycle:** LC04 – Design Definition  
**Authority:** ASIT / Contract `KITDM-CTR-LM-CSDB_ATA28_H2`  
**Special Conditions:** SC-28-H2-001 · SC-28-CRYO-002

---

## Overview

ATA 28-20 covers the **Cryogenic Hydrogen Distribution** subsystem of the
AMPEL360 Q100, including all shut-off valves, isolation valves, and associated
fittings in the LH₂ distribution loop operating at –253 °C.

This directory follows the **OPT-IN_FRAMEWORK** canonical architecture (TLI v2.1)
for Novel Technology (T-domain, C2 subdomain) with IPD data artifacts externalized
from component-level viewer components per the BREX-driven refactoring mandate.

---

## Contents

| Directory | Figure | Description |
|-----------|--------|-------------|
| [`FIG-28-20-001/`](FIG-28-20-001/) | FIG-28-20-001 | H₂ Cryogenic Shut-Off Valve – Assembly Breakdown |

---

## Key Engineering Facts

| Property | Value |
|----------|-------|
| Operating Temperature | –253 °C (LH₂ service) |
| Valve Type | Butterfly (disc-and-stem) |
| Actuation | Pneumatic, spring-return, fail-CLOSED |
| DAL Classification | DAL A (safety-critical, ARP4754A) |
| Applicable Standard | S1000D Issue 5.0 / Info Code 941 |
| Effectivity | ALL (MSN001–UP) |

---

## ⚠️ Safety Notices

**DANGER — HYDROGEN HAZARD (SC-28-H2-001)**  
Hydrogen is extremely flammable (4–75% flammability range in air).
Ensure adequate ventilation and continuous H₂ monitoring before any work.

**DANGER — CRYOGENIC HAZARD (SC-28-CRYO-002)**  
Liquid hydrogen at –253 °C. Full cryogenic PPE mandatory.

---

## Related Documents

| Document | Path |
|----------|------|
| ATA 28 Fuel README | [`../ATA_28-FUEL/README.md`](../ATA_28-FUEL/README.md) |
| C2 Domain README | [`../README.md`](../README.md) |
| SSOT Registry | [`../../../../ENGINEERING_SSOT/00_SSOT_REGISTRY.yaml`](../../../../ENGINEERING_SSOT/00_SSOT_REGISTRY.yaml) |
| DPP Ledger | [`../../../../N-NEURAL_NETWORKS/D-DIGITAL_THREAD_TRACEABILITY/ATA96/DPP-ATA28-20-001.yaml`](../../../../N-NEURAL_NETWORKS/D-DIGITAL_THREAD_TRACEABILITY/ATA96/DPP-ATA28-20-001.yaml) |

---

*Maintained by ASIT · Lifecycle: LC04 · BL-28-004*
