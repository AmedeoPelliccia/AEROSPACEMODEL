# ATA 08I — Leveling and Weighing Infrastructure: Safety Risks

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_08  
**Document Type:** Safety Risks and Mitigations  
**Revision:** 0.1.0

---

## 1. Purpose

This document identifies safety risks associated with leveling and weighing operations for AMPEL360 Q100 aircraft at M2 maintenance facilities, and defines risk mitigations.

---

## 2. Risk Register

### 2.1 Conventional Risks

| Risk ID | Hazard | Consequence | Likelihood | Severity | Mitigation |
|---------|--------|-------------|-----------|----------|------------|
| RISK-08I-001 | Aircraft falls from jack during weighing | Fatality, aircraft structural damage | Low | Catastrophic | Jack rated ≥2× load; safety collars; no personnel under aircraft; jack pads per AMM |
| RISK-08I-002 | Incorrect W&B data recorded (scale error) | Operational overweight/CG exceedance | Medium | Hazardous | Calibrated equipment; triple reading; independent verification |
| RISK-08I-003 | Aircraft rolls off scale platforms | Aircraft damage, personnel injury | Low | Major | Wheel chocks applied before scale reading; level bay floor |
| RISK-08I-004 | Operator error in CG computation | Wrong CG datum used; flight safety risk | Medium | Hazardous | W&B computer validation; independent manual check; AMM reference |
| RISK-08I-005 | Equipment damage (scale overload) | Equipment destruction, delayed operation | Low | Minor | Scale capacity checked before use; overload protection on scales |
| RISK-08I-006 | Personnel struck by moving aircraft | Injury | Low | Major | Tow crew safety briefing; spotters; stop signals |

### 2.2 ⭐ Special Condition Risks (H₂ Aircraft)

| Risk ID | Hazard | Consequence | Likelihood | Severity | Mitigation |
|---------|--------|-------------|-----------|----------|------------|
| RISK-08I-010 | ⭐ LH₂ leak during weighing (isolation valve failure) | H₂ explosion, fire, fatality | Very Low | Catastrophic | H₂ isolation verified closed before operations; H₂ gas detectors; evacuation plan |
| RISK-08I-011 | ⭐ Incorrect LH₂ mass computation (wrong density) | CG error, flight safety risk | Medium | Hazardous | W&B computer uses validated NIST density tables; tank T&P inputs mandatory |
| RISK-08I-012 | ⭐ Cryogenic contact (accidental LH₂ exposure) | Cryogenic burn, frostbite | Very Low | Major | H₂ lines isolated during weighing; cryogenic PPE available; no LH₂ transfer during operation |
| RISK-08I-013 | ⭐ H₂ accumulation in weighing bay | Explosion risk | Very Low | Catastrophic | H₂ detectors in bay; ATEX equipment; ventilation active; no H₂ work during weighing |

---

## 3. Emergency Response

### 3.1 Aircraft Jack Collapse

1. **Evacuate** all personnel from aircraft vicinity immediately.
2. Prevent access to collapsed aircraft — structural instability risk.
3. Call emergency services if personnel injured.
4. Notify Quality Assurance and Safety Officer.
5. Do not attempt to re-jack until structural assessment complete.

### 3.2 ⭐ H₂ Leak Detection During Weighing

If H₂ alarm activates:

1. **STOP** all operations immediately.
2. **EVACUATE** all non-essential personnel from the bay.
3. Do **NOT** operate electrical switches (ignition source risk).
4. Activate facility H₂ emergency shutdown (isolation of H₂ supply).
5. Ventilate bay using intrinsically safe fans.
6. Call emergency services (fire brigade with H₂ capability).
7. Do not re-enter until H₂ concentration < 10% LEL (< 0.4% H₂ by volume).

---

## 4. Personal Protective Equipment (PPE)

### 4.1 Standard Operations

| Activity | Minimum PPE |
|----------|-------------|
| Towing aircraft into bay | High-vis vest, safety shoes |
| Jack operations | High-vis vest, safety shoes, hard hat |
| Scale operations | High-vis vest, safety shoes |

### 4.2 ⭐ H₂ Aircraft Operations

| Activity | Minimum PPE |
|----------|-------------|
| All H₂ aircraft weighing | + H₂ personal gas detector |
| If near exposed cryogenic lines | + Cryogenic gloves, face shield, apron |

---

## 5. Regulatory References

| Regulation | Relevance |
|------------|-----------|
| EASA Part-145 Safety Management | MRO safety management system |
| IATA Ground Operations Manual | Aircraft ground handling safety |
| ATEX Directive 2014/34/EU | ⭐ Equipment in explosive atmospheres (H₂ zones) |
| IECEx | ⭐ International H₂ zone classification |

---

## 6. Related Documents

- [ATA 08I Requirements](01_REQUIREMENTS.md)
- [ATA 08I Procedures](04_PROCEDURES.md)
- [ATA 12I Safety Risks (H₂ Servicing)](../ATA_12-SERVICING_INFRA/05_SAFETY_RISKS.md)
