from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional
from weblite.adapters.source_element import SourceElement

if TYPE_CHECKING:
    from weblite.elements.base import Element


class SourcePage(ABC):
    """Abstract interface for web pages from different automation libraries."""

    @abstractmethod
    def get_root_element(self) -> SourceElement:
        """Get the root element (typically <body>) of the page."""
        pass

    async def to_weblite(self) -> Optional['Element']:
        """Convert the root element of this page to a weblite Element."""
        root = self.get_root_element()
        return await root.to_weblite()