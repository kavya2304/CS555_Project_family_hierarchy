import pytest
import pandas as pd
import pandas as pd
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import user_stories
from user_stories import parents_not_too_old

import pytest
import pandas as pd

def test_parents_not_too_old():
    
    testData = "export-BloodTree.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    families = createFamilyDataframe(testData, individuals_id_and_name)
    strout="ERROR: FAMILY: US12: : F6000000188481846843 Age of child: 5 Age of mother: 32 Age of Father: 53"
    str1=parents_not_too_old(individuals,families,getFamilyIndices(testData))
    print(str1)
    assert strout==parents_not_too_old(individuals,families,getFamilyIndices(testData))
    


#test_parents_not_too_old()
