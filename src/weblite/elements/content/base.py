from typing import List, Union, Dict
from weblite.elements.base import Element
from weblite.elements.display import ElementDisplay

class ContentElement(Element):
    """Base class for HTML elements that can contain child content."""
    
    def __init__(self, tag: str, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None, is_visible: bool = True):
        super().__init__(tag, attributes, is_visible)
        self.content = content if content is not None else []
    
    def _to_display(self) -> ElementDisplay:
        """
        Process child elements and text using the builder pattern.
        """
        display = super()._to_display()

        for item in self.content:
            if isinstance(item, str):
                # add_content() will handle empty string filtering
                display.add_content(item)
            else:  # Element
                child_display = item._to_display()
                display.add_content(child_display)

        return display