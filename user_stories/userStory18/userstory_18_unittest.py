import sys
import unittest
from unittest.mock import patch
from userstory_18 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = __file__.split('_unittest.py')[0] + '_testdata1.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        no_siblings_marriage(individuals, families)
        mock_print.assert_called_with('ERROR: FAMILY: US18: 134: F2: Sibling marriage sharing the same parents')

if __name__ == '__main__':
    unittest.main()