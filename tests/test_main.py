import time
import unittest
from main import *


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

        self.assertIsInstance(result, str)
        print(f"Execution time for encode_json: {execution_time} nanoseconds")

    def test_decode_json(self):
        json_string = '{"name": "John Doe", "age": 30, "city": "New York"}'
        start_time = time.perf_counter_ns()  # get current time in nanoseconds
        result = main.decode_json(json_string)
        end_time = time.perf_counter_ns()  # get current time in nanoseconds
        execution_time = end_time - start_time  # calculate elapsed time

        self.assertIsInstance(result, dict)
        print(f"Execution time for decode_json: {execution_time} nanoseconds")

if __name__ == '__main__':
    unittest.main()