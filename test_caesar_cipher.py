# These are the test cases for the caesar-cypher
import unittest
import mock
from mock import patch
from caesar_cypher import main
from caesar_cypher import calc_spaces_to_shift_by


class test_spaces_to_shift_by(unittest.TestCase):
    def test_it_can_calculate_normal_difference(self):
        expected = 1
        actual = calc_spaces_to_shift_by("a", "b")
        self.assertEqual(actual, expected)

    def test_it_returns_positive_numbers(self):
        expected = 25
        actual = calc_spaces_to_shift_by("b", "a")
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
