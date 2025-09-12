# Weblite Tree Format

## Basic Structure

### Leaf node (no children)
```json
{"tag": "text"}
```

### Parent node with children
```json
{"tag": [child1, child2, ...]}
```

### Parent with own text + children
```json
{
  "tag": [
    "parent's text",  // First string = parent's own text
    {"child1": "..."},
    {"child2": "..."}
  ]
}
```

## Examples

### Simple elements
```json
{"button": "Submit"}
{"h1": "Welcome"}
{"input": ""}  // Empty text
```

### Nested structure
```json
{
  "div": [
    {"h3": "Product Name"},
    {"p": "$99.99"},
    {"button": "Add to Cart"}
  ]
}
```

### Mixed content
```json
{
  "label": [
    "Email: ",
    {"input": "user@example.com"}
  ]
}
```

### Form example
```json
{
  "form": [
    {
      "div": [
        {"label": "Username"},
        {"input": ""}
      ]
    },
    {
      "div": [
        {"label": "Password"},
        {"input": ""}
      ]
    },
    {"button": "Login"}
  ]
}
```

## Rules

1. **Leaf nodes**: Single key-value pair where value is a string
2. **Parent nodes**: Value is an array of children
3. **Mixed content**: First array element as string = parent's text
4. **Empty elements**: Use empty string `""` or empty array `[]`
5. **Visible content only**: Show only what a human can see on screen

## Special Elements

### Input Fields
Show what's currently visible to the user:
- **Empty input with placeholder**: Show placeholder text
- **Input with value**: Show the actual value (placeholder is hidden)
- **Empty input without placeholder**: Show empty string `""`

```json
// HTML: <input placeholder="Search products..." value="">
{"input": "Search products..."}

// HTML: <input placeholder="Search products..." value="laptop">
{"input": "laptop"}

// HTML: <input value="">
{"input": ""}
```

### Images
Use alt text as the visible content:
```json
// HTML: <img src="logo.png" alt="Company Logo">
{"img": "Company Logo"}
```

### Reverting Strategy
When converting selectors back to HTML:
- The system checks the actual DOM state
- For inputs: Determines if text matches value or placeholder
- Dynamically generates the appropriate selector based on current HTML
