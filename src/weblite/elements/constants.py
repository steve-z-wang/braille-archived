"""HTML element classification constants."""
from typing import Set

# Elements to skip entirely during tree building
SKIP_TAGS: Set[str] = {
    # Script and style elements - not user-visible content
    'script', 'style', 'noscript'
}

# Elements to collapse during display tree pruning
WRAPPER_TAGS: Set[str] = {
    'div', 'span'
}