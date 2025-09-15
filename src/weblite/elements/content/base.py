from typing import Optional, List, Union, Dict
from ..base import Element
from ..display import ElementDisplay

class ContentElement(Element):
    """Base class for HTML elements that can contain child content."""
    
    def __init__(self, tag: str, content: List[Union[str, Element]] = None, attributes: Dict[str, str] = None, display_when_empty: bool = False):
        super().__init__(tag, attributes)
        self.content = content if content is not None else []
        self.display_when_empty = display_when_empty
    
    def _to_display(self) -> Optional[ElementDisplay]:
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
                if child_display is not None:
                    content.append(child_display)
        
        # Return None if no meaningful content and shouldn't display when empty
        if not content and not self.display_when_empty:
            return None
            
        return ElementDisplay(tag=self.tag, content=content)