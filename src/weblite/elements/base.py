from abc import ABC, abstractmethod
from typing import Dict, List, Union, Any, Optional
from weblite.elements.display import ElementDisplay

class Element(ABC):

    def __init__(self, tag: str, attributes: Dict[str, str] = None, is_visible: bool = True) -> None:
        self.tag = tag
        self.attributes = attributes if attributes is not None else {}
        self.is_visible = is_visible

    @abstractmethod
    def _to_display(self) -> Optional[ElementDisplay]:
        """
        Internal: Get the display representation for this element.
        Each element type implements its own logic.

        Returns:
            ElementDisplay: Display information for this element
            None: Element should not be displayed
        """
        pass

    def to_dict(self, collapse_wrappers: bool = True) -> Dict:
        """
        Convert element to dictionary representation.

        Args:
            collapse_wrappers: Whether to collapse wrapper elements (default: True)

        Returns:
            Dict: Weblite representation of the element
        """
        from weblite.utils.display_pruner import prune_display_tree

        display = self._to_display()
        if not display:
            return {}

        if collapse_wrappers:
            pruned = prune_display_tree(display)
            return pruned.to_dict() if pruned else {}
        else:
            return display.to_dict()

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

