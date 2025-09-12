from typing import Optional
from weblite.elements.base import Element
from weblite.elements.factory import ElementFactory
from weblite.interfaces import WebElement

async def build_tree(element: WebElement) -> Optional[Element]:
    # Rule 2: remove elements with no visible content
    if not await element.is_visible():
        return None 
    
    tag = await element.get_tag()
    
    
    content = []
    
    # Get all attributes
    attributes = await element.get_attributes()
    
    for item in await element.get_content():
        
        if isinstance(item, str):
            striped_str = item.strip()  
            
            if striped_str != "": 
                content.append(striped_str)
            
        elif isinstance(item, WebElement):
            node = await build_tree(item)
             
            if node: 
                content.append(node)
    
    # ElementFactory returns None for elements that should be skipped
    return ElementFactory.create_element(tag=tag, content=content, attributes=attributes)