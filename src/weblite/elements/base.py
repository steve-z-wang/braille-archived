from abc import ABC, abstractmethod
from typing import Dict, List, Union, Any, Optional
from .display import ElementDisplay

class Element(ABC): 
    
    def __init__(self, tag: str, attributes: Dict[str, str] = None) -> None: 
        self.tag = tag 
        self.attributes = attributes if attributes is not None else {}
    
    @abstractmethod
    def to_display(self) -> Optional[ElementDisplay]:
        """
        Get the display representation for this element.
        Each element type implements its own logic.
        
        Returns:
            ElementDisplay: Display information for this element
            None: Element should not be displayed
        """
        pass
        
