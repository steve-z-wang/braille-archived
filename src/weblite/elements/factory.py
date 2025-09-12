from typing import Dict, List, Union, Optional
from .base import Element
from .constants import SKIP_TAGS
from .content.base import ContentElement
from .content.button import ButtonElement
from .content.textarea import TextareaElement
from .empty.input import InputElement
from .empty.img import ImgElement

class ElementFactory:
    """Factory for creating appropriate Element instances based on HTML tags."""
    
    @staticmethod
    def create_element(tag: str, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None) -> Optional[Element]:
        """
        Create appropriate Element instance based on tag type.
        
        Args:
            tag: HTML tag name
            content: List of content items (ignored for empty elements)
            attributes: Element attributes
            
        Returns:
            Element: Appropriate element instance
            None: If tag should be skipped
        """
        if tag in SKIP_TAGS:
            return None
        
        # Route to specific element classes
        match tag:
            case 'input':
                return InputElement(attributes)
            case 'img':
                return ImgElement(attributes)
            case 'textarea':
                return TextareaElement(content, attributes)
            case 'button':
                return ButtonElement(content, attributes)
            case _:
                # Default: generic content element for div, span, p, h1, a, etc.
                return ContentElement(tag, content, attributes)
    
