from typing import Optional
from weblite.elements.constants import WRAPPER_TAGS
from weblite.elements.display import ElementDisplay


def prune_display_tree(display: ElementDisplay, collapsible_tags=WRAPPER_TAGS) -> Optional[ElementDisplay]:
    """
    Prune ElementDisplay tree by removing unnecessary wrapper elements.
    This works on the already-filtered display tree where content decisions have been made.
    """

    # Create a new display with the same tag
    pruned = ElementDisplay(tag=display.tag)

    # Recursively prune content and add to new display
    for item in display.content:
        if isinstance(item, ElementDisplay):
            pruned_item = prune_display_tree(item, collapsible_tags)
            if pruned_item:
                pruned.add_content(pruned_item)
        else:  # str
            pruned.add_content(item)

    # Rule 1: Remove wrapper if only 1 ElementDisplay child
    if (pruned.tag in collapsible_tags and
        len(pruned.content) == 1 and
        isinstance(pruned.content[0], ElementDisplay)):
        return pruned.content[0]

    # Rule 2: Remove empty wrapper elements
    if (not pruned.is_visible() and
        pruned.tag in collapsible_tags):
        return None

    return pruned