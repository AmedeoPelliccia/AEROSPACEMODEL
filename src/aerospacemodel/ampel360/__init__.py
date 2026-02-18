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

__all__ = [
    "ArtifactID",
    "IDFormat",
    "PhaseType",
    "IDParser",
    "IDGenerator",
    "parse_identifier",
    "validate_identifier",
    "create_identifier",
]
