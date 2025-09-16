from typing import Optional, List, Union, Dict
from weblite.elements.content.base import ContentElement
from weblite.elements.display import ElementDisplay
from weblite.elements.base import Element

class ButtonElement(ContentElement):
    """HTML button element - always displays even when empty (interactive element)."""
    
    def __init__(self, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None, is_visible: bool = True):
        super().__init__('button', content, attributes, is_visible=is_visible)

    def _to_display(self) -> ElementDisplay:
        """
        Button elements should always display even when empty (interactive element).
        """
        display = super()._to_display()

        # Buttons should always display even when empty
        display.add_content("")

        return display