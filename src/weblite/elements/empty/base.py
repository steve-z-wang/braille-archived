from typing import Dict
from weblite.elements.base import Element
from weblite.elements.display import ElementDisplay

class EmptyElement(Element):
    """Base class for HTML void/empty elements that cannot contain child content."""
    
    def __init__(self, tag: str, attributes: Dict[str, str] = None, is_visible: bool = True):
        super().__init__(tag, attributes, is_visible)
    
    def _to_display(self) -> ElementDisplay:
        """
        Default behavior for empty elements: return empty display unless overridden.
        Subclasses should override to provide specific display logic based on attributes.
        """
        return super()._to_display()