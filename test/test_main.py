import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import count_o, output_string, type_error_string
import unittest

class TestMain(unittest.TestCase):
    def test_count_o(self):
        self.assertEqual(count_o("Hello, World"), output_string + str(2))
        self.assertEqual(count_o("LLL"), output_string + str(0))
        self.assertEqual(count_o("Oh my god!"), output_string + str(2))
        self.assertEqual(count_o(2), type_error_string)

if __name__ == '__main__':
    unittest.main()


