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
        result = main.encode_json_native(data)
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
        result = main.decode_json_native(json_string)
        end_time = time.perf_counter_ns()  # get current time in nanoseconds
        execution_time = end_time - start_time  # calculate elapsed time

        self.assertIsInstance(result, dict)

        print(f"decode_json:")
        print(f"{execution_time} nanoseconds")
        print(f"\n\n")

    def test_encode(self):
        data = {
            "name": "John Doe",
            "age": 30,
            "city": "New York"
        }
        start_time = time.perf_counter_ns()
        result = main.encode(data)
        end_time = time.perf_counter_ns()
        execution_time = end_time - start_time

        byte_length = helpers.utf8len(result)

        self.assertIsInstance(result, str)

        print(f"encode:")
        print(f"{byte_length} bytes")
        print(f"{execution_time} nanoseconds")
        print(f"\n\n")


    def test_decode(self):

        some_string = '{"name": "John Doe", "age": 30, "city": "New York"}'
        start_time = time.perf_counter_ns()
        result = main.decode(some_string)
        end_time = time.perf_counter_ns()
        execution_time = end_time - start_time

        self.assertIsInstance(result, dict)

        print(f"decode:")
        print(f"{execution_time} nanoseconds")
        print(f"\n\n")





    def compare_encode(self):
        data = {
            "name": "John Doe",
            "age": 30,
            "city": "New York"
        }
        start_time = time.perf_counter_ns()
        result = main.encode(data)
        end_time = time.perf_counter_ns()
        execution_time = end_time - start_time
        byte_length = helpers.utf8len(result)

        start_time_json = time.perf_counter_ns()
        result_json = main.encode_json_native(data)
        end_time_json = time.perf_counter_ns()
        execution_time_json = end_time_json - start_time_json
        byte_length_json = helpers.utf8len(result_json)

        print(f"encode:")
        print(f"Custom: {execution_time} nanoseconds")
        print(f"{byte_length} bytes")
        print(f"\n")
        print(f"JSON: {execution_time_json} nanoseconds")
        print(f"{byte_length_json} bytes")
        print(f"\n\n")

        # make comparison if its longer or shorter by calculating the difference
        if byte_length_json > byte_length:
            print(f"Custom encode is {byte_length_json - byte_length} bytes shorter")
        else:
            print(f"Custom encode is {byte_length - byte_length_json} bytes longer")


if __name__ == '__main__':
    unittest.main()