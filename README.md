# Weblite

Simplified web scraping and automation with clean JSON output.

## Overview

Weblite converts complex HTML pages into clean, structured JSON trees that focus only on visible, interactive content. It filters out styling wrappers, hidden elements, and irrelevant markup.

## Features

- **Clean Output**: Only visible, meaningful content
- **Tree Format**: Nested JSON structure matching page hierarchy  
- **Formatting Options**: JSON, Markdown, and Tree display formats
- **Playwright Integration**: Works with existing Playwright automation
- **Element Pruning**: Removes wrapper divs and spans automatically

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
