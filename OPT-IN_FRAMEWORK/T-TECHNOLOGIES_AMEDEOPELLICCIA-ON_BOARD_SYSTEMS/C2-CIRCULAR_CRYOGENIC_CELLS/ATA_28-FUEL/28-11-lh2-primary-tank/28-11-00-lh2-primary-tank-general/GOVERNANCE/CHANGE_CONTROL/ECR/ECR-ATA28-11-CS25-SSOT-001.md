# Engineering Change Request — ECR-ATA28-11-CS25-SSOT-001

## 1. Header

| Field | Value |
|-------|-------|
| **ECR ID** | ECR-ATA28-11-CS25-SSOT-001 |
| **Title** | Promote CM-28-11-CS25 to SSOT baseline |
| **Request Type** | Baseline Promotion (DEV → SSOT) |
| **Domain** | ATA 28-11-00 — LH₂ Primary Tank |
| **Programme** | AMPEL360 Q100 |
| **Technology Domain** | C2 — Circular Cryogenic Cells |
| **Current Lifecycle** | LC04 — Design Definition |
| **Requestor** | STK_ENG |
| **Co-owners** | STK_SAF, AIRWORTHINESS |
| **Date** | 2026-02-16 |
| **Current Location** | KDB/DEV/trade-studies/ |
| **Target Location** | KDB/LM/SSOT/ |
| **Configuration Impact** | Compliance baseline / certification evidence index |

## 2. Purpose of Change

Promote the preliminary compliance matrix **CM-28-11-CS25** to SSOT as
the controlled certification-mapping reference for ATA 28-11-00 LH₂
primary tank.

The objective is to establish a governed, traceable, and auditable
baseline linking:

- CS-25 clauses applicable to LH₂ tank architecture,
- explicit LH₂ deltas requiring Special Conditions,
- Means of Compliance (MoC),
- verification and validation (V&V) routes,
- and minimum evidence package expectations for certification progression.

## 3. Baseline Item Under Change

| Item | Identifier |
|------|------------|
| Matrix ID | CM-28-11-CS25 |
| Regulation | EASA CS-25 (+ LH₂ Special Conditions package) |
| ATA | 28-11-00 |
| Status (Current) | Preliminary (DEV — not baselined) |
| Status (Requested) | SSOT Baseline (Controlled) |

## 4. Change Description

Promotion covers the following structured content as controlled baseline:

1. **Section A** — Tank Structural Integrity and Loads
   CS 25.963, 25.965, 25.967, 25.571 mappings with cryogenic-specific deltas.
2. **Section B** — Pressure, Venting, Boil-off Management
   CS 25.969, 25.975 mappings with ullage/relief/transient logic.
3. **Section C** — Fire/Explosion/Ignition Prevention
   CS 25.981, 25.1309 mappings with FHA/PSSA/SSA safety architecture.
4. **Section D** — Materials, Processes, Inspection, ICA
   CS 25.603/605 and 25.1529 with cryogenic M&P and ICA coverage.
5. **Special Conditions Pack**
   SC-LH2-01 … SC-LH2-05 gap closure items beyond literal CS-25 scope.
6. **Minimum Evidence Package index**
   8 required artefacts for certification-readiness.

## 5. Technical Justification

- The matrix provides clause-level compliance decomposition and explicit
  LH₂ gap identification.
- It aligns with performance-based substantiation for hydrogen
  architecture where CS-25 text is fuel-agnostic.
- It defines a coherent MoC path across analysis / test / inspection /
  review.
- It enables deterministic traceability for requirements, safety
  assessments, V&V plans, and ICA.

## 6. Safety and Certification Impact

| Area | Impact |
|------|--------|
| Airworthiness | Positive: formalizes compliance mapping and removes ambiguity in CS-25/LH₂ interpretation. |
| System Safety | Positive: enforces linkage to FHA/PSSA/SSA, ignition prevention strategy, CDCCLs, zonal hazards. |
| Certification Strategy | Positive: provides clear bridge from CS-25 baseline to EASA-agreed LH₂ Special Conditions and Issue Papers. |
| Operational Risk | Reduced through codified requirements for venting, detection, vacuum integrity, and crashworthiness. |

## Safety Impact

