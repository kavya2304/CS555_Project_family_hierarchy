import sys
import unittest
from unittest.mock import patch
from userstory_10 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = __file__.split('_unittest.py')[0] + '_testdata1.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        marriage_after_14(individuals, families)
        mock_print.assert_called_with('ERROR: FAMILY: US10: 151: F5: Wife (I11) married before the age of 14')

if __name__ == '__main__':
    unittest.main()