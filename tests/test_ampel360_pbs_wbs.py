"""
Test AMPEL360 Q100 PBS/WBS Linkage

Tests for Product Breakdown Structure and Work Breakdown Structure linkage
per CV-003 specification.

Author: ASIT (Aircraft Systems Information Transponder)
Document: AMPEL360-CV-003 v3.0
"""

import pytest
from aerospacemodel.ampel360.pbs_wbs import (
    PBSID,
    WBSID,
    OPTINAxis,
    PBSParser,
    WBSParser,
    PBSWBSLinker,
    create_pbs_id,
    create_wbs_id,
    parse_pbs,
    parse_wbs,
    WBS_PHASE_CODES,
    SUBDOMAIN_CODES,
    NOVEL_TECHNOLOGY_SUBDOMAINS,
)


class TestPBSID:
    """Test PBSID class."""
    
    def test_valid_pbs_id(self):
        """Test creating a valid PBS ID."""
        pbs_id = PBSID(
            axis="T",
            subdomain="C2",
            ata_chapter="28",
            section="10",
            subject="00",
            item_name="CRYO_TANK_FWD"
        )
        assert pbs_id.axis == "T"
        assert pbs_id.subdomain == "C2"
        assert pbs_id.item_name == "CRYO_TANK_FWD"
    
    def test_to_string(self):
        """Test PBS ID string generation."""
        pbs_id = PBSID(
            axis="T",
            subdomain="C2",
            ata_chapter="28",
            section="10",
            subject="00",
            item_name="CRYO_TANK_FWD"
        )
        expected = "PBS-TC2-ATA28-10-00-CRYO_TANK_FWD"
        assert pbs_id.to_string() == expected
        assert str(pbs_id) == expected
    
    def test_invalid_axis(self):
        """Test invalid axis validation."""
        with pytest.raises(ValueError, match="Invalid axis"):
            PBSID(
                axis="X",  # Invalid
                subdomain="A",
                ata_chapter="25",
                section="10",
                subject="00",
                item_name="TEST_ITEM"
            )
    
    def test_invalid_subdomain_for_axis(self):
        """Test invalid subdomain for given axis."""
        with pytest.raises(ValueError, match="Invalid subdomain"):
            PBSID(
                axis="O",
                subdomain="C2",  # C2 is only valid for T axis
                ata_chapter="04",
                section="00",
                subject="00",
                item_name="TEST_ITEM"
            )
    
    def test_invalid_item_name(self):
        """Test invalid item name validation."""
        with pytest.raises(ValueError, match="Invalid item name"):
            PBSID(
                axis="T",
                subdomain="A",
                ata_chapter="25",
                section="10",
                subject="00",
                item_name="invalid-item"  # Must be uppercase with underscores
            )
    
    def test_is_novel_technology(self):
        """Test novel technology detection."""
        # Novel technology: C2 (Cryogenic Cells)
        pbs_c2 = PBSID(
            axis="T",
            subdomain="C2",
            ata_chapter="28",
            section="10",
            subject="00",
            item_name="CRYO_TANK"
        )
        assert pbs_c2.is_novel_technology() is True
        
        # Novel technology: I2 (Intelligence)
        pbs_i2 = PBSID(
            axis="T",
            subdomain="I2",
            ata_chapter="95",
            section="10",
            subject="00",
            item_name="AI_MODEL"
        )
        assert pbs_i2.is_novel_technology() is True
        
        # Novel technology: P (Propulsion)
        pbs_p = PBSID(
            axis="T",
            subdomain="P",
            ata_chapter="71",
            section="11",
            subject="00",
            item_name="FUEL_CELL"
        )
        assert pbs_p.is_novel_technology() is True
        
        # Standard technology
        pbs_std = PBSID(
            axis="T",
            subdomain="A",
            ata_chapter="25",
            section="10",
            subject="00",
            item_name="SEAT"
        )
        assert pbs_std.is_novel_technology() is False
    
    def test_get_ata_path(self):
        """Test ATA path generation."""
        pbs_id = PBSID(
            axis="T",
            subdomain="C2",
            ata_chapter="28",
            section="10",
            subject="00",
            item_name="CRYO_TANK"
        )
        assert pbs_id.get_ata_path() == "ATA28-10-00"


