# Weblite LLM Agent Flow

## Overview
The LLM interacts with websites through a simplified tree representation, never seeing raw HTML or complex selectors.

## Process Flow

### 1. Task Input
```
User: "Sign up with email test@example.com and password SecurePass123"
```

### 2. Page Analysis
Weblite converts current page to simplified tree:
```json
{
  "form": [
    {
      "div": [
        {"label": "Email"},
        {"input": ""}
      ]
    },
    {
      "div": [
        {"label": "Password"},
        {"input": ""}
      ]
    },
    {"button": "Sign Up"}
  ]
}
```

### 3. LLM Action Generation
LLM analyzes tree and generates actions:
```python
[
  {
    "action": "fill",
    "selector": "form > div(label(\"Email\")) > input",
    "value": "test@example.com"
  },
  {
    "action": "fill",
    "selector": "form > div(label(\"Password\")) > input",
    "value": "SecurePass123"
  },
  {
    "action": "click",
    "selector": "button(\"Sign Up\")"
  }
]
```

### 4. Selector Translation
Weblite converts to Playwright selectors:
```
form > div(label("Email")) > input
↓
form >> div:has(label:has-text("Email")) >> input
```

### 5. Execution
Playwright executes the actions on the actual page.

### 6. Feedback Loop
- Get new page state after action
- Convert to tree
- LLM analyzes result (success, error messages, next page)
- Generate next actions
- Repeat until task complete

## Action Types

### Basic Actions
- `click(selector)` - Click button/link
- `fill(selector, text)` - Fill input field
- `select(selector, option)` - Select dropdown option
- `check(selector)` - Check checkbox
- `uncheck(selector)` - Uncheck checkbox

### Navigation
- `wait(selector)` - Wait for element to appear
- `scroll(selector)` - Scroll to element

## Error Handling

When selector fails to match:
1. Return error to LLM with current tree
2. LLM adjusts selector based on available elements
3. Retry with corrected selector

## Example Interaction

```python
# LLM sees
tree = {
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

# LLM generates
action = {
  "action": "click",
  "selector": "main > div(h3(\"Laptop\")) > button(\"Add to Cart\")"
}

# Weblite executes
page.click("main >> div:has(h3:has-text('Laptop')) >> button:has-text('Add to Cart')")
```

## Benefits

1. **Simplicity**: LLM works with clean tree structure
2. **Reliability**: Only interacts with visible elements
3. **Context**: Selectors express semantic relationships
4. **Debuggable**: Clear mapping from intent to action