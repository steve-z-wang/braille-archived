from typing import Dict
from weblite.elements.empty.base import EmptyElement
from weblite.elements.display import ElementDisplay
from weblite.elements.utils import format_attribute

class ImgElement(EmptyElement):
    """HTML img element - displays alt text if present."""
    
    def __init__(self, attributes: Dict[str, str] = None, is_visible: bool = True):
        super().__init__('img', attributes, is_visible)
    
    def _to_display(self) -> ElementDisplay:
        """
        Display alt text with @ prefix if present, otherwise empty display.
        """
        display = ElementDisplay(tag=self.tag)

        alt_text = self.attributes.get('alt', '')
        if alt_text:
            display.add_content(format_attribute('alt', alt_text))

        return display