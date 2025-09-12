import json

def to_compact_json(obj, indent=0):
    """
    Pretty print JSON with single-key dictionaries on one line.
    
    Args:
        obj: Object to print (dict, list, or primitive)
        indent: Current indentation level
        
    Returns:
        str: Formatted string representation
    """
    spaces = " " * indent
    if isinstance(obj, dict):
        if len(obj) == 1:
            key, value = next(iter(obj.items()))
            if isinstance(value, str):
                return f'{{"{key}": "{value}"}}'
        
        lines = ["{"]
        items = list(obj.items())
        for i, (key, value) in enumerate(items):
            comma = "," if i < len(items) - 1 else ""
            if isinstance(value, str):
                lines.append(f'{spaces} "{key}": "{value}"{comma}')
            else:
                formatted = to_compact_json(value, indent + 1)
                lines.append(f'{spaces} "{key}": {formatted}{comma}')
        lines.append(f'{spaces}}}')
        return '\n'.join(lines)
    
    elif isinstance(obj, list):
        lines = ["["]
        for i, item in enumerate(obj):
            comma = "," if i < len(obj) - 1 else ""
            formatted = to_compact_json(item, indent + 1)
            lines.append(f'{spaces} {formatted}{comma}')
        lines.append(f'{spaces}]')
        return '\n'.join(lines)
    
    return json.dumps(obj)


def to_markdown(obj, level=0):
    """
    Format Weblite JSON as indented list with dashes.
    
    Args:
        obj: Weblite JSON object (dict, list, or primitive)
        level: Current indentation level
        
    Returns:
        str: Formatted list representation
    """
    indent = " " * level
    lines = []
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            lines.append(f"{indent}- {key}")
            
            if isinstance(value, str):
                if value:  # Only show non-empty strings
                    child_indent = " " * (level + 1)
                    lines.append(f"{child_indent}- {value}")
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        if item:  # Only show non-empty strings
                            child_indent = " " * (level + 1)
                            lines.append(f"{child_indent}- {item}")
                    else:
                        nested = to_markdown(item, level + 1)
                        lines.append(nested)
            elif isinstance(value, dict):
                nested = to_markdown(value, level + 1)
                lines.append(nested)
        
        return '\n'.join(lines)
    
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, str):
                if item:  # Only show non-empty strings
                    lines.append(f"{indent}- {item}")
            else:
                nested = to_markdown(item, level)
                lines.append(nested)
        return '\n'.join(lines)
    
    else:
        return f"{indent}- {str(obj)}"


def to_tree(obj, prefix=""):
    """
    Format Weblite JSON as a tree structure (like Linux tree command).
    
    Args:
        obj: Weblite JSON object (dict, list, or primitive)
        prefix: Current line prefix for tree structure
        
    Returns:
        str: Formatted tree representation
    """
    lines = []
    
    if isinstance(obj, dict):
        items = list(obj.items())
        for i, (key, value) in enumerate(items):
            is_last = (i == len(items) - 1)
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{key}")
            
            # Create prefix for children
            child_prefix = prefix + ("    " if is_last else "│   ")
            
            # Process the value
            child_lines = _format_value(value, child_prefix)
            lines.extend(child_lines)
    
    return '\n'.join(lines)


def _format_value(value, prefix):
    """Helper function to format a value with proper tree structure."""
    lines = []
    
    if isinstance(value, str):
        if value:  # Only show non-empty strings
            if value.startswith("@"):
                lines.append(f"{prefix}└── {value}")
            else:
                lines.append(f"{prefix}└── \"{value}\"")
    
    elif isinstance(value, list) and value:
        for i, item in enumerate(value):
            is_last = (i == len(value) - 1)
            connector = "└── " if is_last else "├── "
            child_prefix = prefix + ("    " if is_last else "│   ")
            
            if isinstance(item, str):
                if item:  # Only show non-empty strings
                    if item.startswith("@"):
                        lines.append(f"{prefix}{connector}{item}")
                    else:
                        lines.append(f"{prefix}{connector}\"{item}\"")
            elif isinstance(item, dict):
                # For dict items in a list, format recursively
                dict_items = list(item.items())
                
                for j, (key, dict_value) in enumerate(dict_items):
                    is_last_dict = (j == len(dict_items) - 1)
                    
                    if j == 0:
                        # First key uses the connector from the list level
                        lines.append(f"{prefix}{connector}{key}")
                        # Use the child_prefix for the first key's children
                        value_prefix = child_prefix
                    else:
                        # Subsequent keys use proper indentation 
                        dict_connector = "└── " if is_last_dict else "├── "
                        lines.append(f"{child_prefix}{dict_connector}{key}")
                        # Create prefix for this key's children
                        value_prefix = child_prefix + ("    " if is_last_dict else "│   ")
                    
                    # Format the dict value
                    value_lines = _format_value(dict_value, value_prefix)
                    lines.extend(value_lines)
    
    elif isinstance(value, dict):
        # Recursively format nested dict - pass through the lines directly
        dict_items = list(value.items())
        for i, (key, dict_value) in enumerate(dict_items):
            is_last = (i == len(dict_items) - 1)
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{key}")
            
            child_prefix = prefix + ("    " if is_last else "│   ")
            value_lines = _format_value(dict_value, child_prefix)
            lines.extend(value_lines)
    
    return lines