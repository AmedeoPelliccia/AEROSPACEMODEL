"""
Tests for ATA 28 Sub-System Section Structures.

Validates the directory structures for all 11 sub-system sections
under ATA_28-FUEL (codes 00, 11, 13, 21, 22, 23, 30, 31, 41, 42, 43).

Each section must have:
- README.md
- SECTION_INDEX.yaml (valid YAML)
- GENESIS/ with O-KNOTS.csv, Y-KNOTS.csv, DISCOVERY_LOG.md,
  GRADUATION_CRITERIA.md, README.md
- A subject directory (28-XX-00-*-general/) with KDB, IDB, CONTRACTS,
  ASIT, GOVERNANCE, INDEX, README.md, SUBJECT_MANIFEST.yaml
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

# (section_code, section_slug, subject_slug)
SECTIONS = [
    ("00", "28-00-general", "28-00-00-general-general"),
    ("11", "28-11-lh2-primary-tank", "28-11-00-lh2-primary-tank-general"),
    ("13", "28-13-lh2-auxiliary-tank", "28-13-00-lh2-auxiliary-tank-general"),
    ("21", "28-21-cryogenic-transfer", "28-21-00-cryogenic-transfer-general"),
    ("22", "28-22-insulated-transfer-lines", "28-22-00-insulated-transfer-lines-general"),
    ("23", "28-23-pressure-control", "28-23-00-pressure-control-general"),
    ("30", "28-30-boil-off-management", "28-30-00-boil-off-management-general"),
    ("31", "28-31-thermal-management", "28-31-00-thermal-management-general"),
    ("41", "28-41-h2-leak-detection", "28-41-00-h2-leak-detection-general"),
    ("42", "28-42-pressure-relief-venting", "28-42-00-pressure-relief-venting-general"),
    ("43", "28-43-fire-detection-suppression", "28-43-00-fire-detection-suppression-general"),
]


# =========================================================================
# Section-Level Tests
# =========================================================================


class TestSectionDirectories:
    """All 11 sub-system section directories must exist."""

    @pytest.mark.parametrize(
        "section_slug", [s[1] for s in SECTIONS], ids=[s[0] for s in SECTIONS]
    )
    def test_section_directory_exists(self, section_slug):
        assert (ATA28 / section_slug).is_dir()


class TestSectionFiles:
    """Each section must have README.md and SECTION_INDEX.yaml."""

    @pytest.mark.parametrize(
        "section_slug", [s[1] for s in SECTIONS], ids=[s[0] for s in SECTIONS]
    )
    def test_section_readme(self, section_slug):
        assert (ATA28 / section_slug / "README.md").exists()

    @pytest.mark.parametrize(
        "section_slug", [s[1] for s in SECTIONS], ids=[s[0] for s in SECTIONS]
    )
    def test_section_index_yaml(self, section_slug):
        path = ATA28 / section_slug / "SECTION_INDEX.yaml"
        assert path.exists()
        with open(path) as f:
            data = yaml.safe_load(f)
        assert data is not None
        assert "ata_section" in data


class TestSectionGenesis:
    """Each section must have a GENESIS directory with standard files."""

    @pytest.mark.parametrize(
        "section_slug", [s[1] for s in SECTIONS], ids=[s[0] for s in SECTIONS]
    )
    def test_genesis_directory(self, section_slug):
        assert (ATA28 / section_slug / "GENESIS").is_dir()

    @pytest.mark.parametrize(
        "section_slug", [s[1] for s in SECTIONS], ids=[s[0] for s in SECTIONS]
    )
    @pytest.mark.parametrize(
        "filename",
        [
            "README.md",
            "O-KNOTS.csv",
            "Y-KNOTS.csv",
            "DISCOVERY_LOG.md",
            "GRADUATION_CRITERIA.md",
        ],
    )
    def test_genesis_file_exists(self, section_slug, filename):
        assert (ATA28 / section_slug / "GENESIS" / filename).exists()


# =========================================================================
# Subject-Level Tests
# =========================================================================


class TestSubjectDirectories:
    """Each section must have a 28-XX-00-*-general subject directory."""

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_subject_directory_exists(self, section_slug, subject_slug):
        assert (ATA28 / section_slug / subject_slug).is_dir()


class TestSubjectRootFiles:
    """Each subject must have README.md and SUBJECT_MANIFEST.yaml."""

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_subject_readme(self, section_slug, subject_slug):
        assert (ATA28 / section_slug / subject_slug / "README.md").exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_subject_manifest(self, section_slug, subject_slug):
        path = ATA28 / section_slug / subject_slug / "SUBJECT_MANIFEST.yaml"
        assert path.exists()
        with open(path) as f:
            data = yaml.safe_load(f)
        assert data is not None
        assert "subject_id" in data


class TestSubjectKDB:
    """Each subject must have KDB with DEV workspace and LM/SSOT/PLM structure."""

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_kdb_readme(self, section_slug, subject_slug):
        assert (ATA28 / section_slug / subject_slug / "KDB" / "README.md").exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_dev_workspace(self, section_slug, subject_slug):
        kdb = ATA28 / section_slug / subject_slug / "KDB"
        for d in ("working", "trade-studies", "prototypes", "dev-evidence"):
            assert (kdb / "DEV" / d).is_dir(), f"KDB/DEV/{d} must exist"

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_ssot_policy(self, section_slug, subject_slug):
        assert (
            ATA28 / section_slug / subject_slug / "KDB" / "LM" / "SSOT" / "SSOT_POLICY.md"
        ).exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    @pytest.mark.parametrize(
        "lc_dir",
        [
            "LC01_PROBLEM_STATEMENT",
            "LC02_SYSTEM_REQUIREMENTS",
            "LC03_SAFETY_RELIABILITY",
            "LC04_DESIGN_DEFINITION_DMU",
            "LC05_ANALYSIS_MODELS_CAE",
            "LC06_INTEGRATION_TEST_PMU",
            "LC07_QUALITY",
            "LC08_FLIGHT_TEST_CERTIFICATION",
            "LC09_GREEN_AIRCRAFT_BASELINES",
            "LC10_INDUSTRIALIZATION_PRODUCTION_CAM",
        ],
    )
    def test_lifecycle_phase_directory(self, section_slug, subject_slug, lc_dir):
        phase = ATA28 / section_slug / subject_slug / "KDB" / "LM" / "SSOT" / "PLM" / lc_dir
        assert phase.is_dir(), f"{lc_dir} must exist"
        assert (phase / "README.md").exists(), f"{lc_dir}/README.md must exist"
        assert (phase / "PACKAGES").is_dir(), f"{lc_dir}/PACKAGES must exist"


class TestSubjectContracts:
    """Each subject must have CONTRACTS directory with standard files."""

    @pytest.mark.parametrize(
        "section_slug,subject_slug,subj_code",
        [(s[1], s[2], f"28-{s[0]}-00") for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_contracts_readme(self, section_slug, subject_slug, subj_code):
        assert (ATA28 / section_slug / subject_slug / "CONTRACTS" / "README.md").exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug,subj_code",
        [(s[1], s[2], f"28-{s[0]}-00") for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_csdb_contract(self, section_slug, subject_slug, subj_code):
        assert (
            ATA28 / section_slug / subject_slug / "CONTRACTS"
            / f"KITDM-CTR-LM-CSDB_ATA{subj_code}.yaml"
        ).exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug,subj_code",
        [(s[1], s[2], f"28-{s[0]}-00") for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_export_contract(self, section_slug, subject_slug, subj_code):
        assert (
            ATA28 / section_slug / subject_slug / "CONTRACTS"
            / f"KITDM-CTR-LM-EXPORT_ATA{subj_code}.yaml"
        ).exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug,subj_code",
        [(s[1], s[2], f"28-{s[0]}-00") for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_ietp_contract(self, section_slug, subject_slug, subj_code):
        assert (
            ATA28 / section_slug / subject_slug / "CONTRACTS"
            / f"KITDM-CTR-LM-IETP_ATA{subj_code}.yaml"
        ).exists()


class TestSubjectASIT:
    """Each subject must have ASIT directory with config and subdirs."""

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_asit_readme(self, section_slug, subject_slug):
        assert (ATA28 / section_slug / subject_slug / "ASIT" / "README.md").exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_asit_config(self, section_slug, subject_slug):
        path = ATA28 / section_slug / subject_slug / "ASIT" / "asit_config.yaml"
        assert path.exists()
        with open(path) as f:
            data = yaml.safe_load(f)
        assert data is not None

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_asit_subdirectories(self, section_slug, subject_slug):
        for d in ("pipelines", "rules", "runs"):
            assert (ATA28 / section_slug / subject_slug / "ASIT" / d).is_dir()


class TestSubjectIDB:
    """Each subject must have IDB with PUB, OPS, and INDEX."""

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_idb_readme(self, section_slug, subject_slug):
        assert (ATA28 / section_slug / subject_slug / "IDB" / "README.md").exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_idb_governance(self, section_slug, subject_slug):
        assert (ATA28 / section_slug / subject_slug / "IDB" / "IDB_GOVERNANCE.md").exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    @pytest.mark.parametrize("pub", ["AMM", "SRM", "CMM"])
    def test_publication_structure(self, section_slug, subject_slug, pub):
        pub_path = ATA28 / section_slug / subject_slug / "IDB" / "PUB" / pub
        assert pub_path.is_dir()
        assert (pub_path / "CSDB" / "DM").is_dir()
        assert (pub_path / "CSDB" / "PM").is_dir()
        assert (pub_path / "CSDB" / "BREX").is_dir()
        assert (pub_path / "EXPORT" / "PDF").is_dir()
        assert (pub_path / "EXPORT" / "HTML").is_dir()
        assert (pub_path / "IETP_RUNTIME").is_dir()

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    def test_ipc_directory(self, section_slug, subject_slug):
        assert (ATA28 / section_slug / subject_slug / "IDB" / "PUB" / "IPC").is_dir()

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    @pytest.mark.parametrize(
        "lc_dir",
        [
            "LC11_OPERATIONS_CUSTOMIZATION",
            "LC12_SUPPORT_SERVICES",
            "LC13_MRO_SUSTAINMENT",
            "LC14_RETIREMENT_CIRCULARITY",
        ],
    )
    def test_ops_lifecycle_phase(self, section_slug, subject_slug, lc_dir):
        phase = ATA28 / section_slug / subject_slug / "IDB" / "OPS" / "LM" / lc_dir
        assert phase.is_dir(), f"{lc_dir} must exist"
        assert (phase / "README.md").exists(), f"{lc_dir}/README.md must exist"

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    @pytest.mark.parametrize(
        "source",
        ["Maintenance_Source", "Overhaul_Source", "Repair_Source"],
    )
    def test_lc13_mro_sources(self, section_slug, subject_slug, source):
        path = (
            ATA28 / section_slug / subject_slug
            / "IDB" / "OPS" / "LM" / "LC13_MRO_SUSTAINMENT" / "PACKAGES" / source
        )
        assert path.is_dir(), f"LC13/{source} must exist"
        assert (path / "README.md").exists()

    @pytest.mark.parametrize(
        "section_slug,subject_slug",
        [(s[1], s[2]) for s in SECTIONS],
        ids=[s[0] for s in SECTIONS],
    )
    @pytest.mark.parametrize(
        "filename",
        [
            "IDB_RELEASE_NOTES.md",
            "IDB_TRACE_SUMMARY.md",
            "PUBLICATION_MANIFEST.yaml",
            "BASELINE_REFERENCE.yaml",
            "COMPLIANCE_CHECKLIST.md",
            "CHANGELOG.md",
        ],
    )
    def test_idb_index_file(self, section_slug, subject_slug, filename):
        assert (ATA28 / section_slug / subject_slug / "IDB" / "INDEX" / filename).exists()


# =========================================================================
# ATA 28 README Navigation
# =========================================================================


class TestATA28Navigation:
    """ATA_28-FUEL/README.md must reference all sub-system sections."""

    @pytest.fixture
    def readme(self) -> str:
        return (ATA28 / "README.md").read_text(encoding="utf-8")

    @pytest.mark.parametrize(
        "section_slug", [s[1] for s in SECTIONS], ids=[s[0] for s in SECTIONS]
    )
    def test_readme_references_section(self, readme, section_slug):
        assert section_slug in readme, (
            f"ATA_28-FUEL/README.md must reference {section_slug}"
        )
