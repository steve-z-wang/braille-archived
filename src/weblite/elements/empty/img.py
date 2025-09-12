from typing import Optional, Dict
from .base import EmptyElement
from ..display import ElementDisplay
from ..utils import format_attribute

class ImgElement(EmptyElement):
    """HTML img element - displays alt text if present."""
    
    def __init__(self, attributes: Dict[str, str] = None):
        super().__init__('img', attributes)
    
    def to_display(self) -> Optional[ElementDisplay]:
        """
        Display alt text with @ prefix if present, otherwise don't display.
        """
        alt_text = self.attributes.get('alt', '')
        if not alt_text:
            return None
            
        return ElementDisplay(tag=self.tag, content=[format_attribute('alt', alt_text)])