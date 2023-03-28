import sys
import unittest
from unittest.mock import patch
from userstory_20 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename1 = __file__.split('_unittest.py')[0] + '_testdata1.ged'
        individuals, families = file_parser(filename1)
        output = output_data(individuals, families, filename1)
        no_newphew_niece_marriage(individuals, families)
        mock_print.assert_called_with('ERROR: FAMILY: US20: <rowID> is a marriage between a nephew and an aunt!')

if __name__ == '__main__':
    unittest.main()