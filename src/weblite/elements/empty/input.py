from typing import Optional, Dict
from .base import EmptyElement
from ..display import ElementDisplay
from ..utils import format_attribute

class InputElement(EmptyElement):
    """HTML input element - displays value attribute if present."""
    
    def __init__(self, attributes: Dict[str, str] = None):
        super().__init__('input', attributes)
    
    def to_display(self) -> Optional[ElementDisplay]:
        """
        Display input attributes that humans can see.
        Priority: value > placeholder
        Always displays (interactive element).
        """
        content = []
        
        # Priority: value > placeholder
        value = self.attributes.get('value', '')
        if value:
            content.append(format_attribute('value', value))
        else:
            placeholder = self.attributes.get('placeholder', '')
            if placeholder:
                content.append(format_attribute('placeholder', placeholder))
        
        # Always return something (interactive element)
        return ElementDisplay(tag=self.tag, content=content)