class TestWBSID:
    """Test WBSID class."""
    
    def test_valid_wbs_id(self):
        """Test creating a valid WBS ID."""
        wbs_id = WBSID(
            phase_code="REQ",
            hierarchy="1.2.3"
        )
        assert wbs_id.phase_code == "REQ"
        assert wbs_id.hierarchy == "1.2.3"
    
    def test_to_string(self):
        """Test WBS ID string generation."""
        wbs_id = WBSID(
            phase_code="DES",
            hierarchy="2.4.1"
        )
        expected = "WBS-DES-2.4.1"
        assert wbs_id.to_string() == expected
        assert str(wbs_id) == expected
    
    def test_invalid_phase_code(self):
        """Test invalid phase code validation."""
        with pytest.raises(ValueError, match="Invalid phase code"):
            WBSID(
                phase_code="XXX",  # Invalid
                hierarchy="1.2"
            )
    
    def test_invalid_hierarchy(self):
        """Test invalid hierarchy validation."""
        with pytest.raises(ValueError, match="Invalid hierarchy"):
            WBSID(
                phase_code="REQ",
                hierarchy="1.2.a"  # Must be numeric
            )
    
    def test_get_lc_phase(self):
        """Test LC phase mapping."""
        wbs_id = WBSID(phase_code="REQ", hierarchy="1.2")
        assert wbs_id.get_lc_phase() == "LC02"
        
        wbs_id = WBSID(phase_code="DES", hierarchy="2.1")
        assert wbs_id.get_lc_phase() == "LC04"
        
        wbs_id = WBSID(phase_code="MRO", hierarchy="3.1")
        assert wbs_id.get_lc_phase() == "LC12"
    
    def test_get_level(self):
        """Test WBS level detection."""
        wbs_1 = WBSID(phase_code="REQ", hierarchy="1")
        assert wbs_1.get_level() == 1
        
        wbs_2 = WBSID(phase_code="REQ", hierarchy="1.2")
        assert wbs_2.get_level() == 2
        
        wbs_3 = WBSID(phase_code="REQ", hierarchy="1.2.3")
        assert wbs_3.get_level() == 3
        
        wbs_4 = WBSID(phase_code="REQ", hierarchy="1.2.3.4")
        assert wbs_4.get_level() == 4
    
    def test_get_parent(self):
        """Test parent WBS retrieval."""
        wbs_id = WBSID(phase_code="REQ", hierarchy="1.2.3")
        parent = wbs_id.get_parent()
        assert parent is not None
        assert parent.hierarchy == "1.2"
        assert parent.phase_code == "REQ"
        
        # Parent of parent
        grandparent = parent.get_parent()
        assert grandparent is not None
        assert grandparent.hierarchy == "1"
        
        # Root has no parent
        root = WBSID(phase_code="REQ", hierarchy="1")
        assert root.get_parent() is None


class TestPBSParser:
    """Test PBSParser class."""
    
    def test_parse_valid_pbs(self):
        """Test parsing valid PBS identifiers."""
        pbs_str = "PBS-TC2-ATA28-10-00-CRYO_TANK_FWD"
        pbs_id = PBSParser.parse(pbs_str)
        
        assert pbs_id is not None
        assert pbs_id.axis == "T"
        assert pbs_id.subdomain == "C2"
        assert pbs_id.ata_chapter == "28"
        assert pbs_id.section == "10"
        assert pbs_id.subject == "00"
        assert pbs_id.item_name == "CRYO_TANK_FWD"
    
    def test_parse_various_subdomains(self):
        """Test parsing PBS IDs with various subdomains."""
        test_cases = [
            ("PBS-TA-ATA25-10-00-SEAT_ASSY", "T", "A"),
            ("PBS-OA-ATA04-00-00-AIRWORTHINESS_LIMITS", "O", "A"),
            ("PBS-PS-ATA12-10-00-REPLENISHING", "P", "S"),
            ("PBS-IM1-ATA85-10-00-TEST_RIG", "I", "M1"),
            ("PBS-ND-ATA96-30-00-HASH_CHAIN", "N", "D"),
        ]
        
        for pbs_str, expected_axis, expected_subdomain in test_cases:
            pbs_id = PBSParser.parse(pbs_str)
            assert pbs_id is not None
            assert pbs_id.axis == expected_axis
            assert pbs_id.subdomain == expected_subdomain
    
    def test_parse_invalid_pbs(self):
        """Test parsing invalid PBS identifiers."""
        invalid_ids = [
            "INVALID_FORMAT",
            "PBS-XX-ATA25-10-00-TEST",  # Invalid axis/subdomain
            "PBS-TA-25-10-00-TEST",  # Missing ATA prefix
            "PBS-TA-ATA25-10-TEST",  # Missing subject
        ]
        
        for invalid_id in invalid_ids:
            pbs_id = PBSParser.parse(invalid_id)
            # Either parse fails (None) or validation fails
            assert pbs_id is None or not PBSParser.validate(invalid_id)
    
    def test_validate(self):
        """Test PBS validation."""
        valid_id = "PBS-TC2-ATA28-10-00-CRYO_TANK"
        assert PBSParser.validate(valid_id) is True
        
        invalid_id = "INVALID"
        assert PBSParser.validate(invalid_id) is False


