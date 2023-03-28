import pytest
import pandas as pd
import pandas as pd
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import user_stories
from user_stories import listUpComingBirthdays

def test_listUpComingBirthdays():
    
    testData = "export-BloodTree33.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    strout='US:38 List of upcoming birthdays: Kavyasri T : age:31 2 DEC 1990'
    str1=listUpComingBirthdays(individuals)
    assert strout==str1[0]

