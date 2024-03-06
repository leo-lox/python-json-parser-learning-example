import json
"""
    Decode the given  string into Python data.
"""
def decode(string):
    
    ## example json decoding

    if string.startswith("{"):
        # Decode dictionaries
        string = string[1:-1]  # Remove the curly braces
        key_value_pairs = string.split(",")
        decoded_dict = {}
        for pair in key_value_pairs:
            key, value = pair.split(":")
            decoded_dict[key.strip()] = value.strip()
        return decoded_dict
    elif string.startswith("["):
        # Decode lists
        string = string[1:-1]  # Remove the square brackets
        items = string.split(",")
        decoded_list = [item.strip() for item in items]
        return decoded_list
    else:
        # For other types (e.g., strings, numbers), return as is
        return string