from typing import List, Union, Dict, Any


class ElementDisplay:
    """
    Self-contained representation of how an HTML element should be displayed in the final JSON output.
    """

    def __init__(self, tag: str, content: List[Union[str, 'ElementDisplay']] = None):
        self.tag = tag
        self.content = content if content is not None else []

    def to_dict(self) -> Dict[str, Any]:
        """Convert to Weblite JSON format."""
        if len(self.content) == 0:
            return {self.tag: ""}

        if len(self.content) == 1:
            item = self.content[0]

            if isinstance(item, str):
                return {self.tag: item}
            else:
                return {self.tag: item.to_dict()}

        content_list = []
        for item in self.content:

            if isinstance(item, str):
                content_list.append(item)
            else:
                content_list.append(item.to_dict())

        return {self.tag: content_list}
