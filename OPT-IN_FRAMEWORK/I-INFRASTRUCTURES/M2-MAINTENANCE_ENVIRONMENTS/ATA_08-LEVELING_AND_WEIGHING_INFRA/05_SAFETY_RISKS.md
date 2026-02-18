# ATA 08 — Leveling and Weighing Infrastructure: Safety & Risk Assessment

**Section:** 6 — Safety & Risk Assessment  
**Parent:** [`README.md`](README.md) | **Crosswalk:** [`../CROSSWALK.md`](../CROSSWALK.md)

> **Escalation:** Any update to this section requires review by **STK_SAF** per BREX rule `SAFETY-002`.

---

## Hazard Identification

### H08-01 — Aircraft Jack Collapse

| Attribute | Detail |
|---|---|
| **Hazard** | Hydraulic jack failure during weighing causing aircraft to fall |
| **Severity** | Catastrophic (potential aircraft damage, personnel fatality) |
| **Probability** | Low (< 1E-5 per operation with proper controls) |
| **Root causes** | Jack overload, worn seals, missing safety locks, incorrect jack placement |
| **Mitigations** | Jack rated ≥ 125% load; safety locks engaged; pre-use inspection; personnel exclusion zone under aircraft |
| **Residual risk** | ALARP |

---

### H08-02 — Exceeding Floor Load Limit

| Attribute | Detail |
|---|---|
| **Hazard** | Floor structural failure under concentrated jack load |
| **Severity** | Hazardous |
| **Probability** | Very Low with correct bay design |
| **Mitigations** | Floor capacity verified per `02_DESIGN_SPEC.md`; jack load plates to distribute load; pre-operation bay inspection |
| **Residual risk** | ALARP |

---

### H08-03 — LH₂ Spill / Leak During Weighing ⭐

| Attribute | Detail |
|---|---|
| **Hazard** | LH₂ venting or leak in enclosed weighing bay causing asphyxiation or explosion |
| **Severity** | Catastrophic |
| **Probability** | Very Low with controls in place |
| **Root causes** | Pressure relief valve activation, damaged vent line, tank overfill during weighing |
| **Mitigations** | H₂ fixed detection (alarm at 10% LEL, evacuation at 25% LEL); forced ventilation ≥ 10 ACH; bay classified Zone 2 (ATEX); LH₂ isolation valves closed before personnel enter zone; personal H₂ detectors; PPE (cryogenic gloves, face shield) |
| **Residual risk** | ALARP — requires STK_SAF sign-off per BREX SAFETY-H2-001 |
| **Reference** | [`../../../.github/instructions/ata28_h2_cryogenic.instructions.md`](../../../.github/instructions/ata28_h2_cryogenic.instructions.md) |

---

### H08-04 — Cryogenic Burn (Personnel Contact with LH₂)

| Attribute | Detail |
|---|---|
| **Hazard** | Skin or eye contact with liquid hydrogen at −253 °C causing cryogenic burns |
| **Severity** | Major |
| **Probability** | Low with correct PPE and procedures |
| **Mitigations** | Mandatory PPE (EN 511 cryogenic gloves, EN 166 face shield); personnel training on cryogenic hazards; LH₂ isolation confirmed before bay entry |
| **Residual risk** | ALARP |

---

### H08-05 — Incorrect Weight Record (Weight and Balance Error)

| Attribute | Detail |
|---|---|
| **Hazard** | Inaccurate weighing data leading to incorrect weight and balance dispatch, CG outside approved envelope |
| **Severity** | Hazardous |
| **Probability** | Low with calibrated equipment and dual verification |
| **Mitigations** | Scale calibration per ISO 17025; independent second check of all arithmetic; approved weighing report format per AC 43.13-1B; independent reviewer sign-off before filing |
| **Residual risk** | ALARP |

---

## Emergency Procedures

### H₂ Alarm During Weighing
1. Immediately alert all personnel — sound evacuation alarm.
2. Evacuate weighing bay to safe muster point (> 15 m upwind).
3. Do NOT operate electrical switches (spark risk).
4. Contact Safety Officer.
5. Do NOT re-enter bay until H₂ concentration confirmed < 10% LEL by Safety Officer using calibrated detector.
6. Notify ATA 28 (LH₂ system) responsible engineer to investigate leak source.

### Aircraft Collapse During Jacking
1. Activate emergency stop on all jacks.
2. Alert all personnel; evacuate.
3. Do not attempt to re-jack until structural inspection completed.
4. Raise incident report; notify quality and safety team.

---

## PPE Requirements Summary

| Hazard Zone | Required PPE |
|---|---|
| Weighing bay (standard) | High-visibility vest, safety shoes, hard hat |
| H₂ weighing bay (LH₂ aboard) | As above + EN 511 cryogenic gloves, EN 166 face shield, personal H₂ detector |

---

*End of ATA 08 — Safety & Risk Assessment*
