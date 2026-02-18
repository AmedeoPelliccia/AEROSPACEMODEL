# ATA 12I — Servicing Infrastructure: Safety Risks

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_12  
**Document Type:** Safety Risks and Mitigations  
**Revision:** 0.1.0

---

## 1. Purpose

This document identifies safety risks associated with aircraft servicing operations at M2 maintenance facilities, including hydrogen fueling and cryogenic servicing risks for AMPEL360 Q100.

---

## 2. Risk Register

### 2.1 Conventional Servicing Risks

| Risk ID | Hazard | Consequence | Likelihood | Severity | Mitigation |
|---------|--------|-------------|-----------|----------|------------|
| RISK-12I-001 | Hydraulic fluid contamination (wrong fluid) | System failure, aircraft unserviceability | Medium | Major | Dedicated carts per fluid type; color-coded connectors; log verification |
| RISK-12I-002 | Engine oil overfill | Engine damage | Medium | Major | Quantity limits in AMM; log fuel quantity; visual check |
| RISK-12I-003 | GPU overvoltage | Avionics damage | Low | Major | GPU with automatic overvoltage protection; verify output before connection |
| RISK-12I-004 | Oxygen contamination (grease contact) | Fire/explosion | Low | Hazardous | Oxygen-clean equipment mandatory; no hydrocarbon in O₂ area |
| RISK-12I-005 | Water contamination of fuel | Engine power loss, fuel system damage | Low | Hazardous | Sump drain before fueling; fuel quality check |
| RISK-12I-006 | GSE collision with aircraft | Structural damage, injury | Medium | Major | Speed limits in servicing area; spotters; markings |

### 2.2 ⭐ Special Condition Risks (H₂ and Cryogenic)

| Risk ID | Hazard | Consequence | Likelihood | Severity | Mitigation |
|---------|--------|-------------|-----------|----------|------------|
| RISK-12I-010 | ⭐ LH₂ leak during fueling | Explosion/fire, fatality | Very Low | Catastrophic | Emergency stop; H₂ detectors; bonding; zone exclusion; trained personnel only |
| RISK-12I-011 | ⭐ Static discharge igniting H₂ | Explosion/fire, fatality | Very Low | Catastrophic | Bonding and grounding before any H₂ operation; no synthetic clothing |
| RISK-12I-012 | ⭐ Cryogenic burn (contact with LH₂ or cold surfaces) | Cryogenic burns, frostbite | Low | Major | PPE mandatory (cryo gloves, face shield, apron); no bare skin contact with cold lines |
| RISK-12I-013 | ⭐ H₂ accumulation in fueling area | Explosion | Very Low | Catastrophic | Active ventilation; H₂ detectors (10% LEL alarm, 25% LEL shutdown); no ignition sources |
| RISK-12I-014 | ⭐ Wrong fuel type dispensed (LH₂ instead of GH₂ or vice versa) | System incompatibility, damage | Very Low | Hazardous | Aircraft-specific coupling prevents wrong connection; training |
| RISK-12I-015 | ⭐ LH₂ quality failure (contamination) | Fuel cell degradation, reduced life | Low | Major | On-site purity check per ISO 14687-2 before fueling; batch certificate required |
| RISK-12I-016 | ⭐ Asphyxiation (H₂ displaces O₂ in enclosed servicing area) | Unconsciousness, death | Very Low | Catastrophic | O₂ monitoring in all enclosed H₂ servicing areas; ventilation; confined space entry procedures |

---

## 3. Emergency Response

### 3.1 Hydraulic Fluid Spill

1. Stop dispensing immediately.
2. Apply spill kit (absorbent) to contain fluid.
3. Dispose per environmental procedures (HAZMAT).
4. Clean area; inspect for slip hazard.
5. Report to safety officer.

### 3.2 ⭐ LH₂ Spill or Major Leak

> ⭐ **DANGER — Immediate Action Required**

1. **STOP** LH₂ transfer immediately (emergency stop button).
2. **EVACUATE** all personnel from 15 m radius. Do NOT run — walk briskly.
3. Do **NOT** operate electrical switches.
4. Call emergency services — H₂ fire brigade capability required.
5. Activate facility H₂ emergency shutdown.
6. Ventilate area using intrinsically safe fans (from outside zone).
7. Do **NOT** re-enter until H₂ < 10% LEL and O₂ > 19.5%.

### 3.3 ⭐ H₂ Fire (Invisible Flame)

> ⭐ **WARNING:** Hydrogen flame is nearly invisible in daylight. Use thermal camera to detect.

1. If H₂ fire is confirmed (thermal camera, heat radiation):
   - **Evacuate** — H₂ fire with unlimited supply can cause explosion.
   - Do NOT attempt to extinguish — allow to burn if H₂ flow cannot be isolated.
2. Isolate H₂ supply from safe distance (remote emergency valve if available).
3. Cool adjacent surfaces with water spray to prevent structure fire.
4. Emergency services: Fire brigade with H₂ capability.

### 3.4 ⭐ Cryogenic Contact

1. Remove cold material from skin immediately (shake off LH₂ — do not wipe).
2. Do NOT rub affected area.
3. Rewarm with lukewarm water (37–41°C); do NOT use hot water.
4. Seek medical attention immediately.
5. Emergency eyewash if eyes affected.

---

## 4. PPE Requirements

### 4.1 Standard Servicing Operations

| Activity | PPE |
|----------|-----|
| GPU connection | Safety shoes, high-vis vest |
| Hydraulic servicing | Safety shoes, high-vis vest, splash goggles |
| Oxygen servicing | Oil-free gloves, face shield, no synthetic clothing |

### 4.2 ⭐ H₂ Servicing Operations

| Activity | PPE |
|----------|-----|
| All H₂ area operations | + H₂ personal gas detector (worn, alarm at 10% LEL) |
| LH₂ hose connection/disconnection | + Cryogenic gloves, face shield, apron |
| LH₂ tank/system work | + Cryogenic apron, safety shoes (cryogenic-rated) |
| Enclosed H₂ spaces | + O₂ monitor |

---

## 5. Regulatory References

| Regulation | Relevance |
|------------|-----------|
| EASA Part-145 | MRO safety and approved maintenance |
| ATEX 2014/34/EU | ⭐ Electrical equipment in H₂ explosive atmosphere |
| IECEx | ⭐ International H₂ zone equipment certification |
| NFPA 2 | ⭐ Hydrogen Technologies Code — fueling safety |
| ISO 14687-2 | ⭐ Hydrogen fuel quality — purity requirements |
| IATA DGR | Dangerous goods regulations (O₂, H₂) |

---

## 6. Related Documents

- [ATA 12I Requirements](01_REQUIREMENTS.md)
- [ATA 12I Procedures](04_PROCEDURES.md)
- [ATA 08I Safety Risks](../ATA_08-LEVELING_AND_WEIGHING_INFRA/05_SAFETY_RISKS.md)
- [ATA 10I Safety Risks](../ATA_10-PARKING_MOORING_STORAGE_RTS_INFRA/05_SAFETY_RISKS.md)
- [ATA 28 H₂ Cryogenic Instructions](../../../../../.github/instructions/ata28_h2_cryogenic.instructions.md)
