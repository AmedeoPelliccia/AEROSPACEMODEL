"""
Topology Module

Provides 3D mesh topology modelling for satellite constellations
governed by the AEROSPACEMODEL framework.  Supports multi-layer
orbital meshes, Topological Service Units (TSUs), functional layer
isolation, QoS-aware routing, and connectivity analysis.
"""

from aerospacemodel.topology.mesh import (
    TopologyError,
    ConnectivityError,
    RoutingError,
    TSUConfigurationError,
    OrbitalLayer,
    LinkType,
    FunctionalLayerType,
    NodeRole,
    QoSClass,
    QoSProfile,
    TopologicalServiceUnit,
    MeshNode,
    MeshLink,
    FunctionalLayer,
    Mesh3DTopology,
)

__all__ = [
    # Exceptions
    "TopologyError",
    "ConnectivityError",
    "RoutingError",
    "TSUConfigurationError",
    # Enumerations
    "OrbitalLayer",
    "LinkType",
    "FunctionalLayerType",
    "NodeRole",
    "QoSClass",
    # Data structures
    "QoSProfile",
    "TopologicalServiceUnit",
    "MeshNode",
    "MeshLink",
    "FunctionalLayer",
    # Manager
    "Mesh3DTopology",
]
