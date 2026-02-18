"""
AMPEL360 Q100 PBS/WBS Linkage Module

This module implements Product Breakdown Structure (PBS) and Work Breakdown
Structure (WBS) linkage per CV-003 specification.

PBS Grammar:
    PBS-{AXIS}{SUBDOM}-{ATA}-{SECTION}-{SUBJECT}-{ITEM}
    
WBS Grammar:
    WBS-{PHASE_CODE}-{HIERARCHY}

Author: ASIT (Aircraft Systems Information Transponder)
Document: AMPEL360-CV-003 v3.0
Date: 2026-02-18
"""

import re
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


class OPTINAxis(Enum):
    """OPT-IN Framework primary domains."""
    O = "O"  # Organizations
    P = "P"  # Programs
    T = "T"  # Technologies
    I = "I"  # Infrastructures
    N = "N"  # Neural Networks


# OPT-IN Sub-domain codes mapping
SUBDOMAIN_CODES = {
    "O": ["A", "B"],  # Authoritative, Business Enforcement
    "P": ["P", "S"],  # Product Definition, Service Instruction
    "T": ["A", "M", "E1", "D", "I", "E2", "E3", "L1", "L2", "C1", 
          "C2", "I2", "A2", "O", "P"],  # Technology subdomains
    "I": ["M1", "M2", "O"],  # Infrastructure subdomains
    "N": ["D", "A", "P*"],  # Neural Network subdomains
}

# Novel Technology designations
NOVEL_TECHNOLOGY_SUBDOMAINS = ["C2", "I2", "P"]

# WBS Phase codes mapping to TLI v2.1
WBS_PHASE_CODES = {
    "LC01": "PRB",  # Problem Statement
    "LC02": "REQ",  # System Requirements
    "LC03": "SAF",  # Safety & Reliability
    "LC04": "DES",  # Design Definition
    "LC05": "ANA",  # Analysis Models
    "LC06": "VER",  # Integration & Test
    "LC07": "QAP",  # QA & Process Compliance
    "LC08": "CRT",  # Certification
    "LC09": "ESG",  # ESG & Sustainability
    "LC10": "IND",  # Industrial & Supply Chain
    "LC11": "OPC",  # Operations Customization
    "LC12": "MRO",  # Continued Airworthiness & MRO
    "LC13": "MSD",  # Maintenance Source Data
    "LC14": "EOL",  # End of Life
}

# Reverse mapping, including cross-cutting PUB phase code with no LC phase
PHASE_CODE_TO_LC = {v: k for k, v in WBS_PHASE_CODES.items()}
PHASE_CODE_TO_LC["PUB"] = None


@dataclass
class PBSID:
    """
    Product Breakdown Structure Identifier.
    
    Format: PBS-{AXIS}{SUBDOM}-{ATA}-{SECTION}-{SUBJECT}-{ITEM}
    Example: PBS-TC2-ATA28-10-00-CRYO_TANK_FWD
    """
    axis: str  # O, P, T, I, N
    subdomain: str  # Sub-domain code (A, B, C2, M1, etc.)
    ata_chapter: str  # ATA chapter (00-98, IN)
    section: str  # Section code (00-99)
    subject: str  # Subject code (00-99)
    item_name: str  # Item identifier (uppercase with underscores)
    
    def __post_init__(self):
        """Validate PBS ID components after initialization."""
        self._validate()
    
    def _validate(self):
        """Validate all PBS ID components."""
        # Axis validation
        if self.axis not in [e.value for e in OPTINAxis]:
            raise ValueError(f"Invalid axis: {self.axis}. Must be O, P, T, I, or N")
        
        # Sub-domain validation
        valid_subdomains = SUBDOMAIN_CODES.get(self.axis, [])
        if self.subdomain not in valid_subdomains:
            raise ValueError(
                f"Invalid subdomain '{self.subdomain}' for axis '{self.axis}'. "
                f"Valid options: {valid_subdomains}"
            )
        
        # ATA chapter validation
        if not re.match(r'^(\d{2}|IN)$', self.ata_chapter):
            raise ValueError(f"Invalid ATA chapter: {self.ata_chapter}")
        if self.ata_chapter != "IN":
            ata_value = int(self.ata_chapter)
            if ata_value < 0 or ata_value > 98:
                raise ValueError(
                    f"Invalid ATA chapter: {self.ata_chapter}. Must be between 00 and 98, or 'IN'"
                )
        
        # Section and subject validation
        if not re.match(r'^\d{2}$', self.section):
            raise ValueError(f"Invalid section: {self.section}")
        if not re.match(r'^\d{2}$', self.subject):
            raise ValueError(f"Invalid subject: {self.subject}")
        
        # Item name validation (uppercase alphanumeric with underscores)
        if not re.match(r'^[A-Z0-9_]+$', self.item_name):
            raise ValueError(
                f"Invalid item name: {self.item_name}. "
                "Must be uppercase alphanumeric with underscores"
            )
    
    def to_string(self) -> str:
        """
        Generate PBS ID string.
        
        Returns:
            PBS-TC2-ATA28-10-00-CRYO_TANK_FWD
        """
        return (f"PBS-{self.axis}{self.subdomain}-"
                f"ATA{self.ata_chapter}-{self.section}-{self.subject}-"
                f"{self.item_name}")
    
    def __str__(self) -> str:
        """String representation."""
        return self.to_string()
    
    def is_novel_technology(self) -> bool:
        """
        Check if this PBS belongs to a Novel Technology subdomain.
        
        Returns:
            True if subdomain is C2, I2, or P
        """
        return self.subdomain in NOVEL_TECHNOLOGY_SUBDOMAINS
    
    def get_ata_path(self) -> str:
        """
        Get ATA path component.
        
        Returns:
            ATA{cc}-{ss}-{ss}
        """
        return f"ATA{self.ata_chapter}-{self.section}-{self.subject}"


