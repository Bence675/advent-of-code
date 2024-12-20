
import unittest
from generic_reader import *

class TestParseInput(unittest.TestCase):
    def test_parse_single_line_string(self):
        data = ["abc"]
        self.assertEqual(parse_input(data), "abc")
        
    def test_parse_single_line_int(self):
        data = ["123"]
        self.assertEqual(parse_input(data), "123")

    def test_parse_single_line_list(self):
        data = ["1 2 3"]
        self.assertEqual(parse_input(data), ["1", "2", "3"])

    def test_parse_single_line_list_int(self):
        data = ["1 2 3"]
        self.assertEqual(parse_input(data, transform = int), [1, 2, 3])

    def test_parse_single_line_list_float(self):
        data = ["1.1 2.2 3.3"]
        self.assertEqual(parse_input(data, transform = float), [1.1, 2.2, 3.3])

    def test_parse_multi_line_string(self):
        data = ["abc", "def", "ghi"]
        self.assertEqual(parse_input(data), ["abc", "def", "ghi"])

    def test_parse_multi_line_list(self):
        data = ["1 2 3", "4 5 6", "7 8 9"]
        self.assertEqual(parse_input(data), [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

    def test_parse_multi_line_list_int(self):
        data = ["1 2 3", "4 5 6", "7 8 9"]
        self.assertEqual(parse_input(data, transform = int), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_parse_multi_line_list_float(self):
        data = ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]
        self.assertEqual(parse_input(data, transform = float), [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]])

    def test_parse_multi_line_list_float_sep(self):
        data = ["1.1,2.2,3.3", "4.4,5.5,6.6", "7.7,8.8,9.9"]
        self.assertEqual(parse_input(data, sep = ",", transform = float), [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]])

    def test_parse_multi_line_list_float_sep_transform_to_int(self):
        data = ["1.1,2.2,3.3", "4.4,5.5,6.6", "7.7,8.8,9.9"]
        self.assertEqual(parse_input(data, sep = ",", transform = lambda x : int(float(x))), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

if __name__ == "__main__":
    unittest.main()