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
    def create_element(tag: str, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None, is_visible: bool = True) -> Optional[Element]:
        """
        Create appropriate Element instance based on tag type.

        Args:
            tag: HTML tag name
            content: List of content items (ignored for empty elements)
            attributes: Element attributes
            is_visible: Whether the element is visible (metadata only)

        Returns:
            Element: Appropriate element instance
            None: If tag should be skipped
        """
        if tag in SKIP_TAGS:
            return None
        
        # Route to specific element classes
        match tag:
            case 'input':
                return InputElement(attributes, is_visible)
            case 'img':
                return ImgElement(attributes, is_visible)
            case 'textarea':
                return TextareaElement(content, attributes, is_visible)
            case 'button':
                return ButtonElement(content, attributes, is_visible)
            case 'svg':
                return SVGElement(content, attributes, is_visible)
            case _:
                # Default: generic content element for div, span, p, h1, a, etc.
                return ContentElement(tag, content, attributes, is_visible=is_visible)
    
