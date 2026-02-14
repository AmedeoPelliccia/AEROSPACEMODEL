"""
Tests for Engineering SSOT Front-End in OPT-IN_FRAMEWORK.

Validates:
- Directory and file existence within OPT-IN_FRAMEWORK
- SSOT registry YAML structure and required fields
- index.html structure and key content
- Cross-references from OPT-IN_FRAMEWORK index and README
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


# Resolve repository root
REPO_ROOT = Path(__file__).resolve().parent.parent
OPT_IN = REPO_ROOT / "OPT-IN_FRAMEWORK"
ENGINEERING_SSOT = OPT_IN / "ENGINEERING_SSOT"


# =============================================================================
# Directory Structure Tests
# =============================================================================


class TestEngineeringSSOTStructure:
    """Tests that ENGINEERING_SSOT directory exists with required files."""

    def test_engineering_ssot_directory_exists(self):
        assert ENGINEERING_SSOT.is_dir(), (
            "ENGINEERING_SSOT/ must exist inside OPT-IN_FRAMEWORK"
        )

    def test_index_html_exists(self):
        path = ENGINEERING_SSOT / "index.html"
        assert path.exists(), "index.html front-end must exist"

    def test_readme_exists(self):
        path = ENGINEERING_SSOT / "README.md"
        assert path.exists(), "README.md must exist"

    def test_ssot_registry_exists(self):
        path = ENGINEERING_SSOT / "00_SSOT_REGISTRY.yaml"
        assert path.exists(), "00_SSOT_REGISTRY.yaml must exist"

    def test_resides_in_opt_in_framework(self):
        """The front-end must reside within the existing OPT-IN_FRAMEWORK directory."""
        assert ENGINEERING_SSOT.parent.name == "OPT-IN_FRAMEWORK"


# =============================================================================
# SSOT Registry YAML Tests
# =============================================================================


class TestSSOTRegistry:
    """Tests for 00_SSOT_REGISTRY.yaml structure and content."""

    @pytest.fixture
    def registry(self) -> dict:
        path = ENGINEERING_SSOT / "00_SSOT_REGISTRY.yaml"
        assert path.exists()
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def test_has_metadata(self, registry):
        assert "metadata" in registry
        assert registry["metadata"]["program"] == "AMPEL360 Q100"

    def test_has_ssot_entries(self, registry):
        assert "ssot_entries" in registry
        assert len(registry["ssot_entries"]) > 0

    def test_has_custom_data_sheets_key(self, registry):
        assert "custom_data_sheets" in registry

    def test_ssot_entries_have_required_fields(self, registry):
        """Each SSOT entry must have the required identification fields."""
        required_fields = [
            "id", "title", "ata_chapter", "technology_domain",
            "baseline_ref", "lifecycle_phase", "status",
        ]
        for entry in registry["ssot_entries"]:
            for field in required_fields:
                assert field in entry, (
                    f"Entry {entry.get('id', '?')} missing field: {field}"
                )

    def test_ssot_entries_have_valid_status(self, registry):
        valid_statuses = {"draft", "in_review", "approved"}
        for entry in registry["ssot_entries"]:
            assert entry["status"] in valid_statuses, (
                f"Entry {entry['id']} has invalid status: {entry['status']}"
            )

    def test_novel_technology_entries_exist(self, registry):
        """Registry must include entries from novel technology domains."""
        domains = {e["technology_domain"] for e in registry["ssot_entries"]}
        assert "C2-CIRCULAR_CRYOGENIC_CELLS" in domains
        assert "P-PROPULSION" in domains
        assert "I2-INTELLIGENCE" in domains

    def test_c2_entries_have_special_conditions(self, registry):
        """C2 entries must reference hydrogen special conditions."""
        c2_entries = [
            e for e in registry["ssot_entries"]
            if e["technology_domain"] == "C2-CIRCULAR_CRYOGENIC_CELLS"
        ]
        assert len(c2_entries) >= 1
        for entry in c2_entries:
            assert "SC-28-H2-001" in entry.get("special_conditions", [])


# =============================================================================
# index.html Front-End Tests
# =============================================================================


class TestIndexHTML:
    """Tests for the index.html front-end content."""

    @pytest.fixture
    def html_content(self) -> str:
        path = ENGINEERING_SSOT / "index.html"
        assert path.exists()
        return path.read_text(encoding="utf-8")

    def test_is_valid_html(self, html_content):
        assert "<!DOCTYPE html>" in html_content
        assert "<html" in html_content
        assert "</html>" in html_content

    def test_references_ampel360_q100(self, html_content):
        assert "AMPEL360 Q100" in html_content

    def test_references_engineering_ssot(self, html_content):
        assert "Engineering SSOT" in html_content or "SSOT Registry" in html_content

    def test_references_custom_information_data_sheet(self, html_content):
        assert "Custom Information Data Sheet" in html_content

    def test_has_ssot_registry_table(self, html_content):
        assert "ssot-registry" in html_content
        assert "SSOT-Q100-C2-001" in html_content

    def test_has_data_sheet_form(self, html_content):
        assert "data-sheet" in html_content or "ds-id" in html_content

    def test_references_opt_in_framework(self, html_content):
        assert "OPT-IN" in html_content

    def test_no_external_dependencies(self, html_content):
        """Front-end must be self-contained (no CDN or external links in head)."""
        # No external stylesheet or script links in head
        assert "cdn." not in html_content.lower()
        assert "unpkg.com" not in html_content.lower()


# =============================================================================
# Cross-Reference Tests
# =============================================================================


class TestOptInFrameworkReferences:
    """Tests that OPT-IN_FRAMEWORK documents reference ENGINEERING_SSOT."""

    def test_readme_references_engineering_ssot(self):
        readme = (OPT_IN / "README.md").read_text(encoding="utf-8")
        assert "ENGINEERING_SSOT" in readme

    def test_index_references_engineering_ssot(self):
        index = (OPT_IN / "00_INDEX.md").read_text(encoding="utf-8")
        assert "ENGINEERING_SSOT" in index

    def test_readme_mentions_front_end(self):
        readme = (OPT_IN / "README.md").read_text(encoding="utf-8")
        assert "front-end" in readme.lower() or "front end" in readme.lower()
