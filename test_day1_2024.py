# Testing of Day1 2024 Advent of code
# source: https://adventofcode.com/2024

import unittest
import io
import sys
from unittest.mock import patch
from day1_2024 import clear_console, calc_distance, calc_distance_pythonic, process_the_data, get_the_data, start_the_engine

class TestAoCDay1(unittest.TestCase):
    def setUp(self):
        self.test_data = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]

    def test_clear_console(self):
        with patch('os.system') as mock_system, patch('sys.stdout', new=io.StringIO()) as fake_out:
            clear_console()
            mock_system.assert_called_once_with('clear')
            self.assertIn('< .... AoC 2024 Day 1, part 1 .... >', fake_out.getvalue())

    def test_calc_distance(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 3, 4, 5, 6]
        self.assertEqual(calc_distance(list1, list2), 5)

    def test_calc_distance_pythonic(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 3, 4, 5, 6]
        self.assertEqual(calc_distance_pythonic(list1, list2), 5)

    def test_process_the_data(self):
        result = process_the_data(self.test_data)
        self.assertEqual(result, 11)  # Expected result for the test dataset

    @patch('builtins.open')
    def test_get_the_data(self, mock_open):
        mock_open.return_value.__enter__.return_value = self.test_data
        result = get_the_data()
        self.assertEqual(result, [line.strip() for line in self.test_data])

    @patch('day1_2024.get_the_data')
    @patch('day1_2024.process_the_data')
    def test_start_the_engine(self, mock_process, mock_get):
        mock_get.return_value = self.test_data
        mock_process.return_value = 11
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            start_the_engine()
            self.assertIn('the total distance between your lists  ->  11', fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
