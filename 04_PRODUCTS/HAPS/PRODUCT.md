# HAPS — High Altitude Platform Station

**Path:** `04_PRODUCTS/HAPS/PRODUCT.md`  
**Authority:** ASIT  
**Status:** ACTIVE_BASELINE

---

## Purpose

This file defines the HAPS (High Altitude Platform Station) product family governed under AEROSPACEMODEL.

HAPS is a solar-electric stratospheric aircraft designed for persistent station-keeping at 18–22 km altitude. It provides telecommunications relay, Earth observation, and intelligence, surveillance and reconnaissance (ISR) services using near-zero carbon propulsion derived entirely from solar energy harvesting.

## Product Family Description

The HAPS product family covers solar-electric unmanned aerial systems operating in the stratosphere (18–22 km). Key characteristics of the platform class are:

- Ultra-high aspect ratio wing (AR > 25) serving as a solar array substrate
- Twin-boom, H-tail airframe configuration using composite materials
- Distributed electric propulsion (4× electric propellers)
- Solar cells and battery buffer for continuous day/night operation
- Payload bay supporting Communications, Electro-Optical (EO), and ISR missions

### ATA Chapter Coverage

| ATA Chapter | System | HAPS Function |
|-------------|--------|---------------|
| 51–57 | Airframe Structures | Ultra-high AR, twin-boom, composite primary structure |
| 57 | Wings | Solar array substrate, flex spar, AR > 25 |
| 24 | Electrical Power | Solar cell array, power electronics |
| 28 | Fuel System | Battery buffer, day/night cycle energy management |
| 61 | Propellers | 4× electric propeller assemblies |
| 71 | Power Plant | Distributed electric motor and controller units |
| 46 | Information Systems | Comms / EO / ISR payload integration |
| 55 | Stabilizers | Twin-boom, H-tail assembly |

## Variants

See `variants/` for product variant instances.

| Variant ID | Description | Status |
|------------|-------------|--------|
| HAPS-SE | Solar Electric baseline configuration | ACTIVE_BASELINE |

## Programmes

See `programmes/` for programme-level governance.

| Programme ID | Description | Status |
|--------------|-------------|--------|
| HAPS-SE-DEV | HAPS Solar Electric development programme | ACTIVE |

## Mission Definition Parameters

The following mission-level parameters govern the HAPS product design space and are linked to lifecycle obligations:

| Parameter | Description | Key Drivers |
|-----------|-------------|-------------|
| Endurance | Weeks to months aloft | Solar harvest, structural life, battery sizing |
| Station-keeping | Persistent position-hold | Wind field model, geofence compliance |
| Energy balance | Day/night power continuity | Solar harvest vs. electrical load |
| Payload budget | Integrated payload sizing | Mass, power, thermal envelope |
| Altitude selection | Stratospheric operating band | 18–22 km optimum for wind/solar |
| Regulatory | Spectrum and airspace compliance | ICAO gap, ITU spectrum allocation |
| Structural life | Fatigue and environmental endurance | Flutter, UV degradation, thermal cycling |
| Launch / recovery | Ground operations | Transit logistics, launch/recovery ground ops |
| Data architecture | Mission data management | Downlink capacity, latency budget |
