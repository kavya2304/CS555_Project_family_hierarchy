import os
import sys
import unittest
from unittest.mock import patch
from userstory_22_refactored import *
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = __file__.split('_unittest_refactored.py')[0] + '_testdata1.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR: INDIVIDUAL: US22: I3 is not a unique Individual ID.')

    @patch('builtins.print')
    def test_file_2(self, mock_print):
        filename = __file__.split('_unittest_refactored.py')[0] + '_testdata2.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR: FAMILY: US22: F6 is not a unique Family ID.')

    @patch('builtins.print')
    def test_file_3(self, mock_print):
        filename = __file__.split('_unittest_refactored.py')[0] + '_testdata3.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR: FAMILY: US22: F4 is not a unique Family ID.\nERROR: FAMILY: US22: F5 is not a unique Family ID.')

    @patch('builtins.print')
    def test_file_4(self, mock_print):
        filename = __file__.split('_unittest_refactored.py')[0] + '_testdata4.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR: INDIVIDUAL: US22: I7 is not a unique Individual ID.\nERROR: INDIVIDUAL: US22: I8 is not a unique Individual ID.')

    @patch('builtins.print')
    def test_file_5(self, mock_print):
        filename = __file__.split('_unittest_refactored.py')[0] + '_testdata5.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        unique_ids(individuals, families)
        mock_print.assert_called_with('File has all unique IDs.')

if __name__ == '__main__':
    unittest.main()