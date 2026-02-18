# ATA 12I — Servicing Infrastructure: Procedures

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_12  
**Document Type:** Operational Procedures  
**Revision:** 0.1.0

---

## 1. Purpose

This document describes the standard operating procedures for aircraft servicing operations using M2 infrastructure.

> **Note:** This document covers infrastructure procedures. Aircraft-specific servicing procedures are in the AMM (ATA 12). Facility operators must cross-reference both documents.

---

## 2. General Servicing Procedure

### 2.1 Pre-Servicing Safety Checks

Before commencing any servicing operation:

- [ ] Aircraft parking brake confirmed set / wheel chocks in place
- [ ] Bonding cable attached (mandatory before any fluid/fuel service)
- [ ] GSE positioned clear of aircraft movement path
- [ ] Required PPE identified and available
- [ ] ⭐ For H₂ aircraft: H₂ monitoring active; no ignition sources in zone

### 2.2 Ground Power Connection

1. Confirm aircraft receiving circuit breakers per AMM.
2. Connect GPU cable to aircraft ground power receptacle.
3. Power up GPU; verify correct voltage and frequency.
4. Transfer aircraft from battery to ground power per AMM ATA 24.
5. Verify aircraft systems nominal on ground power.

---

## 3. Fluid Servicing Procedures

### 3.1 Hydraulic Fluid Servicing

1. Position hydraulic service cart (correct fluid type for aircraft).
2. Connect hydraulic hose to aircraft service point (per AMM ATA 29).
3. Transfer fluid to required quantity (monitor level indicator).
4. Disconnect hose; cap service point.
5. Log: fluid type, batch number, quantity added, operator.

### 3.2 Oil Servicing (Engine/Fuel Cell Coolant)

1. Access oil filler per AMM.
2. Check level; add approved oil/coolant as required.
3. Close filler; check for leaks.
4. Log: oil type, quantity, batch number, operator.

### 3.3 Potable Water

1. Connect water hose (food-grade fitting) to aircraft water service port.
2. Fill per AMM quantity.
3. Disconnect; cap port.

---

## 4. ⭐ LH₂ Fueling Procedure

### 4.1 Pre-Fueling Safety Brief

> ⭐ **DANGER:** Liquid hydrogen at -253°C. Hydrogen is extremely flammable (4–75% in air explosive). All personnel must be qualified in H₂ fueling.

Before commencing LH₂ fueling:

- [ ] ⭐ All non-essential personnel evacuated from H₂ zone (15 m radius)
- [ ] ⭐ H₂ monitoring active; sensors responding
- [ ] ⭐ No open flames or ignition sources in zone
- [ ] ⭐ ATEX-rated equipment only in zone
- [ ] ⭐ Aircraft bonding cable attached
- [ ] ⭐ Fueling vehicle bonded and grounded
- [ ] ⭐ Emergency stop locations identified
- [ ] ⭐ PPE: H₂ gas detector, face shield, cryogenic gloves, apron

### 4.2 LH₂ Fueling Steps

| Step | Action |
|------|--------|
| 1 | Attach aircraft bonding cable; attach fueling vehicle bonding cable |
| 2 | Connect LH₂ fueling hose to aircraft fuel panel |
| 3 | Open aircraft fuel panel isolation valve per AMM ATA 28 |
| 4 | Set transfer rate on dispenser (per AMM ATA 28 max fill rate) |
| 5 | Initiate LH₂ transfer; monitor tank quantity and pressure |
| 6 | Monitor H₂ detectors throughout; stop immediately if alarm |
| 7 | Transfer to required quantity; stop transfer |
| 8 | Close aircraft isolation valve |
| 9 | Disconnect fueling hose (with hose drain/purge per AMM) |
| 10 | Cap aircraft fueling connection |
| 11 | Remove bonding cables (aircraft last) |
| 12 | Record: quantity transferred, LH₂ batch, purity cert ref, operator |

### 4.3 LH₂ Fueling Emergency Stop

If H₂ alarm activates during fueling:

1. **STOP TRANSFER** immediately (hit emergency stop button).
2. **DO NOT** disconnect any lines while H₂ is detected — risk of static spark.
3. **EVACUATE** all non-essential personnel.
4. Wait for H₂ level to fall below 10% LEL before approaching.
5. Vent and purge LH₂ hose per emergency procedure.
6. Report incident to safety officer; do not resume until cleared.

---

## 5. Post-Servicing

1. Confirm all service points closed and capped.
2. Remove all GSE from aircraft vicinity.
3. Complete servicing log (quantities, fluid types, batch numbers, operator signatures).
4. Update aircraft technical log if required.
5. ⭐ Confirm H₂ zone clear and monitoring returns to normal before departing.

---

## 6. Related Documents

- [ATA 12I Services Catalog](03_SERVICES.md)
- [ATA 12I Safety Risks](05_SAFETY_RISKS.md)
- [ATA 12I Requirements](01_REQUIREMENTS.md)
- AMM ATA 12 — Servicing Procedures (aircraft-specific)
- AMM ATA 28 — H₂ Fuel System Servicing Procedures
