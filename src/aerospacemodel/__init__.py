"""
AEROSPACEMODEL
==============

ASIT + ASIGT: Aircraft Systems Information Transponders

Transform governed aerospace engineering knowledge into 
industry-standard technical publications.

Architecture:
    - ASIT: Aircraft Systems Information Transponder
            Governance, structure, lifecycle authority
    - ASIGT: Aircraft Systems Information Generative Transponder
             Content generation under ASIT control
    - TDMS: Total Document Management System
            Hybrid human+machine dual-plane representation

Quick Start:
    >>> from aerospacemodel import ASIT, ASIGT, Contract
    >>> 
    >>> # ASIT governs
    >>> asit = ASIT(config_path="ASIT/config/asit_config.yaml")
    >>> contract = Contract.load("ASIT/CONTRACTS/active/KITDM-CTR-LM-CSDB_ATA28.yaml")
    >>> 
    >>> # ASIGT executes under ASIT control
    >>> asigt = ASIGT(asit_instance=asit)
    >>> result = asigt.execute(contract, baseline="FBL-2026-Q1-003")
    >>> 
    >>> if result.success:
    ...     print(f"Generated {result.output_count} artifacts")
    ...     print(f"Trace coverage: {result.trace_coverage}%")

TDMS Usage (Total Document Management System):
    >>> from aerospacemodel.tdms import HumanPlane, MachinePlane, TDMSConverter
    >>> 
    >>> # Load from human-readable YAML (source of truth)
    >>> human = HumanPlane.load("contract.yaml")
    >>> 
    >>> # Convert to token-efficient format for AI agents
    >>> converter = TDMSConverter()
    >>> machine = converter.to_machine_plane(human)
    >>> machine.to_tsv("contract_compact.tsv")

CLI Usage:
    $ aerospacemodel init --program "MyAircraft" --model-code "MA"
    $ aerospacemodel run --contract KITDM-CTR-LM-CSDB_ATA28
    $ aerospacemodel validate --contract KITDM-CTR-LM-CSDB_ATA28
    $ aerospacemodel tdms convert --input contract.yaml --output compact.tsv

Constraint:
    ASIGT cannot operate standalone. It executes ONLY through
    ASIT contracts, baselines, and governance rules.

Documentation:
    https://docs.aerospacemodel.io

License:
    Apache License 2.0

Copyright:
    2024-2026 AEROSPACEMODEL Contributors
"""

__version__ = "2.0.0"
__author__ = "AEROSPACEMODEL Contributors"
__license__ = "Apache-2.0"

# ═══════════════════════════════════════════════════════════════════════════
# ASIT — Governance Authority Layer
# ═══════════════════════════════════════════════════════════════════════════

from aerospacemodel.asit import (
    ASIT,
    Contract,
    ContractStatus,
    Baseline,
    BaselineType,
    Governance,
    ChangeRequest,
    ChangeOrder,
)

# ═══════════════════════════════════════════════════════════════════════════
# ASIGT — Content Generation Layer (ASIT-controlled)
# ═══════════════════════════════════════════════════════════════════════════

from aerospacemodel.asigt import (
    ASIGT,
    RunResult,
    RunStatus,
    ValidationReport,
    TraceMatrix,
)

# ═══════════════════════════════════════════════════════════════════════════
# EXCEPTIONS
# ═══════════════════════════════════════════════════════════════════════════

from aerospacemodel.exceptions import (
    AerospaceModelError,
    ASITError,
    ASIGTError,
    ContractError,
    BaselineError,
    ValidationError,
    TraceError,
)

# ═══════════════════════════════════════════════════════════════════════════
# TDMS — Total Document Management System (Human + Machine Planes)
# ═══════════════════════════════════════════════════════════════════════════

from aerospacemodel.tdms import (
    HumanPlane,
    MachinePlane,
    PlaneType,
    TDMSConverter,
    ConversionResult,
    ConversionStatus,
    TDMSDictionary,
    DictionaryRegistry,
    DictionaryType,
    TSVFormat,
    CSVFormat,
    LineProtocolFormat,
    FormatType,
    TDMSError,
)

# ═══════════════════════════════════════════════════════════════════════════
# PUBLIC API
# ═══════════════════════════════════════════════════════════════════════════

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__license__",
    
    # ASIT (Governance)
    "ASIT",
    "Contract",
    "ContractStatus",
    "Baseline",
    "BaselineType",
    "Governance",
    "ChangeRequest",
    "ChangeOrder",
    
    # ASIGT (Generation)
    "ASIGT",
    "RunResult",
    "RunStatus",
    "ValidationReport",
    "TraceMatrix",
    
    # TDMS (Total Document Management System)
    "HumanPlane",
    "MachinePlane",
    "PlaneType",
    "TDMSConverter",
    "ConversionResult",
    "ConversionStatus",
    "TDMSDictionary",
    "DictionaryRegistry",
    "DictionaryType",
    "TSVFormat",
    "CSVFormat",
    "LineProtocolFormat",
    "FormatType",
    "TDMSError",
    
    # Exceptions
    "AerospaceModelError",
    "ASITError",
    "ASIGTError",
    "ContractError",
    "BaselineError",
    "ValidationError",
    "TraceError",
]


def get_version() -> str:
    """Return the AEROSPACEMODEL version string."""
    return __version__
