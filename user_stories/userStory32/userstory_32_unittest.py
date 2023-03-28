import os
import sys
import unittest
from unittest.mock import patch
from userstory_32 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data


class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = os.path.dirname(__file__) + '/../../test_data.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        listMultipleBirths(individuals)
        mock_print.assert_called_with([('I1', 23), ('I4', 23)])

if __name__ == '__main__':
    unittest.main()
