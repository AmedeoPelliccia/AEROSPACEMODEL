"""
Test AMPEL360 Q100 Identifier Grammar

Tests for the canonical identifier grammar implementation per CV-003.

Author: ASIT (Aircraft Systems Information Transponder)
Document: AMPEL360-CV-003 v3.0
"""

import pytest
from aerospacemodel.ampel360.identifiers import (
    ArtifactID,
    IDFormat,
    PhaseType,
    IDParser,
    IDGenerator,
    parse_identifier,
    validate_identifier,
    create_identifier,
)


class TestArtifactID:
    """Test ArtifactID class."""
    
    def test_valid_artifact_id(self):
        """Test creating a valid artifact ID."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ",
            sequence="001"
        )
        assert artifact_id.msn == "MSN001"
        assert artifact_id.ata_chapter == "25"
        assert artifact_id.lc_phase == "LC02"
    
    def test_to_compact(self):
        """Test compact format generation."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ",
            sequence="001"
        )
        expected = "AMPEL360_Q100_MSN001_ATA25-10-00_LC02_REQ_001"
        assert artifact_id.to_compact() == expected
        assert str(artifact_id) == expected
    
    def test_to_hyphenated(self):
        """Test hyphenated format generation."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="28",
            section="10",
            subject="00",
            lc_phase="LC04",
            artifact_type="DES",
            sequence="042"
        )
        expected = "AMPEL360-Q100-MSN001-ATA28-10-00-LC04-DES-042"
        assert artifact_id.to_hyphenated() == expected
    
    def test_to_urn(self):
        """Test URN format generation."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="71",
            section="11",
            subject="00",
            lc_phase="LC06",
            artifact_type="TPR",
            sequence="003"
        )
        expected = "urn:ampel360:q100:msn001:ata71-11-00:lc06:tpr:003"
        assert artifact_id.to_urn() == expected
    
    def test_invalid_msn(self):
        """Test invalid MSN validation."""
        with pytest.raises(ValueError, match="Invalid MSN"):
            ArtifactID(
                msn="MSN01",  # Should be MSN001
                ata_chapter="25",
                lc_phase="LC02",
                artifact_type="REQ"
            )
    
    def test_invalid_ata_chapter(self):
        """Test invalid ATA chapter validation."""
        with pytest.raises(ValueError, match="Invalid ATA chapter"):
            ArtifactID(
                msn="MSN001",
                ata_chapter="999",  # Out of range
                lc_phase="LC02",
                artifact_type="REQ"
            )
    
    def test_invalid_lc_phase(self):
        """Test invalid LC phase validation."""
        with pytest.raises(ValueError, match="Invalid LC phase"):
            ArtifactID(
                msn="MSN001",
                ata_chapter="25",
                lc_phase="LC00",  # Invalid phase
                artifact_type="REQ"
            )
        
        with pytest.raises(ValueError, match="Invalid LC phase"):
            ArtifactID(
                msn="MSN001",
                ata_chapter="25",
                lc_phase="LC15",  # Out of range
                artifact_type="REQ"
            )
    
    def test_ata_in_chapter(self):
        """Test ATA IN (Infrastructure) chapter."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="IN",
            section="50",
            subject="00",
            lc_phase="LC10",
            artifact_type="IND",
            sequence="001"
        )
        assert "ATAIN-50-00" in artifact_id.to_compact()
    
    def test_get_phase_type(self):
        """Test phase type detection."""
        plm_artifact = ArtifactID(
            msn="MSN001",
            ata_chapter="25",
            lc_phase="LC02",
            artifact_type="REQ"
        )
        assert plm_artifact.get_phase_type() == PhaseType.PLM
        
        ops_artifact = ArtifactID(
            msn="MSN001",
            ata_chapter="25",
            lc_phase="LC12",
            artifact_type="SBL"
        )
        assert ops_artifact.get_phase_type() == PhaseType.OPS
    
    def test_get_ssot_root(self):
        """Test SSOT root directory determination."""
        plm_artifact = ArtifactID(
            msn="MSN001",
            ata_chapter="25",
            lc_phase="LC04",
            artifact_type="DES"
        )
        assert plm_artifact.get_ssot_root() == "KDB/LM/SSOT/PLM"
        
        ops_artifact = ArtifactID(
            msn="MSN001",
            ata_chapter="25",
            lc_phase="LC13",
            artifact_type="MSR"
        )
        assert ops_artifact.get_ssot_root() == "IDB/OPS/LM"


class TestIDParser:
    """Test IDParser class."""
    
    def test_parse_compact_format(self):
        """Test parsing compact format."""
        identifier = "AMPEL360_Q100_MSN001_ATA25-10-00_LC02_REQ_001"
        artifact_id = IDParser.parse(identifier)
        
        assert artifact_id is not None
        assert artifact_id.msn == "MSN001"
        assert artifact_id.ata_chapter == "25"
        assert artifact_id.section == "10"
        assert artifact_id.subject == "00"
        assert artifact_id.lc_phase == "LC02"
        assert artifact_id.artifact_type == "REQ"
        assert artifact_id.sequence == "001"
    
    def test_parse_hyphenated_format(self):
        """Test parsing hyphenated format."""
        identifier = "AMPEL360-Q100-MSN042-ATA28-10-00-LC04-DES-123"
        artifact_id = IDParser.parse(identifier)
        
        assert artifact_id is not None
        assert artifact_id.msn == "MSN042"
        assert artifact_id.ata_chapter == "28"
        assert artifact_id.lc_phase == "LC04"
        assert artifact_id.artifact_type == "DES"
        assert artifact_id.sequence == "123"
    
    def test_parse_urn_format(self):
        """Test parsing URN format."""
        identifier = "urn:ampel360:q100:msn001:ata71-11-00:lc06:tpr:003"
        artifact_id = IDParser.parse(identifier)
        
        assert artifact_id is not None
        assert artifact_id.msn == "MSN001"
        assert artifact_id.ata_chapter == "71"
        assert artifact_id.section == "11"
        assert artifact_id.lc_phase == "LC06"
        assert artifact_id.artifact_type == "TPR"
        assert artifact_id.sequence == "003"
    
    def test_parse_invalid_format(self):
        """Test parsing invalid format."""
        identifier = "INVALID_FORMAT_STRING"
        artifact_id = IDParser.parse(identifier)
        assert artifact_id is None
    
    def test_validate_valid_identifier(self):
        """Test validation of valid identifier."""
        identifier = "AMPEL360_Q100_MSN001_ATA25-10-00_LC02_REQ_001"
        is_valid, error = IDParser.validate(identifier)
        assert is_valid is True
        assert error is None
    
    def test_validate_invalid_identifier(self):
        """Test validation of invalid identifier."""
        identifier = "INVALID_FORMAT"
        is_valid, error = IDParser.validate(identifier)
        assert is_valid is False
        assert error is not None
    
    def test_parse_with_artifact_type_hyphen(self):
        """Test parsing artifact types with hyphens."""
        identifier = "AMPEL360_Q100_MSN001_ATA25-10-00_LC02_REQ-TRC_001"
        artifact_id = IDParser.parse(identifier)
        assert artifact_id is not None
        assert artifact_id.artifact_type == "REQ-TRC"


class TestIDGenerator:
    """Test IDGenerator class."""
    
    def test_generate_with_explicit_sequence(self):
        """Test generation with explicit sequence."""
        generator = IDGenerator()
        artifact_id = generator.generate(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ",
            sequence=5
        )
        assert artifact_id.sequence == "005"
    
    def test_generate_with_auto_sequence(self):
        """Test generation with auto-sequencing."""
        generator = IDGenerator()
        
        # First artifact
        artifact_id1 = generator.generate(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ"
        )
        assert artifact_id1.sequence == "001"
        
        # Second artifact (should auto-increment)
        artifact_id2 = generator.generate(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ"
        )
        assert artifact_id2.sequence == "002"
        
        # Different artifact type (should start at 1)
        artifact_id3 = generator.generate(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="DES"
        )
        assert artifact_id3.sequence == "001"
    
    def test_reset_sequence(self):
        """Test sequence counter reset."""
        generator = IDGenerator()
        
        # Generate some artifacts
        generator.generate(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ"
        )
        generator.generate(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ"
        )
        
        # Reset and verify
        generator.reset_sequence(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ"
        )
        
        artifact_id = generator.generate(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ"
        )
        assert artifact_id.sequence == "001"
    
    def test_sequence_out_of_range(self):
        """Test sequence number validation."""
        generator = IDGenerator()
        
        with pytest.raises(ValueError, match="Sequence must be 1-999"):
            generator.generate(
                msn="MSN001",
                ata_chapter="25",
                section="10",
                subject="00",
                lc_phase="LC02",
                artifact_type="REQ",
                sequence=0  # Invalid
            )
        
        with pytest.raises(ValueError, match="Sequence must be 1-999"):
            generator.generate(
                msn="MSN001",
                ata_chapter="25",
                section="10",
                subject="00",
                lc_phase="LC02",
                artifact_type="REQ",
                sequence=1000  # Invalid
            )


class TestConvenienceFunctions:
    """Test convenience functions."""
    
    def test_parse_identifier(self):
        """Test parse_identifier convenience function."""
        identifier = "AMPEL360_Q100_MSN001_ATA25-10-00_LC02_REQ_001"
        artifact_id = parse_identifier(identifier)
        assert artifact_id is not None
        assert artifact_id.artifact_type == "REQ"
    
    def test_validate_identifier(self):
        """Test validate_identifier convenience function."""
        valid_id = "AMPEL360_Q100_MSN001_ATA25-10-00_LC02_REQ_001"
        is_valid, error = validate_identifier(valid_id)
        assert is_valid is True
        
        invalid_id = "INVALID"
        is_valid, error = validate_identifier(invalid_id)
        assert is_valid is False
    
    def test_create_identifier(self):
        """Test create_identifier convenience function."""
        identifier = create_identifier(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ",
            sequence=1,
            format=IDFormat.COMPACT
        )
        assert identifier == "AMPEL360_Q100_MSN001_ATA25-10-00_LC02_REQ_001"
        
        # Test URN format
        urn = create_identifier(
            msn="MSN001",
            ata_chapter="25",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ",
            sequence=1,
            format=IDFormat.URN
        )
        assert urn == "urn:ampel360:q100:msn001:ata25-10-00:lc02:req:001"


class TestRealWorldExamples:
    """Test with real-world examples from CV-003."""
    
    def test_cryogenic_cell_requirement(self):
        """Test identifier for cryogenic cell requirement."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="28",
            section="10",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ",
            sequence="001"
        )
        assert "ATA28-10-00" in artifact_id.to_compact()
        assert artifact_id.get_phase_type() == PhaseType.PLM
    
    def test_fuel_cell_design(self):
        """Test identifier for fuel cell design."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="71",
            section="11",
            subject="00",
            lc_phase="LC04",
            artifact_type="DES",
            sequence="042"
        )
        assert "ATA71-11-00" in artifact_id.to_compact()
        assert artifact_id.get_ssot_root() == "KDB/LM/SSOT/PLM"
    
    def test_maintenance_source_record(self):
        """Test identifier for maintenance source record."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="28",
            section="40",
            subject="00",
            lc_phase="LC13",
            artifact_type="MSR",
            sequence="001"
        )
        assert artifact_id.get_phase_type() == PhaseType.OPS
        assert artifact_id.get_ssot_root() == "IDB/OPS/LM"
    
    def test_ai_model_artifact(self):
        """Test identifier for AI/ML model (ATA 95)."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="95",
            section="10",
            subject="00",
            lc_phase="LC05",
            artifact_type="MDL",
            sequence="001"
        )
        assert "ATA95-10-00" in artifact_id.to_compact()


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_all_lifecycle_phases(self):
        """Test all LC phases LC01-LC14."""
        for phase_num in range(1, 15):
            lc_phase = f"LC{phase_num:02d}"
            artifact_id = ArtifactID(
                msn="MSN001",
                ata_chapter="25",
                lc_phase=lc_phase,
                artifact_type="TEST"
            )
            assert artifact_id.lc_phase == lc_phase
    
    def test_boundary_ata_chapters(self):
        """Test boundary ATA chapters."""
        # Minimum
        artifact_id_min = ArtifactID(
            msn="MSN001",
            ata_chapter="00",
            lc_phase="LC01",
            artifact_type="GOV"
        )
        assert artifact_id_min.ata_chapter == "00"
        
        # Maximum
        artifact_id_max = ArtifactID(
            msn="MSN001",
            ata_chapter="98",
            lc_phase="LC14",
            artifact_type="EEL"
        )
        assert artifact_id_max.ata_chapter == "98"
    
    def test_maximum_sequence(self):
        """Test maximum sequence number."""
        artifact_id = ArtifactID(
            msn="MSN001",
            ata_chapter="25",
            lc_phase="LC02",
            artifact_type="REQ",
            sequence="999"
        )
        assert artifact_id.sequence == "999"
    
    def test_section_and_subject_boundaries(self):
        """Test section and subject boundary values."""
        # All zeros
        artifact_id_zeros = ArtifactID(
            msn="MSN001",
            ata_chapter="25",
            section="00",
            subject="00",
            lc_phase="LC02",
            artifact_type="REQ"
        )
        assert artifact_id_zeros.section == "00"
        assert artifact_id_zeros.subject == "00"
        
        # Maximum values
        artifact_id_max = ArtifactID(
            msn="MSN001",
            ata_chapter="25",
            section="99",
            subject="99",
            lc_phase="LC02",
            artifact_type="REQ"
        )
        assert artifact_id_max.section == "99"
        assert artifact_id_max.subject == "99"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
