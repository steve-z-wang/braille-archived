from typing import Optional, List, Union, Dict
from weblite.elements.content.base import ContentElement
from weblite.elements.display import ElementDisplay
from weblite.elements.utils import format_attribute
from weblite.elements.base import Element

class TextareaElement(ContentElement):
    """HTML textarea element - shows text content and attributes humans can see."""
    
    def __init__(self, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None):
        # Textarea should always display (interactive element)
        super().__init__('textarea', content, attributes, display_when_empty=True)
    
    def _to_display(self) -> Optional[ElementDisplay]:
        """
        Display textarea content and attributes that humans can see.
        Priority: text content > value > placeholder
        Always displays (interactive element).
        """
        content = []
        
        # First check if textarea has text content
        display = super()._to_display()
        if display and display.content:
            content.extend(display.content)
        else:
            # If no text content, check value > placeholder
            value = self.attributes.get('value', '')
            if value:
                content.append(format_attribute('value', value))
            else:
                placeholder = self.attributes.get('placeholder', '')
                if placeholder:
                    content.append(format_attribute('placeholder', placeholder))
        
        # Always return something (interactive element)
        return ElementDisplay(tag=self.tag, content=content)