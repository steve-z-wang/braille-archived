from typing import Optional
from weblite.elements.display import ElementDisplay


def filter_invisible_elements(display: ElementDisplay) -> Optional[ElementDisplay]:
    """
    DFS filtering that removes invisible elements.
    Bottom-up approach: children → parent

    Args:
        display: ElementDisplay to filter

    Returns:
        ElementDisplay: Filtered display with invisible elements removed
        None: If element should be filtered out (invisible)
    """
    # Create new display with same properties
    filtered_display = ElementDisplay(tag=display.tag, is_visible=display.is_inherently_visible)

    # Process children first (DFS)
    for item in display.content:
        if isinstance(item, str):
            # Always include string content
            filtered_display.add_content(item)
        elif isinstance(item, ElementDisplay):
            # Recursively filter child elements
            filtered_child = filter_invisible_elements(item)
            if filtered_child is not None:
                # Use add_content() to respect visibility rules
                filtered_display.add_content(filtered_child)

    # After processing children, decide on parent
    if not filtered_display.is_visible():
        return None

    return filtered_display