import pytest
import pandas as pd
import pandas as pd
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import user_stories
from user_stories import listRecentDeaths


def test_listRecentDeaths():
    
    testData = "export-BloodTree42.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    strout='US:36 List of recent deaths:  Sandy /T : age:72 20 OCT 2022'
    str1=listRecentDeaths(individuals)
    assert strout==str1[0]

