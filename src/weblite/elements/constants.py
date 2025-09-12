"""HTML element classification constants."""
from typing import Set

# Elements to skip entirely during tree building
SKIP_TAGS: Set[str] = {
    # SVG drawing elements - no semantic meaning for LLMs
    'path', 'circle', 'rect', 'line', 'polygon', 'polyline', 'ellipse', 'g',
    
    # Script and style elements - not user-visible content  
    'script', 'style', 'noscript'
}

# Elements to collapse during display tree pruning
WRAPPER_TAGS: Set[str] = {
    'div', 'span '
}