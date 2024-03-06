import time
import unittest
from main import *
from helpers import *

class JsonTests(unittest.TestCase):
    def test_encode_json(self):
        data = {
            "name": "John Doe",
            "age": 30,
            "city": "New York"
        }
        start_time = time.perf_counter_ns()  # get current time in nanoseconds
        result = main.encode_json(data)
        end_time = time.perf_counter_ns()  # get current time in nanoseconds
        execution_time = end_time - start_time  # calculate elapsed time

        # measure also the length of the result in bytes
        byte_length = helpers.utf8len(result)


        self.assertIsInstance(result, str)

        print(f"encode_json:")
        print(f"{byte_length} bytes")
        print(f"{execution_time} nanoseconds")
        print(f"\n\n")

    def test_decode_json(self):
        json_string = '{"name": "John Doe", "age": 30, "city": "New York"}'
        start_time = time.perf_counter_ns()  # get current time in nanoseconds
        result = main.decode_json(json_string)
        end_time = time.perf_counter_ns()  # get current time in nanoseconds
        execution_time = end_time - start_time  # calculate elapsed time

        self.assertIsInstance(result, dict)
        
        print(f"decode_json:")
        print(f"{execution_time} nanoseconds")
        print(f"\n\n")

if __name__ == '__main__':
    unittest.main()