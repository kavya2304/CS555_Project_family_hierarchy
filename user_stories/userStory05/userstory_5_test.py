import os
import sys
import unittest
from userstory_5 import *
from unittest.mock import patch
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_marriage_before_death1(self, mock_print):
        filename = os.path.dirname(__file__) + '/../../test_data.ged'
        individuals, families = file_parser(filename)
        output = output_data(individuals, families, filename)
        marriageBeforeDeath(individuals, families)
        mock_print.assert_called_with("ERROR: US 06: Husband ID: Marriage before Death ")


if __name__ == '__main__':
    unittest.main