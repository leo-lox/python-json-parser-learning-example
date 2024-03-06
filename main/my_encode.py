
"""
Encode the given data into a string.
"""
# encode data to a string witch is significant shorter than typical json string
# by using a custom encoding method
def encode(obj):
    """
    Encode the given data into a string.
    """
    if isinstance(obj, dict):
        # For dictionaries, we'll use a comma-separated key-value pair format
        return "{" + ",".join(f"{key}:{value}" for key, value in obj.items()) + "}"
    elif isinstance(obj, list):
        # For lists, we'll use a comma-separated value format
        return "[" + ",".join(str(item) for item in obj) + "]"
    else:
        # For other types (e.g., strings, numbers), simply convert to a string
        return str(obj)