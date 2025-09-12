from typing import Dict, Union

from .tree.builder import build_tree
from .tree.display_pruner import prune_display_tree
from .interfaces.web_element import WebElement
from .interfaces.web_page import WebPage 
    

async def parse(element_or_page: Union[WebElement, WebPage]) -> Dict:
    
    web_element = _to_web_element(element_or_page)    
    
    tree = await build_tree(web_element)
    
    if not tree: 
        return {}
    
    display = tree.to_display()
    if not display:
        return {}
    
    pruned_display = prune_display_tree(display)
    if not pruned_display:
        return {}
        
    return pruned_display.to_dict()

def locate(selector: str, element_or_page) -> str:
    """
    Convert Weblite selector to CSS/Playwright selector.
    
    Args:
        selector: Weblite selector (e.g., 'button("Submit")')
        element_or_page: Playwright Page or element for context
        
    Returns:
        str: CSS/Playwright selector
    """
    pass


def _to_web_element(element_or_page: Union[WebElement, WebPage]) -> WebElement:
    if isinstance(element_or_page, WebPage):
        return element_or_page.get_root_element() 
    return element_or_page