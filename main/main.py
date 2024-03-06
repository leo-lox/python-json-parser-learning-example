import json

def encode_json(data):
    """
    Encode the given data into a JSON string.
    """
    return json.dumps(data)

def decode_json(json_string):
    """
    Decode the given JSON string into Python data.
    """
    return json.loads(json_string)

def main():
    # Example usage
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Encoding data to JSON
    encoded_json = encode_json(data)
    print("Encoded JSON:", encoded_json)

    # Decoding JSON to data
    decoded_data = decode_json(encoded_json)
    print("Decoded data:", decoded_data)

if __name__ == "__main__":
    main()