class TestWBSParser:
    """Test WBSParser class."""
    
    def test_parse_valid_wbs(self):
        """Test parsing valid WBS identifiers."""
        wbs_str = "WBS-REQ-1.2.3"
        wbs_id = WBSParser.parse(wbs_str)
        
        assert wbs_id is not None
        assert wbs_id.phase_code == "REQ"
        assert wbs_id.hierarchy == "1.2.3"
    
    def test_parse_various_phases(self):
        """Test parsing WBS IDs with various phases."""
        test_cases = [
            ("WBS-PRB-1", "PRB"),
            ("WBS-REQ-1.2", "REQ"),
            ("WBS-SAF-2.1", "SAF"),
            ("WBS-DES-2.4.1", "DES"),
            ("WBS-VER-3.1.2", "VER"),
            ("WBS-MRO-4.2.1", "MRO"),
            ("WBS-EOL-5.1", "EOL"),
        ]
        
        for wbs_str, expected_phase in test_cases:
            wbs_id = WBSParser.parse(wbs_str)
            assert wbs_id is not None
            assert wbs_id.phase_code == expected_phase
    
    def test_parse_invalid_wbs(self):
        """Test parsing invalid WBS identifiers."""
        invalid_ids = [
            "INVALID_FORMAT",
            "WBS-XXX-1.2",  # Invalid phase code
            "WBS-REQ-a.b",  # Non-numeric hierarchy
            "WBS-REQ",  # Missing hierarchy
        ]
        
        for invalid_id in invalid_ids:
            assert WBSParser.parse(invalid_id) is None
    
    def test_validate(self):
        """Test WBS validation."""
        valid_id = "WBS-REQ-1.2.3"
        assert WBSParser.validate(valid_id) is True
        
        invalid_id = "INVALID"
        assert WBSParser.validate(invalid_id) is False


class TestPBSWBSLinker:
    """Test PBSWBSLinker class."""
    
    def test_link_pbs_wbs(self):
        """Test linking PBS and WBS."""
        linker = PBSWBSLinker()
        
        pbs_id = "PBS-TC2-ATA28-10-00-CRYO_TANK"
        wbs_id = "WBS-REQ-1.2"
        
        linker.link(pbs_id, wbs_id)
        
        # Verify link
        wbs_list = linker.get_wbs_for_pbs(pbs_id)
        assert wbs_id in wbs_list
        
        pbs_list = linker.get_pbs_for_wbs(wbs_id)
        assert pbs_id in pbs_list
    
    def test_multiple_wbs_per_pbs(self):
        """Test linking multiple WBS to one PBS."""
        linker = PBSWBSLinker()
        
        pbs_id = "PBS-TC2-ATA28-10-00-CRYO_TANK"
        wbs_ids = ["WBS-REQ-1.2", "WBS-DES-2.1", "WBS-VER-3.1"]
        
        for wbs_id in wbs_ids:
            linker.link(pbs_id, wbs_id)
        
        wbs_list = linker.get_wbs_for_pbs(pbs_id)
        assert len(wbs_list) == 3
        for wbs_id in wbs_ids:
            assert wbs_id in wbs_list
    
    def test_link_invalid_pbs(self):
        """Test linking with invalid PBS."""
        linker = PBSWBSLinker()
        
        with pytest.raises(ValueError, match="Invalid PBS ID"):
            linker.link("INVALID_PBS", "WBS-REQ-1.2")
    
    def test_link_invalid_wbs(self):
        """Test linking with invalid WBS."""
        linker = PBSWBSLinker()
        
        with pytest.raises(ValueError, match="Invalid WBS ID"):
            linker.link("PBS-TC2-ATA28-10-00-TEST", "INVALID_WBS")


class TestConvenienceFunctions:
    """Test convenience functions."""
    
    def test_create_pbs_id(self):
        """Test create_pbs_id convenience function."""
        pbs_str = create_pbs_id(
            axis="T",
            subdomain="C2",
            ata_chapter="28",
            section="10",
            subject="00",
            item_name="CRYO_TANK"
        )
        assert pbs_str == "PBS-TC2-ATA28-10-00-CRYO_TANK"
    
    def test_create_wbs_id(self):
        """Test create_wbs_id convenience function."""
        wbs_str = create_wbs_id(
            lc_phase="LC02",
            hierarchy="1.2.3"
        )
        assert wbs_str == "WBS-REQ-1.2.3"
        
        wbs_str = create_wbs_id(
            lc_phase="LC04",
            hierarchy="2.1"
        )
        assert wbs_str == "WBS-DES-2.1"
    
    def test_parse_pbs(self):
        """Test parse_pbs convenience function."""
        pbs_id = parse_pbs("PBS-TC2-ATA28-10-00-CRYO_TANK")
        assert pbs_id is not None
        assert pbs_id.subdomain == "C2"
    
    def test_parse_wbs(self):
        """Test parse_wbs convenience function."""
        wbs_id = parse_wbs("WBS-REQ-1.2.3")
        assert wbs_id is not None
        assert wbs_id.phase_code == "REQ"


