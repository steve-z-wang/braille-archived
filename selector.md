# Weblite Selector Syntax

## Basic Syntax
- `tag` - element by tag name
- `tag("text")` - element with specific text
- `tag(children)` - element containing specific children

## Examples

### Simple Selection
```
button("Submit")
input("Email")
h1("Welcome")
```

### Parent-Child Selection
```
div > button("Add to Cart")
form > input("Email")
```

### Context Selection
Select element based on siblings/parent content:
```
div(
  h3("Product 2")
) > button("Add to Cart")
```

### Multiple Conditions
```
div(
  h3("Product 2"),
  p("$199")
) > button("Add to Cart")
```

### Multi-line Format
For readability with complex selectors:
```
form(
  label("Email"),
  label("Password")
) > button("Login")
```

### Index for Duplicates
When multiple elements match:
```
button("Submit")[0]
button("Submit")[1]
```

## Translation to Playwright
```
button("Submit")           → button:has-text("Submit")
div > input               → div >> input
div(h3("Product"))        → div:has(h3:has-text("Product"))
```