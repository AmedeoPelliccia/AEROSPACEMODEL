# ATA 12I — Servicing Infrastructure: Services Catalog

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_12  
**Document Type:** Services Catalog  
**Revision:** 0.1.0

---

## 1. Purpose

This document catalogs all servicing services and associated ground support equipment (GSE) available at M2 maintenance environments for AMPEL360 Q100 aircraft.

---

## 2. Electrical Services

| Service | Equipment | Specification | Availability |
|---------|-----------|---------------|-------------|
| Ground power (AC) | 400 Hz GPU | 115/200V, 3-phase, 400 Hz, ≥ 90 kVA | All stations |
| Ground power (DC) | 28V DC power supply | 28V, ≥ 400A | All stations |
| Battery charger | Aircraft-specific charger | Per AMM ATA 24 | All stations |
| ⭐ Fuel cell system ground power | H₂-compatible GPU | Isolated from H₂ zone | ⭐ H₂-rated stations |

---

## 3. Pneumatic / Air Services

| Service | Equipment | Specification | Availability |
|---------|-----------|---------------|-------------|
| High-pressure air | Air start unit (ASU) | Per AMM ATA 80 requirements | All stations |
| Low-pressure air | Compressor cart | For system testing, purging | All stations |
| Nitrogen (inert) | N₂ cylinder cart | Aviation-grade, ≥ 99.95% | All stations |
| ⭐ H₂ system purge (N₂) | Dedicated N₂ supply | For H₂ line purge per ATA 28 | ⭐ H₂-rated stations |

---

## 4. Fluid Services

| Service | Equipment | Fluid Type | Availability |
|---------|-----------|-----------|-------------|
| Hydraulic servicing | Hydraulic cart | Per AMM ATA 29 | All stations |
| Engine oil | Oil dispenser | Per AMM ATA 72/73 | All stations |
| Potable water fill | Water cart | WHO potable standard | All stations |
| Waste water drain | Waste cart | — | All stations |
| Windshield wash | Supply cart | Per AMM | All stations |
| ⭐ Fuel cell coolant | Dedicated coolant cart | Per AMM ATA 71 | ⭐ Base maintenance |

---

## 5. ⭐ Hydrogen Fueling Services (Special Condition)

### 5.1 LH₂ Fueling

| Service | Equipment | Specification | Notes |
|---------|-----------|---------------|-------|
| ⭐ LH₂ fuel transfer | LH₂ dispenser unit | Cryogenic, vacuum-jacketed hose, aircraft coupling | H₂-rated stations only |
| ⭐ LH₂ quantity check | Aircraft fuel computer interface | — | Before and after fueling |
| ⭐ LH₂ purity verification | On-site H₂ analyzer | ISO 14687-2 compliance | Per fueling event |

### 5.2 LH₂ Defueling

| Service | Equipment | Notes |
|---------|-----------|-------|
| ⭐ LH₂ defueling | Defuel pump + recovery system | Controlled boil-off or return to storage |
| ⭐ H₂ tank purge | N₂ purge system | After defueling before maintenance |

### 5.3 Availability Classification

| Station Type | LH₂ Fueling | LH₂ Defueling | H₂ Purge | H₂ Monitoring |
|-------------|------------|--------------|---------|--------------|
| Airport line station (H₂-capable) | ✅ | ✅ | ✅ | ✅ |
| Airport line station (conventional) | ❌ | ❌ | ❌ | ❌ |
| MRO hangar (H₂-approved) | ✅ | ✅ | ✅ | ✅ |
| MRO hangar (conventional) | ❌ | ❌ | ✅ | ✅ |

> ⭐ **Note:** AMPEL360 Q100 can only be fueled/defueled at H₂-rated stations. Verify station approval before dispatch.

---

## 6. Landing Gear Services

| Service | Equipment | Specification |
|---------|-----------|---------------|
| Tire inflation | N₂ inflation cart | Aviation-grade N₂; per AMM ATA 32 tire pressure |
| Strut servicing | Strut service kit | Per AMM ATA 32 |
| Wheel/brake change | Hydraulic jack, wheel dolly | Per AMM ATA 32 |

---

## 7. Service Level Classification

| Classification | Description | Applicable Stations |
|----------------|-------------|---------------------|
| Level A | Transit servicing (power, water, basic fluids) | All operational airports |
| Level B | Full line servicing (all fluids, tire, defect clearance) | Certified line stations |
| Level C | Base maintenance servicing (all + H₂ capable) | Approved MRO with Part-145 H₂ extension |

---

## 8. Related Documents

- [ATA 12I Requirements](01_REQUIREMENTS.md)
- [ATA 12I Design Specifications](02_DESIGN_SPEC.md)
- [ATA 12I Procedures](04_PROCEDURES.md)
- [ATA 12I Safety Risks](05_SAFETY_RISKS.md)
- [O-OPERATIONS H₂ GSE Supply Chain](../../O-OPERATIONS_SERVICE_STRUCTURES/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN/)
