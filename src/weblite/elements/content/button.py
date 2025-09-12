from typing import Optional, List, Union, Dict
from .base import ContentElement
from ..display import ElementDisplay
from ..base import Element

class ButtonElement(ContentElement):
    """HTML button element - always displays even when empty (interactive element)."""
    
    def __init__(self, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None):
        # Buttons should always display even when empty
        super().__init__('button', content, attributes, display_when_empty=True)