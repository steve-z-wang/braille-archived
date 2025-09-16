from typing import Optional, List, Union, Dict
from weblite.elements.content.base import ContentElement
from weblite.elements.display import ElementDisplay
from weblite.elements.base import Element

class SVGElement(ContentElement):
    """HTML svg element - always displays even when empty (interactive element)."""
    
    def __init__(self, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None, is_visible: bool = True):
        # SVG should always display even when empty
        super().__init__('svg', content, attributes, display_when_empty=True, is_visible=is_visible)