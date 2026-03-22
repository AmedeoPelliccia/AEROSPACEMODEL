# Propulsion Architecture Trade Study
**Reusable Spaceplane — Combined-Cycle vs Rocket-Dominant vs Hybrid**

| Field | Value |
| :--- | :--- |
| **Document ID** | KNU-SP-02-ANA-001 |
| **Parent KNOT** | KNOT-SP-02: Propulsion-sequence closure |
| **GU Reference** | GU-02 |
| **KNU Type** | ANA (Screening Analysis) — Qualitative pre-model trade study |
| **Lifecycle Position** | Supports LC01/LC02 architecture screening; precedes LC05 model-based analyses |
| **MN Trace** | MN-01; MN-03; MN-10 |
| **Priority** | P0 (Programme-gate prerequisite) |
| **Owner** | STK_SE (Systems Engineering) |
| **Stakeholders** | STK_SAF; STK_CERT; STK_TEST |
| **Version** | 0.4 |
| **Date** | 2026-03-22 |
| **Status** | IN_REVIEW |

### Change Log

| Version | Date | Change |
| :--- | :--- | :--- |
| 0.1 | 2026-03-22 | Initial draft |
| 0.2 | 2026-03-22 | Incorporated review corrections: reclassified as screening trade; corrected terminology; revised Branch A verdict. |
| 0.3 | 2026-03-22 | Final review corrections: Corrected M ≤ 2.5 classification; added sensitivity indicators; softened analogues; expanded residual trajectory; tagged abort numbers as notional. |
| 0.4 | 2026-03-22 | **Final Polish:** Softened language in Section 1 (screening limitations); standardized mass breakdown line items in Sections 4.2/4.3; added GAIA spillover qualifier; restored Review & Approval table. |

---

## 1. Objective

This trade study evaluates three candidate propulsion architectures for a reusable spaceplane supporting **Hypersonic Point-to-Point Transport (Branch A)** and **Single-Stage-to-Orbit (Branch B)**. The architectures are assessed against propulsive performance, mass penalty, thermal compatibility, mode-transition risk, and branch-closure viability.

This is the first executed KNU in the feasibility programme, directly addressing **Governing Uncertainty GU-02 (Propulsion-Sequence Closure)**. The outcome determines whether the design space **may** contain an architecture capable of supporting both mission branches and identifies which option minimizes risk to the concept-fatal KNOTs: **KNOT-SP-05 (Dry-Mass Fraction Closure)** and **KNOT-SP-11 (Abort Coverage)**.

### 1.1 Artifact Classification
This document is a **qualitative screening trade study**. No computational models were executed. The purpose is architecture selection and non-viable option elimination, not performance prediction. Quantitative closure evidence will be produced by follow-on KNUs (ANA-002 through ANA-004), which constitute LC05 analysis-model artifacts.

### 1.2 Acceptance Criteria
Per the KNU_PLAN, this artifact is accepted when:
*   Three architectures have been assessed against Isp, mass, thermal, and mode-transition criteria.
*   Architectures are ranked with qualitative sensitivity indications and explicit downstream dependencies.
*   A provisional baseline recommendation is issued with traceability to downstream KNOTs.

### 1.3 Downstream Dependencies
The selected architecture constrains all subsequent analyses:
*   **KNOT-SP-05 (Dry-Mass Fraction Closure):** Propulsion mass is the largest single contributor to inert mass.
*   **KNOT-SP-04 (Mode-Transition Controllability):** Transition complexity is architecture-dependent.
*   **KNOT-SP-07 (TPS Closure):** Ascent trajectory and thermal environment are propulsion-dependent.
*   **KNOT-SP-10 (Trajectory Closure):** Isp schedule governs achievable trajectories.
*   **KNOT-SP-B1 (Orbital Delta-v Closure):** Propellant fraction and Isp determine payload capacity.

---

## 2. Candidate Architectures

### 2.1 Architecture A — Turbine-Based Combined Cycle (TBCC)
**Description:** A variable-cycle turbojet/turbofan for Mach 0–2.5, transitioning to ramjet (M 2.5–5) and scramjet (M 5–12+). A separate LH₂/LOX rocket provides exo-atmospheric thrust for SSTO. Engines share a common inlet and flowpath with variable geometry.

**Representative Analogues:** SABRE (Reaction Engines — precooled air-breathing rocket); NASA GRC TBCC studies; ATREX (Japan). Note: No full-scale combined-cycle spaceplane engine has been flight-demonstrated.

*   **Key Advantage:** Highest air-breathing Isp (2,000–3,500 s), drastically reducing propellant fraction during atmospheric ascent.
*   **Key Penalty:** Engine mass is 2–4× heavier than equivalent-thrust rocket. Complex variable-geometry inlet required. Three mode transitions present significant certification risk. Forebody-inlet coupling creates high integration risk (GU-03).

