import pytest
import pandas as pd
import user_stories
from user_stories import marriage_before_divorce_getting_error_line_no
from user_stories import get_line1

def test_marriage_before_divorce_getting_error_line_no():
    details = [{'id': 'F1',
    'Husband ID': 'I2',
    'Husband Name': ' Steven /Brindley/',
     'Wife ID': 'I3',
     'Wife Name': ' Amy /Brooks/',
     'children': ['I1', 'I4'],
     'married': ' 9 JUN 1992',
     'divorced': ' 10 JUL 2015'}]
    strout= "the line number is 130"
    assert strout == marriage_before_divorce_getting_error_line_no(details)