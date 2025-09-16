from typing import List, Union, Dict, Any, Optional


class ElementDisplay:
    """
    Builder pattern for element display representation.

    Key principle: An element is visible if and only if it has content.
    Use add_content() to add visible content to the element.
    """

    def __init__(self, tag: str, is_visible: bool = True):
        """
        Initialize with tag name and visibility status.

        Args:
            tag: HTML tag name for this element
            is_visible: Whether this element is inherently visible (not CSS hidden)
        """
        self.tag = tag
        self.is_inherently_visible = is_visible
        self.content: List[Union[str, 'ElementDisplay']] = []

    def add_content(self, item: Union[str, 'ElementDisplay']) -> 'ElementDisplay':
        """
        Add visible content to this element.

        Args:
            item: Either a text string or another ElementDisplay

        Returns:
            Self for method chaining
        """
        self.content.append(item)
        return self

    def is_visible(self) -> bool:
        """
        Check if this element is visible.
        An element is visible if it's inherently visible AND has content.

        Returns:
            True if element is inherently visible and has content, False otherwise
        """
        return self.is_inherently_visible and len(self.content) > 0

    def to_dict(self) -> Optional[Dict[str, Any]]:
        """Convert to Weblite JSON format."""

        if len(self.content) == 1:
            item = self.content[0]

            if isinstance(item, str):
                return {self.tag: item}
            else:
                item_dict = item.to_dict()
                if item_dict is None:
                    return {self.tag: ""}
                return {self.tag: item_dict}

        content_list = []
        for item in self.content:

            if isinstance(item, str):
                content_list.append(item)
            else:
                item_dict = item.to_dict()
                if item_dict is not None:
                    content_list.append(item_dict)

        # If all children were filtered out, check if we have any content left
        if not content_list:
            return None

        return {self.tag: content_list}
