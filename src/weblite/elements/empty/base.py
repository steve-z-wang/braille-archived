from typing import Optional, Dict
from ..base import Element
from ..display import ElementDisplay

class EmptyElement(Element):
    """Base class for HTML void/empty elements that cannot contain child content."""
    
    def __init__(self, tag: str, attributes: Dict[str, str] = None):
        super().__init__(tag, attributes)
    
    def _to_display(self) -> Optional[ElementDisplay]:
        """
        Default behavior for empty elements: don't display unless overridden.
        Subclasses should override to provide specific display logic based on attributes.
        """
        return None