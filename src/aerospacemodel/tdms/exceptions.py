"""
TDMS Exceptions
===============

Exception classes for the Total Document Management System.
"""

from aerospacemodel.exceptions import AerospaceModelError


class TDMSError(AerospaceModelError):
    """
    Base exception for TDMS errors.
    
    Raised when document management operations fail.
    """
    pass


class ConversionError(TDMSError):
    """
    Conversion error between planes.
    
    Raised when conversion between human and machine planes fails,
    typically due to:
        - Invalid data structure
        - Missing required fields
        - Incompatible formats
        - Validation failures during conversion
    """
    pass


class ValidationError(TDMSError):
    """
    Validation error in TDMS operations.
    
    Raised when:
        - Machine plane data doesn't match human plane source of truth
        - Data integrity checks fail
        - Schema validation fails
    """
    pass


class DictionaryError(TDMSError):
    """
    Dictionary lookup or management error.
    
    Raised when:
        - ID not found in dictionary
        - Duplicate ID registration
        - Dictionary corruption detected
        - Invalid dictionary format
    """
    pass


class FormatError(TDMSError):
    """
    Format-specific error.
    
    Raised when:
        - Invalid CSV/TSV format
        - Malformed line protocol
        - Encoding errors
    """
    pass


__all__ = [
    "TDMSError",
    "ConversionError",
    "ValidationError",
    "DictionaryError",
    "FormatError",
]
