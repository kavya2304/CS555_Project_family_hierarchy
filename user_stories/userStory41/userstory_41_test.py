from datetime import *
from dateutil.relativedelta import *
import unittest
from unittest.mock import patch

def include_partial_dates(date):
    listDate = date.split()
    if len(listDate) == 3:
        datetime_object = datetime.strptime(date, " %d %b %Y")
    if len(listDate) == 2:
        datetime_object = datetime.strptime(date, " %b %Y")
    if len(listDate) == 1:
        datetime_object = datetime.strptime(date, " %Y")
    
    print(str(datetime_object))


class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_include_partial_dates1(self, mock_print):
        include_partial_dates(" 10 JUN 2018")
        mock_print.assert_called_with("2018-06-10 00:00:00")

    @patch('builtins.print')
    def test_include_partial_dates2(self, mock_print):
        include_partial_dates(" FEB 2001")
        mock_print.assert_called_with("2001-02-01 00:00:00")

    @patch('builtins.print')
    def test_include_partial_dates3(self, mock_print):
        include_partial_dates(" 2020")
        mock_print.assert_called_with("2020-01-01 00:00:00")

    @patch('builtins.print')
    def test_include_partial_dates4(self, mock_print):
        include_partial_dates(" 29 FEB 2020")
        mock_print.assert_called_with("2020-02-29 00:00:00")

if __name__ == '__main__':
    unittest.main

