from datetime import *
from dateutil.relativedelta import *

def include_partial_dates(date, index):
    listDate = date.split()
    if len(listDate) == 3:
        str_date = date
    if len(listDate) == 2:
        str_date = ' 1 ' + listDate[0] + " " + listDate[1]
        print("ERROR: INDIVIDUAL: US41: Input Line #: " + str(index) +" Partial date " + str(listDate) + " converted into usable format.")
    if len(listDate) == 1:
        str_date = ' 1 ' + 'JAN ' + listDate[0]
        print("ERROR: INDIVIDUAL: US41: Input Line #: " + str(index) + " Partial date " + str(listDate) + " converted into usable format.")
    return str_date
