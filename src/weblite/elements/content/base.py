from typing import List, Union, Dict
from weblite.elements.base import Element
from weblite.elements.display import ElementDisplay

class ContentElement(Element):
    """Base class for HTML elements that can contain child content."""
    
    def __init__(self, tag: str, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None, display_when_empty: bool = False, is_visible: bool = True):
        super().__init__(tag, attributes, is_visible)
        self.content = content if content is not None else []
        self.display_when_empty = display_when_empty
    
    def _to_display(self) -> ElementDisplay:
        """
        Process child elements and text using the builder pattern.
        """
        display = ElementDisplay(tag=self.tag)

        for item in self.content:
            if isinstance(item, str):
                # add_content() will handle empty string filtering
                display.add_content(item)
            else:  # Element
                child_display = item._to_display()
                # add_content() will check if child is visible
                display.add_content(child_display)

        return display