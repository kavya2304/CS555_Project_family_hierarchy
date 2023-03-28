from datetime import *
from dateutil.relativedelta import *
import unittest
from unittest.mock import patch

def reject_illegitimate_dates(date):
    date_format = " %d %b %Y"

    try:
        date_object = datetime.strptime(date, date_format)
        print(str(date_object))
    except:
       print("Incorrect date format, format must be in DD MM YYYY")

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_reject_illegitimate_dates1(self, mock_print):
        reject_illegitimate_dates(" 10 JUN 2018")
        mock_print.assert_called_with("2018-06-10 00:00:00")

    @patch('builtins.print')
    def test_reject_illegitimate_dates2(self, mock_print):
        reject_illegitimate_dates(" 29 FEB 2018")
        mock_print.assert_called_with("Incorrect date format, format must be in DD MM YYYY")

    @patch('builtins.print')
    def test_reject_illegitimate_dates3(self, mock_print):
        reject_illegitimate_dates(" 29 FEB 2020")
        mock_print.assert_called_with("2020-02-29 00:00:00")

    @patch('builtins.print')
    def test_reject_illegitimate_dates4(self, mock_print):
        reject_illegitimate_dates(" 31 JUL 1999")
        mock_print.assert_called_with("1999-07-31 00:00:00")

if __name__ == '__main__':
    unittest.main



