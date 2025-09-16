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
        Process child elements and text, filtering out empty strings.
        """
        content = []

        for item in self.content:
            if isinstance(item, str):
                # Filter out empty/whitespace strings
                stripped = item.strip()
                if stripped:
                    content.append(stripped)
            else:  # Element
                child_display = item._to_display()
                # Always include child displays (they're never None now)
                content.append(child_display)

        return ElementDisplay(tag=self.tag, content=content)