- [x] Yes — requires STK_SAF review within 72 h

## 7. Scope and Interfaces Affected

- **Primary ATA:** 28-11-00
- **Related interfaces:** 28-21 (transfer), 28-41 (detection), ATA 26
  (fire protection), ATA 71/24 (powerplant/power integration), zonal and
  safety repositories.
- **Governance repositories:** change control, SSOT registry, compliance
  index, safety evidence library.

## 8. Deliverables to Baseline (Promotion Set)

| # | Artefact |
|---|----------|
| 1 | ATA28-11_LH2_PrimaryTank_StructuralSpec.md |
| 2 | CS25_compliance_matrix.yaml |
| 3 | FHA_PSSA_SSA_ATA28-11_LH2.pdf |
| 4 | Tank_Qualification_TestPlan_Report.pdf |
| 5 | VentingAndReliefSizing_Report.pdf |
| 6 | MaterialsAndProcesses_Cryogenic_Qualification.pdf |
| 7 | ThermalBridge_HeatLeak_Decomposition.pdf |
| 8 | ICA_ATA28-11_LH2_PrimaryTank_Draft.pdf |

## 9. Entry / Exit Criteria

### 9.1 Entry Criteria (must be satisfied before CCB review)

- BREX validation completed (no blocking errors).
- Trace coverage available from matrix rows to requirements and evidence
  stubs.
- Safety ownership assigned for all Critical/Very High rows.
- Special Conditions rows (SC-LH2-xx) linked to MoC owners.

### 9.2 Exit Criteria (for SSOT approval)

- CCB approval by STK_ENG + STK_SAF + Airworthiness.
- Matrix version frozen and tagged in SSOT.
- Traceability report archived.
- Open actions, assumptions, and TBDs captured in controlled issue list
  with due dates.

## 10. Verification of Change Quality

| Check | Method | Owner | Pass/Fail Rule |
|-------|--------|-------|----------------|
| BREX conformance | Automated validation | DOC/CFG | 0 blocking errors |
| Trace completeness | Coverage script + review | STK_ENG | 100 % rows linked to req + evidence placeholder |
| Safety consistency | FHA/PSSA/SSA cross-check | STK_SAF | No orphan hazards / no uncaptured catastrophic paths |
| Certification coherence | Compliance review board | AIRWORTHINESS | All CS + SC rows mapped to acceptable MoC |
| ICA consistency | Technical publication review | CUST_SERV_DOC | No contradictions with maintenance assumptions |

## 11. Risk Register (Residual / Transition)

| Risk ID | Description | Severity | Mitigation |
|---------|-------------|----------|------------|
| R-01 | CS text interpretation drift for LH₂ scenarios | High | Freeze interpretation notes in matrix annex + regulator alignment meetings |
| R-02 | Incomplete evidence maturity for some rows | High | Mark maturity level per row and gate baseline as "controlled preliminary" with action plan |
| R-03 | SC package evolution during certification dialogue | Medium | Maintain SC versioning and MoC delta logs |
| R-04 | Interface mismatch with ATA 28-41 detection logic | High | Add cross-ATA verification checkpoint before next baseline increment |

## 12. Proposed Approval Workflow

1. Technical readiness review — STK_ENG
2. Safety readiness review — STK_SAF
3. Airworthiness review — Certification lead
4. CCB decision — Approve / Approve with actions / Reject
5. If approved: publish to KDB/LM/SSOT/, tag version, register in
   baseline index.

## 13. Implementation Plan After Approval

- Copy controlled artefacts from DEV package to SSOT path.
- Assign immutable version tag (e.g., v1.0.0-SSOT).
- Update SSOT registry/catalog and backlinks from ATA 28 master index.
- Open follow-up ECRs for any deferred actions (if approval is
  conditional).

## 14. Draft Decision Statement (for CCB Minutes)

> **Decision proposal:** Approve promotion of CM-28-11-CS25 from DEV to
> SSOT as controlled baseline for LC04 Design Definition, subject to
> closure of any open actions recorded during CCB review.

---

## Approval Status

| Role | Decision | Date | Signature |
|------|----------|------|-----------|
| STK_ENG | | | |
| STK_SAF | | | |
| AIRWORTHINESS | | | |
| CCB Chair | | | |
