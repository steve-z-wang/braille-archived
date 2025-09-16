"""
Weblite selector system for parsing and converting weblite selectors to Playwright selectors.
"""

from .ast import SelectorNode
from .parser import parse_selector

__all__ = ['SelectorNode', 'parse_selector']