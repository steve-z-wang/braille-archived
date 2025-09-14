# Weblite

A text-based web representation that retains meaningful structure information while displaying only human-visible content.

## Overview

Weblite transforms complex web pages into a clean, text-based representation optimized for both LLMs and human comprehension. By extracting only the visible elements and their hierarchical relationships, it creates a simplified yet structurally accurate view of web content.

Key characteristics:
- **LLM-Optimized**: Designed for AI agents to understand and interact with web pages efficiently
- **Human-Readable**: Clear, intuitive format that humans can easily parse and understand
- **Structural Integrity**: Preserves the DOM hierarchy and element relationships, unlike flat accessibility trees
- **Selector Construction**: Maintains enough structural context to enable accurate CSS/XPath selector generation
- **Visibility-Focused**: Filters out hidden elements, displaying only what users actually see on the page

This approach bridges the gap between raw HTML complexity and oversimplified text extraction, providing just the right amount of information for effective web automation and analysis.

## Installation

Install weblite using pip:

```bash
pip install weblite
```

Or install from source:

```bash
git clone https://github.com/steve-z-wang/weblite.git
cd weblite
pip install -e .
```

### Requirements

- Python 3.8 or higher
- Playwright (automatically installed as a dependency)

After installation, you'll need to install Playwright browsers:

```bash
playwright install
```

## Quick Start

```python
import asyncio
from playwright.async_api import async_playwright
from weblite import parse
from weblite.adapters.playwright import PlaywrightPage

async def scrape_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://example.com")
        
        web_page = PlaywrightPage(page)
        result = await parse(web_page)
        
        print(result)
        await browser.close()

asyncio.run(scrape_page())
```

## Output Example

Input HTML:
```html
<div class="wrapper">
  <h1>Products</h1>
  <div class="card">
    <h3>Laptop</h3>
    <p>$999</p>
    <button>Add to Cart</button>
  </div>
</div>
```

Weblite Output:
```json
{
  "main": [
    {"h1": "Products"},
    {
      "div": [
        {"h3": "Laptop"},
        {"p": "$999"},
        {"button": "Add to Cart"}
      ]
    }
  ]
}
```
