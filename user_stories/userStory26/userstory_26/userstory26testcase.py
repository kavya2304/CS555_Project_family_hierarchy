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
from userstory26 import hasCorrespondingEntries

#Test Case for User Story 26

class UserStoryTwentySixTestCase(unittest.TestCase):

  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def testMissingEntries(self, mock_stdout):
    testData = "/content/userStory26TestData.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    families = createFamilyDataframe(testData,individuals_id_and_name)
    print(hasCorrespondingEntries(individuals, families))
    self.assertTrue("ERROR: INDIVIDUAL: US26: I2 not in Family F1 as a spouse." in mock_stdout.getvalue())
    self.assertTrue("ERROR: INDIVIDUAL: US26: I8 not in Family F2 as a child." in mock_stdout.getvalue())
    self.assertTrue("ERROR: FAMILY: US26: Wife I3 not in table of individuals" in mock_stdout.getvalue())
    self.assertTrue("ERROR: FAMILY: US26: Child I3 not in table of individuals" in mock_stdout.getvalue())
    self.assertTrue("ERROR: FAMILY: US26: Child I1 not in table of individuals" in mock_stdout.getvalue())

testCases = UserStoryTwentySixTestCase()
unittest.main(argv=['first-arg-is-ignored','-v'], exit=False)
