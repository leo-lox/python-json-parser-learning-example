import json
"""
    Decode the given  string into Python data.
"""
def decode(encoded_string):
    
    ## example json decoding

    def decode_value(encoded_value):
        type_marker = encoded_value[0]
        if type_marker == "S":
            length_end_index = encoded_value.index("S", 1)
            length = int(encoded_value[1:length_end_index])
            value = encoded_value[length_end_index+1:length_end_index+1+length]
            remaining = encoded_value[length_end_index+1+length:]
            return value, remaining
        elif type_marker == "I":
            value_end_index = encoded_value.index("I", 1)
            value = int(encoded_value[1:value_end_index])
            remaining = encoded_value[value_end_index+1:]
            return value, remaining
        elif type_marker == "N":
            return None, encoded_value[1:]
        elif type_marker == "L":
            length_end_index = encoded_value.index("[")
            length = int(encoded_value[1:length_end_index])
            remaining = encoded_value[length_end_index+1:]
            value = []
            for _ in range(length):
                decoded_element, remaining = decode_value(remaining)
                value.append(decoded_element)
            remaining = remaining[1:]  # remove the closing "]"
            return value, remaining
        else:
            raise ValueError(f"Unsupported type marker: {type_marker}")

    obj = {}
    while encoded_string:
        key, encoded_string = decode_value(encoded_string)
        value, encoded_string = decode_value(encoded_string)
        obj[key] = value
    return obj