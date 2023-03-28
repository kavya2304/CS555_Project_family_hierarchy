import os
import sys
from userstory_39 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data

filename = os.path.dirname(__file__) + '/../../test_data.ged'
individuals, families = file_parser(filename)
output = output_data(individuals, families, filename)
list_upcoming_anniversaries(individuals, families)