### 2.2 Architecture B — Rocket-Dominant with Subsonic Augmentation
**Description:** LH₂/LOX rockets perform the entire ascent. Small turbojets or fans provide low-speed ground handling and go-around capability. The vehicle climbs steeply to minimize drag/heating, similar to a vertical launch vehicle.

**Representative Analogues:** VentureStar/X-33 (Lockheed Martin); DC-X (McDonnell Douglas); Skylon rocket-only studies. Note: No operational SSTO achieved.

*   **Key Advantage:** Simplest propulsion system; lightest engine mass per unit thrust. No mode transitions. Extensive flight heritage (RL-10, RS-25). Minimizes air-breathing thermal loads.
*   **Key Penalty:** Isp limited to ~450 s. Requires extreme propellant fraction (~90% GTOM). Steep ascent limits aerodynamic lift utilization, increasing gravity losses. Functionally a runway-launched rocket, negating aircraft-like operational advantages.

### 2.3 Architecture C — Hybrid Rocket + Air-Breathing Boost
**Description:** Air-breathing propulsion (turbofan/jet) for Mach 0–2.5, then direct transition to LH₂/LOX rocket for M 2.5+. Eliminates ramjet/scramjet regimes.

**Representative Analogues:** **Partial architectural analogues only; no direct flight-proven turbofan-to-rocket reusable spaceplane precedent exists.** Relevant reference classes include runway-operable high-speed aircraft, reusable LH₂/LOX rocket vehicles, and concept studies combining aircraft-like take-off with rocket ascent.

*   **Key Advantage:** Captures low-speed operational benefits (runway takeoff, diversion) without high-Mach air-breathing complexity. Single mode transition (M 2.5). Significantly lighter than TBCC.
*   **Key Penalty:** Isp above M 2.5 limited to rocket-class (~450 s). Higher propellant fraction than TBCC. Sustained hypersonic cruise is not viable (fuel-inefficient).

---

## 3. Trade Matrix

**Scoring Scale:**
*   `++` Strong advantage
*   `+` Advantage
*   `0` Neutral
*   `–` Disadvantage
*   `––` Severe disadvantage

### 3.1 Summary Matrix

| Dimension | A: TBCC | B: Rocket-Dominant | C: Hybrid |
| :--- | :--- | :--- | :--- |
| **Air-breathing Isp** | ++ (2,000–3,500 s to M 12) | –– (N/A above M 0.5) | + (to M 2.5 only) |
| **Engine mass/thrust** | –– (2–4× rocket) | ++ (Lightest) | + (Light subsystems) |
| **Mode transitions** | –– (3 high-risk events) | ++ (0 events) | + (1 event at M 2.5) |
| **Propellant fraction (SSTO)** | + (~82–85%) | –– (~90–92%) | – (~87–89%) |
| **Thermal integration** | –– (Inlet >2,000 K) | + (Steep climb) | 0 (Moderate) |
| **Aircraft-like operability** | ++ (Full envelope) | –– (No diversion) | + (Low-speed diversion) |
| **TRL / Heritage** | –– (No flight-proven system) | ++ (High heritage) | + (Proven subsystems) |

### 3.2 Interpretation
No architecture dominates all dimensions. The trade is between **performance (A)**, **simplicity (B)**, and **pragmatic balance (C)**. Architecture A wins on Isp but fails on mass/complexity. Architecture B wins on simplicity but fails on operability and mass fraction. Architecture C preserves essential operability while mitigating the highest technology risks.

### 3.3 Sensitivity Indicators
The ranking is most sensitive to:
*   Inert mass fraction margins.
*   Propulsion-system packaging volume constraints.
*   Transition corridor controllability boundaries.
*   Branch A mission definition requirements above M 2.5.

---

## 4. Architecture-Specific Closure Assessment

### 4.1 Architecture A — TBCC
The TBCC offers theoretical performance advantages via high Isp, reducing propellant fraction. However, the engine mass penalty (2–4× rocket) consumes much of the inert mass savings. For a vehicle requiring <10–12% inert mass fraction, this penalty is critical.

**Risk Profile:**
*   **Mode Transition:** Three transitions (Turbojet → Ramjet → Scramjet → Rocket) must occur within narrow corridors. No certification framework exists for in-flight thermodynamic cycle changes.
*   **Integration:** Forebody-inlet coupling (GU-03) creates cross-discipline fragility; aerodynamic changes for re-entry may invalidate inlet operability.

