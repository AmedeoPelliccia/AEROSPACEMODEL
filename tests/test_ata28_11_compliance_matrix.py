"""
Tests for CS-25 Compliance Matrix in KDB/DEV/trade-studies/.

Validates the EASA CS-25 compliance matrix YAML and Markdown records
for ATA 28-11-00 LH₂ Primary Tank (Cryogenic Cells).
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRADE_STUDIES = (
    REPO_ROOT
    / "OPT-IN_FRAMEWORK"
    / "T-TECHNOLOGIES_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"
    / "C2-CIRCULAR_CRYOGENIC_CELLS"
    / "ATA_28-FUEL"
    / "28-11-lh2-primary-tank"
    / "28-11-00-lh2-primary-tank-general"
    / "KDB"
    / "DEV"
    / "trade-studies"
)

ECR_DIR = (
    REPO_ROOT
    / "OPT-IN_FRAMEWORK"
    / "T-TECHNOLOGIES_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"
    / "C2-CIRCULAR_CRYOGENIC_CELLS"
    / "ATA_28-FUEL"
    / "28-11-lh2-primary-tank"
    / "28-11-00-lh2-primary-tank-general"
    / "GOVERNANCE"
    / "CHANGE_CONTROL"
    / "ECR"
)


# =========================================================================
# File Existence
# =========================================================================


class TestComplianceMatrixFiles2811:
    """CS-25 compliance matrix files for 28-11 must exist."""

    def test_yaml_exists(self):
        assert (TRADE_STUDIES / "CS25_compliance_matrix.yaml").exists()

    def test_markdown_exists(self):
        assert (TRADE_STUDIES / "CS25_compliance_matrix.md").exists()


# =========================================================================
# YAML Validity & Top-Level Schema
# =========================================================================


class TestComplianceMatrixYAML2811:
    """CS-25 compliance matrix YAML for 28-11 must parse and have required fields."""

    @pytest.fixture()
    def cm_data(self):
        path = TRADE_STUDIES / "CS25_compliance_matrix.yaml"
        with open(path) as f:
            return yaml.safe_load(f)

    def test_parses_without_error(self, cm_data):
        assert cm_data is not None

    def test_has_matrix_id(self, cm_data):
        assert cm_data.get("matrix_id") == "CM-28-11-CS25"

    def test_has_ata_code(self, cm_data):
        assert cm_data.get("ata_code") == "28-11-00"

    def test_has_technology_domain(self, cm_data):
        assert cm_data.get("technology_domain") == "C2"

    def test_has_regulation(self, cm_data):
        assert "CS-25" in cm_data.get("regulation", "")

    def test_has_lifecycle_phase(self, cm_data):
        assert cm_data.get("lifecycle_phase") == "LC04"


# =========================================================================
# Sections Structure (A–D)
# =========================================================================


class TestComplianceMatrixSections2811:
    """Sections A–D must be present with requirements."""

    @pytest.fixture()
    def cm_data(self):
        path = TRADE_STUDIES / "CS25_compliance_matrix.yaml"
        with open(path) as f:
            return yaml.safe_load(f)

    def test_four_sections(self, cm_data):
        sections = cm_data.get("sections", [])
        assert len(sections) == 4

    @pytest.mark.parametrize("section_id", ["A", "B", "C", "D"])
    def test_section_present(self, cm_data, section_id):
        ids = [s["id"] for s in cm_data.get("sections", [])]
        assert section_id in ids

    def test_total_requirements_count(self, cm_data):
        total = sum(
            len(s.get("requirements", []))
            for s in cm_data.get("sections", [])
        )
        assert total == 10


# =========================================================================
# Requirement Schema
# =========================================================================


class TestRequirementSchema2811:
    """Every requirement entry must have the expected fields."""

    @pytest.fixture()
    def all_reqs(self):
        path = TRADE_STUDIES / "CS25_compliance_matrix.yaml"
        with open(path) as f:
            data = yaml.safe_load(f)
        reqs = []
        for section in data.get("sections", []):
            reqs.extend(section.get("requirements", []))
        return reqs

    def test_all_have_req_id(self, all_reqs):
        for r in all_reqs:
            assert "req_id" in r, f"Missing req_id in {r}"

    def test_all_have_cs25_ref(self, all_reqs):
        for r in all_reqs:
            assert "cs25_ref" in r, f"Missing cs25_ref in {r.get('req_id')}"

    def test_all_have_topic(self, all_reqs):
        for r in all_reqs:
            assert "topic" in r, f"Missing topic in {r.get('req_id')}"

    def test_all_have_moc(self, all_reqs):
        for r in all_reqs:
            assert "moc" in r, f"Missing moc in {r.get('req_id')}"

    def test_all_have_evidence(self, all_reqs):
        for r in all_reqs:
            ev = r.get("evidence")
            assert isinstance(ev, list) and len(ev) >= 1, (
                f"Missing/empty evidence in {r.get('req_id')}"
            )

    def test_all_have_vv(self, all_reqs):
        for r in all_reqs:
            assert "vv" in r, f"Missing vv in {r.get('req_id')}"

    def test_req_ids_unique(self, all_reqs):
        ids = [r["req_id"] for r in all_reqs]
        assert len(ids) == len(set(ids)), "Duplicate req_id found"


# =========================================================================
# Special Conditions
# =========================================================================


class TestSpecialConditions2811:
    """Special Conditions (SC-LH2-*) must be present."""

    @pytest.fixture()
    def cm_data(self):
        path = TRADE_STUDIES / "CS25_compliance_matrix.yaml"
        with open(path) as f:
            return yaml.safe_load(f)

    def test_special_conditions_present(self, cm_data):
        sc = cm_data.get("special_conditions", [])
        assert isinstance(sc, list)
        assert len(sc) == 5

    def test_sc_ids_format(self, cm_data):
        for sc in cm_data.get("special_conditions", []):
            assert sc["sc_id"].startswith("SC-LH2-")

    def test_sc_have_required_fields(self, cm_data):
        for sc in cm_data.get("special_conditions", []):
            assert "topic" in sc
            assert "description" in sc
            assert "moc" in sc


# =========================================================================
# Evidence Package
# =========================================================================


class TestEvidencePackage2811:
    """Minimum evidence package must list at least 8 artefacts."""

    @pytest.fixture()
    def cm_data(self):
        path = TRADE_STUDIES / "CS25_compliance_matrix.yaml"
        with open(path) as f:
            return yaml.safe_load(f)

    def test_evidence_package_present(self, cm_data):
        pkg = cm_data.get("evidence_package", [])
        assert isinstance(pkg, list)
        assert len(pkg) >= 8


# =========================================================================
# Traceability
# =========================================================================


class TestComplianceMatrixTraceability2811:
    """Traceability links to parent matrix and lifecycle phases."""

    @pytest.fixture()
    def cm_data(self):
        path = TRADE_STUDIES / "CS25_compliance_matrix.yaml"
        with open(path) as f:
            return yaml.safe_load(f)

    def test_derives_from_parent_matrix(self, cm_data):
        derives = cm_data.get("traceability", {}).get("derives_from", [])
        assert "CM-28-10-CS25" in derives

    def test_feeds_lifecycle_phases(self, cm_data):
        feeds = cm_data.get("traceability", {}).get("feeds", [])
        lcs = [f["lifecycle"] for f in feeds]
        assert "LC03" in lcs
        assert "LC05" in lcs


# =========================================================================
# ECR Document
# =========================================================================


class TestECRDocument2811:
    """ECR-ATA28-11-CS25-SSOT-001 must exist and contain key fields."""

    def test_ecr_file_exists(self):
        assert (ECR_DIR / "ECR-ATA28-11-CS25-SSOT-001.md").exists()

    def test_ecr_contains_ecr_id(self):
        text = (ECR_DIR / "ECR-ATA28-11-CS25-SSOT-001.md").read_text()
        assert "ECR-ATA28-11-CS25-SSOT-001" in text

    def test_ecr_references_matrix(self):
        text = (ECR_DIR / "ECR-ATA28-11-CS25-SSOT-001.md").read_text()
        assert "CM-28-11-CS25" in text

    def test_ecr_has_approval_table(self):
        text = (ECR_DIR / "ECR-ATA28-11-CS25-SSOT-001.md").read_text()
        assert "STK_ENG" in text
        assert "STK_SAF" in text
        assert "CCB Chair" in text


# =========================================================================
# Artifact Catalog Registration
# =========================================================================


class TestArtifactCatalogComplianceMatrix2811:
    """ARTIFACT_CATALOG.yaml must reflect updated compliance_matrices count."""

    @pytest.fixture()
    def catalog_data(self):
        path = (
            REPO_ROOT
            / "OPT-IN_FRAMEWORK"
            / "T-TECHNOLOGIES_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"
            / "C2-CIRCULAR_CRYOGENIC_CELLS"
            / "ATA_28-FUEL"
            / "INDEX"
            / "ARTIFACT_CATALOG.yaml"
        )
        with open(path) as f:
            return yaml.safe_load(f)

    def test_compliance_matrices_registered(self, catalog_data):
        cm = catalog_data.get("artifact_types", {}).get("compliance_matrices")
        assert cm is not None

    def test_compliance_matrices_count(self, catalog_data):
        cm = catalog_data["artifact_types"]["compliance_matrices"]
        assert cm["count"] == 2
