from typing import Optional, Dict
from weblite.elements.empty.base import EmptyElement
from weblite.elements.display import ElementDisplay
from weblite.elements.utils import format_attribute

class ImgElement(EmptyElement):
    """HTML img element - displays alt text if present."""
    
    def __init__(self, attributes: Dict[str, str] = None, is_visible: bool = True):
        super().__init__('img', attributes, is_visible)
    
    def _to_display(self) -> Optional[ElementDisplay]:
        """
        Display alt text with @ prefix if present, otherwise don't display.
        """
        alt_text = self.attributes.get('alt', '')
        if not alt_text:
            return None

        return ElementDisplay(tag=self.tag, content=[format_attribute('alt', alt_text)])