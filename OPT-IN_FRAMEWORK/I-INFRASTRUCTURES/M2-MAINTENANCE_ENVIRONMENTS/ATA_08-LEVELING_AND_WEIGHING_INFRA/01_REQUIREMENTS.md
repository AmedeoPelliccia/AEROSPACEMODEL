# ATA 08I — Leveling and Weighing Infrastructure: Requirements

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_08  
**Document Type:** Normative Requirements  
**Revision:** 0.1.0

---

## 1. General Requirements

### 1.1 Purpose

This document defines normative requirements for leveling and weighing infrastructure used to support AMPEL360 Q100 weight and balance operations at all maintenance facilities.

### 1.2 Applicability

These requirements apply to:
- Maintenance, Repair, and Overhaul (MRO) organizations holding Part-145 approval
- Manufacturer's final assembly line (FAL) facility
- Line maintenance stations performing scheduled weight checks

---

## 2. Regulatory Requirements

### 2.1 Certification Basis

| Requirement | Source | Description |
|-------------|--------|-------------|
| REQ-08I-001 | CS-25.25 | Maximum weights must be established for the aircraft |
| REQ-08I-002 | CS-25.1519 | Weight and CG must be recorded in the Airplane Flight Manual |
| REQ-08I-003 | EASA Part-145 | MRO facilities must have calibrated weighing equipment |
| REQ-08I-004 | CAT.POL.A.100 | Mass and balance data must be maintained per approved procedures |

### 2.2 Equipment Calibration

| Requirement | Description |
|-------------|-------------|
| REQ-08I-010 | All weighing equipment shall be calibrated to traceable national standards (ISO/IEC 17025) |
| REQ-08I-011 | Calibration interval shall not exceed 12 months or after any repair/modification |
| REQ-08I-012 | Calibration records shall be retained for a minimum of 5 years |
| REQ-08I-013 | Equipment accuracy shall be within ±0.05% of full-scale reading |

---

## 3. Facility Requirements

### 3.1 Hangar/Workspace

| Requirement | Description |
|-------------|-------------|
| REQ-08I-020 | Weighing area shall be level to within ±0.05° in any direction |
| REQ-08I-021 | Facility shall be wind-protected (enclosed or with appropriate shielding) |
| REQ-08I-022 | Floor load capacity shall exceed maximum aircraft ramp weight by ≥25% margin |
| REQ-08I-023 | Ambient temperature shall be stable within ±5°C during weighing operations |

### 3.2 Leveling Infrastructure

| Requirement | Description |
|-------------|-------------|
| REQ-08I-030 | Leveling system shall achieve ±0.05° accuracy |
| REQ-08I-031 | Jack pad locations shall conform to aircraft maintenance manual (AMM) specifications |
| REQ-08I-032 | Jacks shall be rated for combined aircraft weight with ≥2:1 safety factor |

---

## 4. Novel Technology Requirements

### 4.1 ⭐ Special Condition: Hydrogen Fuel State Compensation

For AMPEL360 Q100 aircraft with LH₂ cryogenic fuel systems:

| Requirement | Description |
|-------------|-------------|
| REQ-08I-040 | ⭐ Weight and balance computation system shall account for LH₂ fuel density variation with temperature |
| REQ-08I-041 | ⭐ LH₂ tank pressure and temperature sensors shall be integrated with weight computation |
| REQ-08I-042 | ⭐ Weighing procedures shall specify fuel state (full, empty, or known partial) |
| REQ-08I-043 | ⭐ CG computation shall include correction factor for cryogenic fuel mass vs. indicated quantity |
| REQ-08I-044 | ⭐ Maintenance personnel performing weight checks on H₂ aircraft shall hold H₂ safety qualification |

---

## 5. Traceability

| Requirement | Cross-Reference | Lifecycle Phase |
|-------------|----------------|-----------------|
| REQ-08I-001 to 004 | CS-25, EASA Part-145 | LC04, LC08 |
| REQ-08I-010 to 013 | ISO/IEC 17025 | LC04, LC10 |
| REQ-08I-020 to 023 | AMM Section 08 | LC04, LC06 |
| REQ-08I-040 to 044 | ATA 28 (H₂ systems), SC-28-H2-001 | LC04, LC08 |

---

## 6. Related Documents

- [ATA 08I README](README.md)
- [ATA 08I Design Specifications](02_DESIGN_SPEC.md)
- [ATA 08I Safety Risks](05_SAFETY_RISKS.md)
- [P-PROGRAMS ATA 08 Procedures](../../../P-PROGRAMS/P-PRODUCT_DEFINITION/ATA_08-LEVELING_AND_WEIGHING/)
