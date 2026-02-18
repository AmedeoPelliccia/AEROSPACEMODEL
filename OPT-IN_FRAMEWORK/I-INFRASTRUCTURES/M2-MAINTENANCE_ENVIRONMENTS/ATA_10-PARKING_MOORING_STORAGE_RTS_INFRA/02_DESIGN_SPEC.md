# ATA 10I — Parking, Mooring, Storage, and RTS Infrastructure: Design Specifications

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_10  
**Document Type:** Design Specification  
**Revision:** 0.1.0

---

## 1. Purpose

This document specifies the design requirements for parking, mooring, storage, and RTS infrastructure facilities for the AMPEL360 Q100 aircraft.

---

## 2. Parking Position Design

### 2.1 Apron Parking Position

| Parameter | Value | Notes |
|-----------|-------|-------|
| Pavement bearing strength | PCN ≥ AMPEL360 Q100 ACN | Per ICAO Annex 14 |
| Minimum clearance to adjacent aircraft | 7.5 m (ICAO Code E) | Standard |
| H₂ aircraft clearance | 15 m (per REQ-10I-044) | ⭐ Enhanced |
| Parking position markings | Yellow, retroreflective, per ICAO Annex 14 | |
| Nose-in guidance markings | Centerline, lead-in, stop bar | |
| Electrical bonding point | At each parking position | Mandatory |

### 2.2 Hangar Parking Position

| Parameter | Value |
|-----------|-------|
| Floor clearance (aircraft to hangar structure) | ≥ 3 m each side |
| Floor surface | Concrete, minimum C30, slip-resistant |
| Hangar door width | Aircraft span + 10% |
| Overhead clearance | Aircraft tail height + 2 m minimum |

---

## 3. Tie-Down and Mooring Infrastructure

### 3.1 Apron Mooring Points

| Component | Specification |
|-----------|---------------|
| Tie-down ring type | Flush-mounted, swivel, per IATA AHM 922 |
| Load rating | ≥ 25,000 kg (250 kN) per point |
| Material | Hot-dip galvanized steel, corrosion-resistant |
| Spacing | Per aircraft footprint (nose, each wing, tail) |
| Inspection interval | 12 months or after significant gust/storm event |

### 3.2 Mooring Lines

| Component | Specification |
|-----------|---------------|
| Rope type | Polyester or nylon, per IATA/ICAO rating |
| MBL (minimum breaking load) | ≥ 2× calculated gust load per tie-down point |
| Tie-down pattern | Per AMM ATA 10 mooring diagram |

---

## 4. Storage Facility Design

### 4.1 Indoor Storage

| Parameter | Value |
|-----------|-------|
| Temperature range | 15–25°C (operational); -10 to +45°C (storage) |
| Relative humidity | < 60% RH (controlled) |
| Ventilation | Positive pressure filtered air supply |
| Lighting | 500 lux at floor level |

### 4.2 Outdoor Storage

| Parameter | Value |
|-----------|-------|
| Surface | Hard standing, sealed, drainage provisions |
| Wind load | Tie-down rated per local maximum gust |
| Cover provisions | Aircraft cover attachment points at wing tips, nose, tail |

---

## 5. ⭐ Special Condition: H₂ Aircraft Parking and Storage Design

### 5.1 H₂ Parking Position Classification

H₂ parking positions shall be classified per ATEX Directive 2014/34/EU:

| Zone | Boundary | Requirement |
|------|----------|-------------|
| Zone 2 | 3 m radius around each H₂ vent/relief point | ATEX Group IIC Rated equipment only |
| Zone 1 | Not applicable during normal parked condition | Fueling only (separate area) |
| Bonding zone | Entire aircraft footprint | Bonding cable required |

### 5.2 Boil-Off Management Infrastructure

For aircraft parked with LH₂ aboard:

| Component | Specification |
|-----------|---------------|
| BOG vent connection | Ground-side stainless steel flexible connector |
| Vent header pipe | Routed to safe outdoor vent point > 15 m from any building |
| BOG pressure monitoring | 0–10 bar, continuous, with alarm at 80% of PRV setpoint |
| Automatic isolation valve | Fail-open on BOG vent (fail-safe release) |

### 5.3 H₂ Leak Detection Coverage

| Sensor Location | Type | Alarm Threshold |
|-----------------|------|-----------------|
| 3 m height above parking position | Catalytic / Electrochemical | 10% LEL (0.4% H₂) |
| Roof/ceiling of hangar | Thermal conductivity (buoyancy-aware) | 10% LEL |
| BOG connection area | Electrochemical | 10% LEL |

### 5.4 Separation and Access Control

- ⭐ H₂ aircraft parking positions shall have physical separation barrier (minimum bollards)
- ⭐ Access to H₂ parking zone requires H₂ safety qualification
- ⭐ No open flame or unrated electrical equipment within Zone 2 at any time

---

## 6. RTS Infrastructure

### 6.1 RTS Bay Equipment

| Equipment | Purpose |
|-----------|---------|
| Ground power unit (400 Hz, 115V AC) | Aircraft system power during RTS check |
| Ground air start unit | Engine/APU start testing |
| Hydraulic ground service cart | Hydraulic system replenishment |
| Aircraft docking system | Safe access to aircraft for inspection |

### 6.2 ⭐ H₂ RTS Infrastructure

| Equipment | Purpose |
|-----------|---------|
| LH₂ tank pressure/temperature readout | Remote monitoring of H₂ system status |
| H₂ system leak test connection | For H₂ tightness check post-maintenance |
| H₂ purge gas supply (N₂) | For H₂ system purging before/after work |

---

## 7. Related Documents

- [ATA 10I Requirements](01_REQUIREMENTS.md)
- [ATA 10I Operations](03_OPERATIONS.md)
- [ATA 10I Safety Risks](05_SAFETY_RISKS.md)
- [ATA 28 H₂ Cryogenic Instructions](../../../../../.github/instructions/ata28_h2_cryogenic.instructions.md)
