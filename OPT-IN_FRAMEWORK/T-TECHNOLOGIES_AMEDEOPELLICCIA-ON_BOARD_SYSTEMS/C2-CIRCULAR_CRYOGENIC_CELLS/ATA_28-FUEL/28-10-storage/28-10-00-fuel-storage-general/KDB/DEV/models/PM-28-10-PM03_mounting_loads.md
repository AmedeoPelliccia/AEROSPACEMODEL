# PM-28-10-PM03 — Mounting / Load Path Analysis

| Key | Value |
|-----|-------|
| Model ID | PM-28-10-PM03 |
| ATA Code | 28-10-00 |
| Technology Domain | C2 — Circular Cryogenic Cells |
| Aircraft Programme | AMPEL360 Q100 |
| Lifecycle Phase | LC05 (Detail Design) |
| Status | Preliminary |
| Author | STK_ENG |
| Date | 2026-02-15 |

## Objective

Define the structural analysis model for cryogenic cell mounting and
load paths.  The model evaluates vibration response, crash loads, and
thermal cycling effects on the support structure to ensure compliance
with CS 25.561 (emergency landing), CS 25.571 (fatigue and damage
tolerance), and DO-160 vibration requirements while accommodating
cryogenic thermal contraction.

---

## Analysis Policy

| Category | Description |
|----------|-------------|
| **Limit loads** | Loads expected in service; no permanent deformation (thermal cycling, normal ops) |
| **Ultimate loads** | Emergency / crash loads; structure must not fail; factor = 1.5 x limit |
| **Combined case rule** | Thermal pre-stress (LC-THERM-01) superposed algebraically with crash inertia; most conservative (max principal or vM) governs |

---

## Mass Properties

| Symbol | Name | Unit | Range / Notes |
|--------|------|------|---------------|
| $m_{\mathrm{cell}}$ | Cell total mass (filled) | kg | 200–2000; drives crash inertia |
| CG | Centre of gravity | [m, m, m] | Body-frame [x, y, z]; TBD from PM-01 |
| $I_{xx}$ | Moment of inertia (roll) | kg m^2 | About longitudinal axis |
| $I_{yy}$ | Moment of inertia (pitch) | kg m^2 | About lateral axis |
| $I_{zz}$ | Moment of inertia (yaw) | kg m^2 | About vertical axis |

> Full 3x3 inertia tensor derived from FEA mass model once PM-01 geometry frozen.
> Off-diagonal terms assumed negligible for symmetric cylindrical cell at preliminary level.

---

## CTE Parameters (Thermal Mismatch)

| Symbol | Name | Unit | Default | Description |
|--------|------|------|---------|-------------|
| $\alpha_{\mathrm{tank}}$ | Tank CTE | 1/K | 22.5E-6 | Al 5083 (293-20 K mean) |
| $\alpha_{\mathrm{mount}}$ | Mount CTE | 1/K | 11.5E-6 | Steel / composite strut |
| $\Delta T$ | Temperature excursion | K | -273 | 293 K to 20 K |
| $L_{\mathrm{span}}$ | Mount span | m | 1.0–6.0 | Fixed-to-sliding support distance |

### Thermal mismatch displacement

$$
\delta_{\mathrm{thermal}} = (\alpha_{\mathrm{tank}} - \alpha_{\mathrm{mount}}) \cdot \Delta T \cdot L_{\mathrm{span}}
$$

---

## Mount Heat Leak (PM-02 coupling)

$$
\dot Q_{\mathrm{mount}} = n_{\mathrm{mounts}} \cdot \frac{k_{\mathrm{strut}} \cdot A_{\mathrm{strut}} \cdot (T_h - T_c)}{L_{\mathrm{strut}}}
\quad [\mathrm{W}]
$$

| Symbol | Unit | Range |
|--------|------|-------|
| $n_{\mathrm{mounts}}$ | – | 3–8 |
| $k_{\mathrm{strut}}$ | W/(m K) | 0.3 (composite) – 15 (steel) |
| $A_{\mathrm{strut}}$ | m^2 | 1E-4 – 1E-2 |
| $L_{\mathrm{strut}}$ | m | 0.1–0.5 |

**Constraint:** $\dot Q_{\mathrm{mount}} \le$ allocated thermal budget (from PM-28-10-PM02).

---

## Load Cases

### Vibration

| ID | Name | Standard | Spectrum | Freq Range | Damping |
|----|------|----------|----------|------------|---------|
| LC-VIB-01 | Random vibration (flight) | DO-160G S8 | Cat S2 | 10–2000 Hz | 2% critical |
| LC-VIB-02 | Ground taxi vibration | DO-160G S8 | Cat T | 5–500 Hz | 2% critical |

