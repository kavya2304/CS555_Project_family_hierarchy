from datetime import *
from dateutil.relativedelta import *


def reject_illegitimate_dates(date, index):
    date_format = " %d %b %Y"

    try:
        date_object = datetime.strptime(date, date_format)
        #print(date_object)
    except:
        print ("ERROR: INDIVIDUAL: US42: Input Line # " + str(index) + " Incorrect date format")

