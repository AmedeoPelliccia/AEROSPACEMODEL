# AI Training Material — ATA 28-11-00 LH₂ Primary Tank

AI Training Material (AIT) package for training AEROSPACEMODEL ASI — the AI system orchestrating digital production from design generation through certification evidence compilation.

## Scope

This AIT package structures the MTL-28-11-00 token library as training material for AI models that will execute, validate, and govern LH₂ cryogenic tank engineering procedures in production. The package trains AI on the identical token structures (MTK subject tokens, MTP process tokens, STP standard procedures) that the AI will orchestrate in live operations.

Training progresses through six layers:
1. **Domain Knowledge (L1)**: First-principles cryogenic physics and materials science
2. **Method Execution (L2)**: Closed-form calculations and empirical correlations
3. **Procedural Composition (L3)**: End-to-end standard procedures with token orchestration
4. **Acceptance Logic (L4)**: Gate evaluation and decision boundaries
5. **Failure Mode Recognition (L5)**: Anomaly detection and disposition
6. **Production Governance (L6)**: Optimization under constitutional constraints

## Lifecycle State

**DEV** — Not baselined. Subject to change during LC04 preliminary design phase.

## Owner

**STK_ENG** (Engineering Stakeholder)

## Constitution

**AEROSPACEMODEL-MDC v1.0.0**

Applicable constitutional articles:
- **A4**: Data Provenance — All training examples provenance-linked to source MTL tokens
- **A5**: Explainability — All AI decisions explainable through token audit trail
- **A6**: Safety Guardrails — Harm-sensitive decisions require human oversight
- **A8**: Labor Continuity — AI augments, does not replace, human expertise
- **A10**: Constitutional Supremacy — Constitutional constraints override optimization objectives
- **A11**: Transparency — Full audit trail of AI decisions

**Key governance note**: Autonomous actuation is DENIED by default. Promotion to SSOT requires deterministic validation + constitutional controls pass.

## Contents

| File | Description | Version | Status |
|------|-------------|---------|--------|
| AIT-28-11-00-ai-training-material.yaml | Complete AI training material package with 6 training layers, 6 datasets (DS-01 to DS-06), governance controls, and promotion criteria | 0.1.1 | DEV |

## Promotion Criteria (Definition of Done)

Package is promotion-ready when ALL of the following gates pass:

| Gate | Requirement | Validation Method |
|------|-------------|-------------------|
| PC-01 | 100% DS examples signed and provenance-linked to MTL tokens | Automated: all provenance.source_token_id exist in MTL |
| PC-02 | Numeric verification error within declared tolerance for all MTP methods | Automated: run DS-02 examples, verify ±0.5% accuracy |
| PC-03 | STP replay deterministic across repeated runs (same inputs → same outputs) | Automated: replay DS-03 examples 10x, verify bit-identical outputs |
| PC-04 | Constitutional controls enforced (A4/A5/A6/A8/A10/A11) | Manual review: verify governance section implementation |
| PC-05 | Version lock enforced (ASI == MTL) with automatic HOLD on mismatch | Automated: verify model_lock policy implementation |
| PC-06 | Human oversight path validated for all harm-sensitive branches | Manual review: verify escalation routes for safety gates |
| PC-07 | Labor continuity constraints validated for optimization actions | Manual review: verify DS-06 examples satisfy labor continuity policy |

## Dependencies

This AIT package depends on and derives from:

- **MTL-28-11-00** (Method Token Library — subject tokens)
- **MTL-28-11-00-PROC** (Process and Scaling Method Tokens)
- **STP-28-11-00** (Standard Token Procedures)
- **SSOT_POLICY.md** (SSOT promotion policy at ATA 28-00-00)
- **KDB_IDB_PARTITION.md** (KDB/IDB partition rules at ASIT/STRUCTURE)

## Naming Convention

`AIT-28-{SS}-{NN}_{topic}.yaml`

Where:
- `{SS}` = ATA sub-system code (e.g., "11" for LH₂ primary tank)
- `{NN}` = Sequential identifier (e.g., "00" for general)
- `{topic}` = Descriptive slug (e.g., "ai-training-material")

## Training Architecture

### Layer 1: Domain Knowledge
**Source**: MTK-28-11-TS-*, MTK-28-11-CM-*, MTK-28-11-SC-*, MTK-28-11-EC-*  
**Objective**: Master first-principles cryogenic physics, materials science at 20K, boil-off thermodynamics  
**Dataset**: DS-01 (reasoning chains)

