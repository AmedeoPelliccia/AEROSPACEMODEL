"""
Data Lifecycle Module

Implements the data lifecycle framework for the AEROSPACEMODEL architecture,
covering data generation, classification, transmission, processing, and
consumption across aerospace network nodes.
"""

from __future__ import annotations

from .lifecycle import (
    DataLifecycleError,
    ClassificationError,
    RoutingError,
    ProcessingError,
    LifecycleStage,
    DataClass,
    SecurityDomain,
    ProcessingLocation,
    DataOriginType,
    ConsumptionAction,
    DataClassification,
    QoSAssignment,
    ProcessingDirective,
    DataRecord,
    DataLifecycleManager,
)

__all__ = [
    # Exceptions
    "DataLifecycleError",
    "ClassificationError",
    "RoutingError",
    "ProcessingError",
    # Enumerations
    "LifecycleStage",
    "DataClass",
    "SecurityDomain",
    "ProcessingLocation",
    "DataOriginType",
    "ConsumptionAction",
    # Dataclasses
    "DataClassification",
    "QoSAssignment",
    "ProcessingDirective",
    "DataRecord",
    # Manager
    "DataLifecycleManager",
]
