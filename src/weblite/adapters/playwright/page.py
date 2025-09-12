from ...interfaces.web_page import WebPage
from ...interfaces.web_element import WebElement
from .element import PlaywrightElement


class PlaywrightPage(WebPage):
    """Playwright implementation of WebPage interface."""
    
    def __init__(self, page):
        """
        Initialize with a Playwright Page.
        
        Args:
            page: Playwright Page object
        """
        self._page = page
    
    def get_root_element(self) -> WebElement:
        """Get the root element (body) of the page."""
        body_locator = self._page.locator('body').first
        return PlaywrightElement(body_locator)