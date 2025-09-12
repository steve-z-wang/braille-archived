
# Prune rules

## Rule 1: Remove the wrapper if only 1 visible child

### Case 1: one visible child

Before:

``` html
<div>
    <div> text <div> <!-- Only 1 visible children -->
<div>
```

After:

``` html
<div> text <div>
```

### Case 2: multiple children

Before:

``` html
<div>
    text
    <div> text <div> <!-- 2 children: text + dev -->
<div>
```

After:

``` html
<div>
    text
    <div> text <div>
<div>
```

## Rule 2: Remove elements with no visible content

### Case 1: Empty element

Before:
```html
<div>
    <span></span>  <!-- Empty, no content -->
    <div>text</div>
</div>
```

After:
```html
<div>
    <div>text</div>  <!-- Empty span removed -->
</div>
```

### Case 2: Element with only whitespace

Before:
```html
<div>
    <div>   </div>  <!-- Only whitespace -->
    <button>Click</button>
</div>
```

After:
```html
<div>
    <button>Click</button>  <!-- Whitespace-only div removed -->
</div>
```

