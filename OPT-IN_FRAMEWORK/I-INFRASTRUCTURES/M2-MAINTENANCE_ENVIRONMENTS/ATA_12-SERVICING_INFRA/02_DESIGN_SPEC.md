# ATA 12 — Servicing Infrastructure: Design Specification

**Section:** 3 — Design Specification  
**Parent:** [`README.md`](README.md) | **Crosswalk:** [`../CROSSWALK.md`](../CROSSWALK.md)

---

## Servicing Bay Design

### General Servicing Bay
- **Dimensions:** Aircraft + 4 m clearance all sides; sufficient to manoeuvre servicing carts with loaded fluid tanks.
- **Floor:** Impermeable with secondary containment bund (sill height ≥ 150 mm) to capture hydraulic fluid, water, or LH₂ condensate spills.
- **Lighting:** Minimum 300 lux at service points; ATEX-rated luminaires in LH₂ zone.
- **Drainage:** Oil-water separator on all drains; LH₂ spill management per NFPA 2 §7.

### LH₂ Fuelling Zone ⭐
- **Electrical classification:** Zone 1 (IEC 60079-10-1) within 1 m of LH₂ fuelling port; Zone 2 within 3 m.
- **Ventilation:** Minimum 15 ACH; exhaust discharge to safe outdoor vent stack.
- **H₂ detection:** Pre-alarm 10% LEL; evacuation alarm 25% LEL; minimum 6 fixed sensors per fuelling bay.
- **Bonding:** Dedicated earthing circuit for aircraft and LH₂ servicing cart; daisy-chained bonding required before coupling connection.
- **Fuelling port clearance:** 1.5 m exclusion zone marked on floor; no ignition sources within 7.5 m during fuelling.

---

## LH₂ Servicing Cart Specifications ⭐

| Parameter | Specification |
|---|---|
| Working fluid | LH₂ at −253 °C |
| Tank capacity | ≥ 500 L LH₂ (vacuum-jacketed Dewar) |
| Fill rate | ≥ 100 L/min at aircraft interface |
| Operating pressure | 0.1–0.6 MPa (gauge) at aircraft inlet |
| Hose assembly | Vacuum-jacketed, rated to −253 °C; flex hose ≤ 5 m |
| Coupling type | Bayonet cryogenic coupling, rated per SC-28-H2-001 |
| Boil-off recovery | Integrated gas return line; capacity ≥ fill rate × 5% |
| H₂ purity sensor | In-line electrochemical cell; ISO 14687-2 thresholds |
| Electrical classification | ATEX Zone 1 rated (all electrical components) |
| Bonding point | Permanent cable and clamp; resistance ≤ 1 Ω |
| Mass (loaded) | ≤ 1,200 kg (transport on standard apron tug) |

---

## Conventional Fluid Servicing Cart Specifications

| Service | Fluid | Cart Capacity | Pressure Range |
|---|---|---|---|
| Hydraulic | Skydrol LD4 / PE-5 | 50 L | 0–210 bar |
| Engine oil | OEM-approved oil | 20 L | Gravity / hand pump |
| Oxygen (crew) | Aviators breathing oxygen (BOC) | 2 × D cylinders | 1500 psi regulated |
| Nitrogen (tyre/pneumatic) | GN₂ 99.9% purity | 2 × T cylinders | 0–400 psi regulated |
| Potable water | Drinking-quality per ICAO Annex 6 | 200 L | Low-pressure gravity fill |

---

*End of ATA 12 — Design Specification*
