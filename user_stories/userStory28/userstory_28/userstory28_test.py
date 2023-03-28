import unittest
import unittest.mock
import pandas as pd
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import gedcom_master
from user_stories import userstory_28

class userstory28testCase(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testChildSort(self, mock_stdout):
        correctOrder = [('I1',' Roger /Henry/'),('I2',' Rick /Henry/'),('I3',' Jill /Alberts/')]
        filename = 'test_cases/userstory_28/userstory28_test.ged'
        (indi_dataframe, id_indices) = gedcom_master.createIndDataframe(filename)
        families_dataframe = gedcom_master.createFamilyDataframe(filename,id_indices)
        userstory_28.listChildrenByAge(indi_dataframe,families_dataframe)
        self.assertTrue("['I1', 'I4']" in mock_stdout.getvalue())


testCases = userstory28testCase()
if __name__ == '__main__':
    unittest.main()
