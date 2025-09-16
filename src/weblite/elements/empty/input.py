from typing import Optional, Dict
from weblite.elements.empty.base import EmptyElement
from weblite.elements.display import ElementDisplay
from weblite.elements.utils import format_attribute

class InputElement(EmptyElement):
    """HTML input element - displays value attribute if present."""
    
    def __init__(self, attributes: Dict[str, str] = None, is_visible: bool = True):
        super().__init__('input', attributes, is_visible)
    
    def _to_display(self) -> Optional[ElementDisplay]:
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