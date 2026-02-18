# ATA 08 — Leveling and Weighing Infrastructure: Case Studies

**Section:** 7 — Case Studies  
**Parent:** [`README.md`](README.md) | **Crosswalk:** [`../CROSSWALK.md`](../CROSSWALK.md)

---

## CS-08-001 — Post-Modification Weighing After Fuel System Retrofit

**Context:** A regional operator retrofitted a conventional Jet-A fuel system with a hybrid H₂ boost system (analogous to AMPEL360 Q100 stage-1 configuration). Post-modification weighing was required to update the aircraft's approved weight and balance data.

**Challenge:** The new LH₂ tank added 87 kg of structural mass and shifted CG aft by 12 cm. The existing weighing bay was not H₂-classified.

**Actions Taken:**
1. Weighing bay upgraded to Zone 2 classification with ATEX electrical equipment and forced ventilation.
2. H₂ fixed detection installed (four electrochemical sensors).
3. Scale calibration re-verified to ISO 17025 after bay modification.
4. LH₂ density correction procedure developed and approved by airworthiness authority.
5. Post-modification weighing performed with dry (empty) LH₂ tank and again with nominal LH₂ load to validate correction formula.

**Outcome:** Revised Weight and Balance Manual approved by EASA. Weighing bay upgrade template adopted as best practice for the M2-MAINTENANCE_ENVIRONMENTS ATA 08 design specification.

**Lessons Learned:**
- Bay H₂ classification must be planned before LH₂ system installation, not retrofitted.
- Density correction formula must be validated against at least two fuel temperatures.
- Personnel training on cryogenic hazards added ≈ 4 h to project timeline.

---

## CS-08-002 — Annual Weighing Programme Optimisation

**Context:** An MRO organisation managing 40 narrowbody aircraft implemented a risk-based weighing programme, reducing required weighing frequency for well-maintained aircraft while maintaining safety.

**Key Finding:** Aircraft with no structural repairs, no configuration changes, and fully documented mass-item tracking for 24 months could be extended from annual to 48-month weighing intervals with regulatory authority agreement (EASA acceptable means of compliance).

**Relevance for AMPEL360 Q100:**
- The LH₂ tank and fuel cell stack represent significant mass items that must be tracked continuously; any replacement or repair triggers a new weighing.
- Digital mass-item tracking (integrated into the digital thread) can satisfy the documentation evidence requirement for extended weighing intervals.
- Reference: `OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS/D-DIGITAL_THREAD_TRACEABILITY/` for mass-change traceability via digital thread.

---

## CS-08-003 ⭐ — LH₂ Mass Correction Validation Trial (Concept)

**Context:** As of the date of this document, no certified LH₂-fuelled commercial aircraft has been weighed under operational conditions. This case study documents the proposed validation approach for the AMPEL360 Q100 programme.

**Proposed Approach:**
1. Weigh aircraft with empty LH₂ tanks (known dry mass baseline).
2. Load known mass of LH₂ (measured at fill point by Coriolis mass flow meter traceable to ISO 17025).
3. Re-weigh aircraft on calibrated scales.
4. Compare scale-derived mass with Coriolis-derived mass.
5. Validate density correction formula (ρ(T) per NIST SR 69) against test results.
6. Submit validation report to EASA for SC-28-H2-001 compliance credit.

**Expected Outcome:** ≤ 0.5% error between scale and flow-meter mass measurements across fuel temperatures from 20 K to 25 K.

**Status:** Planned for LC06 (Integration & Test) phase.

---

*End of ATA 08 — Case Studies*
