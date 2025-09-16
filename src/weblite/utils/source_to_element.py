"""Convert source elements to weblite elements with parallel processing."""

import asyncio
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from weblite.adapters.source_element import SourceElement
    from weblite.elements.base import Element

from weblite.elements.factory import ElementFactory


async def convert_to_weblite(source_element: 'SourceElement') -> Optional['Element']:
    """
    Convert a source element to weblite Element with parallel processing.

    Args:
        source_element: The source element to convert

    Returns:
        Converted Element or None if tag should be skipped
    """

    # Get tag, attributes, content, and visibility in parallel
    tag_task = source_element.get_tag()
    attributes_task = source_element.get_attributes()
    content_task = source_element.get_content()
    visibility_task = source_element.is_visible()

    tag, attributes, raw_content, is_visible = await asyncio.gather(tag_task, attributes_task, content_task, visibility_task)

    content = []

    # Process content while preserving order
    child_tasks = []
    child_indices = []

    for item in raw_content:
        if isinstance(item, str):
            stripped_str = item.strip()
            if stripped_str != "":
                content.append(stripped_str)
        else:  # Assume it's a SourceElement
            child_tasks.append(convert_to_weblite(item))
            child_indices.append(len(content))  # Remember where this child should go
            content.append(None)  # Placeholder to preserve order

    # Process all child elements in parallel, preserving order
    if child_tasks:
        child_results = await asyncio.gather(*child_tasks)

        # Insert results back in correct positions
        for result, index in zip(child_results, child_indices):
            if result:
                content[index] = result
            else:
                # Remove placeholder for None results
                content[index] = None

        # Remove None placeholders
        content = [item for item in content if item is not None]

    # ElementFactory returns None for elements that should be skipped
    return ElementFactory.create_element(tag=tag, content=content, attributes=attributes, is_visible=is_visible)