@dataclass
class WBSID:
    """
    Work Breakdown Structure Identifier.
    
    Format: WBS-{PHASE_CODE}-{HIERARCHY}
    Example: WBS-REQ-1.2.3, WBS-DES-2.4.1
    """
    phase_code: str  # PRB, REQ, SAF, DES, etc.
    hierarchy: str  # Hierarchical numbering (e.g., 1.2.3)
    
    def __post_init__(self):
        """Validate WBS ID components after initialization."""
        self._validate()
    
    def _validate(self):
        """Validate all WBS ID components."""
        # Phase code validation
        if self.phase_code not in PHASE_CODE_TO_LC:
            raise ValueError(
                f"Invalid phase code: {self.phase_code}. "
                f"Valid options: {list(PHASE_CODE_TO_LC.keys())}"
            )
        
        # Hierarchy validation (numeric dot-separated)
        if not re.match(r'^\d+(\.\d+)*$', self.hierarchy):
            raise ValueError(
                f"Invalid hierarchy: {self.hierarchy}. "
                "Must be numeric dot-separated (e.g., 1.2.3)"
            )
    
    def to_string(self) -> str:
        """
        Generate WBS ID string.
        
        Returns:
            WBS-REQ-1.2.3
        """
        return f"WBS-{self.phase_code}-{self.hierarchy}"
    
    def __str__(self) -> str:
        """String representation."""
        return self.to_string()
    
    def get_lc_phase(self) -> str:
        """
        Get corresponding lifecycle phase.
        
        Returns:
            LC code (e.g., LC02)
        """
        return PHASE_CODE_TO_LC[self.phase_code]
    
    def get_level(self) -> int:
        """
        Get WBS hierarchy level.
        
        Returns:
            Number of levels (e.g., 1.2.3 -> 3)
        """
        return len(self.hierarchy.split('.'))
    
    def get_parent(self) -> Optional['WBSID']:
        """
        Get parent WBS ID.
        
        Returns:
            Parent WBSID or None if at root level
        """
        parts = self.hierarchy.split('.')
        if len(parts) <= 1:
            return None
        parent_hierarchy = '.'.join(parts[:-1])
        return WBSID(phase_code=self.phase_code, hierarchy=parent_hierarchy)


class PBSParser:
    """Parse PBS identifiers."""
    
    PBS_PATTERN = re.compile(
        r'^PBS-([OPTIN])([A-Z0-9\*]+)-ATA(\d{2}|IN)-(\d{2})-(\d{2})-([A-Z0-9_]+)$'
    )
    
    @classmethod
    def parse(cls, pbs_string: str) -> Optional[PBSID]:
        """
        Parse a PBS identifier string.
        
        Args:
            pbs_string: PBS identifier string
            
        Returns:
            PBSID object or None if parsing fails
        """
        match = cls.PBS_PATTERN.match(pbs_string)
        if not match:
            return None
        
        axis, subdomain, ata, section, subject, item = match.groups()
        
        try:
            return PBSID(
                axis=axis,
                subdomain=subdomain,
                ata_chapter=ata,
                section=section,
                subject=subject,
                item_name=item
            )
        except ValueError:
            return None
    
    @classmethod
    def validate(cls, pbs_string: str) -> bool:
        """Validate a PBS identifier string."""
        return cls.parse(pbs_string) is not None


