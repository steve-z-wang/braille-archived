from typing import List, Union, Dict
from weblite.elements.content.base import ContentElement
from weblite.elements.display import ElementDisplay
from weblite.elements.utils import format_attribute
from weblite.elements.base import Element

class TextareaElement(ContentElement):
    """HTML textarea element - shows text content and attributes humans can see."""
    
    def __init__(self, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None, is_visible: bool = True):
        # Textarea should always display (interactive element)
        super().__init__('textarea', content, attributes, display_when_empty=True, is_visible=is_visible)
    
    def _to_display(self) -> ElementDisplay:
        """
        Display textarea content and attributes that humans can see.
        Priority: text content > value > placeholder
        Always displays (interactive element).
        """
        # Get the base display from parent class
        display = super()._to_display()

        # If no text content, add value or placeholder attributes
        if not display.is_visible():
            value = self.attributes.get('value', '')
            if value:
                display.add_content(format_attribute('value', value))
            else:
                placeholder = self.attributes.get('placeholder', '')
                if placeholder:
                    display.add_content(format_attribute('placeholder', placeholder))

        return display