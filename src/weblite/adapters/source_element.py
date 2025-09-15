from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union, TYPE_CHECKING
from weblite.utils.source_to_element import convert_to_weblite

if TYPE_CHECKING:
    from weblite.elements.base import Element

class SourceElement(ABC):
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
    async def get_content(self) -> List[Union[str, 'SourceElement']]:
        """Get ordered mix of text strings and child elements."""
        pass

    @abstractmethod
    async def get_attributes(self) -> Dict[str, str]:
        """Get all element attributes as a dictionary."""
        pass

    async def to_weblite(self) -> Optional['Element']:
        """Convert this source element to a weblite Element."""
        return await convert_to_weblite(self)