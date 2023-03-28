import os
import sys
import unittest
from unittest.mock import patch
from userstory_30 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = os.path.dirname(__file__) + '/../../test_data.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        list_living_married(individuals, families)
        mock_print.assert_called_with("US30: The list of living people that are married: [('I5', 78), ('I6', 77), ('I7', 32)]")

if __name__ == '__main__':
    unittest.main()