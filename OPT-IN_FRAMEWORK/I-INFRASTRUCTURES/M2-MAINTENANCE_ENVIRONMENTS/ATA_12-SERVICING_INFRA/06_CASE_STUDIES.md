# ATA 12I — Servicing Infrastructure: Case Studies

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_12  
**Document Type:** Case Studies and Lessons Learned  
**Revision:** 0.1.0

---

## 1. Purpose

This document captures case studies, industry references, and lessons learned relevant to servicing infrastructure, including novel hydrogen servicing technology for AMPEL360 Q100.

---

## 2. Case Study: ZEROe Ground Servicing Infrastructure Development

### Background
The Airbus ZEROe hydrogen aircraft program has published preliminary findings on ground service equipment (GSE) requirements for LH₂ aircraft. Key challenge identified: conventional airport servicing infrastructure cannot be directly adapted for cryogenic hydrogen fueling. Purpose-built LH₂ GSE requires new training, certification, and physical infrastructure not previously required at commercial airports.

### Key Findings
- LH₂ fueling takes longer than kerosene fueling for equivalent energy content.
- Cryogenic hose management (cool-down, purge) adds significant time to fueling operations.
- Ground crew must hold specialist H₂ fueling qualifications (no existing standard at time of publication).
- Airport H₂ safety zone requirements are significantly larger than kerosene refueling zones.

### ⭐ AMPEL360 Q100 Action
- 03_SERVICES.md establishes H₂ station Level C classification requiring Part-145 H₂ extension.
- 01_REQUIREMENTS.md REQ-12I-068 mandates H₂ fueling qualification for personnel.
- 04_PROCEDURES.md includes H₂ fueling procedure with cool-down and purge steps.

---

## 3. Case Study: H₂ Bus Fueling Infrastructure — Technology Transfer

### Background
The hydrogen bus industry (Ballard Power Systems, Nel ASA, ITM Power) has extensive operational experience with high-volume H₂ fueling. Key learnings transfer to aviation: bonding and grounding discipline, cryogenic hose management, and H₂ purity verification are operationally well-understood in road transport but need adaptation for aviation regulatory environment.

### Lessons Transferred
- Double-check bonding before every fueling event — static ignition is the primary risk.
- H₂ purity degradation can occur in supply chain — on-site verification required.
- Automatic leak detection with interlock (abort transfer) is standard in road transport; should be adopted for aviation.

### ⭐ AMPEL360 Q100 Action
- REQ-12I-065 mandates bonding before transfer.
- REQ-12I-071 requires purity verification per fueling event.
- 02_DESIGN_SPEC.md Section 4.3 includes automatic interlock on H₂ alarm.

---

## 4. Case Study: Ground Power Unit Failure — Aviation Industry Reference

### Background
Industry incidents have occurred where incorrectly regulated ground power units (GPU) caused avionics damage due to frequency deviation (not 400 Hz) or voltage spike. The introduction of advanced electronic aircraft systems (fly-by-wire, fuel cell management) increases sensitivity to power quality.

### Lessons Learned
- GPU output must be verified (voltage, frequency) before connecting to aircraft.
- GPU should include automatic protection (overcurrent, overvoltage, phase loss).
- Pre-connection check procedure must be mandated.

### AMPEL360 Q100 Action
- REQ-12I-003 requires GPU automatic protection.
- 04_PROCEDURES.md Section 2.2 includes GPU output verification before connection.

---

## 5. Case Study: Oxygen Servicing Fire — Industry Reference (Anonymized)

### Background
An incident at an MRO facility occurred when oxygen was dispensed using a hose that had been previously used for hydraulic fluid, causing combustion in the oxygen line. Despite labeling, the cross-contamination occurred because equipment was not physically prevented from being exchanged.

### Lesson Learned
- Physical separation of oxygen service equipment from all hydrocarbon-contaminated equipment.
- Color-coding alone is insufficient — physical coupling differences are required.
- Dedicated, sealed oxygen service equipment storage.

### AMPEL360 Q100 Action
- REQ-12I-040 mandates oxygen-clean equipment with physical incompatibility measures.
- RISK-12I-004 captures this risk with mitigation.

---

## 6. Lessons Learned Summary

| ID | Lesson | Implemented In |
|----|--------|---------------|
| LL-12I-001 | LH₂ fueling requires specialist qualification | REQ-12I-068, 03_SERVICES.md |
| LL-12I-002 | Bonding mandatory before every H₂ transfer | REQ-12I-065, 04_PROCEDURES.md |
| LL-12I-003 | H₂ purity must be verified at point of use | REQ-12I-071, 04_PROCEDURES.md |
| LL-12I-004 | Automatic H₂ leak interlock required | 02_DESIGN_SPEC.md |
| LL-12I-005 | GPU output verification before aircraft connection | REQ-12I-003, 04_PROCEDURES.md |
| LL-12I-006 | Oxygen equipment must be physically incompatible with hydrocarbon equipment | REQ-12I-040, RISK-12I-004 |

---

## 7. Related Documents

- [ATA 12I Safety Risks](05_SAFETY_RISKS.md)
- [ATA 12I Design Specifications](02_DESIGN_SPEC.md)
- [ATA 08I Case Studies](../ATA_08-LEVELING_AND_WEIGHING_INFRA/06_CASE_STUDIES.md)
- [ATA 10I Case Studies](../ATA_10-PARKING_MOORING_STORAGE_RTS_INFRA/06_CASE_STUDIES.md)
