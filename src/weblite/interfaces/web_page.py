from abc import ABC, abstractmethod
from .web_element import WebElement


class WebPage(ABC):
    """Abstract interface for web pages from different automation libraries."""
    
    @abstractmethod
    def get_root_element(self) -> WebElement:
        """Get the root element (typically <body>) of the page."""
        pass