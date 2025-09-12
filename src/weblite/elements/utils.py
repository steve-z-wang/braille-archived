"""Utility functions for element formatting."""

def format_attribute(name: str, value: str) -> str:
    """
    Format an attribute with @ prefix notation.
    
    Args:
        name: Attribute name (e.g., 'href', 'value', 'alt')
        value: Attribute value
        
    Returns:
        Formatted attribute string (e.g., '@href=https://example.com')
    """
    return f"@{name}={value}"