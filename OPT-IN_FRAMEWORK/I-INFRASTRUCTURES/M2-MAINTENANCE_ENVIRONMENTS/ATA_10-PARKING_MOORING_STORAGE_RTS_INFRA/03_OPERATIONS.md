# ATA 10I — Parking, Mooring, Storage, and RTS Infrastructure: Operations

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_10  
**Document Type:** Operational Standards  
**Revision:** 0.1.0

---

## 1. Purpose

This document defines the operational standards for parking, mooring, storage, and return-to-service activities using M2 maintenance environment infrastructure. It supplements aircraft AMM procedures with facility-level requirements.

---

## 2. Parking Operations

### 2.1 Nose-In Parking (Standard)

| Step | Action | Facility Infrastructure Used |
|------|--------|------------------------------|
| 1 | Marshaller positions aircraft on centerline | Parking guidance markings |
| 2 | Aircraft stops at designated stop bar | Stop bar marking / VDGS system |
| 3 | Wheel chocks applied (nose + main) | Chock set from equipment store |
| 4 | Bonding cable attached | Bonding point at parking position |
| 5 | Ground power connected | GPU at parking position |
| 6 | Safety cones/barriers placed (if needed) | From ground handling equipment store |

### 2.2 Pushback Parking (Nose-Out)

| Step | Action | Facility Infrastructure Used |
|------|--------|------------------------------|
| 1 | Tow tractor connected | Tow bar from equipment store |
| 2 | Aircraft pushed to position | Parking guidance markings |
| 3 | Tow bar disconnected | Return to store |
| 4 | Wheel chocks applied | Chock set |
| 5 | Bonding cable attached | Bonding point |

---

## 3. Mooring Operations

### 3.1 Apron Mooring (Overnight / Weather)

Mooring shall be applied when forecast or actual wind exceeds operating limit:

| Condition | Action |
|-----------|--------|
| Wind forecast > 40 kt | Apply full mooring per AMM ATA 10 |
| Gust > 50 kt | Apply storm mooring (additional tie-down points) |
| Aircraft unattended > 8 hours | Apply standard mooring |

### 3.2 Mooring Equipment Release

| Step | Action |
|------|--------|
| 1 | Confirm departure clearance and weather within limits |
| 2 | Remove tie-down lines in reverse order of application |
| 3 | Stow all mooring equipment in designated store |
| 4 | Remove bonding cable as final step |

---

## 4. Storage Operations

### 4.1 Short-Term Storage (≤ 30 days)

| Frequency | Action |
|-----------|--------|
| Entry | Apply storage configuration per AMM ATA 10 |
| Daily | Visual check for obvious damage or leaks |
| Weekly | Battery charge check; external condition |
| On removal | RTS inspection per 04_PROCEDURES.md |

### 4.2 Long-Term Storage (> 30 days)

| Activity | Interval | Notes |
|----------|----------|-------|
| Full aircraft inspection | Monthly | Per Part-145 approval |
| Corrosion inhibitor check | Per AMM | Engine, landing gear, etc. |
| System exercising | Per AMM | Control surfaces, landing gear |
| Battery replacement/conditioning | Per AMM | |
| ⭐ LH₂ system defuel | Before entry to long-term | REQ-10I-046 |

---

## 5. ⭐ H₂ Aircraft Parking Operations

### 5.1 Arrival to H₂ Parking Position

On arrival at an H₂-rated parking position:

1. ⭐ Confirm parking position is H₂-rated (placard/marking).
2. ⭐ Attach aircraft bonding cable before any other connection.
3. ⭐ Connect BOG vent line if aircraft will be parked > 2 hours with LH₂ aboard.
4. ⭐ Activate H₂ monitoring in bay (confirm detectors are operational).
5. Proceed with standard parking steps.

### 5.2 LH₂ Tank Monitoring During Storage

| Interval | Action |
|----------|--------|
| Every 12 hours | Read LH₂ tank pressure; confirm < 80% of PRV setpoint |
| If pressure rising | Confirm BOG vent is active; escalate to engineering if pressure exceeds 80% PRV |
| Every 72 hours | Full LH₂ system status check per AMM ATA 28 |

### 5.3 ⭐ H₂ Departure Operations

Before aircraft departs H₂ parking position:

1. ⭐ Disconnect BOG vent line with H₂ isolation confirmed closed.
2. ⭐ Check H₂ levels in bay are < 10% LEL before disconnecting any lines.
3. ⭐ Remove bonding cable as final step.
4. Confirm all ground equipment cleared from H₂ zone.

---

## 6. Return to Service (RTS) Operations

### 6.1 RTS After Short-Term Storage

RTS check shall include as minimum:
- [ ] Aircraft exterior visual inspection
- [ ] Ground safety pin/flag status check (remove for flight)
- [ ] Fuel quantity check (conventional + ⭐ LH₂ pressure/temperature)
- [ ] Ground power connection test
- [ ] Walk-around per AMM pre-flight scope
- [ ] Release to service signed by Part-145 approved person

### 6.2 ⭐ H₂ RTS Specific Actions

- [ ] ⭐ LH₂ tank pressure and temperature within operating limits
- [ ] ⭐ No H₂ leak indications on sensors
- [ ] ⭐ BOG vent line disconnected and capped
- [ ] ⭐ H₂ isolation valves confirmed operational

---

## 7. Related Documents

- [ATA 10I Requirements](01_REQUIREMENTS.md)
- [ATA 10I Design Specifications](02_DESIGN_SPEC.md)
- [ATA 10I Procedures](04_PROCEDURES.md)
- [ATA 10I Safety Risks](05_SAFETY_RISKS.md)
