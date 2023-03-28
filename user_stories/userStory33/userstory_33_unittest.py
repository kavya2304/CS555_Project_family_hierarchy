import os
import sys
import unittest
from unittest.mock import patch
from userstory_33 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data


class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = 'userstory_33_test_data.ged'
        individuals, families = file_parser(filename)
        listOrphans(individuals, families)
        mock_print.assert_called_with(['I3'])

if __name__ == '__main__':
    unittest.main()
