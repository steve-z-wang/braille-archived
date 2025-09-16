from typing import Optional, List, Union, Dict
from weblite.elements.content.base import ContentElement
from weblite.elements.display import ElementDisplay
from weblite.elements.base import Element

class SVGElement(ContentElement):
    """HTML svg element - always displays even when empty (interactive element)."""

    def __init__(self, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None, is_visible: bool = True):
        super().__init__('svg', content, attributes, is_visible=is_visible)

    def _to_display(self) -> ElementDisplay:
        """
        SVG elements should always display even when empty (interactive element).
        """
        display = super()._to_display()

        # SVG should always display even when empty
        display.add_content("")

        return display