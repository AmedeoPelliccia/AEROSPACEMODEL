# ATA 12 — Servicing Infrastructure: Case Studies

**Section:** 7 — Case Studies  
**Parent:** [`README.md`](README.md) | **Crosswalk:** [`../CROSSWALK.md`](../CROSSWALK.md)

---

## CS-12-001 — LH₂ Servicing Cart Qualification Trial

**Context:** In preparation for first-of-type LH₂ commercial aircraft operations, a consortium of European MRO organisations and ground equipment manufacturers conducted a six-month LH₂ servicing cart qualification trial at a dedicated hydrogen test facility.

**Objectives:**
1. Validate cryogenic coupling connect/disconnect cycle life (target: ≥ 500 cycles without leak).
2. Validate in-line purity sensor accuracy against laboratory ISO 14687-2 analysis.
3. Validate boil-off recovery efficiency (target: ≥ 95% capture rate).
4. Develop and validate personnel training programme for LH₂ servicing.

**Key Results:**
- Coupling demonstrated 600 cycles without measurable leak (acceptance criterion met).
- In-line purity sensor agreed with laboratory analysis to within ±5% for CO and CO₂ (acceptance criterion met).
- Boil-off recovery achieved 97% capture rate (acceptance criterion met).
- Training programme of 8 h developed, covering cryogenic hazards, coupling procedure, emergency response, and PPE use.

**Lessons Learned:**
- Coupling ice formation at −253 °C required a thermal management cover; add to cart design specification.
- Pre-use inspection must include visual check for ice formation on hose; add to `04_PROCEDURES.md`.
- Purity sensor requires 5-min warm-up period after cold-start; add pre-fuelling wait step to procedure.

**Relevance to AMPEL360 Q100:** This trial provides the qualification evidence base for the LH₂ servicing cart specified in `02_DESIGN_SPEC.md`.

---

## CS-12-002 — Hydrogen Boil-Off Recovery System Integration at Regional Airport

**Context:** A regional airport in Norway integrated a boil-off recovery system connecting aircraft parking bays and servicing aprons to an on-site electrolytic H₂ compressor and buffer storage.

**System Architecture:**
- Aircraft fuelling bay → vacuum-jacketed boil-off return line (50 m) → heat exchanger (LH₂ → GH₂ vaporisation) → 350 bar compressor → 300 kg H₂ buffer storage.
- Buffer storage feeds the airport's hydrogen bus fleet and building heating system.

**Energy Recovery:**
- System captures ≈ 3–5% of uploaded LH₂ as boil-off gas per fuelling cycle.
- Energy recovery value: approximately €0.15/kg LH₂ fuelled (at €5/kg H₂ market price).

**Interface with M2 / ATA 12:**
- Bay-side cam-lock connection in `03_SERVICES.md` connects to this system.
- O-OPERATIONS / `ATA_IN_H2_GSE_AND_SUPPLY_CHAIN` documents the full supply-chain integration.

---

## CS-12-003 ⭐ — Proposed Full LH₂ Fuelling Validation for AMPEL360 Q100 (Concept)

**Context:** Before entry into service, the AMPEL360 Q100 LH₂ fuelling procedure requires end-to-end validation under realistic conditions. This case study documents the planned validation approach.

**Validation Scope:**
1. Full fuelling cycle (empty → nominal fuel load) at a qualified hydrogen test facility.
2. Purity verification (in-line sensor vs laboratory sample comparison across 10 fuelling cycles).
3. Boil-off capture rate measurement (flowmeter-validated).
4. Emergency stop test: simulate H₂ alarm mid-fuelling; verify cart isolation in ≤ 2 s.
5. Personnel performance assessment: timed coupling connect/disconnect under observation.

**Success Criteria:**
- Zero H₂ releases above 10% LEL during any normal fuelling cycle.
- Purity sensor accuracy within ±10% of laboratory ISO 14687-2 analysis.
- Emergency isolation in ≤ 2 s on simulated alarm.
- All personnel complete coupling procedure within 5 min unassisted.

**Status:** Planned for LC06 (Integration & Test) phase, first quarter of aircraft ground testing.

---

*End of ATA 12 — Case Studies*