**Closure Verdict:**
*   **SSTO (Branch B):** **Unlikely to close.** Engine mass penalty likely exceeds Isp benefits. Historical precedent (NASP/X-30 termination) aligns with this assessment.
*   **Hypersonic P2P (Branch A):** **Conditional.** Viable only if cruise is limited to M 5–6 (ramjet), avoiding scramjet complexity. Does not close the full Branch A requirement.

### 4.2 Architecture B — Rocket-Dominant
Closes easily on propulsion simplicity and heritage. However, mass-fraction arithmetic is unforgiving.

**Illustrative Mass Breakdown (GTOM 250,000 kg / 91% Propellant):**
*   **Non-propellant Budget:** 22,500 kg (9%)
*   **Estimated Inert Mass:**
    *   Structure (4% GTOM): 10,000 kg
    *   TPS (2% GTOM): 5,000 kg
    *   Propulsion - Rocket (1.5% GTOM): 3,750 kg
    *   Propulsion - Air-breathing (0% GTOM): 0 kg
    *   Landing Gear (0.8% GTOM): 2,000 kg
    *   Systems, Avionics, Margins (0.7% GTOM): 1,750 kg
*   **Total Inert:** 22,500 kg
*   **Remaining Payload:** **0 kg**

**Operational Impact:** Abandons the aircraft-like rationale. Cannot divert or loiter. Functionally an inferior vertical rocket with landing gear.

**Closure Verdict:**
*   **SSTO (Branch B):** **Marginal.** Fails on mass fraction (KNOT-SP-05) and operability (MN-02).
*   **Hypersonic P2P (Branch A):** **Invalid.** Rocket Isp is prohibitive for sustained atmospheric cruise.

### 4.3 Architecture C — Hybrid
Occupies the pragmatic middle ground. The single transition (Turbofan → Rocket at M 2.5) occurs in a well-characterized regime. The air-breathing phase provides critical operational capabilities (takeoff, diversion) and reduces gravity losses via lift-supported ascent.

**Illustrative Mass Breakdown (GTOM 250,000 kg / 88% Propellant):**
*   **Non-propellant Budget:** 30,000 kg (12%)
*   **Estimated Inert Mass:**
    *   Structure (4% GTOM): 10,000 kg
    *   TPS (2% GTOM): 5,000 kg
    *   Propulsion - Rocket (1.2% GTOM): 3,000 kg
    *   Propulsion - Turbofan (0.8% GTOM): 2,000 kg
    *   Landing Gear (0.8% GTOM): 2,000 kg
    *   Systems, Avionics, Margins (0.7% GTOM): 1,750 kg
*   **Total Inert:** 23,750 kg
*   **Remaining Payload:** **6,250 kg (~2.5% GTOM)**

**Analysis:** The margin is thin but non-zero. Both subsystems have flight heritage, bounding development risk.

**Closure Verdict:**
*   **SSTO (Branch B):** **Most likely to close.** Preserves concept rationale with manageable risk.
*   **Hypersonic P2P (Branch A):** **Not closed (current definition).** Efficient cruise limited to M ≤ 2.5. Branch A viability under this architecture requires:
    1.  **Redefinition** to a high-speed but non-hypersonic transport mission (M ≤ 2.5 cruise).
    2.  **Separation** into a different architecture family.
    3.  **Deferral** of the branch.

---

## 5. Integrated Scoring Summary

| Assessment | A: TBCC | B: Rocket-Dominant | C: Hybrid |
| :--- | :--- | :--- | :--- |
| **Branch A (Hypersonic) Closure** | Conditional/High-risk | Invalid | Not closed |
| **Branch B (SSTO) Closure** | Unlikely | Marginal | **Most Likely** |
| **GU-01 (Branch Convergence)** | Not closed | Not closed | Not closed |
| **Technology Risk** | Very High | Low | Moderate |
| **Certification Risk** | Very High | Moderate | Moderate |
| **Programme Baseline Suitability** | No | Fallback only | **Provisional Baseline** |

---

## 6. Recommendation

**Architecture C (Hybrid: Turbofan + LH₂/LOX Rocket) is recommended as the provisional baseline for further Branch B (Orbital SSTO) mass, trajectory, transition, and packaging studies.**

This selection does **not** close GU-01 (Branch Convergence). Architecture C cannot satisfy the original requirement for sustained high-Mach cruise (Branch A). Branch A must be:
1.  **Redefined** to a high-speed but non-hypersonic transport mission (M ≤ 2.5).
2.  **Separated** into a distinct architecture family.
3.  **Deferred** to lower priority.

### 6.1 Architecture Disposition

| Architecture | Disposition |
| :--- | :--- |
| **A: TBCC** | **Not Selected.** Technology risk excessive for baseline. Retain as long-term option pending TRL maturation. |
| **B: Rocket-Dominant** | **Fallback.** Retain if Architecture C fails mass closure. Accepts loss of Branch A and operability rationale. |
| **C: Hybrid** | **Provisional Baseline.** Proceed to integrated mass/trajectory studies. |

