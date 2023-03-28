from userstory_6 import *
from unittest.mock import patch

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_divorce_before_death1(self, mock_print):
        divorceBeforeDeath(gedcom_file)
        mock_print.assert_called_with("ERROR: US 06: Husband ID: Divorce before Death ")


if __name__ == '__main__':
    unittest.main