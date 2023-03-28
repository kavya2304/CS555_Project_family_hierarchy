import os
import sys
import unittest
from userstory_34 import *
from unittest.mock import patch
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_large_age_difference(self, mock_print):
        filename = os.path.dirname(__file__) + '/../../test_data.ged'
        individuals, families = file_parser(filename)
        output = output_data(individuals, families, filename)
        large_age_difference(individuals, families)
        mock_print.assert_called_with("US 34: Husband ID: Large age difference at marriage")


if __name__ == '__main__':
    unittest.main