### 6.2 Programme Decision Required
**Decision Point:** Definition of Branch A scope.
The mass model (KNU-SP-05-ANA-001) cannot finalize inputs until Branch A scope is resolved. If Branch A remains a requirement for M > 2.5 cruise, GU-01 cannot close under this architecture. This decision is required before the next programme review.

---

## 7. Residual Assessment and Follow-On KNUs

### 7.1 Required Follow-On KNUs

| KNU ID | Title | Scope |
| :--- | :--- | :--- |
| **KNU-SP-02-ANA-002** | Mode-Transition Thrust Gap | Quantify thrust/altitude loss during Turbofan → Rocket handover. |
| **KNU-SP-02-ANA-003** | Isp vs Mach Performance Map | Map performance M 0–25+ for trajectory integration. |
| **KNU-SP-02-ANA-004** | Propulsion Mass/Volume Estimate | Verify packaging within inert mass budget. |

### 7.2 Residual Reduction Trajectory
*   **Baseline:** Unbounded.
*   **Post-Study (Current):** Partially bounded; non-viable options screened out and provisional Branch B baseline selected.
*   **Post-ANA-002:** Transition corridor bounded.
*   **Post-ANA-003:** Performance envelope linked to trajectory logic.
*   **Post-ANA-004:** Propulsion mass/volume packaging bounded.
*   **Closure Candidate:** Ready only after cross-check with KNOT-SP-05 and KNOT-SP-10.

---

## 8. Impact on Cross-Coupling KNOTs

### 8.1 KNOT-SP-05 (Dry-Mass Fraction Closure)
**Impact:** Partially de-risked. Hybrid is lighter than TBCC and more efficient than pure rocket. However, mass-fraction remains the dominant risk. A ±1% shift in inert mass fraction shifts payload by ~2,500 kg. The design space is extremely narrow.

### 8.2 KNOT-SP-11 (Abort Coverage)
**Impact:** Significantly de-risked below M 2.5 due to air-breathing capability (diversion/go-around).
**Remaining Risk:** The "abort coverage gap" exists between the last viable return-to-launch-site point (**notional placeholder, to be quantified**) and the first viable abort-to-orbit point (**notional placeholder, to be quantified**). This gap must be characterized in KNU-SP-11-SAF-001.

### 8.3 GU-01 (Branch Convergence)
**Impact:** Not closed. Architecture C supports SSTO (Branch B) but not sustained hypersonic P2P (Branch A). Programme must down-select or split branches.

---

## 9. Programme Spillover (AMPEL360 / GAIA)

*   **AMPEL360 Q100 (Propulsion):** The hybrid architecture's power management and transition control logic may inform the Q100's fuel-cell transient management and distributed propulsion assurance (DO-178C/DO-254).
*   **AMPEL360 Q100 (Cryogenics):** LH₂/LOX system integration (KNOT-SP-06) shares a technology base with Q100 ATA 28 C² Cell architecture.
*   **GAIA-SPACE-LAUNCHER:** The rocket phase (M 2.5+) is applicable to upper-stage design studies. Note: Transfer is limited to engine design and restart logic; the trajectory and staging architecture differ significantly, as the spaceplane's rocket operates from an initial condition of M 2.5 / ~15 km (air-launched state), whereas GAIA upper stages typically operate from vertical staging conditions.

---

## 10. Appendix — Assessment Methodology

### 10.1 Scoring Basis
Scores derived from engineering judgment, published data, historical outcomes (NASP, X-33), and certification precedent (CS-25, CS-E). No computational models executed.

### 10.2 Limitations
*   Propellant fractions are approximate (ideal rocket equation with assumed losses).
*   TBCC engine mass estimates carry ±30–40% uncertainty.
*   Mass breakdowns are parametric illustrations, not design-point calculations.
*   Economic analysis deferred to KNOT-SP-14.

### 10.3 Review and Approval

| Role | Name | Date | Status |
| :--- | :--- | :--- | :--- |
| Author | STK_SE | 2026-03-22 | Complete |
| Reviewer (v0.1) | Programme Lead | 2026-03-22 | Complete; corrections in v0.2 |
| Reviewer (v0.2 → v0.3) | Programme Lead | 2026-03-22 | Complete; corrections in v0.3 |
| Reviewer (v0.3 → v0.4) | Programme Lead | 2026-03-22 | Complete; final polish |
| Reviewer | STK_SAF | — | Pending |
| Reviewer | STK_CERT | — | Pending |
| Approver | Programme Lead | — | Pending final reviews |
