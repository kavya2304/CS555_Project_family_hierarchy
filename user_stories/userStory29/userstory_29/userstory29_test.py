import unittest
import unittest.mock
import pandas as pd
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import gedcom_master
from user_stories import userstory_29

class userstory29testCase(unittest.TestCase):
    def testGetDead(self):
        deadPeople = [('I1',' Roger /Henry/'),('I2',' Rick /Henry/'),('I3',' Jill /Alberts/')]
        filename = 'test_cases/userstory_29/userstory29_test.ged'
        (indi_dataframe, id_indices) = gedcom_master.createIndDataframe(filename)
        self.assertEqual(userstory_29.getDeadPeople(indi_dataframe),deadPeople)

testCases = userstory29testCase()
if __name__ == '__main__':
    unittest.main()