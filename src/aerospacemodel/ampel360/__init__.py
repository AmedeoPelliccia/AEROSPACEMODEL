"""
AMPEL360 Q100 Module

This package provides utilities for working with AMPEL360 Q100 artifacts,
including identifier grammar, metadata validation, and PBS/WBS linkage.

Author: ASIT (Aircraft Systems Information Transponder)
Document: AMPEL360-CV-003 v3.0
"""

__version__ = "3.0.0"

from .identifiers import (
    ArtifactID,
    IDFormat,
    PhaseType,
    IDParser,
    IDGenerator,
    parse_identifier,
    validate_identifier,
    create_identifier,
)

from .pbs_wbs import (
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

__all__ = [
    # Identifiers
    "ArtifactID",
    "IDFormat",
    "PhaseType",
    "IDParser",
    "IDGenerator",
    "parse_identifier",
    "validate_identifier",
    "create_identifier",
    # PBS/WBS
    "PBSID",
    "WBSID",
    "OPTINAxis",
    "PBSParser",
    "WBSParser",
    "PBSWBSLinker",
    "create_pbs_id",
    "create_wbs_id",
    "parse_pbs",
    "parse_wbs",
    "WBS_PHASE_CODES",
    "SUBDOMAIN_CODES",
    "NOVEL_TECHNOLOGY_SUBDOMAINS",
]
