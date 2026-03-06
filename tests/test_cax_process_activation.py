"""
Tests for CAx Process Activation Map.

Validates:
- YAML structure and required fields
- 15 canonical CAx process definitions
- Domain activation entries reference only canonical processes
- PDM-PLM is mandatory in every domain
- Novel technology domains activate all 15 processes
- No duplicate CAx entries per domain
- Every domain has opt_in flag
- Path mapping keys match domain_activation keys
- Path mapping values point to existing OPT-IN_FRAMEWORK directories
- Cross-reference consistency with T_SUBDOMAIN_LC_ACTIVATION.yaml
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


# Resolve repository root
REPO_ROOT = Path(__file__).resolve().parent.parent
CAX_ACTIVATION = REPO_ROOT / "lifecycle" / "CAX_PROCESS_ACTIVATION.yaml"
LC_ACTIVATION = REPO_ROOT / "lifecycle" / "T_SUBDOMAIN_LC_ACTIVATION.yaml"

# Canonical set of 15 CAx processes
CANONICAL_CAX = frozenset([
    "CAD", "CAE", "CFD", "CAM", "CAPP", "VP",
    "PDM-PLM", "SCM", "MRP-ERP", "CIM",
    "CAI", "CAA", "CASE", "KBE", "CAT",
])


@pytest.fixture(scope="module")
def cax_data() -> dict:
    """Load the CAx Process Activation YAML."""
    assert CAX_ACTIVATION.exists(), "CAX_PROCESS_ACTIVATION.yaml must exist"
    return yaml.safe_load(CAX_ACTIVATION.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def lc_data() -> dict:
    """Load the T-Subdomain LC Activation YAML."""
    assert LC_ACTIVATION.exists(), "T_SUBDOMAIN_LC_ACTIVATION.yaml must exist"
    return yaml.safe_load(LC_ACTIVATION.read_text(encoding="utf-8"))


# =============================================================================
# Meta Section Tests
# =============================================================================


class TestMetaSection:
    """Tests for the meta section of CAX_PROCESS_ACTIVATION.yaml."""

    def test_meta_exists(self, cax_data: dict):
        assert "meta" in cax_data

    def test_schema_version(self, cax_data: dict):
        assert "schema_version" in cax_data["meta"]

    def test_file_version(self, cax_data: dict):
        assert "file_version" in cax_data["meta"]

    def test_program(self, cax_data: dict):
        assert cax_data["meta"]["program"] == "AMPEL360 Q100"

    def test_owner(self, cax_data: dict):
        assert cax_data["meta"]["owner"] == "ASIT"

    def test_status_active(self, cax_data: dict):
        assert cax_data["meta"]["status"] == "ACTIVE"


# =============================================================================
# CAx Process Definitions Tests
# =============================================================================


class TestCaxProcessDefinitions:
    """Tests for the cax_processes definitions section."""

    def test_cax_processes_section_exists(self, cax_data: dict):
        assert "cax_processes" in cax_data

    def test_exactly_15_processes(self, cax_data: dict):
        assert len(cax_data["cax_processes"]) == 15

    def test_all_canonical_processes_defined(self, cax_data: dict):
        defined = set(cax_data["cax_processes"].keys())
        assert defined == CANONICAL_CAX, \
            f"Missing: {CANONICAL_CAX - defined}, Extra: {defined - CANONICAL_CAX}"

    @pytest.mark.parametrize("process_id", sorted(CANONICAL_CAX))
    def test_process_has_name(self, cax_data: dict, process_id: str):
        proc = cax_data["cax_processes"][process_id]
        assert "name" in proc, f"{process_id} must have a name"
        assert len(proc["name"]) > 0

    @pytest.mark.parametrize("process_id", sorted(CANONICAL_CAX))
    def test_process_has_description(self, cax_data: dict, process_id: str):
        proc = cax_data["cax_processes"][process_id]
        assert "description" in proc, f"{process_id} must have a description"
        assert len(proc["description"]) > 0


# =============================================================================
# Domain Activation Tests
# =============================================================================


class TestDomainActivation:
    """Tests for the domain_activation section."""

    def test_domain_activation_exists(self, cax_data: dict):
        assert "domain_activation" in cax_data

    def test_at_least_19_domains(self, cax_data: dict):
        """20 domains expected: O, P, 15 T-subdomains, I, N."""
        assert len(cax_data["domain_activation"]) >= 19

    def test_all_domains_have_cax_list(self, cax_data: dict):
        for domain, config in cax_data["domain_activation"].items():
            assert "cax" in config, f"{domain} must have a cax list"
            assert isinstance(config["cax"], list), f"{domain} cax must be a list"
            assert len(config["cax"]) >= 1, f"{domain} cax must have at least 1 entry"

    def test_all_domains_have_opt_in(self, cax_data: dict):
        for domain, config in cax_data["domain_activation"].items():
            assert "opt_in" in config, f"{domain} must have opt_in field"
            assert isinstance(config["opt_in"], bool), f"{domain} opt_in must be boolean"

    def test_all_cax_entries_are_canonical(self, cax_data: dict):
        for domain, config in cax_data["domain_activation"].items():
            for proc in config["cax"]:
                assert proc in CANONICAL_CAX, \
                    f"{domain}: '{proc}' is not a canonical CAx process"

    def test_no_duplicate_cax_entries(self, cax_data: dict):
        for domain, config in cax_data["domain_activation"].items():
            cax_list = config["cax"]
            assert len(cax_list) == len(set(cax_list)), \
                f"{domain} has duplicate CAx entries"

    def test_pdm_plm_mandatory_in_all_domains(self, cax_data: dict):
        for domain, config in cax_data["domain_activation"].items():
            assert "PDM-PLM" in config["cax"], \
                f"{domain} must include PDM-PLM"


# =============================================================================
# Novel Technology Full Activation Tests
# =============================================================================


class TestNovelTechnologyActivation:
    """Novel technology domains must activate all 15 CAx processes."""

    NOVEL_DOMAINS = [
        "T/C2-CIRCULAR_CRYOGENIC_CELLS",
        "T/P-PROPULSION",
    ]

    @pytest.mark.parametrize("domain", NOVEL_DOMAINS)
    def test_novel_domain_has_all_15_processes(self, cax_data: dict, domain: str):
        config = cax_data["domain_activation"][domain]
        activated = set(config["cax"])
        assert activated == CANONICAL_CAX, \
            f"{domain} must activate all 15 CAx processes. " \
            f"Missing: {CANONICAL_CAX - activated}"

    @pytest.mark.parametrize("domain", NOVEL_DOMAINS)
    def test_novel_domain_has_note(self, cax_data: dict, domain: str):
        config = cax_data["domain_activation"][domain]
        assert "note" in config, f"{domain} (novel) should have a note"


# =============================================================================
# Specific Domain CAx Content Tests
# =============================================================================


class TestSpecificDomainCax:
    """Spot-check specific domain CAx lists match the specification."""

    def test_o_organizations_cax(self, cax_data: dict):
        cax = set(cax_data["domain_activation"]["O-ORGANIZATIONS"]["cax"])
        assert cax == {"PDM-PLM", "CASE", "CAA", "KBE"}

    def test_p_programs_cax(self, cax_data: dict):
        cax = set(cax_data["domain_activation"]["P-PROGRAMS"]["cax"])
        assert cax == {"PDM-PLM", "SCM", "CAA", "CASE"}

    def test_i_infrastructures_cax(self, cax_data: dict):
        cax = set(cax_data["domain_activation"]["I-INFRASTRUCTURES"]["cax"])
        assert cax == {"CAD", "CAM", "CAPP", "CIM", "PDM-PLM", "SCM", "MRP-ERP", "CAA"}

    def test_n_neural_networks_cax(self, cax_data: dict):
        cax = set(cax_data["domain_activation"]["N-NEURAL_NETWORKS"]["cax"])
        assert cax == {"CASE", "CAI", "CAA", "KBE", "PDM-PLM"}

    def test_t_i2_intelligence_cax(self, cax_data: dict):
        cax = set(cax_data["domain_activation"]["T/I2-INTELLIGENCE"]["cax"])
        assert cax == {"CAI", "CASE", "KBE", "PDM-PLM", "CAA", "CAT"}

    def test_t_a_airframe_cabins_cax(self, cax_data: dict):
        cax = set(cax_data["domain_activation"]["T/A-AIRFRAME_CABINS"]["cax"])
        assert cax == {"CAD", "CAE", "CFD", "CAM", "CAPP", "VP", "PDM-PLM", "SCM", "CIM", "KBE", "CAT"}

    def test_t_e1_environment_cax(self, cax_data: dict):
        cax = set(cax_data["domain_activation"]["T/E1-ENVIRONMENT"]["cax"])
        assert cax == {"CAD", "CAE", "CFD", "PDM-PLM", "CAT"}

    def test_t_l1_logics_cax(self, cax_data: dict):
        cax = set(cax_data["domain_activation"]["T/L1-LOGICS"]["cax"])
        assert cax == {"CASE", "KBE", "PDM-PLM"}


# =============================================================================
# Path Mapping Tests
# =============================================================================


class TestPathMapping:
    """Tests for the path_mapping section."""

    def test_path_mapping_exists(self, cax_data: dict):
        assert "path_mapping" in cax_data

    def test_every_domain_has_path(self, cax_data: dict):
        domains = set(cax_data["domain_activation"].keys())
        paths = set(cax_data["path_mapping"].keys())
        assert domains == paths, \
            f"Mismatch: domains without path: {domains - paths}, " \
            f"paths without domain: {paths - domains}"

    def test_all_paths_start_with_optin(self, cax_data: dict):
        for domain, path in cax_data["path_mapping"].items():
            assert path.startswith("OPT-IN_FRAMEWORK/"), \
                f"{domain} path must start with OPT-IN_FRAMEWORK/"

    def test_all_paths_point_to_existing_directories(self, cax_data: dict):
        for domain, rel_path in cax_data["path_mapping"].items():
            full_path = REPO_ROOT / rel_path
            assert full_path.is_dir(), \
                f"{domain} path does not exist: {rel_path}"


# =============================================================================
# Validation Rules Tests
# =============================================================================


class TestValidationRules:
    """Tests for the validation_rules section."""

    def test_validation_rules_exist(self, cax_data: dict):
        assert "validation_rules" in cax_data
        assert len(cax_data["validation_rules"]) >= 5

    def test_all_rules_have_required_fields(self, cax_data: dict):
        for rule in cax_data["validation_rules"]:
            assert "id" in rule
            assert "name" in rule
            assert "rule" in rule
            assert "enforcement" in rule

    def test_rule_ids_are_unique(self, cax_data: dict):
        ids = [r["id"] for r in cax_data["validation_rules"]]
        assert len(ids) == len(set(ids)), "Validation rule IDs must be unique"

    def test_rule_ids_follow_pattern(self, cax_data: dict):
        import re
        for rule in cax_data["validation_rules"]:
            assert re.match(r"^CAX-VAL-\d{3}$", rule["id"]), \
                f"Rule ID {rule['id']} must match CAX-VAL-NNN pattern"


# =============================================================================
# Cross-Reference with T_SUBDOMAIN_LC_ACTIVATION.yaml
# =============================================================================


class TestCrossReferenceConsistency:
    """Tests that CAx activation is cross-referenced in LC activation."""

    def test_lc_activation_has_cax_references(self, lc_data: dict):
        """Check that subdomain entries in LC activation reference CAx."""
        sd = lc_data.get("subdomains", {})
        # Novel technology subdomains should have cax field
        for key in ["C2_CIRCULAR_CRYOGENIC_CELLS", "P_PROPULSION", "I2_INTELLIGENCE"]:
            if key in sd:
                assert "cax" in sd[key], \
                    f"Subdomain {key} in LC activation must reference CAx processes"

    def test_novel_subdomains_cax_match(self, cax_data: dict, lc_data: dict):
        """Cross-check that CAx lists in LC activation match the activation map."""
        sd = lc_data.get("subdomains", {})
        mapping = {
            "C2_CIRCULAR_CRYOGENIC_CELLS": "T/C2-CIRCULAR_CRYOGENIC_CELLS",
            "P_PROPULSION": "T/P-PROPULSION",
            "I2_INTELLIGENCE": "T/I2-INTELLIGENCE",
        }
        for lc_key, cax_key in mapping.items():
            if lc_key in sd and "cax" in sd[lc_key]:
                lc_cax = set(sd[lc_key]["cax"])
                act_cax = set(cax_data["domain_activation"][cax_key]["cax"])
                assert lc_cax == act_cax, \
                    f"CAx mismatch for {lc_key}: LC has {lc_cax}, " \
                    f"activation has {act_cax}"

    def test_standard_subdomains_cax_match(self, cax_data: dict, lc_data: dict):
        """Cross-check standard subdomain CAx with activation map."""
        sd = lc_data.get("subdomains", {})
        mapping = {
            "O_AUTHORITATIVE": "O-ORGANIZATIONS",
            "O_BUSINESS_ENFORCEMENT": "O-ORGANIZATIONS",
            "P_PRODUCT_DEFINITION": "P-PROGRAMS",
            "P_SERVICE_INSTRUCTION": "P-PROGRAMS",
            "I_MANUFACTURING_FACILITIES": "I-INFRASTRUCTURES",
            "I_MAINTENANCE_ENVIRONMENTS": "I-INFRASTRUCTURES",
            "I_OPERATIONS_SERVICE_STRUCTURES": "I-INFRASTRUCTURES",
            "N_DIGITAL_THREAD_TRACEABILITY": "N-NEURAL_NETWORKS",
            "N_AI_GOVERNANCE_ASSURANCE": "N-NEURAL_NETWORKS",
            "N_PROGRAM_RESERVED": "N-NEURAL_NETWORKS",
        }
        for lc_key, cax_domain in mapping.items():
            if lc_key in sd and "cax" in sd[lc_key]:
                lc_cax = set(sd[lc_key]["cax"])
                act_cax = set(cax_data["domain_activation"][cax_domain]["cax"])
                assert lc_cax == act_cax, \
                    f"CAx mismatch for {lc_key}: LC has {lc_cax}, " \
                    f"activation map has {act_cax}"
