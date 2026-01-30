"""
TDMS Dictionary Module
======================

Provides ID-based disambiguation dictionaries for efficient token representation.

The dictionary system allows:
    - Compact ID references instead of full strings
    - Consistent disambiguation across documents
    - Bidirectional lookup (ID ↔ value)
    - Type-specific dictionaries for different domains

Dictionary Types:
    - ATA: ATA chapter codes and descriptions
    - S1000D: S1000D element codes
    - PUBLICATION: Publication type codes
    - ARTIFACT: Artifact type codes  
    - STATUS: Status codes
    - STAKEHOLDER: Stakeholder codes
    - CUSTOM: User-defined dictionaries

Example:
    >>> dict_ata = TDMSDictionary.load_ata()
    >>> dict_ata.get_value("28")
    'Fuel'
    >>> dict_ata.get_id("Fuel")
    '28'
"""

from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple, Union

import yaml

from aerospacemodel.tdms.exceptions import DictionaryError

logger = logging.getLogger(__name__)


class DictionaryType(Enum):
    """Types of TDMS dictionaries."""
    ATA = "ata"                     # ATA chapter codes
    S1000D = "s1000d"               # S1000D codes
    PUBLICATION = "publication"     # Publication types
    ARTIFACT = "artifact"           # Artifact types
    STATUS = "status"               # Status codes
    STAKEHOLDER = "stakeholder"     # Stakeholder roles
    BASELINE = "baseline"           # Baseline types
    LIFECYCLE = "lifecycle"         # Lifecycle phases
    SEVERITY = "severity"           # Severity levels
    CUSTOM = "custom"               # User-defined


