"""
Tests for AMPEL360 Q100 — ATA 28 Circular Cryogenic Cells (C2).

Validates:
- YAML structure of program config, requirements, contract, BREX rules, and pipeline
- BREXGovernedValidator with C2 context (sub_system field, generate_srm_task)
- Documentation existence and structure
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from aerospacemodel.asigt.brex_governance import (
    BREXGovernedValidator,
    GovernedValidationResult,
    OperationContext,
    OPERATION_RULES,
)


# Resolve repository root
REPO_ROOT = Path(__file__).resolve().parent.parent
EXAMPLE_DIR = REPO_ROOT / "examples" / "ampel360_q100"


# =============================================================================
# YAML File Loading Helpers
# =============================================================================


def _load_yaml(path: Path) -> dict:
    """Load and parse a YAML file."""
    assert path.exists(), f"File must exist: {path}"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


# =============================================================================
# Program Configuration Tests
# =============================================================================


class TestProgramConfig:
    """Tests for AMPEL360 Q100 program_config.yaml."""

    @pytest.fixture
    def config(self) -> dict:
        return _load_yaml(EXAMPLE_DIR / "program_config.yaml")

    def test_program_name(self, config):
        assert config["program"]["name"] == "AMPEL360 Q100"

    def test_model_code(self, config):
        assert config["program"]["model_code"] == "Q100"

    def test_fuel_type_lh2(self, config):
        assert "Liquid Hydrogen" in config["program"]["aircraft"]["fuel"]["type"]

    def test_tank_type_c2(self, config):
        assert "Circular Cryogenic Cells" in config["program"]["aircraft"]["fuel"]["tank_type"]

    def test_special_conditions(self, config):
        scs = config["certification"]["special_conditions"]
        sc_ids = [sc.split(":")[0] for sc in scs]
        assert "SC-28-H2-001" in sc_ids
        assert "SC-28-CRYO-002" in sc_ids

    def test_novel_technology_c2(self, config):
        domains = [nt["domain"] for nt in config["certification"]["novel_technology"]]
        assert "C2_CIRCULAR_CRYOGENIC_CELLS" in domains

    def test_s1000d_issue(self, config):
        assert config["standards"]["s1000d"]["issue"] == "5.0"


# =============================================================================
# KDB Requirements Tests
# =============================================================================


class TestC2Requirements:
    """Tests for ATA 28 C2 cryogenic fuel requirements."""

    @pytest.fixture
    def reqs(self) -> dict:
        return _load_yaml(
            EXAMPLE_DIR / "KDB" / "requirements" / "ata28_c2_cryogenic_fuel.yaml"
        )

    def test_metadata_ata_chapter(self, reqs):
        assert reqs["metadata"]["ata_chapter"] == "28"

    def test_metadata_program(self, reqs):
        assert reqs["metadata"]["program"] == "AMPEL360 Q100"

    def test_metadata_novel_technology(self, reqs):
        assert reqs["metadata"]["novel_technology"] == "C2_CIRCULAR_CRYOGENIC_CELLS"

    def test_has_requirements(self, reqs):
        assert len(reqs["requirements"]) > 0

    def test_section_00_system_overview(self, reqs):
        """Section 00: System overview requirement exists."""
        ids = [r["id"] for r in reqs["requirements"]]
        assert "REQ-Q100-C2-001" in ids

    def test_section_10_cryogenic_cells(self, reqs):
        """Section 10: Cryogenic cells design requirement exists."""
        ids = [r["id"] for r in reqs["requirements"]]
        assert "REQ-Q100-C2-010" in ids

    def test_section_20_distribution(self, reqs):
        """Section 20: Distribution piping requirement exists."""
        ids = [r["id"] for r in reqs["requirements"]]
        assert "REQ-Q100-C2-020" in ids

    def test_section_30_monitoring(self, reqs):
        """Section 30: Sensors and telemetry requirement exists."""
        ids = [r["id"] for r in reqs["requirements"]]
        assert "REQ-Q100-C2-030" in ids

    def test_section_40_maintenance(self, reqs):
        """Section 40: Routine inspection requirement exists."""
        ids = [r["id"] for r in reqs["requirements"]]
        assert "REQ-Q100-C2-040" in ids

    def test_hydrogen_warnings_present(self, reqs):
        """Hydrogen hazard warnings must be present."""
        warnings_found = False
        for req in reqs["requirements"]:
            for w in req.get("warnings", []):
                if w["type"] == "hydrogen":
                    warnings_found = True
                    break
        assert warnings_found, "At least one hydrogen warning must exist"

    def test_cryogenic_warnings_present(self, reqs):
        """Cryogenic hazard warnings must be present."""
        warnings_found = False
        for req in reqs["requirements"]:
            for w in req.get("warnings", []):
                if w["type"] == "cold-injury":
                    warnings_found = True
                    break
        assert warnings_found, "At least one cryogenic warning must exist"

    def test_all_requirements_have_ata_code(self, reqs):
        """Every requirement must have an ATA code starting with 28."""
        for req in reqs["requirements"]:
            assert req["ata_code"].startswith("28"), (
                f"{req['id']} ATA code must start with 28"
            )

    def test_safety_critical_requirements(self, reqs):
        """Safety-critical requirements must exist."""
        safety_reqs = [r for r in reqs["requirements"] if r.get("safety_critical")]
        assert len(safety_reqs) >= 5, "At least 5 safety-critical requirements expected"


# =============================================================================
# Contract Tests
# =============================================================================


class TestC2Contract:
    """Tests for the Q100 AMM contract."""

    @pytest.fixture
    def contract(self) -> dict:
        return _load_yaml(
            EXAMPLE_DIR / "ASIT" / "CONTRACTS" / "active" / "Q100-CTR-AMM-001.yaml"
        )

    def test_contract_id(self, contract):
        assert contract["contract"]["id"] == "Q100-CTR-AMM-001"

    def test_contract_type(self, contract):
        assert contract["contract"]["type"] == "KDB_TO_CSDB"

    def test_contract_active(self, contract):
        assert contract["contract"]["status"] == "active"

    def test_scope_ata28(self, contract):
        assert "28" in contract["source"]["scope"]["ata_chapters"]

    def test_brex_contract_ref(self, contract):
        assert "KITDM-CTR-LM-CSDB_ATA28" in contract["contract"]["metadata"]["brex_contract_ref"]

    def test_hydrogen_safety_validation(self, contract):
        additional = contract["validation"]["additional"]
        types = [v["type"] for v in additional]
        assert "hydrogen_safety" in types
        assert "cryogenic_safety" in types

    def test_pipeline_reference(self, contract):
        assert contract["execution"]["pipeline"] == "ata28_h2_pipeline"


# =============================================================================
# BREX Rules Tests
# =============================================================================


class TestC2BREXRules:
    """Tests for the Q100 C2 BREX rules."""

    @pytest.fixture
    def brex(self) -> dict:
        return _load_yaml(EXAMPLE_DIR / "ASIGT" / "brex" / "q100_c2_brex.yaml")

    def test_brex_id(self, brex):
        assert brex["brex"]["id"] == "Q100-BREX-C2-001"

    def test_brex_ata_chapter(self, brex):
        assert brex["brex"]["ata_chapter"] == "28"

    def test_brex_novel_technology(self, brex):
        assert brex["brex"]["novel_technology"] == "C2_CIRCULAR_CRYOGENIC_CELLS"

    def test_has_rules(self, brex):
        assert len(brex["brex"]["rules"]) >= 10

    def test_safety_rules_exist(self, brex):
        """Safety rules C2-SAFETY-001 through C2-SAFETY-004 must exist."""
        rule_ids = [r["id"] for r in brex["brex"]["rules"]]
        for i in range(1, 5):
            assert f"C2-SAFETY-00{i}" in rule_ids

    def test_boiloff_rules_exist(self, brex):
        """Boil-off management rules must exist."""
        rule_ids = [r["id"] for r in brex["brex"]["rules"]]
        assert "C2-BOG-001" in rule_ids
        assert "C2-BOG-002" in rule_ids

    def test_boiloff_thresholds(self, brex):
        """Boil-off thresholds must be defined."""
        bog_rule = next(
            r for r in brex["brex"]["rules"] if r["id"] == "C2-BOG-001"
        )
        assert "thresholds" in bog_rule
        assert "design_target" in bog_rule["thresholds"]
        assert "warning" in bog_rule["thresholds"]
        assert "alarm" in bog_rule["thresholds"]

    def test_ai_governance_rules(self, brex):
        """AI governance rules must exist."""
        rule_ids = [r["id"] for r in brex["brex"]["rules"]]
        assert "C2-AI-001" in rule_ids
        assert "C2-AI-002" in rule_ids

    def test_material_compatibility_rule(self, brex):
        """Material compatibility rule must list approved and prohibited materials."""
        mat_rule = next(
            r for r in brex["brex"]["rules"] if r["id"] == "C2-MAT-001"
        )
        assert len(mat_rule["approved_materials"]) > 0
        assert len(mat_rule["prohibited_materials"]) > 0

    def test_audit_retention(self, brex):
        assert "7 years" in brex["brex"]["audit"]["retention"]


# =============================================================================
# Pipeline Tests
# =============================================================================


class TestH2Pipeline:
    """Tests for ata28_h2_pipeline.yaml."""

    @pytest.fixture
    def pipeline(self) -> dict:
        return _load_yaml(REPO_ROOT / "pipelines" / "ata28_h2_pipeline.yaml")

    def test_pipeline_id(self, pipeline):
        assert pipeline["pipeline"]["metadata"]["pipeline_id"] == "PIPELINE-ATA28-H2-001"

    def test_has_stages(self, pipeline):
        assert len(pipeline["pipeline"]["stages"]) == 8

    def test_stage_names(self, pipeline):
        names = [s["stage"] for s in pipeline["pipeline"]["stages"]]
        assert "initialization" in names
        assert "source_loading" in names
        assert "transformation" in names
        assert "validation" in names
        assert "traceability" in names
        assert "publication_assembly" in names
        assert "finalization" in names

    def test_hydrogen_safety_validation(self, pipeline):
        """Pipeline must include hydrogen safety validation."""
        validate_stage = next(
            s for s in pipeline["pipeline"]["stages"] if s["stage"] == "validation"
        )
        step_names = [step["step"] for step in validate_stage["steps"]]
        assert "hydrogen_safety_validation" in step_names

    def test_special_conditions_check(self, pipeline):
        """Pipeline initialization must check special conditions."""
        init_stage = next(
            s for s in pipeline["pipeline"]["stages"] if s["stage"] == "initialization"
        )
        sc_step = next(
            step for step in init_stage["steps"] if step["step"] == "check_special_conditions"
        )
        assert "SC-28-H2-001" in sc_step["inputs"]["required"]
        assert "SC-28-CRYO-002" in sc_step["inputs"]["required"]


# =============================================================================
# BREXGovernedValidator Integration Tests
# =============================================================================


class TestBREXGovernedValidatorC2:
    """Tests for BREXGovernedValidator with C2 context."""

    def test_operation_context_sub_system(self):
        """OperationContext must support sub_system field."""
        ctx = OperationContext(
            contract_id="KITDM-CTR-LM-CSDB_ATA28",
            ata_domain="ATA 28",
            sub_system="40",
            safety_impact=True,
        )
        assert ctx.sub_system == "40"
        assert ctx.to_dict()["sub_system"] == "40"

    def test_generate_srm_task_in_operations(self):
        """generate_srm_task must be a registered operation."""
        assert "generate_srm_task" in OPERATION_RULES

    def test_generate_srm_task_rules(self):
        """generate_srm_task must require safety rule."""
        rules = OPERATION_RULES["generate_srm_task"]
        assert "SAFETY-002" in rules

    def test_validator_with_c2_contract(self):
        """Validator initializes with ATA 28 C2 contract."""
        validator = BREXGovernedValidator(
            contract_id="KITDM-CTR-LM-CSDB_ATA28",
            baseline_id="DBL-Q100-2026-Q2",
        )
        assert validator.contract_id == "KITDM-CTR-LM-CSDB_ATA28"
        assert validator.baseline_id == "DBL-Q100-2026-Q2"

    def test_validate_srm_task_operation(self):
        """Validate generate_srm_task with C2 context."""
        validator = BREXGovernedValidator(
            contract_id="KITDM-CTR-LM-CSDB_ATA28",
            baseline_id="DBL-Q100-2026-Q2",
        )
        result = validator.validate_operation(
            operation="generate_srm_task",
            context=OperationContext(
                contract_id="KITDM-CTR-LM-CSDB_ATA28",
                ata_domain="ATA 28",
                sub_system="40",
                safety_impact=True,
            ),
        )
        assert isinstance(result, GovernedValidationResult)
        assert result.operation == "generate_srm_task"
        # In fallback mode (no BREX engine), should still be allowed
        assert result.allowed is True

    def test_validate_without_contract_blocked(self):
        """Operation without contract must be blocked."""
        validator = BREXGovernedValidator(
            contract_id="",
            baseline_id="DBL-Q100-2026-Q2",
        )
        result = validator.validate_operation(
            operation="generate_srm_task",
            context=OperationContext(
                contract_id="",
                ata_domain="ATA 28",
                sub_system="40",
            ),
        )
        assert result.allowed is False


# =============================================================================
# Documentation Tests
# =============================================================================


class TestC2Documentation:
    """Tests for C2 documentation files."""

    def test_c2_structure_doc_exists(self):
        path = REPO_ROOT / "docs" / "ATA_28_C2_AMPEL360_Q100.md"
        assert path.exists(), "ATA 28 C2 structure document must exist"

    def test_c2_structure_doc_content(self):
        path = REPO_ROOT / "docs" / "ATA_28_C2_AMPEL360_Q100.md"
        text = path.read_text(encoding="utf-8")
        assert "AMPEL360 Q100" in text
        assert "Circular Cryogenic Cells" in text
        assert "SC-28-H2-001" in text
        assert "SC-28-CRYO-002" in text

    def test_example_readme_exists(self):
        path = EXAMPLE_DIR / "README.md"
        assert path.exists(), "Example README must exist"

    def test_h2_pipeline_exists(self):
        path = REPO_ROOT / "pipelines" / "ata28_h2_pipeline.yaml"
        assert path.exists(), "ATA 28 H2 pipeline must exist"
