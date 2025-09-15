from typing import Optional
from weblite.elements.constants import WRAPPER_TAGS
from weblite.elements.display import ElementDisplay


def prune_display_tree(display: ElementDisplay, collapsible_tags=WRAPPER_TAGS) -> Optional[ElementDisplay]:
    """
    Prune ElementDisplay tree by removing unnecessary wrapper elements.
    This works on the already-filtered display tree where content decisions have been made.
    """

    # Recursively prune content first
    pruned_content = []
    for item in display.content:
        if isinstance(item, ElementDisplay):
            pruned_item = prune_display_tree(item, collapsible_tags)
            if pruned_item:
                pruned_content.append(pruned_item)
        else:  # str
            pruned_content.append(item)

    # Update content with pruned items
    display.content = pruned_content

    # Rule 1: Remove wrapper if only 1 ElementDisplay child
    if (display.tag in collapsible_tags and
        len(display.content) == 1 and
        isinstance(display.content[0], ElementDisplay)):
        return display.content[0]

    # Rule 2: Remove empty wrapper elements
    if (len(display.content) == 0 and
        display.tag in collapsible_tags):
        return None

    return display