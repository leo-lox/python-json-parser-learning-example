
"""
Encode the given data into a string.
"""
# encode data to a string witch is significant shorter than typical json string
# by using a custom encoding method
def encode(obj):
    """
    Encode the given data into a string.
    """
    def encode_value(value):
        if isinstance(value, str):
            return f"S{len(value)}{value}"
        elif isinstance(value, int):
            return f"I{value}"
        elif value is None:
            return "N"
        elif isinstance(value, list):
            encoded_elements = "".join(encode_value(item) for item in value)
            return f"L{len(value)}[{encoded_elements}]"
        else:
            raise ValueError(f"Unsupported type: {type(value)}")

    encoded_string = ""
    for key, value in obj.items():
        encoded_string += f"S{len(key)}{key}{encode_value(value)}"
    return encoded_string


