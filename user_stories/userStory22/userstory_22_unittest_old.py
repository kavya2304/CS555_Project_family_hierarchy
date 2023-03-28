from gc import get_debug
import os
import unittest
from unittest.mock import patch
from userstory_22_old import *

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename1 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata1.ged'
        unique_ids(filename1)
        mock_print.assert_called_with('ID I3 is not a unique ID.')

    @patch('builtins.print')
    def test_file_2(self, mock_print):
        filename2 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata2.ged'
        unique_ids(filename2)
        mock_print.assert_called_with('ID F6 is not a unique ID.')

    @patch('builtins.print')
    def test_file_3(self, mock_print):
        filename3 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata3.ged'
        unique_ids(filename3)
        mock_print.assert_called_with('ID F4 is not a unique ID.\nID F5 is not a unique ID.')

    @patch('builtins.print')
    def test_file_4(self, mock_print):
        filename4 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata4.ged'
        unique_ids(filename4)
        mock_print.assert_called_with('ID I7 is not a unique ID.\nID I8 is not a unique ID.')

    @patch('builtins.print')
    def test_file_5(self, mock_print):
        filename5 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata5.ged'
        unique_ids(filename5)
        mock_print.assert_called_with('File has all unique IDs.')

if __name__ == '__main__':
    unittest.main()