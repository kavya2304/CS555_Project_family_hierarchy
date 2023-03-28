import os
import sys
import unittest
from unittest.mock import patch
from userstory_39 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = os.path.dirname(__file__) + '/../../test_data.ged'
        individuals, families = file_parser(filename)
        output = output_data(individuals, families, filename)
        list_upcoming_anniversaries(individuals, families)
        mock_print.assert_called_with("US39: The list of all living couples with marriage anniversaries in the next 30 days: [('I5', 'I6')]")

if __name__ == '__main__':
    unittest.main()