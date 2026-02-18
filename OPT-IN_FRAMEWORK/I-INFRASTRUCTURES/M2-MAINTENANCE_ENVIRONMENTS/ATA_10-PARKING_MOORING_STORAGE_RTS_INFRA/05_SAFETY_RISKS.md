# ATA 10I — Parking, Mooring, Storage, and RTS Infrastructure: Safety Risks

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_10  
**Document Type:** Safety Risks and Mitigations  
**Revision:** 0.1.0

---

## 1. Purpose

This document identifies safety risks associated with parking, mooring, storage, and return-to-service operations for AMPEL360 Q100 aircraft at M2 maintenance facilities.

---

## 2. Risk Register

### 2.1 Conventional Risks

| Risk ID | Hazard | Consequence | Likelihood | Severity | Mitigation |
|---------|--------|-------------|-----------|----------|------------|
| RISK-10I-001 | Aircraft departs parking without chocks | Aircraft collision, injury | Low | Catastrophic | Double-chock procedure; chock-in-place check before crew boarding |
| RISK-10I-002 | Mooring line failure in high wind | Aircraft movement/collision | Low | Hazardous | Line rated ≥ 2× gust load; inspect before storm forecast |
| RISK-10I-003 | Ground crew struck by aircraft during parking | Fatality | Low | Catastrophic | Marshaller in control; no personnel in aircraft path |
| RISK-10I-004 | Incorrect RTS release (defect not cleared) | Air accident | Medium | Catastrophic | Part-145 approval required; deferred defect review mandatory |
| RISK-10I-005 | Aircraft damage during storage (weather) | Structural damage | Low | Major | Cover/shelter; regular inspections; storm protection plan |
| RISK-10I-006 | Corrosion damage during long-term storage | Airworthiness issue | Medium | Major | AMM preservation program; humidity control; inspection intervals |

### 2.2 ⭐ Special Condition Risks (H₂ Aircraft)

| Risk ID | Hazard | Consequence | Likelihood | Severity | Mitigation |
|---------|--------|-------------|-----------|----------|------------|
| RISK-10I-010 | ⭐ LH₂ tank overpressure during storage (BOG accumulation) | Explosion/fire, fatality | Very Low | Catastrophic | Continuous pressure monitoring; active BOG vent system; PRV with automatic venting |
| RISK-10I-011 | ⭐ H₂ leak at parking position (line fitting failure) | Explosion/fire, fatality | Very Low | Catastrophic | H₂ detectors at parking position; bonding required; no ignition sources within Zone 2 |
| RISK-10I-012 | ⭐ H₂ accumulation in hangar during storage | Explosion risk | Very Low | Catastrophic | Continuous roof-level H₂ detection; ventilation activation on alarm; evacuation plan |
| RISK-10I-013 | ⭐ H₂ aircraft parked in non-rated position | Personnel exposure to undetected H₂ | Medium | Catastrophic | H₂-rated position markings; pre-parking checklist; dispatcher approval |
| RISK-10I-014 | ⭐ Cryogenic contact during BOG line connection | Cryogenic burn | Low | Major | PPE mandatory; H₂-qualified personnel only; isolation valve confirmed before connection |
| RISK-10I-015 | ⭐ Incorrect RTS after H₂ leak event | Release of aircraft with undetected leak | Low | Catastrophic | H₂ system inspection required after any alarm event; engineering sign-off |

---

## 3. Emergency Response

### 3.1 Aircraft Movement Without Authorization

1. Alert ATC/operations if on maneuvering area.
2. Attempt to contact aircraft crew by radio.
3. Position emergency vehicles as necessary.
4. Complete incident report.

### 3.2 ⭐ LH₂ Overpressure Alert

If LH₂ pressure approaches PRV setpoint:

1. **Do not approach** aircraft until pressure stabilizes.
2. Activate emergency BOG vent (if not automatic).
3. Evacuate zone; H₂ monitors to confirm levels.
4. Notify engineering and safety department.
5. Do not restore aircraft to service until H₂ engineering assessment complete.

### 3.3 ⭐ H₂ Leak at Parking Position

1. Activate H₂ emergency alarm.
2. Evacuate all personnel from bay/zone (> 15 m from aircraft).
3. Do NOT operate any electrical switches.
4. Call emergency services with H₂ capability.
5. Ventilate using intrinsically safe fans from outside the zone.
6. Re-enter only when H₂ < 10% LEL (< 0.4% by volume).

---

## 4. PPE Requirements

### 4.1 Standard Parking Operations

| Activity | PPE |
|----------|-----|
| Ground marshalling | High-vis vest, safety shoes, hearing protection |
| Chock and mooring application | High-vis vest, safety shoes, gloves |

### 4.2 ⭐ H₂ Aircraft Operations

| Activity | Additional PPE |
|----------|---------------|
| H₂ aircraft all operations | H₂ personal gas detector |
| BOG line connection/disconnection | Cryogenic gloves, face shield |
| Any work near H₂ lines | + Cryogenic apron |

---

## 5. Regulatory References

| Regulation | Relevance |
|------------|-----------|
| EASA Part-M | Continuing airworthiness (storage programs) |
| EASA Part-145 | MRO safety and release to service |
| IATA AHM 900 | Ground handling safety |
| ATEX 2014/34/EU | ⭐ H₂ explosive atmosphere equipment |
| IECEx | ⭐ H₂ zone equipment certification |

---

## 6. Related Documents

- [ATA 10I Requirements](01_REQUIREMENTS.md)
- [ATA 10I Procedures](04_PROCEDURES.md)
- [ATA 08I Safety Risks](../ATA_08-LEVELING_AND_WEIGHING_INFRA/05_SAFETY_RISKS.md)
- [ATA 12I Safety Risks](../ATA_12-SERVICING_INFRA/05_SAFETY_RISKS.md)
