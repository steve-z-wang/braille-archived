from typing import Optional, Tuple
from weblite.elements.display import ElementDisplay


def filter_invisible_elements(display: ElementDisplay) -> Tuple[Optional[ElementDisplay], bool]:
    """
    Single-pass bottom-up filtering that removes elements with no visible content.
    O(n) time complexity.

    Args:
        display: ElementDisplay to filter

    Returns:
        Tuple of (filtered_element, has_visible_content):
        - filtered_element: ElementDisplay with invisible children removed, None if no visible content
        - has_visible_content: Boolean indicating if this subtree has any visible content
    """
    # Create new display with same properties
    filtered_display = ElementDisplay(tag=display.tag, is_visible=display.is_inherently_visible)
    has_visible_content = False

    # Process children first (DFS)
    for item in display.content:
        if isinstance(item, str):
            # String content is always added
            filtered_display.add_content(item)
            if item.strip():  # Non-empty string = visible content
                has_visible_content = True
        elif isinstance(item, ElementDisplay):
            # Recursively filter child elements
            filtered_child, child_has_visible = filter_invisible_elements(item)
            if child_has_visible:  # Only add children with visible content
                filtered_display.add_content(filtered_child)
                has_visible_content = True

    # Return None if no visible content found
    if not has_visible_content:
        return None, False

    return filtered_display, True