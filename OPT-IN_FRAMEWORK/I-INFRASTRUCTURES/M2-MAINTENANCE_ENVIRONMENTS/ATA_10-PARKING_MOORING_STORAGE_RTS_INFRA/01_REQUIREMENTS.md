# ATA 10I — Parking, Mooring, Storage, and RTS Infrastructure: Requirements

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_10  
**Document Type:** Normative Requirements  
**Revision:** 0.1.0

---

## 1. General Requirements

### 1.1 Purpose

This document defines normative requirements for parking, mooring, storage, and return-to-service infrastructure for AMPEL360 Q100 operations.

### 1.2 Applicability

These requirements apply to:
- Aircraft operators and handling agents at all operational airports
- MRO facilities providing storage services
- Line maintenance organizations performing RTS checks

---

## 2. Regulatory Requirements

### 2.1 Certification and Operational

| Requirement | Source | Description |
|-------------|--------|-------------|
| REQ-10I-001 | ICAO Annex 14 | Apron design shall meet ICAO aerodrome code standards |
| REQ-10I-002 | EASA Part-M | Aircraft in storage shall have valid continuing airworthiness |
| REQ-10I-003 | IATA AHM 900 | Ground handling shall conform to IATA AHM standards |
| REQ-10I-004 | EASA Part-145 | RTS inspection shall be performed by approved organization |

### 2.2 Tie-Down and Mooring

| Requirement | Description |
|-------------|-------------|
| REQ-10I-010 | Tie-down points shall meet aircraft MTOW × 2.5g load requirement |
| REQ-10I-011 | Mooring lines shall be rated for maximum gust load per local weather criteria |
| REQ-10I-012 | Chocks shall prevent aircraft movement in winds up to VFR operating limits |
| REQ-10I-013 | Ground attachment points shall be tested per EN 13796 or equivalent |

---

## 3. Storage Requirements

### 3.1 Short-Term Storage (≤ 30 days)

| Requirement | Description |
|-------------|-------------|
| REQ-10I-020 | Aircraft shall be parked per AMM ATA 10 parking procedure |
| REQ-10I-021 | Wheel chocks shall be applied at all times |
| REQ-10I-022 | Ground safety pins shall be installed per AMM |
| REQ-10I-023 | Aircraft shall be inspected at intervals per operator storage program |

### 3.2 Long-Term Storage (> 30 days)

| Requirement | Description |
|-------------|-------------|
| REQ-10I-030 | Storage environment shall maintain temperature and humidity within AMM limits |
| REQ-10I-031 | Aircraft shall be placed in approved storage configuration per AMM ATA 10 |
| REQ-10I-032 | Corrosion prevention measures shall be applied per AMM |
| REQ-10I-033 | Battery condition monitoring shall be maintained during storage |

---

## 4. Novel Technology Requirements

### 4.1 ⭐ Special Condition: H₂ Aircraft Storage

For AMPEL360 Q100 aircraft with LH₂ cryogenic fuel systems:

| Requirement | Description |
|-------------|-------------|
| REQ-10I-040 | ⭐ Aircraft stored with LH₂ aboard shall be parked in H₂-rated parking position only |
| REQ-10I-041 | ⭐ LH₂ tank pressure monitoring shall be continuous during storage (max 72-hr check interval) |
| REQ-10I-042 | ⭐ Boil-off gas (BOG) management system shall be active during all LH₂ storage periods |
| REQ-10I-043 | ⭐ H₂ parking positions shall be classified per ATEX/IECEx Zone 2 requirements |
| REQ-10I-044 | ⭐ Minimum separation distance from H₂ aircraft to other aircraft: 15 m |
| REQ-10I-045 | ⭐ H₂ leak detection coverage shall extend to entire parking footprint |
| REQ-10I-046 | ⭐ Long-term storage of H₂ aircraft shall require defueling of LH₂ system if storage > 7 days |

---

## 5. RTS Infrastructure Requirements

| Requirement | Description |
|-------------|-------------|
| REQ-10I-050 | RTS facility shall provide access to all aircraft inspection zones |
| REQ-10I-051 | Ground power and pneumatic support shall be available for RTS checks |
| REQ-10I-052 | RTS inspection documentation shall be completed by Part-145 approved personnel |
| REQ-10I-053 | ⭐ H₂ aircraft RTS shall include LH₂ system pressure/temperature check |

---

## 6. Traceability

| Requirement | Cross-Reference | Lifecycle Phase |
|-------------|----------------|-----------------|
| REQ-10I-001 to 004 | ICAO Annex 14, EASA Part-M/145 | LC04, LC08 |
| REQ-10I-010 to 013 | AMM ATA 10 | LC04, LC06 |
| REQ-10I-040 to 046 | ATA 28 H₂ Systems, SC-28-H2-001 | LC04, LC08 |
| REQ-10I-050 to 053 | EASA Part-145 | LC04, LC12 |

---

## 7. Related Documents

- [ATA 10I README](README.md)
- [ATA 10I Design Specifications](02_DESIGN_SPEC.md)
- [ATA 10I Safety Risks](05_SAFETY_RISKS.md)
