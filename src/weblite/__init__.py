"""
Weblite - Simplified web page tree representation for LLMs
"""

from .elements.base import Element
from .adapters import SourceElement, SourcePage, PlaywrightPage, PlaywrightElement

__version__ = "0.2.0"
__all__ = ["Element", "SourceElement", "SourcePage", "PlaywrightPage", "PlaywrightElement"]