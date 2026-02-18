# ATA 08I — Leveling and Weighing Infrastructure: Case Studies

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_08  
**Document Type:** Case Studies and Lessons Learned  
**Revision:** 0.1.0

---

## 1. Purpose

This document captures case studies, reference examples, and lessons learned relevant to leveling and weighing infrastructure for novel-technology aircraft maintenance environments.

---

## 2. Case Study: Conventional Aircraft — CG Shift During LH₂ Adoption

### Background
Early hydrogen aircraft programs (e.g., Airbus ZEROe feasibility studies) identified that liquid hydrogen fuel systems introduce greater weight variability than jet fuel due to the low density of LH₂ and its sensitivity to temperature. The same fuel quantity sensor reading can correspond to very different masses depending on tank temperature.

### Lesson Learned
Weight and balance computation systems must integrate real-time tank temperature and pressure data when LH₂ is the primary fuel. Traditional fuel quantity to mass conversion tables (based on constant density) are inadequate.

### ⭐ AMPEL360 Q100 Action
- REQ-08I-040 to 043 implement LH₂ density correction as a mandatory requirement.
- W&B computer design (02_DESIGN_SPEC.md Section 6) includes cryogenic temperature interface.

---

## 3. Case Study: Scale Calibration Gap — Industry Reference

### Background
Aviation industry audits have identified instances where aircraft were weighed using scales that had lapsed calibration certificates. In some cases, CG positions were recorded outside AMM limits, leading to airworthiness directives.

### Lesson Learned
- Calibration tracking must be automatic, not manual.
- Equipment should be tagged with next-due calibration date visible to operators.
- Pre-operation checklist must include explicit calibration currency check.

### AMPEL360 Q100 Action
- REQ-08I-010 to 013 require calibration traceability.
- Equipment checklist (04_PROCEDURES.md Section 2.1) includes calibration check as first item.

---

## 4. Case Study: H₂ Zone Classification for Maintenance Hangars

### Background
Several research programs (NASA, DLR) have investigated hydrogen safety zone requirements for maintenance hangars when servicing H₂ aircraft. Key finding: natural ventilation may not be sufficient to prevent H₂ accumulation in roof areas during maintenance with minor leaks.

### Lesson Learned
- Maintenance hangars accommodating H₂ aircraft must have dedicated ventilation assessment.
- Roof-mounted H₂ sensors are required due to hydrogen buoyancy.
- ATEX zone classification must be conducted by qualified safety engineer before first H₂ aircraft entry.

### ⭐ AMPEL360 Q100 Action
- Design specifications (02_DESIGN_SPEC.md Section 6.2) include weighing bay zone classification.
- Safety risks document (05_SAFETY_RISKS.md) captures H₂ accumulation risk RISK-08I-013.

---

## 5. Lessons Learned Summary

| ID | Lesson | Implemented In |
|----|--------|---------------|
| LL-08I-001 | LH₂ density must be temperature/pressure-corrected | REQ-08I-040 to 043, 02_DESIGN_SPEC.md |
| LL-08I-002 | Calibration must be tracked and pre-checked | REQ-08I-010 to 013, 04_PROCEDURES.md |
| LL-08I-003 | H₂ zone classification required for weighing bay | 02_DESIGN_SPEC.md, 05_SAFETY_RISKS.md |
| LL-08I-004 | H₂ isolation must be verified before any maintenance operations | 04_PROCEDURES.md, 05_SAFETY_RISKS.md |

---

## 6. Related Documents

- [ATA 08I Safety Risks](05_SAFETY_RISKS.md)
- [ATA 08I Design Specifications](02_DESIGN_SPEC.md)
- [ATA 12I Case Studies](../ATA_12-SERVICING_INFRA/06_CASE_STUDIES.md)
