# Weblite

Simplified web page tree representation for LLMs and web automation.

## Overview

Weblite converts complex HTML pages into clean, simplified tree structures that are easy for LLMs to understand and interact with. It works as a high-level abstraction layer on top of Playwright.

## Features

- **Simplified Trees**: Convert messy HTML into clean JSON structures
- **Semantic Selectors**: Use intuitive selectors like `button("Submit")` 
- **LLM-Friendly**: Designed for AI agents to understand web pages
- **Playwright Integration**: Built on top of Playwright's reliable automation
- **Visibility-Aware**: Only shows elements visible to users

## Installation

```bash
# For development
pip install -e .

# Install with dev dependencies
pip install -e ".[dev]"
playwright install
```

## Quick Start

```python
from playwright.sync_api import sync_playwright
from weblite import parse, locate

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    
    # Get simplified tree
    tree = parse(page)
    print(tree)
    # Output: {"body": [{"h1": "Example"}, {"button": "Click me"}]}
    
    # Convert Weblite selector to CSS
    css_selector = locate('button("Click me")', page)
    print(css_selector)  # "button:has-text('Click me')"
    
    # Use with Playwright
    page.click(css_selector)
```

## Tree Format

Weblite converts HTML like this:
```html
<div class="card">
  <h3>Product Name</h3>
  <p>$99.99</p>
  <button>Add to Cart</button>
</div>
```

Into this simple tree:
```json
{
  "div": [
    {"h3": "Product Name"},
    {"p": "$99.99"},
    {"button": "Add to Cart"}
  ]
}
```

## Selector Syntax

Use natural selectors that express intent:
```python
# Simple element selection
button("Submit")
input("Email")

# Parent-child relationships
form > button("Login")
div(h3("Product Name")) > button("Add to Cart")

# Multiple conditions
div(h3("Product 2"), p("$199")) > button
```

## Development

```bash
# Run tests
python -m pytest tests/

# Test with example
cd tests
python test_parse.py
```

## Documentation

- [Tree Format](docs/tree_format.md) - How HTML converts to trees
- [Selector Syntax](docs/selector.md) - Weblite selector reference  
- [Agent Flow](docs/agent.md) - How LLMs use Weblite
- [Architecture](docs/architecture.md) - Technical design

## License

MIT License