class TestRealWorldExamples:
    """Test with real-world examples from CV-003."""
    
    def test_cv003_example_1(self):
        """Test: PBS-TA-ATA25-10-00-SEAT_ASSY"""
        pbs_str = "PBS-TA-ATA25-10-00-SEAT_ASSY"
        pbs_id = PBSParser.parse(pbs_str)
        
        assert pbs_id is not None
        assert pbs_id.axis == "T"
        assert pbs_id.subdomain == "A"  # Airframe & Cabins
        assert pbs_id.ata_chapter == "25"
        assert pbs_id.is_novel_technology() is False
    
    def test_cv003_example_2(self):
        """Test: PBS-TC2-ATA28-10-00-CRYO_TANK_FWD"""
        pbs_str = "PBS-TC2-ATA28-10-00-CRYO_TANK_FWD"
        pbs_id = PBSParser.parse(pbs_str)
        
        assert pbs_id is not None
        assert pbs_id.axis == "T"
        assert pbs_id.subdomain == "C2"  # Cryogenic Cells
        assert pbs_id.ata_chapter == "28"
        assert pbs_id.is_novel_technology() is True  # ⭐ Novel
    
    def test_cv003_example_3(self):
        """Test: PBS-IM1-ATA85-10-00-TEST_RIG_FCS"""
        pbs_str = "PBS-IM1-ATA85-10-00-TEST_RIG_FCS"
        pbs_id = PBSParser.parse(pbs_str)
        
        assert pbs_id is not None
        assert pbs_id.axis == "I"
        assert pbs_id.subdomain == "M1"  # Manufacturing Facilities
        assert pbs_id.ata_chapter == "85"
    
    def test_cv003_example_4(self):
        """Test: PBS-IO-ATAIN-50-00-GSE_COUPLER"""
        pbs_str = "PBS-IO-ATAIN-50-00-GSE_COUPLER"
        pbs_id = PBSParser.parse(pbs_str)
        
        assert pbs_id is not None
        assert pbs_id.axis == "I"
        assert pbs_id.subdomain == "O"  # Operations & Service Structures
        assert pbs_id.ata_chapter == "IN"  # Infrastructure chapter
    
    def test_cv003_example_5(self):
        """Test: PBS-ND-ATA96-30-00-HASH_CHAIN"""
        pbs_str = "PBS-ND-ATA96-30-00-HASH_CHAIN"
        pbs_id = PBSParser.parse(pbs_str)
        
        assert pbs_id is not None
        assert pbs_id.axis == "N"
        assert pbs_id.subdomain == "D"  # Digital Thread & Traceability
        assert pbs_id.ata_chapter == "96"


class TestConstants:
    """Test module constants."""
    
    def test_subdomain_codes(self):
        """Test SUBDOMAIN_CODES structure."""
        assert "O" in SUBDOMAIN_CODES
        assert "P" in SUBDOMAIN_CODES
        assert "T" in SUBDOMAIN_CODES
        assert "I" in SUBDOMAIN_CODES
        assert "N" in SUBDOMAIN_CODES
        
        # Check specific subdomains
        assert "A" in SUBDOMAIN_CODES["O"]
        assert "B" in SUBDOMAIN_CODES["O"]
        assert "C2" in SUBDOMAIN_CODES["T"]
        assert "I2" in SUBDOMAIN_CODES["T"]
        assert "P" in SUBDOMAIN_CODES["T"]
        assert "M1" in SUBDOMAIN_CODES["I"]
        assert "D" in SUBDOMAIN_CODES["N"]
    
    def test_novel_technology_subdomains(self):
        """Test NOVEL_TECHNOLOGY_SUBDOMAINS."""
        assert "C2" in NOVEL_TECHNOLOGY_SUBDOMAINS
        assert "I2" in NOVEL_TECHNOLOGY_SUBDOMAINS
        assert "P" in NOVEL_TECHNOLOGY_SUBDOMAINS
        assert len(NOVEL_TECHNOLOGY_SUBDOMAINS) == 3
    
    def test_wbs_phase_codes(self):
        """Test WBS_PHASE_CODES mapping."""
        assert WBS_PHASE_CODES["LC01"] == "PRB"
        assert WBS_PHASE_CODES["LC02"] == "REQ"
        assert WBS_PHASE_CODES["LC03"] == "SAF"
        assert WBS_PHASE_CODES["LC04"] == "DES"
        assert WBS_PHASE_CODES["LC12"] == "MRO"
        assert WBS_PHASE_CODES["LC14"] == "EOL"
        assert len(WBS_PHASE_CODES) == 14  # LC01-LC14


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
