# ATA 10 — Parking, Mooring, Storage, and RTS Infrastructure: Safety & Risk Assessment

**Section:** 6 — Safety & Risk Assessment  
**Parent:** [`README.md`](README.md) | **Crosswalk:** [`../CROSSWALK.md`](../CROSSWALK.md)

> **Escalation:** Any update to this section requires review by **STK_SAF** per BREX rule `SAFETY-002`.

---

## Hazard Identification

### H10-01 — Ground Collision During Parking / Push-Back

| Attribute | Detail |
|---|---|
| **Hazard** | Aircraft or ground vehicle collision during push-back or towing |
| **Severity** | Hazardous |
| **Probability** | Low with marshalling controls |
| **Mitigations** | Trained marshaller required; VDGS (visual docking guidance system) recommended; FOD check before entry; speed limit ≤ 5 km/h in bay |
| **Residual risk** | ALARP |

---

### H10-02 — LH₂ Leak in Enclosed Parking Bay ⭐

| Attribute | Detail |
|---|---|
| **Hazard** | H₂ leak accumulation in enclosed bay leading to explosion or asphyxiation |
| **Severity** | Catastrophic |
| **Probability** | Very Low with bay H₂ classification and controls |
| **Root causes** | Pressure relief valve open, damaged vent line, boil-off recovery line disconnection failure |
| **Mitigations** | Bay Zone 2 classification (ATEX); H₂ fixed detection (alarm at 10% LEL, evacuation at 25% LEL); forced ventilation ≥ 10 ACH; personal H₂ detectors; bonding and earthing |
| **Residual risk** | ALARP — requires STK_SAF sign-off per BREX SAFETY-H2-001 |
| **Reference** | [`../../../.github/instructions/ata28_h2_cryogenic.instructions.md`](../../../.github/instructions/ata28_h2_cryogenic.instructions.md) |

---

### H10-03 — Tie-Down / Mooring Failure in High Wind

| Attribute | Detail |
|---|---|
| **Hazard** | Aircraft breaks free of moorings in high-wind event, causing structural damage or injury |
| **Severity** | Hazardous |
| **Probability** | Low with correctly rated and inspected tie-downs |
| **Mitigations** | Tie-down rated ≥ 1.5 × MTOW wind load; pre-event inspection; weather monitoring; escalate to hangar if wind > design limit |
| **Residual risk** | ALARP |

---

### H10-04 — Fire in Parking Bay

| Attribute | Detail |
|---|---|
| **Hazard** | Fuel or H₂ leak ignition in parking bay |
| **Severity** | Catastrophic |
| **Probability** | Very Low with detection and suppression |
| **Mitigations** | H₂ and hydrocarbon detection; bonding/earthing to prevent static; no ignition sources in Zone 2 area; fire suppression system (bay-level) in enclosed hangars |
| **Residual risk** | ALARP |

---

## Emergency Procedures

### H₂ Alarm in Parking Bay
1. Sound evacuation alarm; clear bay of all personnel.
2. Do NOT operate electrical switches.
3. Contact Safety Officer.
4. Do not re-enter until H₂ < 10% LEL confirmed.
5. Notify ATA 28 responsible engineer.

### Aircraft Mooring Failure (High Wind)
1. Do not approach aircraft until wind has subsided.
2. Contact maintenance to assess structural damage.
3. Re-moor with additional tie-down sets if approved by engineer.

---

## PPE Requirements

| Hazard Zone | Required PPE |
|---|---|
| Parking bay (standard) | High-visibility vest, safety shoes |
| H₂ parking bay (LH₂ aboard) | As above + personal H₂ detector, cryogenic gloves if near vent ports |

---

*End of ATA 10 — Safety & Risk Assessment*
