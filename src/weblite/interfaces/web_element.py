from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union


class WebElement(ABC):
    """Abstract interface for web elements from different automation libraries."""
    
    @abstractmethod
    async def is_visible(self) -> bool:
        """
        Check if element is visible to user.
        
        Return False if: 
        - Element itself is invisible (display: none, visibility: hidden, etc.)
        - ANY ancestor is invisible (CSS inheritance)
        
        Return True only if element AND all ancestors are visible. 
        """
        pass
    
    @abstractmethod
    async def get_tag(self) -> str:
        """Get element's tag name in lowercase."""
        pass
    
    @abstractmethod
    async def get_content(self) -> List[Union[str, 'WebElement']]:
        """Get ordered mix of text strings and child elements."""
        pass
    
    @abstractmethod
    async def get_attributes(self) -> Dict[str, str]:
        """Get all element attributes as a dictionary."""
        pass