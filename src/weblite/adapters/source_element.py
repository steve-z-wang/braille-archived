from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from ..elements.base import Element


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

    async def _to_weblite(self) -> Optional['Element']:
        """Internal: Convert this source element to weblite Element, returns None if invisible."""
        from ..elements.factory import ElementFactory

        # Rule: remove elements with no visible content
        if not await self.is_visible():
            return None

        tag = await self.get_tag()
        content = []

        # Get all attributes
        attributes = await self.get_attributes()

        for item in await self.get_content():
            if isinstance(item, str):
                stripped_str = item.strip()
                if stripped_str != "":
                    content.append(stripped_str)
            elif isinstance(item, SourceElement):
                child_element = await item._to_weblite()
                if child_element:  # Only add if not None
                    content.append(child_element)

        # ElementFactory returns None for elements that should be skipped
        return ElementFactory.create_element(tag=tag, content=content, attributes=attributes)

    async def to_weblite(self) -> Optional['Element']:
        """Convert this source element to a weblite Element."""
        return await self._to_weblite()