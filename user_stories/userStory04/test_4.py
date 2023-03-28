#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
import pandas as pd
import pandas as pd
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import user_stories
from user_stories import marriage_before_divorce

def test_marriage_before_divorce():
    
    testData = "export-BloodTree4.ged"
    (individuals,individuals_id_and_name) = createIndDataframe("export-BloodTree4.ged")
    families = createFamilyDataframe("export-BloodTree4.ged", individuals_id_and_name)
    str1=marriage_before_divorce(families,getFamilyIndices("export-BloodTree4.ged"))
    strout='ERROR: FAMILY: US04: 102 :F6000000188715090958: Divorced date  10 AUG 1980, Before Marriage date  20 AUG 1980 , therefore it is not valid.'
    assert strout==str1