@dataclass
class DictionaryEntry:
    """
    A single entry in a TDMS dictionary.
    
    Attributes:
        id: Short compact ID (e.g., "28", "AMM", "FBL")
        value: Full human-readable value (e.g., "Fuel", "Aircraft Maintenance Manual")
        description: Optional detailed description
        metadata: Optional additional metadata
    """
    id: str
    value: str
    description: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert entry to dictionary representation."""
        result = {"id": self.id, "value": self.value}
        if self.description:
            result["description"] = self.description
        if self.metadata:
            result["metadata"] = self.metadata
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> DictionaryEntry:
        """Create entry from dictionary representation."""
        return cls(
            id=data["id"],
            value=data["value"],
            description=data.get("description", ""),
            metadata=data.get("metadata", {}),
        )


@dataclass
class TDMSDictionary:
    """
    TDMS Dictionary for ID-value disambiguation.
    
    Provides bidirectional lookup between compact IDs and full values.
    Used to minimize token usage while maintaining semantic clarity.
    
    Attributes:
        name: Dictionary name
        dict_type: Type of dictionary
        version: Dictionary version
        entries: List of dictionary entries
        
    Example:
        >>> dict_pub = TDMSDictionary(
        ...     name="Publication Types",
        ...     dict_type=DictionaryType.PUBLICATION,
        ...     version="1.0.0"
        ... )
        >>> dict_pub.add("AMM", "Aircraft Maintenance Manual")
        >>> dict_pub.add("SRM", "Structural Repair Manual")
        >>> dict_pub.get_value("AMM")
        'Aircraft Maintenance Manual'
    """
    name: str
    dict_type: DictionaryType
    version: str = "1.0.0"
    entries: List[DictionaryEntry] = field(default_factory=list)
    description: str = ""
    created: Optional[datetime] = None
    
    # Internal lookup indices
    _id_to_entry: Dict[str, DictionaryEntry] = field(default_factory=dict, repr=False)
    _value_to_entry: Dict[str, DictionaryEntry] = field(default_factory=dict, repr=False)
    
    def __post_init__(self) -> None:
        """Build indices after initialization."""
        self._rebuild_indices()
        if self.created is None:
            self.created = datetime.now()
    
    def _rebuild_indices(self) -> None:
        """Rebuild lookup indices from entries."""
        self._id_to_entry = {}
        self._value_to_entry = {}
        for entry in self.entries:
            self._id_to_entry[entry.id] = entry
            # Normalize value for case-insensitive lookup
            self._value_to_entry[entry.value.lower()] = entry
    
    def add(
        self,
        id: str,
        value: str,
        description: str = "",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> DictionaryEntry:
        """
        Add a new entry to the dictionary.
        
        Args:
            id: Compact ID
            value: Full value
            description: Optional description
            metadata: Optional metadata
            
        Returns:
            The created entry
            
        Raises:
            DictionaryError: If ID already exists
        """
        if id in self._id_to_entry:
            raise DictionaryError(f"ID '{id}' already exists in dictionary '{self.name}'")
        
        entry = DictionaryEntry(
            id=id,
            value=value,
            description=description,
            metadata=metadata or {},
        )
        self.entries.append(entry)
        self._id_to_entry[id] = entry
        self._value_to_entry[value.lower()] = entry
        return entry
    
    def get_entry(self, id: str) -> Optional[DictionaryEntry]:
        """Get entry by ID."""
        return self._id_to_entry.get(id)
    
    def get_value(self, id: str) -> str:
        """
        Get value by ID.
        
        Args:
            id: The compact ID
            
        Returns:
            The full value
            
        Raises:
            DictionaryError: If ID not found
        """
        entry = self._id_to_entry.get(id)
        if entry is None:
            raise DictionaryError(f"ID '{id}' not found in dictionary '{self.name}'")
        return entry.value
    
    def get_id(self, value: str) -> str:
        """
        Get ID by value (case-insensitive).
        
        Args:
            value: The full value
            
        Returns:
            The compact ID
            
        Raises:
            DictionaryError: If value not found
        """
        entry = self._value_to_entry.get(value.lower())
        if entry is None:
            raise DictionaryError(f"Value '{value}' not found in dictionary '{self.name}'")
        return entry.id
    
    def has_id(self, id: str) -> bool:
        """Check if ID exists in dictionary."""
        return id in self._id_to_entry
    
    def has_value(self, value: str) -> bool:
        """Check if value exists in dictionary (case-insensitive)."""
        return value.lower() in self._value_to_entry
    
    def __len__(self) -> int:
        """Return number of entries."""
        return len(self.entries)
    
    def __iter__(self) -> Iterator[DictionaryEntry]:
        """Iterate over entries."""
        return iter(self.entries)
    
    def __contains__(self, item: str) -> bool:
        """Check if ID is in dictionary."""
        return self.has_id(item)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert dictionary to serializable format."""
        return {
            "name": self.name,
            "type": self.dict_type.value,
            "version": self.version,
            "description": self.description,
            "created": self.created.isoformat() if self.created else None,
            "entries": [e.to_dict() for e in self.entries],
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> TDMSDictionary:
        """Create dictionary from serializable format."""
        entries = [DictionaryEntry.from_dict(e) for e in data.get("entries", [])]
        created = None
        if data.get("created"):
            created = datetime.fromisoformat(data["created"])
        
        return cls(
            name=data["name"],
            dict_type=DictionaryType(data["type"]),
            version=data.get("version", "1.0.0"),
            description=data.get("description", ""),
            created=created,
            entries=entries,
        )
    
    def save(self, path: Union[str, Path], format: str = "yaml") -> None:
        """
        Save dictionary to file.
        
        Args:
            path: Output file path
            format: Output format ('yaml' or 'json')
        """
        path = Path(path)
        data = self.to_dict()
        
        with open(path, "w", encoding="utf-8") as f:
            if format == "yaml":
                yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)
            elif format == "json":
                json.dump(data, f, indent=2)
            else:
                raise DictionaryError(f"Unsupported format: {format}")
        
        logger.info(f"Dictionary '{self.name}' saved to {path}")
    
    @classmethod
    def load(cls, path: Union[str, Path]) -> TDMSDictionary:
        """
        Load dictionary from file.
        
        Args:
            path: Input file path (YAML or JSON)
            
        Returns:
            Loaded dictionary
        """
        path = Path(path)
        
        with open(path, "r", encoding="utf-8") as f:
            if path.suffix in [".yaml", ".yml"]:
                data = yaml.safe_load(f)
            elif path.suffix == ".json":
                data = json.load(f)
            else:
                raise DictionaryError(f"Unsupported file format: {path.suffix}")
        
        return cls.from_dict(data)
    
    def to_compact_map(self) -> Dict[str, str]:
        """
        Export as simple ID→value map.
        
        Returns:
            Dictionary mapping IDs to values
        """
        return {e.id: e.value for e in self.entries}
    
    def compute_hash(self) -> str:
        """Compute hash of dictionary content for integrity checking."""
        content = json.dumps(self.to_dict(), sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    # =========================================================================
    # FACTORY METHODS FOR STANDARD DICTIONARIES
    # =========================================================================
    
    @classmethod
    def create_ata_dictionary(cls) -> TDMSDictionary:
        """
        Create standard ATA chapter dictionary.
        
        Returns:
            Dictionary with ATA iSpec 2200 chapter codes
        """
        dict_ata = cls(
            name="ATA Chapters",
            dict_type=DictionaryType.ATA,
            version="1.0.0",
            description="ATA iSpec 2200 chapter codes and descriptions",
        )
        
        # Core ATA chapters
        ata_chapters = [
            ("00", "General"),
            ("05", "Time Limits/Maintenance Checks"),
            ("06", "Dimensions and Areas"),
            ("07", "Lifting and Shoring"),
            ("08", "Leveling and Weighing"),
            ("09", "Towing and Taxiing"),
            ("10", "Parking, Mooring, Storage and Return to Service"),
            ("11", "Placards and Markings"),
            ("12", "Servicing"),
            ("20", "Standard Practices — Airframe"),
            ("21", "Air Conditioning"),
            ("22", "Auto Flight"),
            ("23", "Communications"),
            ("24", "Electrical Power"),
            ("25", "Equipment/Furnishings"),
            ("26", "Fire Protection"),
            ("27", "Flight Controls"),
            ("28", "Fuel"),
            ("29", "Hydraulic Power"),
            ("30", "Ice and Rain Protection"),
            ("31", "Indicating/Recording Systems"),
            ("32", "Landing Gear"),
            ("33", "Lights"),
            ("34", "Navigation"),
            ("35", "Oxygen"),
            ("36", "Pneumatic"),
            ("37", "Vacuum"),
            ("38", "Water/Waste"),
            ("45", "Central Maintenance System"),
            ("46", "Information Systems"),
            ("49", "Airborne Auxiliary Power"),
            ("51", "Standard Practices — Structures"),
            ("52", "Doors"),
            ("53", "Fuselage"),
            ("54", "Nacelles/Pylons"),
            ("55", "Stabilizers"),
            ("56", "Windows"),
            ("57", "Wings"),
            ("71", "Power Plant"),
            ("72", "Engine"),
            ("73", "Engine Fuel and Control"),
            ("74", "Ignition"),
            ("75", "Air"),
            ("76", "Engine Controls"),
            ("77", "Engine Indicating"),
            ("78", "Exhaust"),
            ("79", "Oil"),
            ("80", "Starting"),
        ]
        
        for code, description in ata_chapters:
            dict_ata.add(code, description)
        
        return dict_ata
    
    @classmethod
    def create_publication_dictionary(cls) -> TDMSDictionary:
        """
        Create standard publication type dictionary.
        
        Returns:
            Dictionary with publication type codes
        """
        dict_pub = cls(
            name="Publication Types",
            dict_type=DictionaryType.PUBLICATION,
            version="1.0.0",
            description="Standard aerospace publication types",
        )
        
        publications = [
            ("AMM", "Aircraft Maintenance Manual"),
            ("SRM", "Structural Repair Manual"),
            ("CMM", "Component Maintenance Manual"),
            ("IPC", "Illustrated Parts Catalog"),
            ("FCOM", "Flight Crew Operating Manual"),
            ("TSM", "Troubleshooting Manual"),
            ("WDM", "Wiring Diagram Manual"),
            ("SB", "Service Bulletin"),
            ("IETP", "Interactive Electronic Technical Publication"),
            ("CSDB", "Common Source Database"),
            ("AFM", "Aircraft Flight Manual"),
            ("MEL", "Minimum Equipment List"),
            ("QRH", "Quick Reference Handbook"),
        ]
        
        for code, description in publications:
            dict_pub.add(code, description)
        
        return dict_pub
    
    @classmethod
    def create_status_dictionary(cls) -> TDMSDictionary:
        """
        Create standard status code dictionary.
        
        Returns:
            Dictionary with status codes
        """
        dict_status = cls(
            name="Status Codes",
            dict_type=DictionaryType.STATUS,
            version="1.0.0",
            description="Document and contract status codes",
        )
        
        statuses = [
            ("DFT", "Draft"),
            ("REV", "Review"),
            ("APV", "Approved"),
            ("ACT", "Active"),
            ("SUP", "Superseded"),
            ("WTH", "Withdrawn"),
            ("PND", "Pending"),
            ("RUN", "Running"),
            ("SUC", "Success"),
            ("FAL", "Failed"),
            ("PAR", "Partial"),
            ("CAN", "Cancelled"),
        ]
        
        for code, description in statuses:
            dict_status.add(code, description)
        
        return dict_status
    
    @classmethod
    def create_stakeholder_dictionary(cls) -> TDMSDictionary:
        """
        Create standard stakeholder role dictionary.
        
        Returns:
            Dictionary with stakeholder codes
        """
        dict_stake = cls(
            name="Stakeholder Roles",
            dict_type=DictionaryType.STAKEHOLDER,
            version="1.0.0",
            description="ASIT stakeholder role codes",
        )
        
        stakeholders = [
            ("ENG", "Engineering"),
            ("CM", "Configuration Management"),
            ("QA", "Quality Assurance"),
            ("CERT", "Certification"),
            ("OPS", "Operations"),
            ("MRO", "Maintenance, Repair, Overhaul"),
            ("TRN", "Training"),
            ("SUP", "Supply Chain"),
        ]
        
        for code, description in stakeholders:
            dict_stake.add(code, description)
        
        return dict_stake
    
    @classmethod
    def create_baseline_dictionary(cls) -> TDMSDictionary:
        """
        Create standard baseline type dictionary.
        
        Returns:
            Dictionary with baseline type codes
        """
        dict_base = cls(
            name="Baseline Types",
            dict_type=DictionaryType.BASELINE,
            version="1.0.0",
            description="ASIT baseline type codes",
        )
        
        baselines = [
            ("FBL", "Functional Baseline"),
            ("ABL", "Allocated Baseline"),
            ("PBL", "Product Baseline"),
            ("OBL", "Operational Baseline"),
            ("DBL", "Documentation Baseline"),
        ]
        
        for code, description in baselines:
            dict_base.add(code, description)
        
        return dict_base
    
    @classmethod
    def create_all_standard_dictionaries(cls) -> Dict[DictionaryType, TDMSDictionary]:
        """
        Create all standard TDMS dictionaries.
        
        Returns:
            Dictionary mapping types to their dictionaries
        """
        return {
            DictionaryType.ATA: cls.create_ata_dictionary(),
            DictionaryType.PUBLICATION: cls.create_publication_dictionary(),
            DictionaryType.STATUS: cls.create_status_dictionary(),
            DictionaryType.STAKEHOLDER: cls.create_stakeholder_dictionary(),
            DictionaryType.BASELINE: cls.create_baseline_dictionary(),
        }


class DictionaryRegistry:
    """
    Registry for managing multiple TDMS dictionaries.
    
    Provides a central access point for all dictionaries used
    in document conversion operations.
    
    Example:
        >>> registry = DictionaryRegistry.create_with_defaults()
        >>> registry.resolve("AMM", DictionaryType.PUBLICATION)
        'Aircraft Maintenance Manual'
    """
    
    def __init__(self) -> None:
        """Initialize empty registry."""
        self._dictionaries: Dict[DictionaryType, TDMSDictionary] = {}
    
    def register(self, dictionary: TDMSDictionary) -> None:
        """Register a dictionary."""
        self._dictionaries[dictionary.dict_type] = dictionary
        logger.debug(f"Registered dictionary: {dictionary.name}")
    
    def get(self, dict_type: DictionaryType) -> Optional[TDMSDictionary]:
        """Get dictionary by type."""
        return self._dictionaries.get(dict_type)
    
    def resolve(self, id: str, dict_type: DictionaryType) -> str:
        """
        Resolve ID to value using specified dictionary.
        
        Args:
            id: The compact ID
            dict_type: Dictionary type to use
            
        Returns:
            The resolved value
            
        Raises:
            DictionaryError: If dictionary or ID not found
        """
        dictionary = self._dictionaries.get(dict_type)
        if dictionary is None:
            raise DictionaryError(f"Dictionary type '{dict_type.value}' not registered")
        return dictionary.get_value(id)
    
    def compact(self, value: str, dict_type: DictionaryType) -> str:
        """
        Compact value to ID using specified dictionary.
        
        Args:
            value: The full value
            dict_type: Dictionary type to use
            
        Returns:
            The compact ID
            
        Raises:
            DictionaryError: If dictionary or value not found
        """
        dictionary = self._dictionaries.get(dict_type)
        if dictionary is None:
            raise DictionaryError(f"Dictionary type '{dict_type.value}' not registered")
        return dictionary.get_id(value)
    
    @classmethod
    def create_with_defaults(cls) -> DictionaryRegistry:
        """
        Create registry with all standard dictionaries.
        
        Returns:
            Registry populated with default dictionaries
        """
        registry = cls()
        for dict_type, dictionary in TDMSDictionary.create_all_standard_dictionaries().items():
            registry.register(dictionary)
        return registry
    
    def save_all(self, directory: Union[str, Path], format: str = "yaml") -> None:
        """Save all dictionaries to directory."""
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        
        for dict_type, dictionary in self._dictionaries.items():
            filename = f"dict_{dict_type.value}.{format}"
            dictionary.save(directory / filename, format=format)
    
    @classmethod
    def load_all(cls, directory: Union[str, Path]) -> DictionaryRegistry:
        """Load all dictionaries from directory."""
        registry = cls()
        directory = Path(directory)
        
        for path in directory.glob("dict_*.yaml"):
            dictionary = TDMSDictionary.load(path)
            registry.register(dictionary)
        
        for path in directory.glob("dict_*.json"):
            dictionary = TDMSDictionary.load(path)
            registry.register(dictionary)
        
        return registry


__all__ = [
    "DictionaryType",
    "DictionaryEntry",
    "TDMSDictionary",
    "DictionaryRegistry",
]