> PSD breakpoints TBD — populate from DO-160G Table 8-1.

### Crash (CS 25.561)

| ID | Direction | Load Factor | Applied Force |
|----|-----------|-------------|---------------|
| LC-CRASH-01 | Forward | 9.0 g | $F = m_{\mathrm{cell}} \times 9.0 \times 9.81$ N at CG |
| LC-CRASH-02 | Downward | 6.0 g | $F = m_{\mathrm{cell}} \times 6.0 \times 9.81$ N at CG |
| LC-CRASH-03 | Lateral | 3.0 g | $F = m_{\mathrm{cell}} \times 3.0 \times 9.81$ N at CG |
| LC-CRASH-04 | Aft | 1.5 g | $F = m_{\mathrm{cell}} \times 1.5 \times 9.81$ N at CG |

### Thermal Cycling

| ID | Name | $\Delta T$ | Cycles |
|----|------|------------|--------|
| LC-THERM-01 | Cryogenic cool-down | 293 to 20 K (-273 K) | – |
| LC-THERM-02 | Mission thermal cycle | 293 to/from 20 K | 20 000 over service life |

### Combined

| ID | Name | Components | Superposition |
|----|------|------------|---------------|
| LC-COMB-01 | Crash + cryogenic | LC-CRASH-01 + LC-THERM-01 | Algebraic: thermal pre-stress + crash inertia |

---

## Mount Concepts

| ID | Name | Thermal Contraction | Crash Retention | Heritage |
|----|------|---------------------|-----------------|----------|
| MNT-A | Ring cradle + PTFE pads | Sliding interface | Shear pins + straps | LNG marine |
| MNT-B | Bipod strut frame | Bearing articulation | Strut ultimate capacity | Spacecraft cryo |
| MNT-C | Skirt / ring-frame | Bellows / flex joints | Frame shear-web | Aircraft fuselage |

### Trade Matrix

| Criterion | Weight |
|-----------|--------|
| Mass | 0.25 |
| Thermal isolation | 0.20 |
| Crash retention margin | 0.20 |
| Thermal contraction accommodation | 0.15 |
| Manufacturing complexity | 0.10 |
| Heritage / TRL | 0.10 |

Weights sum to 1.0.  Score each concept 1–5 per criterion; weighted total selects winner.

---

## Analysis Methods

| Method | Tool | Output |
|--------|------|--------|
| Modal analysis | FEA SOL 103 | Natural frequencies, mode shapes |
| Random vibration response | FEA SOL 111 | RMS stress, acceleration at mounts |
| Static crash analysis | FEA SOL 101 | Reactions, stress, margins of safety |
| Thermal stress analysis | FEA SOL 153 | Interface forces, sliding displacements |
| Fatigue & damage tolerance | Miner's rule + crack growth | Fatigue life, inspection intervals |

---

## Acceptance Criteria

| Criterion | Standard | Load Type |
|-----------|----------|-----------|
| Natural frequency > 25 Hz (mounted) | DO-160G | limit |
| Positive margin of safety — all crash cases at ultimate | CS 25.561 | ultimate |
| No yielding under limit crash loads | CS 25.305 | limit |
| Thermal cycling life >= 2x design service life | CS 25.571 | limit |
| Mount heat leak <= thermal budget (PM-02) | Thermal ICD | operational |
| No yielding — combined crash + cryogenic at limit | CS 25.305 | limit |
| No failure — combined crash + cryogenic at ultimate (1.5x) | CS 25.305 | ultimate |

---

## Outputs

| Output | Description |
|--------|-------------|
| Mount concept trade matrix | Weighted evaluation of MNT-A / MNT-B / MNT-C per criteria |
| Reaction force envelopes | Max mount forces per load case |
| Thermal displacement map | $\delta_{\mathrm{thermal}}$ at each mount station (analytical + FEA) |
| Fatigue life prediction | Cycles to crack initiation at critical locations |
| Vibration response spectra | Tank acceleration vs frequency under DO-160 |
| Mount heat leak summary | $\dot Q_{\mathrm{mount}}$ per concept vs PM-02 budget |

---

## Feeds

| Lifecycle | Artifact |
|-----------|----------|
| LC06 | Vibration and static load qualification tests |
| LC05 | Mount detail design drawings |
| LC03 | Safety FHA update — mount failure modes |

## Traceability

- **Derives from:** TS-28-10-TS01, TS-28-10-TS02, FBL-Q100-ATA28-001
- **Satisfies:** FBL-REQ-001, FBL-REQ-004, FBL-REQ-010