### Layer 2: Method Execution
**Source**: MTP-28-11-GEOM-*, MTP-28-11-THRM-*, MTP-28-11-MATL-*, MTP-28-11-CERT-*, MTP-28-11-EVAL-*  
**Objective**: Execute geometric sizing, thermal analysis, material selection with numerical precision  
**Dataset**: DS-02 (calculation verification)

### Layer 3: Procedural Composition
**Source**: STP-28-11-001 through STP-28-11-005  
**Objective**: Orchestrate multi-step procedures with deterministic sequencing and full audit trail  
**Dataset**: DS-03 (procedural execution traces)

### Layer 4: Acceptance Logic
**Source**: Acceptance gates from STP procedures, RTM-*, CERT-*  
**Objective**: Evaluate pass/fail gates, trigger escalations, maintain traceability  
**Dataset**: DS-04 (boundary classification)

### Layer 5: Failure Mode Recognition
**Source**: RTM-28-11-*, CERT-28-11-*, failure modes from compliance matrix  
**Objective**: Detect anomalies, classify failure modes, recommend disposition  
**Dataset**: DS-05 (anomaly reasoning)

### Layer 6: Production Governance
**Source**: PAL-28-11-*, production metrics, optimization constraints  
**Objective**: Optimize throughput/quality under constitutional and safety constraints  
**Dataset**: DS-06 (production governance with RL constraints)

## AI Capabilities After Training

1. **Autonomous Design Generation** (C1) — Generate preliminary tank designs from mission requirements
2. **Real-Time Gate Evaluation** (C2) — Evaluate acceptance gates with 100% accuracy and escalation routing
3. **Anomaly Detection & Disposition** (C3) — Detect deviations, classify failure modes, recommend disposition
4. **Production Optimization** (C4) — Optimize production parameters under constitutional constraints
5. **Certification Evidence Compilation** (C5) — Compile certification packages with requirement traceability
6. **Self-Validation** (C6) — Detect model drift and trigger retraining when performance degrades

## Version Lock Policy

AI model version MUST match token library version:
- **Format**: `ASI-{MTL_version}-{training_stage}`
- **Example**: `ASI-0.1.0-stage_6`
- **Enforcement**: Hard lock with automatic HOLD on version mismatch
- **Rationale**: Prevents AI from consuming token structures it wasn't trained on

## Continuous Learning

Production feedback loops enable model improvement:
- **Production line sensor data** → DS-05 (new failure modes)
- **NDE inspection results** → DS-04, DS-05 (gate validation, anomaly detection)
- **Acceptance gate outcomes** → DS-04 (gate waiver decisions)
- **Engineering design changes (ECRs)** → DS-01, DS-02, DS-03 (baseline updates)

All continuous learning updates require human-in-the-loop labeling, validation, and approval before deployment.

## Reference Values

LH₂ physical properties used throughout training:
- **Density**: 70.8 kg/m³ (at saturation, ~20 K, 1 atm)
- **Latent heat of vaporization**: 445.5 kJ/kg
- **Saturation temperature**: 20.3 K (at 1 atm)

## Constitutional Constraints

### Governance
- **Enforcement mode**: Deny by default
- **Autonomous actuation**: DENIED without explicit enablement
- **Enablement requires**: SSOT token set + human authorizer + evidence sink + version lock pass

### Safety
- **Uncertainty action**: DEGRADE → PAUSE → ESCALATE
- **Harm-sensitive decisions**: Require human oversight
- **Prohibited**: Unbounded stochastic execution, silent gate overrides

### Labor Continuity
- **Net human exclusion**: DENIED
- **Role shifts**: Require documented reabsorption plan
- **Optimization**: Must augment human expertise, not replace it

## Traceability

This AIT package feeds into downstream lifecycle artifacts:
- **LC05**: Parametric model pipelines (each STP = one model entry point)
- **LC06**: Verification test sequences (each STP = one test procedure)
- **LC08**: S1000D procedural data modules (each STP = one DM procedure)
- **LC09**: Manufacturing work instructions (robotics line execution)
- **LC10**: MRO repair procedures (AEROSPACEROBOTICS)

## Status

**Current**: DEV (preliminary)  
**Next gate**: LC04 preliminary design review  
**Promotion path**: DEV → SSOT (via ECR approval + all 7 promotion criteria gates pass)

---

*Last updated: 2026-02-16*
