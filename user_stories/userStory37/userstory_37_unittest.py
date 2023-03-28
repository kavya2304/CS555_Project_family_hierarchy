import os
import sys
import unittest
from unittest.mock import patch
from userstory_37 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = os.path.dirname(__file__) + '/../../test_data.ged'
        individuals, families = file_parser(filename)
        output = output_data(individuals, families, filename)
        list_recent_survivors(individuals, families)
        mock_print.assert_called_with("US37: The list of all living spouses and descendants of people who died in the last 30 days: [{'name': ('I2', 53), 'living spouses': [('I7', 32)], 'living descendants': [('I1', 33), ('I4', 23), ('I8', 5)]}, {'name': ('I3', 52), 'living spouses': [], 'living descendants': [('I1', 33), ('I4', 23)]}]")

if __name__ == '__main__':
    unittest.main()