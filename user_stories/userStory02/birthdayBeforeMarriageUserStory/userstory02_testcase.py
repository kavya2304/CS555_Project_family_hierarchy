import io
import unittest
import unittest.mock
import pandas as pd
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

def isDateBeforeCurrentDate(event_date):
  if date.today() > event_date.date():
    return True
  return False

def createIndDataframe(filename):
  individuals = []
  individuals_id_and_name = {}
  f = open(filename, "r")
  lines = f.readlines()

  indices = []
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'INDI' in line.split() and level == '0':
      indices.append(i)

  for i in indices:
    is_dead = False
    person = {
    }
    if indices.index(i) != len(indices)-1:
      for j in range(i,indices[indices.index(i)+1]):
        line = lines[j]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
          person['id'] = line.split()[1].replace('@','')
        if 'NAME' in line.split():
          person['name'] = line.split('NAME')[1].replace('\n','')
          individuals_id_and_name[person['id']] = person['name']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          person['birthday'] =  lines[j+1].split('DATE')[1].replace('\n','')
        if 'DEAT' in line.split():
          is_dead = True
          person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'FAMC' in line.split():
          person['child'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          person['spouse'] = line.split()[2].replace('@','')
    else:
      for j in range(i,len(lines)-1):
        line = lines[j]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
          person['id'] = line.split()[1].replace('@','')
        if 'NAME' in line.split():
          person['name'] = line.split('NAME')[1].replace('\n','')
          individuals_id_and_name[person['id']] = person['name']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          person['birthday'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'DEAT' in line.split():
          is_dead = True
          person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'FAMC' in line.split():
          person['child'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          person['spouse'] = line.split()[2].replace('@','')

    if is_dead:
       person['alive'] = False
       person['age'] = relativedelta(datetime.strptime(person['death']," %d %b %Y"),datetime.strptime(person['birthday']," %d %b %Y")).years
    else:
      person['alive'] = True
      today = date.today()
      person['age'] = relativedelta(today, datetime.strptime(person['birthday']," %d %b %Y")).years


    individuals.append(person)

      
  return (pd.DataFrame(individuals),individuals_id_and_name)

def createFamilyDataframe(filename, individuals_id_and_name):
  families = []
  f = open(filename, "r")
  lines = f.readlines()

  indices = []
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'FAM' in line.split() and level == '0':
      indices.append(i)
  
  for i in indices:
    family = {
    }
    if indices.index(i) != len(indices)-1:
      for j in range(i,indices[indices.index(i)+1]):
        line = lines[j]
        level = line[0]
        if 'FAM' in line.split() and level == '0':
          family['id'] = line.split()[1].replace('@','')
        if 'MARR' in line.split():
          family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'DIV' in line.split():
          family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'HUSB' in line.split():
          family['Husband ID'] = line.split()[2].replace('@','')
          family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
        if 'WIFE' in line.split():
          family['Wife ID'] = line.split()[2].replace('@','')
          family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
        if 'CHIL' in line.split():
          if 'children' in family: 
            family['children'].append(line.split()[2].replace('@',''))
          else:
            family['children'] = []
            family['children'].append(line.split()[2].replace('@',''))
    else:
      for j in range(i,len(lines)-1):
        line = lines[j]
        level = line[0]
        if 'FAM' in line.split() and level == '0':
          family['id'] = line.split()[1].replace('@','')
        if 'MARR' in line.split():
          family['are divorced'] = False
          family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'DIV' in line.split():
          family['are divorced'] = True
          family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'HUSB' in line.split():
          family['Husband ID'] = line.split()[2].replace('@','')
          family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
        if 'WIFE' in line.split():
          family['Wife ID'] = line.split()[2].replace('@','')
          family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
        if 'CHIL' in line.split():
          if 'children' in family: 
            family['children'].append(line.split()[2].replace('@',''))
          else:
            family['children'] = []
            family['children'].append(line.split()[2].replace('@',''))

    families.append(family)

  return pd.DataFrame(families)

def getIDIndices(filename):
  indices = {}
  f = open(filename, "r")
  lines = f.readlines()
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'INDI' in line.split() and level == '0':
      indices[line.split()[1].replace('@','')] = i
  return indices


def getFamilyIndices(filename):
  indices = {}
  f = open(filename, "r")
  lines = f.readlines()
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'FAM' in line.split() and level == '0':
      indices[line.split()[1].replace('@','')] = i
  return indices


def compareDates(date_one, date_two):
  if datetime.strptime(date_one," %d %b %Y") > datetime.strptime(date_two," %d %b %Y"):
    return True
  return False

def areBirthdaysBeforeMarriages(individuals_dataframe, families_dataframe, family_id_indices):
  for index, row in families_dataframe.iterrows():
    marriage_date = row['married']
    husband_birthday = individuals_dataframe.loc[individuals_dataframe['id'] == row['Husband ID'], 'birthday'].iloc[0]
    wife_birthday = individuals_dataframe.loc[individuals_dataframe['id'] == row['Wife ID'], 'birthday'].iloc[0]

    if compareDates(marriage_date, husband_birthday) == False:
      print("ERROR: FAMILY: US02: " + str(family_id_indices[row['id']]) + ": " + row['id'] + " Husband's birth date" + husband_birthday + " after marriage date" + marriage_date)
    
    if compareDates(marriage_date, wife_birthday) == False:
      print("ERROR: FAMILY: US02: " + str(family_id_indices[row['id']]) + ": " + row['id'] + " Wife's birth date" + wife_birthday + " after marriage date" + marriage_date)

(individuals,individuals_id_and_name) = createIndDataframe("/content/birthdayBeforeMarriageTestData1.ged")
families = createFamilyDataframe("/content/birthdayBeforeMarriageTestData1.ged", individuals_id_and_name)
areBirthdaysBeforeMarriages(individuals,families,getFamilyIndices("/content/birthdayBeforeMarriageTestData1.ged"))

#Test Cases for User Story 2

class UserStoryTwoTestMethods(unittest.TestCase):

  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def testAllBirthDatesAfterMarriage(self, mock_stdout):
    testData = "/content/birthdayBeforeMarriageTestData1.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    families = createFamilyDataframe(testData, individuals_id_and_name)
    areBirthdaysBeforeMarriages(individuals,families,getFamilyIndices(testData))
    self.assertTrue("ERROR: FAMILY: US02: 40: F1 Husband's birth date 7 JUN 2300 after marriage date 10 JUN 2000" in mock_stdout.getvalue())
    self.assertTrue("ERROR: FAMILY: US02: 40: F1 Wife's birth date 8 JUL 2320 after marriage date 10 JUN 2000" in mock_stdout.getvalue())

  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def testAllBirthDatesBeforeMarriage(self, mock_stdout):
    testData = "/content/birthdayBeforeMarriageTestData2.ged"
    (individuals,individuals_id_and_name) = createIndDataframe(testData)
    families = createFamilyDataframe(testData, individuals_id_and_name)
    areBirthdaysBeforeMarriages(individuals,families,getFamilyIndices(testData))
    self.assertTrue(mock_stdout.getvalue() == "")

testCases = UserStoryTwoTestMethods()
unittest.main(argv=['first-arg-is-ignored','-v'], exit=False)