from typing import List, Union, Dict, Any, Optional


class ElementDisplay:
    """
    Builder pattern for element display representation.

    Key principle: An element is visible if and only if it has content.
    Use add_content() to add visible content to the element.
    """

    def __init__(self, tag: str):
        """
        Initialize with just the tag name. Content must be added via add_content().

        Args:
            tag: HTML tag name for this element
        """
        self.tag = tag
        self.content: List[Union[str, 'ElementDisplay']] = []

    def add_content(self, item: Union[str, 'ElementDisplay']) -> 'ElementDisplay':
        """
        Add visible content to this element.

        Args:
            item: Either a text string or another ElementDisplay

        Returns:
            Self for method chaining
        """
        if isinstance(item, str):
            # Only add non-empty strings
            stripped = item.strip()
            if stripped:
                self.content.append(stripped)
        elif isinstance(item, ElementDisplay):
            # Only add visible child elements
            if item.is_visible():
                self.content.append(item)
        return self

    def is_visible(self) -> bool:
        """
        Check if this element is visible (has content).

        Returns:
            True if element has any content, False if empty
        """
        return len(self.content) > 0

    def to_dict(self) -> Optional[Dict[str, Any]]:
        """Convert to Weblite JSON format. Returns None if element is not visible."""
        if not self.is_visible():
            return None

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
