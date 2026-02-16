# CS-25 Compliance Matrix — ATA 28-11-00 LH₂ Primary Tank (Cryogenic Cells)

| Key | Value |
|-----|-------|
| Matrix ID | CM-28-11-CS25 |
| Regulation | EASA CS-25 |
| ATA Code | 28-11-00 |
| Technology Domain | C2 — Circular Cryogenic Cells |
| Aircraft Programme | AMPEL360 Q100 |
| Lifecycle Phase | LC04 (Design Definition) |
| Status | Preliminary (DEV — not baselined) |

> **Note:** CS-25 is written for conventional fuels.  For LH₂ cryogenic
> primary tank an additional package of **Special Conditions (SC)**, Issue
> Papers and Means of Compliance agreed with EASA is required.  Items
> flagged **SC-LH2-XX** identify those gaps explicitly.

---

## A) Tank Structural Integrity and Loads

| Req ID | CS-25 Ref | Topic | Applicability | Strategy (MoC) | Evidence / Artefacts | V&V |
|--------|-----------|-------|---------------|----------------|----------------------|-----|
| CM-A-001 | CS 25.963 | Fuel tanks general (integrity, drainage, ventilation, expansion) | Very High | Structural analysis + margin definition + leak tests | Tank structural spec, stress report, leak test plan, vent path analysis | Analysis + Test |
| CM-A-002 | CS 25.965 | Fuel tank tests — cryogenic qualification | Very High | Cryogenic test campaign (pressure, cycles, thermal shock) | Tank Qualification TestPlan/Report, acceptance criteria, instrumentation | Test |
| CM-A-003 | CS 25.967 | Fuel tank installation (supports, loads, vibration) | Very High | FEM + vibration tests + limit/ultimate load analysis | FEM, loads report, installation drawings, fastener substantiation | Analysis + Test |
| CM-A-004 | CS 25.571 | Damage tolerance / fatigue — cryogenic cycling | Very High | Cryogenic fatigue tests/analysis + DT substantiation | Fatigue & DT report, crack growth assumptions, test coupons, thermal cycling data | Analysis + Test |

**Delta LH₂ (SC/MoC):** cryogenic thermal cycling, embrittlement,
vacuum jacket loads, crash-load cases unique to LH₂ primary tank geometry.

---

## B) Pressure, Venting, Boil-off Management

| Req ID | CS-25 Ref | Topic | Applicability | Strategy (MoC) | Evidence / Artefacts | V&V |
|--------|-----------|-------|---------------|----------------|----------------------|-----|
| CM-B-001 | CS 25.969 | Fuel tank expansion space — ullage and transient control | High | Ullage definition + transient analysis + pressure/vent control | Vent/relief sizing report, pressure control spec, transient simulation | Analysis |
| CM-B-002 | CS 25.975 | Fuel tank vents and relief — cryogenic sizing | Very High | Vent/relief sizing + plume analysis + thermal analysis | Relief valve sizing, vent routing, plume/ingestion analysis, thermal bridge heat leak decomposition | Analysis + Test |

**Delta LH₂:** LH₂ boil-off phenomenology, ullage gas management,
relief valve sizing for cryogenic transients, vent plume hazard analysis.

---

## C) Fire / Explosion / Ignition Prevention

| Req ID | CS-25 Ref | Topic | Applicability | Strategy (MoC) | Evidence / Artefacts | V&V |
|--------|-----------|-------|---------------|----------------|----------------------|-----|
| CM-C-001 | CS 25.981 | Fuel tank ignition prevention | Critical | FHA/SSA + zonal safety + ignition source control + bonding/earthing | FHA/SSA (ATA 28-11), Zonal Hazard Analysis, EWIS segregation, ignition source control | Analysis + Inspection |
| CM-C-002 | CS 25.1309 | System safety — catastrophic/hazardous failure conditions | Critical | ARP4761: FHA → PSSA → SSA + DAL/IDAL allocation | FHA/PSSA/SSA pack, fault trees, FMEA, CDCCLs, requirements trace | Analysis |

**Delta LH₂:** H₂ ignition energy is far lower than kerosene; diffusivity
and buoyancy create unique ventilation and detection requirements.  EASA
typically requires a dedicated safety argument (Issue Paper).

---

## D) Materials, Processes, Inspection and ICA

| Req ID | CS-25 Ref | Topic | Applicability | Strategy (MoC) | Evidence / Artefacts | V&V |
|--------|-----------|-------|---------------|----------------|----------------------|-----|
| CM-D-001 | CS 25.603 / CS 25.605 | Materials / fabrication — cryogenic qualification | Very High | Cryogenic-compatible material selection (embrittlement, permeation) | Material allowables, M&P spec, welding/brazing qualification, cryogenic test data | Analysis + Test |
| CM-D-002 | CS 25.1529 | Instructions for Continued Airworthiness | High | LH₂-specific ICA: purges, inspections, leak checks, vacuum integrity | ICA draft (ATA 28-11), maintenance tasks, intervals, troubleshooting | Inspection + Review |

**Delta LH₂:** Cryogenic-compatible materials, hydrogen permeation limits,
embrittlement screening, and LH₂-specific ICA for continued airworthiness.

---

## Special Conditions — LH₂ Gaps Beyond CS-25

These items fall outside the literal CS-25 text (or are only indirectly
covered) and require explicit Special Conditions agreed with EASA:

| SC ID | Topic | Description | MoC |
|-------|-------|-------------|-----|
| SC-LH2-01 | Boil-off management | Pressure, vent, normal/abnormal modes, dispatch criteria | Analysis + Test |
| SC-LH2-02 | Hydrogen detection and isolation | Sensor locations, thresholds, alert logic, SIL/DAL allocation | Analysis + Test + Inspection |
| SC-LH2-03 | Cryogenic thermal shock and vacuum integrity | Structure + insulation + interface survivability under thermal transients | Analysis + Test |
| SC-LH2-04 | Permeation / leak-before-burst | Quantitative criteria for hydrogen permeation and LBB argument | Analysis + Test |
| SC-LH2-05 | Crashworthiness — cryogenic tank | Crash load cases, post-crash H₂ release mitigation, survivability | Analysis + Test |

---

## Minimum Evidence Package (Certification-Ready)

| # | Artefact |
|---|----------|
| 1 | ATA28-11_LH2_PrimaryTank_StructuralSpec.md |
| 2 | CS25_compliance_matrix.yaml |
| 3 | FHA_PSSA_SSA_ATA28-11_LH2.pdf |
| 4 | Tank_Qualification_TestPlan_Report.pdf |
| 5 | VentingAndReliefSizing_Report.pdf |
| 6 | MaterialsAndProcesses_Cryogenic_Qualification.pdf |
| 7 | ThermalBridge_HeatLeak_Decomposition.pdf |
| 8 | ICA_ATA28-11_LH2_PrimaryTank_Draft.pdf |

---

## Governance

This compliance matrix resides in `KDB/DEV/trade-studies/` and is **not
baselined**.  Promotion to `KDB/LM/SSOT/` requires:

- BREX validation
- Trace coverage verification
- STK_ENG / STK_SAF / Airworthiness approval
- ECR submission via `GOVERNANCE/CHANGE_CONTROL/`

See **ECR-ATA28-11-CS25-SSOT-001** for the active promotion request.
