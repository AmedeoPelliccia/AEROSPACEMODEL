# ATA 08I — Leveling and Weighing Infrastructure: Procedures

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_08  
**Document Type:** Operational Procedures  
**Revision:** 0.1.0

---

## 1. Purpose

This document describes the standard operating procedures for conducting aircraft weighing and leveling operations using the M2 maintenance environment infrastructure.

> **Note:** This document covers infrastructure procedures. Aircraft-specific weighing procedures are in the AMM (ATA 08). Facility operators must cross-reference both documents.

---

## 2. Preparation Procedures

### 2.1 Pre-Operation Checklist

Before commencing any weighing operation:

- [ ] Confirm weighing equipment calibration is current (within 12-month interval)
- [ ] Confirm facility floor is level (check bay-level indicator)
- [ ] Verify ambient conditions: temperature stable ±5°C, no wind/drafts
- [ ] Confirm all personnel are clear of aircraft during jack operations
- [ ] Review aircraft W&B data from last weighing record
- [ ] Confirm aircraft configuration (per AMM ATA 08) — remove/stow specified equipment

### 2.2 ⭐ H₂ Aircraft Pre-Operation (Additional Steps)

For AMPEL360 Q100 with LH₂ systems:

- [ ] ⭐ Confirm LH₂ fueling is **not** in progress and H₂ isolation valves are **closed**
- [ ] ⭐ Record LH₂ tank temperature and pressure prior to weighing
- [ ] ⭐ Distribute H₂ personal gas detectors to all personnel
- [ ] ⭐ Confirm ATEX-rated equipment only is in use within Zone 2 areas

---

## 3. Weighing Procedure

### 3.1 Aircraft Positioning

1. Tow aircraft to weighing bay per ATA 09 towing procedures.
2. Position aircraft over scale platforms.
3. Lower aircraft onto scales (remove from jacks or deflate suspension as applicable).
4. Apply wheel chocks after aircraft is on scales.
5. Confirm each wheel is centered on its respective scale platform.

### 3.2 Leveling

1. Connect inclinometer to aircraft leveling datum (per AMM ATA 08).
2. Adjust aircraft attitude using nose gear steering or jacks until longitudinal and lateral level within ±0.05°.
3. Record level readings.

### 3.3 Scale Reading

1. Allow scales to stabilize for ≥ 2 minutes after final leveling.
2. Zero scales with aircraft in final configuration (fuel as specified, equipment as specified).
3. Record readings from all three scales simultaneously.
4. Repeat readings three times; use average if variation > 0.1% of total.

### 3.4 ⭐ H₂ Fuel Compensation

For AMPEL360 Q100:

1. ⭐ Enter LH₂ tank temperature and pressure into W&B computer.
2. ⭐ W&B computer automatically computes LH₂ mass and CG correction.
3. ⭐ Verify fuel state matches aircraft fuel quantity indicator.
4. ⭐ Record corrected gross weight and CG position (% MAC).

### 3.5 Calculation and Record

1. W&B computer computes: total weight, CG position (% MAC), moments.
2. Print official W&B record including:
   - Date, time, location
   - Aircraft registration and serial number
   - Scale readings (individual and total)
   - Aircraft configuration
   - Fuel state and correction (⭐ including LH₂ density if applicable)
   - Computed CG (% MAC) and total weight
   - Operator name and qualification
   - Calibration reference numbers for equipment used

---

## 4. Post-Operation

1. Remove aircraft from scales per towing procedure.
2. Store weighing equipment in designated location.
3. Update equipment usage log.
4. File W&B record in aircraft technical records.
5. Update aircraft W&B schedule (next weighing date).

---

## 5. Calibration Verification Procedure

### 5.1 Monthly Check

1. Place certified reference weight (known mass) on each scale in turn.
2. Record displayed reading.
3. Verify accuracy within ±0.1% of reference weight.
4. Record in calibration check log.

### 5.2 Annual Full Calibration

Performed by approved calibration laboratory. Includes multi-point calibration, linearity check, repeatability assessment, and certificate issue.

---

## 6. Related Documents

- [ATA 08I Equipment Catalog](03_EQUIPMENT.md)
- [ATA 08I Safety Risks](05_SAFETY_RISKS.md)
- [ATA 08I Requirements](01_REQUIREMENTS.md)
- AMM ATA 08 — Aircraft Leveling and Weighing (aircraft-specific)
