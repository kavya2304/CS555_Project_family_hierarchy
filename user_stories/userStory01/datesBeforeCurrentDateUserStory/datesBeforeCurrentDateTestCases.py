import unittest
import pandas as pd
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

#Test Cases for User Story 1

class UserStoryOneTestMethods(unittest.TestCase):

  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def testIndividualDeathDates(self, mock_stdout):
    testData = "/content/datesBeforeCurrentDateTestData1.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    id_indices = getIDIndices(testData)
    areIndividualDatesBeforeCurrentDate(individuals,id_indices)
    self.assertTrue("ERROR: INDIVIDUAL: US01: 31: I3 Death 8 AUG 3000 occurs in the future" in mock_stdout.getvalue())


  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def testIndividualBirthdayDates(self, mock_stdout):
    testData = "/content/datesBeforeCurrentDateTestData1.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    id_indices = getIDIndices(testData)
    areIndividualDatesBeforeCurrentDate(individuals,id_indices)
    self.assertTrue("ERROR: INDIVIDUAL: US01: 13: I1 Birthday 9 APR 2023 occurs in the future" in mock_stdout.getvalue())

  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def testFamilyMarriageDates(self,mock_stdout):
    testData = "/content/datesBeforeCurrentDateTestData1.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    families = createFamilyDataframe(testData,individuals_id_and_name)
    family_indices = getFamilyIndices(testData)
    areFamilyDatesBeforeCurrentDate(families,family_indices)
    self.assertTrue("ERROR: FAMILY: US01:42: F1 Married 9 AUG 2030 occurs in the future" in mock_stdout.getvalue())

  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def testFamilyDivorceDates(self,mock_stdout):
    testData = "/content/datesBeforeCurrentDateTestData1.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    families = createFamilyDataframe(testData,individuals_id_and_name)
    family_indices = getFamilyIndices(testData)
    areFamilyDatesBeforeCurrentDate(families,family_indices)
    self.assertTrue("ERROR: FAMILY: US01:42: F1 Divorce 9 MAY 2024 occurs in the future" in mock_stdout.getvalue())

  def testAllDatesBeforeCurrentDate(self):
      count = 0
      testData = "/content/datesBeforeCurrentDateTestData2.ged"
      f = open(testData, "r")
      lines = f.readlines()
      index = 0
      for line in lines:
        if 'DATE' in line.split():
          date = datetime.strptime(line.split('DATE')[1].replace('\n',''), " %d %b %Y")
          with self.subTest(date=date):
            self.assertTrue(isDateBeforeCurrentDate(date))

testCases = UserStoryOneTestMethods()
unittest.main(argv=['first-arg-is-ignored','-v'], exit=False)