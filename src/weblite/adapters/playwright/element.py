from typing import Dict, List, Union, Optional
import asyncio
from weblite.adapters.source_element import SourceElement


class PlaywrightElement(SourceElement):
    """Playwright implementation of WebElement interface."""
    
    def __init__(self, locator):
        """
        Initialize with a Playwright Locator.
        
        Args:
            locator: Playwright Locator object
        """
        self._locator = locator
    
    async def is_visible(self) -> bool:
        """Check if element is visible to user."""
        try:
            return await self._locator.is_visible()
        except Exception:
            return False
    
    async def get_tag(self) -> str:
        """Get element's tag name in lowercase."""
        try:
            return await self._locator.evaluate('el => el.tagName.toLowerCase()')
        except Exception:
            return ''
    
    async def get_content(self) -> List[Union[str, 'SourceElement']]:
        """
        Get ordered mix of text strings and child elements.
        
        This is simplified - gets visible child elements and approximates text order.
        For complex mixed content, this may not preserve exact text positioning.
        """
        try:
            content = []
            
            # Get direct text content (only text nodes, not from style/script/etc)
            direct_text = await self._locator.evaluate('''el => {
                let text = '';
                for (const node of el.childNodes) {
                    if (node.nodeType === Node.TEXT_NODE) {
                        const textContent = node.textContent.trim();
                        if (textContent) {
                            text += (text ? ' ' : '') + textContent;
                        }
                    }
                }
                return text;
            }''')
            
            # Add text if it exists and isn't too long (filter out CSS/JS)
            if direct_text and len(direct_text) < 500:  # Reasonable text length limit
                content.append(direct_text)
            
            # Get visible child elements
            try:
                child_count = await self._locator.locator('> *').count()
                for i in range(child_count):
                    child_locator = self._locator.locator(f'> *:nth-child({i + 1})')
                    if await child_locator.is_visible():
                        content.append(PlaywrightElement(child_locator))
            except Exception:
                pass
            
            return content
            
        except Exception:
            return []
    
    async def get_attributes(self) -> Dict[str, str]:
        """Get all element attributes as a dictionary."""
        try:
            # Get all attributes using JavaScript
            attributes = await self._locator.evaluate('''el => {
                const attrs = {};
                for (const attr of el.attributes) {
                    attrs[attr.name] = attr.value;
                }
                return attrs;
            }''')
            return attributes or {}
        except Exception:
            return {}