import io
import unittest
import unittest.mock
import pandas as pd
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
from gedcom_master import createIndDataframe
from gedcom_master import createFamilyDataframe
from userstory9 import areBirthsBeforeParentDeaths

class UserStoryNineTestCase(unittest.TestCase):

  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def testBornBeforeParentsDeath(self, mock_stdout):
    testData = "/content/userStory9TestData.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    families = createFamilyDataframe(testData,individuals_id_and_name)
    areBirthsBeforeParentDeaths(individuals, families)
    self.assertTrue("ERROR: FAMILY: US09: Husband I9 in Family F3 dies before Child I2 is born." in mock_stdout.getvalue())


testCases = UserStoryNineTestCase()
unittest.main(argv=['first-arg-is-ignored','-v'], exit=False)