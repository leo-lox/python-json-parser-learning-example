import json
import main.my_decode as my_decode
import main.my_encode as my_encode

def encode_json_native(data):
    """
    Encode the given data into a JSON string.
    """
    return json.dumps(data)

def decode_json_native(json_string):
    """
    Decode the given JSON string into Python data.
    """
    return json.loads(json_string)


def encode(data):
    """
    Encode the given data into a string.
    """
    return my_encode.encode(data)

def decode(some_string):
    """
    Decode the given  string into Python data.
    """
    return my_decode.decode(some_string)



def main():
    # Example usage
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Encoding data to JSON
    encoded_json = encode_json_native(data)
    print("Encoded JSON:", encoded_json)

    # Decoding JSON to data
    decoded_data = decode_json_native(encoded_json)
    print("Decoded data:", decoded_data)

    decode(encoded_json)
    encode(data)

if __name__ == "__main__":
    main()