# These are the test cases for the caesar-cypher
from caesar_cypher import Caesar_cypher
import unittest
from unitest import mock
from unittet import TestCase


@mock.patch("")
def test_it_correctly_outputs_short_string():
    with mock.patch("builtins.input", first_input="1"):
        assert caesar_cypher() == "Please enter a letter!"
