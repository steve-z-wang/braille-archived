from typing import Dict, List, Union, Optional
from weblite.elements.base import Element
from weblite.elements.constants import SKIP_TAGS
from weblite.elements.content.base import ContentElement
from weblite.elements.content.button import ButtonElement
from weblite.elements.content.svg import SVGElement
from weblite.elements.content.textarea import TextareaElement
from weblite.elements.empty.input import InputElement
from weblite.elements.empty.img import ImgElement

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
            case 'svg':
                return SVGElement(content, attributes)
            case _:
                # Default: generic content element for div, span, p, h1, a, etc.
                return ContentElement(tag, content, attributes)
    
