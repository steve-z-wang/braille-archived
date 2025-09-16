from abc import ABC
from typing import Dict, List, Union, Any, Optional
from weblite.elements.display import ElementDisplay

class Element(ABC):

    def __init__(self, tag: str, attributes: Dict[str, str] = None, is_visible: bool = True) -> None:
        self.tag = tag
        self.attributes = attributes if attributes is not None else {}
        self.is_visible = is_visible

    def _to_display(self) -> ElementDisplay:
        """
        Get the base display representation with visibility info.
        Subclasses should call super()._to_display() and add their content.

        Returns:
            ElementDisplay: Base display with tag and visibility info
        """
        return ElementDisplay(tag=self.tag, is_visible=self.is_visible)

    def to_dict(self, collapse_wrappers: bool = True, include_invisible: bool = False) -> Dict:
        """
        Convert element to dictionary representation.

        Args:
            collapse_wrappers: Whether to collapse wrapper elements (default: True)
            include_invisible: Whether to include invisible elements in output (default: False)

        Returns:
            Dict: Weblite representation of the element
        """
        from weblite.utils.display_pruner import prune_display_tree
        from weblite.utils.visibility_filter import filter_invisible_elements

        display = self._to_display()

        # Apply visibility filtering only if needed
        filtered_display = display if include_invisible else filter_invisible_elements(display)
        if filtered_display is None:
            return {}

        # Apply wrapper collapsing if needed
        collapsed_display = prune_display_tree(filtered_display) if collapse_wrappers else filtered_display
        if collapsed_display is None:
            return {}

        result = collapsed_display.to_dict()
        return result if result is not None else {}

    def locate(self, selector: str) -> str:
        """
        Convert Weblite selector to CSS/Playwright selector using proximity scoring.

        Args:
            selector: Weblite selector (e.g., 'input near label="Colour"')

        Returns:
            str: CSS/Playwright selector for the best match
        """
        # TODO: Implement smart selector with proximity scoring
        # Use self._to_display() for full tree context
        return f"/* TODO: Smart selector for '{selector}' */"

