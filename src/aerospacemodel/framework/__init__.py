"""
Framework Module — Unified 3-Axis Cube

Implements the unified cube framework for AEROSPACEMODEL, representing
the intersection of data lifecycle, topology, and domains/layers as a
three-dimensional decision space.
"""

from __future__ import annotations

from .cube import (
    FrameworkError,
    CellConfigurationError,
    ProfileValidationError,
    ServiceProfile,
    SecurityProfile,
    ModelRole,
    CubeCell,
    UnifiedFramework,
)

__all__ = [
    # Exceptions
    "FrameworkError",
    "CellConfigurationError",
    "ProfileValidationError",
    # Dataclasses
    "ServiceProfile",
    "SecurityProfile",
    "ModelRole",
    "CubeCell",
    # Manager
    "UnifiedFramework",
]
