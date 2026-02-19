# ATA 26 – Traceability Conventions

> Relationship types and trace link semantics for ATA 26 Fire Protection.

---

## 1. Directional Relationships

| Relationship | Direction | Meaning |
|--------------|-----------|---------|
| `derives_from` | child → parent | Child requirement is derived from parent |
| `satisfies` | design → requirement | Design element satisfies a requirement |
| `verifies` | test → requirement | Test case verifies a requirement |
| `implements` | code/HW → design | Implementation realises a design element |
| `allocates_to` | requirement → subsystem | Requirement is allocated to a subsystem |

All relationships are **directional**. The source owns the link.

## 2. Trace Link Format

Trace links are stored as CSV with the following columns:

```csv
source_id,target_id,relationship,direction,rationale,status
REQ-Q100-E1-012,KNOT-ATA26-11-00-001,derives_from,up,Fire detection requirement from KNOT,approved
DMC-Q100-A-26-11-00-00A-040A-A,REQ-Q100-E1-012,satisfies,up,Design description satisfies REQ,approved
TC-Q100-E1-012-01,REQ-Q100-E1-012,verifies,up,Detection test verifies requirement,planned
```

| Column | Description |
|--------|-------------|
| `source_id` | The artifact that owns the trace link |
| `target_id` | The artifact being traced to |
| `relationship` | One of the five defined relationship types |
| `direction` | `up` (toward parent/need) or `down` (toward implementation) |
| `rationale` | Brief justification for the link |
| `status` | `planned`, `approved`, `verified`, or `retired` |

## 3. Example Trace Chain

```
KNOT-ATA26-11-00-001        (Knowledge Node – Fire Detection)
  └─► KNU-ATA26-11-00-001-01  (Knowledge Unit – Smoke Detector)
        └─► REQ-Q100-E1-012     (Requirement – Detection Response Time)
              ├─► DES-Q100-E1-012  (Design – Detector Configuration)
              │     └─► IMP-Q100-E1-012  (Implementation – Detector Installation)
              ├─► TC-Q100-E1-012-01  (Test Case – Response Time Test)
              └─► DMC-Q100-A-26-11-00-00A-040A-A  (Publication)
```

## 4. Directionality Rules

- **Unidirectional:** `derives_from`, `satisfies`, `verifies`, `implements`
  — the source artifact declares the link; the target does not repeat it.
- **Bidirectional (by convention):** `allocates_to` — both the requirement
  index and the subsystem index record the allocation for cross-reference.

## 5. Mandatory Traces per Lifecycle Phase

| Phase | Required Trace | Enforcement |
|-------|---------------|-------------|
| LC01 – Concept | KNOT → KNU | Block release without link |
| LC02 – Requirements | REQ → parent KNOT/KNU | Block baseline (FBL) without link |
| LC04 – Design | REQ → DES (satisfies) | Block design baseline (DBL) without link |
| LC06 – Verification | REQ → TEST (verifies) | Block test readiness review (TRR) |
| LC08 – Certification | REQ → CERT_EVIDENCE | Block certification submission |
| LC10 – Production | DES → IMP (implements) | Block production baseline (PBL) |

Missing mandatory traces raise a **BREX Trace Coverage Violation** and block
the lifecycle gate transition.

---

*Trace links are auditable artifacts. Retention: 7 years minimum (certification).*
