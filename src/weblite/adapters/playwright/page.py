from weblite.adapters.source_page import SourcePage
from weblite.adapters.source_element import SourceElement
from weblite.adapters.playwright.element import PlaywrightElement


class PlaywrightPage(SourcePage):
    """Playwright implementation of WebPage interface."""
    
    def __init__(self, page):
        """
        Initialize with a Playwright Page.
        
        Args:
            page: Playwright Page object
        """
        self._page = page
    
    def get_root_element(self) -> SourceElement:
        """Get the root element (body) of the page."""
        body_locator = self._page.locator('body').first
        return PlaywrightElement(body_locator)