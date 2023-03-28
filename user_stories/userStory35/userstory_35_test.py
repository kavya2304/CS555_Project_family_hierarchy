import os
import sys
import unittest
from userstory_35 import *
from unittest.mock import patch
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def list_recent_births_test1(self, mock_print):
        filename = os.path.dirname(__file__) + '/../../test_data.ged'
        individuals, families = file_parser(filename)
        output = output_data(individuals, families, filename)
        listRecentBirths(individuals)
        mock_print.assert_called_with("US 35: Husband ID: Recently was born ")


if __name__ == '__main__':
    unittest.main