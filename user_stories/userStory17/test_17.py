import pytest
import pandas as pd
import pandas as pd
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import user_stories
from user_stories import no_marriages_to_descendants

def test_no_marriages_to_descendants():
    
    testData = "export-BloodTree22.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    families = createFamilyDataframe(testData, individuals_id_and_name)
    strout="ERROR: FAMILY: US17: 85: F6000000188483093827 Id of child: I6000000188482038862 ,Wife ID: I6000000188483093824 ,Husband ID: I6000000188482038862"
    assert strout==no_marriages_to_descendants(families,getFamilyIndices(testData))