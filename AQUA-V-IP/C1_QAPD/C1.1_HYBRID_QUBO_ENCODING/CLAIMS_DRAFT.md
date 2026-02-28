# Claims Draft — C1.1 Hybrid QUBO Encoding

**Title:** Hybrid Discrete-Continuous QUBO Encoding with Domain-Specific Aerospace Constraint Penalty Terms  
**Docket:** AQUA-V-C1.1-2026-001  
**Parent:** AQUA-V-P0-2026-001  
**Date:** 2026-02-19

---

## CLAIMS

### Independent Claim 1 — Method

**1.** A computer-implemented method for encoding an aerospace systems design problem as a Quadratic Unconstrained Binary Optimisation (QUBO) instance, the method comprising:

(a) receiving a set of design parameters for an aerospace system, wherein the design parameters comprise at least one continuous design parameter having a value in a continuous range and at least one discrete design parameter representing a selection from a finite set of options;

(b) encoding the at least one discrete design parameter as a first set of binary variables, each binary variable representing selection or non-selection of a corresponding design option;

(c) encoding the at least one continuous design parameter as a second set of binary variables forming a binary register representation of the continuous range, wherein the number of bits in the binary register is selected based on a required precision for the continuous parameter;

(d) receiving a set of domain-specific aerospace constraints comprising at least one of: a cryogenic temperature constraint specifying material structural integrity requirements at or below −253°C; a material compatibility constraint specifying compatibility of materials with hydrogen fuel systems; a Design Assurance Level (DAL) failure probability constraint derived from a safety assessment; or an aerodynamic packaging constraint specifying centre-of-gravity or volumetric bounds;

(e) constructing, for each domain-specific aerospace constraint, a quadratic penalty term over the first and second sets of binary variables, wherein equality constraints are formulated as P(x) = λ(Σ_{i=1}^N w_i x_i - C)^2 and inequality constraints are transformed using slack variables before expansion into a quadratic matrix form Σ_{i=1}^N Σ_{j=i}^N Q_ij x_i x_j, where N is a dimension of the quadratic form after any slack-variable expansion, and wherein a penalty coefficient λ for each penalty term is determined dynamically from a physical severity metric associated with the corresponding constraint; and

(f) assembling a QUBO cost matrix comprising an objective function expressed as a quadratic form over the first and second sets of binary variables, plus the sum of the constructed penalty terms, wherein the assembled QUBO instance is executable on a quantum processing unit or hybrid quantum-classical solver.

---

### Independent Claim 2 — System

**2.** A system for encoding an aerospace systems design problem as a QUBO instance, comprising one or more processors and a non-transitory memory storing instructions that when executed cause the system to perform operations comprising:
receiving discrete and continuous design parameters for an aerospace system;
encoding discrete parameters as binary categorical variables and continuous parameters as binary register variables;
receiving domain-specific aerospace constraints including at least one of cryogenic temperature, material compatibility, DAL failure probability, or aerodynamic packaging constraints;
constructing quadratic penalty terms for each constraint with physically motivated penalty coefficients; and
assembling a QUBO cost matrix combining the objective function and penalty terms.

---

### Independent Claim 3 — Computer Program Product

**3.** A non-transitory computer-readable medium storing instructions that when executed by one or more processors perform a method for encoding an aerospace systems design problem as a QUBO instance, the method comprising: receiving discrete and continuous aerospace design parameters; encoding discrete parameters as binary variables and continuous parameters as binary register representations; receiving domain-specific aerospace constraints; constructing quadratic penalty terms with physically motivated penalty coefficients; and assembling a QUBO cost matrix.

---

### Dependent Claims

**4.** The method of claim 1, wherein the aerospace system is an aircraft comprising a liquid hydrogen fuel system and the cryogenic temperature constraint specifies that materials selected for cryogenic fuel system components must maintain structural integrity at temperatures at or below −253°C, and wherein the corresponding penalty term penalises binary variable combinations that select materials not present in a pre-validated cryogenic-compatible material catalogue.

**5.** The method of claim 1, wherein the material compatibility constraint is derived from a material compatibility matrix mapping each material option to a binary compatibility indicator for each fluid or environment in the aerospace system, and wherein the penalty term penalises binary variable combinations that assign an incompatible material to a component exposed to the corresponding fluid or environment.

**6.** The method of claim 1, wherein the DAL failure probability constraint encodes an upper bound on the worst-case failure probability of the aerospace system as a function of the design variables, derived from a functional hazard assessment, and wherein the penalty coefficient is set proportional to the ratio of the failure probability bound to a target failure probability requirement.

**7.** The method of claim 1, wherein the number of bits in the binary register for a continuous design parameter is selected as the smallest integer n such that the quantisation error (x_max − x_min) / (2^n − 1) is less than a specified precision tolerance for the parameter.

**8.** The method of claim 1, further comprising generating a constraint schema record that maps each penalty term to: a reference in a technical standards document (ATA chapter, DO-178C section, CS-25 subpart, or ARP4761 section); a lifecycle phase identifier; and a regulatory authority identifier.

**9.** The method of claim 1, wherein the penalty coefficient (λ) for a cryogenic temperature constraint is dynamically calculated as a function of a coefficient-of-thermal-expansion mismatch between adjacent materials, and is increased according to an exponential function λ = λ_0·exp(k·σ_excess) when modeled thermo-mechanical stress exceeds a yield strength threshold at -253°C, where λ_0 is a baseline penalty coefficient, k is a material-dependent scaling factor, and σ_excess is stress above the yield strength threshold.

**10.** The method of claim 1, wherein penalty coefficients for safety-critical domain constraints are scaled to be greater than a maximum possible variation of the objective function, such that any physically invalid aerospace configuration corresponds to a higher QUBO energy state than a worst-performing valid configuration.

**11.** The method of claim 1, wherein the binary register encoding a continuous design parameter uses a non-linear mapping function to translate binary variables into a continuous range, such that numerical distance between adjacent binary states is non-uniform to provide higher parameter resolution proximate to critical aerospace safety thresholds and lower resolution in nominal operating regions, thereby reducing a total number of required qubits.

---

*Preliminary draft — to be reviewed by patent counsel prior to filing.*
