"""
Tests for FBL-Q100-ATA28-001 Functional Baseline in KDB/LM/SSOT/.

Validates the Functional Baseline definition for the AMPEL360 Q100
BWB Hydrogen Fuel Storage System, including architecture decisions,
functional requirements, promotion gates, and traceability.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
ATA28 = (
    REPO_ROOT
    / "OPT-IN_FRAMEWORK"
    / "T-TECHNOLOGIES_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"
    / "C2-CIRCULAR_CRYOGENIC_CELLS"
    / "ATA_28-FUEL"
)
SSOT = (
    ATA28
    / "28-10-storage"
    / "28-10-00-fuel-storage-general"
    / "KDB"
    / "LM"
    / "SSOT"
)


# =========================================================================
# File Existence
# =========================================================================


class TestFBLFiles:
    """FBL baseline files must exist."""

    def test_yaml_exists(self):
        assert (SSOT / "FBL-Q100-ATA28-001.yaml").exists()

    def test_markdown_exists(self):
        assert (SSOT / "FBL-Q100-ATA28-001.md").exists()


# =========================================================================
# YAML Validity & Top-Level Schema
# =========================================================================


class TestFBLYAML:
    """FBL YAML must parse and have required top-level fields."""

    @pytest.fixture()
    def fbl(self):
        with open(SSOT / "FBL-Q100-ATA28-001.yaml") as f:
            return yaml.safe_load(f)

    def test_parses_without_error(self, fbl):
        assert fbl is not None

    def test_has_baseline_id(self, fbl):
        assert fbl.get("baseline_id") == "FBL-Q100-ATA28-001"

    def test_has_baseline_type(self, fbl):
        assert fbl.get("baseline_type") == "FBL"

    def test_has_ata_code(self, fbl):
        assert fbl.get("ata_code") == "28-10-00"

    def test_has_technology_domain(self, fbl):
        assert fbl.get("technology_domain") == "C2"

    def test_has_lifecycle_phase(self, fbl):
        assert fbl.get("lifecycle_phase") == "LC04"

    def test_has_status_established(self, fbl):
        assert fbl.get("status") == "established"

    def test_has_approver(self, fbl):
        assert "CCB" in fbl.get("approver", "")
        assert "STK_SAF" in fbl.get("approver", "")


# =========================================================================
# Architecture Decisions
# =========================================================================


class TestArchitectureDecisions:
    """Architecture decisions must reference the three trade studies."""

    @pytest.fixture()
    def decisions(self):
        with open(SSOT / "FBL-Q100-ATA28-001.yaml") as f:
            data = yaml.safe_load(f)
        return data.get("architecture_decisions", [])

    def test_three_decisions(self, decisions):
        assert len(decisions) == 3

    def test_decisions_have_required_fields(self, decisions):
        for d in decisions:
            assert "decision_id" in d
            assert "trade_study_ref" in d
            assert "selected_option" in d
            assert "key_rationale" in d
            assert isinstance(d["key_rationale"], list)
            assert len(d["key_rationale"]) >= 1

    def test_trade_study_refs(self, decisions):
        refs = [d["trade_study_ref"] for d in decisions]
        assert "TS-28-10-TS01" in refs
        assert "TS-28-10-TS02" in refs
        assert "TS-28-10-TS03" in refs


# =========================================================================
# Functional Requirements
# =========================================================================


class TestFunctionalRequirements:
    """FBL must define functional requirements with acceptance criteria."""

    @pytest.fixture()
    def reqs(self):
        with open(SSOT / "FBL-Q100-ATA28-001.yaml") as f:
            data = yaml.safe_load(f)
        return data.get("functional_requirements", [])

    def test_at_least_ten_requirements(self, reqs):
        assert len(reqs) >= 10

    def test_all_have_required_fields(self, reqs):
        for r in reqs:
            assert "req_id" in r, f"Missing req_id in {r}"
            assert "title" in r, f"Missing title in {r.get('req_id')}"
            assert "acceptance" in r, f"Missing acceptance in {r.get('req_id')}"
            assert "verification" in r, f"Missing verification in {r.get('req_id')}"

    def test_req_ids_unique(self, reqs):
        ids = [r["req_id"] for r in reqs]
        assert len(ids) == len(set(ids))

    def test_req_ids_follow_convention(self, reqs):
        for r in reqs:
            assert r["req_id"].startswith("FBL-REQ-")


# =========================================================================
# Promotion Criteria (Acceptance Gates)
# =========================================================================


class TestPromotionCriteria:
    """Promotion gates must be defined for DEV → SSOT promotion."""

    @pytest.fixture()
    def gates(self):
        with open(SSOT / "FBL-Q100-ATA28-001.yaml") as f:
            data = yaml.safe_load(f)
        return data.get("promotion_criteria", {}).get("gates", [])

    def test_at_least_seven_gates(self, gates):
        assert len(gates) >= 7

    def test_gates_have_required_fields(self, gates):
        for g in gates:
            assert "gate_id" in g
            assert "title" in g
            assert "authority" in g
            assert "mandatory" in g

    def test_all_gates_mandatory(self, gates):
        for g in gates:
            assert g["mandatory"] is True

    def test_gate_ids_follow_convention(self, gates):
        for g in gates:
            assert g["gate_id"].startswith("FBL-GATE-")

    def test_brex_gate_present(self, gates):
        ids = [g["gate_id"] for g in gates]
        assert "FBL-GATE-001" in ids

    def test_safety_gate_present(self, gates):
        authorities = [g["authority"] for g in gates]
        assert any("STK_SAF" in a for a in authorities)

    def test_ecr_gate_present(self, gates):
        titles = [g["title"] for g in gates]
        assert any("ECR" in t for t in titles)


# =========================================================================
# Evaluation Criteria
# =========================================================================


class TestFBLEvaluationCriteria:
    """Evaluation criteria weights must sum to 100%."""

    @pytest.fixture()
    def criteria(self):
        with open(SSOT / "FBL-Q100-ATA28-001.yaml") as f:
            data = yaml.safe_load(f)
        return data.get("evaluation_criteria", [])

    def test_criteria_present(self, criteria):
        assert len(criteria) >= 5

    def test_weights_sum_to_100(self, criteria):
        total = sum(c["weight_pct"] for c in criteria)
        assert total == 100


# =========================================================================
# Traceability
# =========================================================================


class TestFBLTraceability:
    """FBL must have traceability to trade studies and WBS."""

    @pytest.fixture()
    def trace(self):
        with open(SSOT / "FBL-Q100-ATA28-001.yaml") as f:
            data = yaml.safe_load(f)
        return data.get("traceability", {})

    def test_derives_from_trade_studies(self, trace):
        derives = trace.get("derives_from", [])
        assert "TS-28-10-TS01" in derives
        assert "TS-28-10-TS02" in derives
        assert "TS-28-10-TS03" in derives

    def test_satisfies_wbs(self, trace):
        satisfies = trace.get("satisfies", [])
        assert len(satisfies) >= 1

    def test_feeds_lifecycle_phases(self, trace):
        feeds = trace.get("feeds", [])
        lcs = [f["lifecycle"] for f in feeds]
        assert "LC03" in lcs
        assert "LC05" in lcs


# =========================================================================
# Evidence Package
# =========================================================================


class TestFBLEvidencePackage:
    """Evidence package must list all supporting artefacts."""

    @pytest.fixture()
    def evidence(self):
        with open(SSOT / "FBL-Q100-ATA28-001.yaml") as f:
            data = yaml.safe_load(f)
        return data.get("evidence_package", [])

    def test_at_least_six_items(self, evidence):
        assert len(evidence) >= 6


# =========================================================================
# Baseline Register Consistency
# =========================================================================


class TestBaselineRegister:
    """BASELINE_REGISTER.csv must list FBL-Q100-ATA28-001 with correct fields."""

    @pytest.fixture()
    def fbl_row(self):
        import csv

        path = ATA28 / "GOVERNANCE" / "BASELINE_REGISTER.csv"
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["baseline_id"] == "FBL-Q100-ATA28-001":
                    return row
        return None

    def test_fbl_in_register(self, fbl_row):
        assert fbl_row is not None, "FBL-Q100-ATA28-001 not found in BASELINE_REGISTER.csv"

    def test_fbl_type(self, fbl_row):
        assert fbl_row["type"] == "FBL"

    def test_fbl_status(self, fbl_row):
        assert fbl_row["status"] == "established"

    def test_fbl_approver_includes_stk_saf(self, fbl_row):
        assert "STK_SAF" in fbl_row["approver"]


# =========================================================================
# Artifact Catalog Registration
# =========================================================================


class TestArtifactCatalogBaselines:
    """ARTIFACT_CATALOG.yaml must include baselines entry."""

    @pytest.fixture()
    def catalog(self):
        with open(ATA28 / "INDEX" / "ARTIFACT_CATALOG.yaml") as f:
            return yaml.safe_load(f)

    def test_baselines_registered(self, catalog):
        bl = catalog.get("artifact_types", {}).get("baselines")
        assert bl is not None

    def test_baselines_count(self, catalog):
        bl = catalog["artifact_types"]["baselines"]
        assert bl["count"] == 1