class WBSParser:
    """Parse WBS identifiers."""
    
    WBS_PATTERN = re.compile(
        r'^WBS-([A-Z]{3})-(\d+(?:\.\d+)*)$'
    )
    
    @classmethod
    def parse(cls, wbs_string: str) -> Optional[WBSID]:
        """
        Parse a WBS identifier string.
        
        Args:
            wbs_string: WBS identifier string
            
        Returns:
            WBSID object or None if parsing fails
        """
        match = cls.WBS_PATTERN.match(wbs_string)
        if not match:
            return None
        
        phase_code, hierarchy = match.groups()
        
        try:
            return WBSID(
                phase_code=phase_code,
                hierarchy=hierarchy
            )
        except ValueError:
            return None
    
    @classmethod
    def validate(cls, wbs_string: str) -> bool:
        """Validate a WBS identifier string."""
        return cls.parse(wbs_string) is not None


class PBSWBSLinker:
    """Link PBS and WBS structures."""
    
    def __init__(self):
        """Initialize the linker."""
        self._links = {}  # {pbs_id: [wbs_ids]}
    
    def link(self, pbs_id: str, wbs_id: str):
        """
        Create a link between PBS and WBS.
        
        Args:
            pbs_id: PBS identifier string
            wbs_id: WBS identifier string
        """
        if not PBSParser.validate(pbs_id):
            raise ValueError(f"Invalid PBS ID: {pbs_id}")
        if not WBSParser.validate(wbs_id):
            raise ValueError(f"Invalid WBS ID: {wbs_id}")
        
        if pbs_id not in self._links:
            self._links[pbs_id] = []
        if wbs_id not in self._links[pbs_id]:
            self._links[pbs_id].append(wbs_id)
    
    def get_wbs_for_pbs(self, pbs_id: str) -> List[str]:
        """
        Get all WBS elements linked to a PBS element.
        
        Args:
            pbs_id: PBS identifier string
            
        Returns:
            List of linked WBS identifiers
        """
        return self._links.get(pbs_id, [])
    
    def get_pbs_for_wbs(self, wbs_id: str) -> List[str]:
        """
        Get all PBS elements linked to a WBS element.
        
        Args:
            wbs_id: WBS identifier string
            
        Returns:
            List of linked PBS identifiers
        """
        return [pbs for pbs, wbs_list in self._links.items() if wbs_id in wbs_list]


# Convenience functions

def create_pbs_id(axis: str, subdomain: str, ata_chapter: str, 
                  section: str, subject: str, item_name: str) -> str:
    """
    Create a PBS identifier string.
    
    Args:
        axis: OPT-IN axis (O, P, T, I, N)
        subdomain: Sub-domain code
        ata_chapter: ATA chapter
        section: Section code
        subject: Subject code
        item_name: Item identifier
        
    Returns:
        PBS identifier string
    """
    pbs = PBSID(
        axis=axis,
        subdomain=subdomain,
        ata_chapter=ata_chapter,
        section=section,
        subject=subject,
        item_name=item_name
    )
    return pbs.to_string()


def create_wbs_id(lc_phase: str, hierarchy: str) -> str:
    """
    Create a WBS identifier string from LC phase.
    
    Args:
        lc_phase: Lifecycle phase (LC01-LC14)
        hierarchy: WBS hierarchy (e.g., 1.2.3)
        
    Returns:
        WBS identifier string
    """
    if lc_phase not in WBS_PHASE_CODES:
        raise ValueError(f"Invalid LC phase: {lc_phase}")
    
    phase_code = WBS_PHASE_CODES[lc_phase]
    wbs = WBSID(phase_code=phase_code, hierarchy=hierarchy)
    return wbs.to_string()


def parse_pbs(pbs_string: str) -> Optional[PBSID]:
    """Parse a PBS identifier string."""
    return PBSParser.parse(pbs_string)


def parse_wbs(wbs_string: str) -> Optional[WBSID]:
    """Parse a WBS identifier string."""
    return WBSParser.parse(wbs_string)
