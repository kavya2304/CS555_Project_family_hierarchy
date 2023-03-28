import pandas as pd
import os
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
from collections import Counter

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
          family['are divorced'] = False
        if 'DIV' in line.split():
          family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
          family['are divorced'] = True
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
          family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
          family['are divorced'] = False
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

#user story 1
def isDateBeforeCurrentDate(event_date):
  if date.today() > event_date.date():
    return True
  return False


def areIndividualDatesBeforeCurrentDate(individuals_dataframe, id_indices):
  #birthdays
  for id in individuals_dataframe['id']:
    birthday_date = individuals_dataframe.loc[individuals_dataframe['id'] == id, 'birthday'].iloc[0]
    if isDateBeforeCurrentDate(datetime.strptime(birthday_date," %d %b %Y")) == False:
      print("ERROR: INDIVIDUAL: US01: " + str(id_indices[id]) + ": " + id + " Birthday" + birthday_date + " occurs in the future")

    #deaths
    is_alive = individuals_dataframe.loc[individuals_dataframe['id'] == id, 'alive'].iloc[0]
    if is_alive == False:
      death_date = individuals_dataframe.loc[individuals_dataframe['id'] == id, 'death'].iloc[0]
      if isDateBeforeCurrentDate(datetime.strptime(death_date," %d %b %Y")) == False:
        print("ERROR: INDIVIDUAL: US01: " + str(id_indices[id]) + ": " + id + " Death" + death_date + " occurs in the future")

def areFamilyDatesBeforeCurrentDate(families_dataframe, family_id_indices):
  for id in families_dataframe['id']:
    marriage_date = families_dataframe.loc[families_dataframe['id'] == id, 'married'].iloc[0]
    if isDateBeforeCurrentDate(datetime.strptime(marriage_date," %d %b %Y")) == False:
      print("ERROR: FAMILY: US01: " + str(family_id_indices[id]) + ": " + id + " Married" + marriage_date + " occurs in the future")
    
    are_divorced = families_dataframe.loc[families_dataframe['id'] == id, 'are divorced'].iloc[0]
    if are_divorced:
      divorce_date = families_dataframe.loc[families_dataframe['id'] == id, 'divorced'].iloc[0]
      if isDateBeforeCurrentDate(datetime.strptime(divorce_date," %d %b %Y")) == False:
        print("ERROR: FAMILY: US01: " + str(family_id_indices[id]) + ": " + id + " Divorce" + divorce_date + " occurs in the future")

#user story 2

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

#user story 3 and 4

def birth_before_death(individuals_dataframe, id_indices):
    df=individuals_dataframe
    for row in df.itertuples(index=False):
        if not type(row.death)==float or not math.isnan(row.death):
            if compareDates(row.birthday, row.death):
                print("ERROR: INDIVIDUAL: US03: " + row.id + ": " + "Died " + row.death + " before born " + row.birthday)
                

def marriage_before_divorce(families_dataframe, family_id_indices):
    error_type = "US04 Marriage before divorce"
    df2=families_dataframe
    for row in df2.itertuples(index=False):
        if not type(row.married)==float and not type(row.divorced)==float:
            marr = row.married
            divv = row.divorced
            if marr > divv:
                message = "Divorced date "+str(divv)+", Before Marriage date "+str(marr)+ " , therefore it is not valid."
                print(message)

#user story 5

def greaterDate(first_date, second_date):
    if datetime.strptime(first_date, " %d %b %Y") > datetime.strptime(second_date, " %d %b %Y"):
        return True
    return False

def marriageBeforeDeath(individuals, families):
    for index, row in families.iterrows():
        marriageDate = row['married']

        husband_death = individuals.loc[individuals['id'] == row['Husband ID'], 'death'].iloc[0]
        wife_death = individuals.loc[individuals['id'] == row['Wife ID'], 'death'].iloc[0]

        if str(husband_death) != 'nan' and str(marriageDate) != 'nan':
          if greaterDate(str(husband_death), str(marriageDate)) == False:
              print("ERROR: Husband death date before marriage.")

        if str(wife_death) != 'nan' and str(marriageDate) != 'nan':
          if greaterDate(str(wife_death), str(marriageDate)) == False:
              print("Error: Wife death date before marriage.")

# user story 6

def divorceBeforeDeath(individuals, families):
    for index, row in families.iterrows():
        divorceDate = row['divorced']

        husband_death = individuals.loc[individuals['id'] == row['Husband ID'], 'death'].iloc[0]
        wife_death = individuals.loc[individuals['id'] == row['Wife ID'], 'death'].iloc[0]

        if str(husband_death) != 'nan' and str(divorceDate) != 'nan':
          if greaterDate(str(husband_death), str(divorceDate)) == False:
              print("ERROR: Husband death date before divorce.")

        if str(wife_death) != 'nan' and str(divorceDate) != 'nan':
          if greaterDate(str(wife_death), str(divorceDate)) == False:
              print("Error: Wife death date before divorce.")

# user story 7

def check_id(id_list):
    c1 = Counter(id_list)
    c2 = Counter(set(id_list))
    diff = c1-c2
    diff_list = set(diff.elements())
    for x in diff_list:
        print("ID", x, "is not a unique ID")

def unique_ids(filename):
    (individuals,individuals_id_and_name) = createIndDataframe(filename)
    individual_id_list = sorted(list(individuals['id']))
    families = createFamilyDataframe(filename, individuals_id_and_name)
    #family_id_list = ['F1', 'F2', 'F3', 'F3', 'F4', 'F5']
    family_id_list = sorted(list(families['id']))
    check_id(family_id_list)
    check_id(individual_id_list)

# user story 8

def unique_families(filename):
    (individuals,individuals_id_and_name) = createIndDataframe(filename)
    families = createFamilyDataframe(filename, individuals_id_and_name)
    #temp = families.head(1)
    #families = pd.concat([families, temp], ignore_index = True)
    #families.iat[5,0] = 'F6'
    family_ids = families[['Husband ID', 'Wife ID']]
    check_duplicated = list(family_ids.duplicated())


    for i in range(len(check_duplicated)):
        if (check_duplicated[i]):
            print("Family ID", families.loc[i].at['id'], "is not a unique ID with a unique spouse.")
    
    if (not any(check_duplicated)):
        print("File has all unique families.")

# Sprint 1 Acceptance Test

filename = '/content/acceptance_test.ged'

def sprint1acceptancetest(filename):
  id_indices = getIDIndices(filename)
  family_indices = getFamilyIndices(filename)

  (individuals,individuals_id_and_name) = createIndDataframe(filename)
  families = createFamilyDataframe(filename, individuals_id_and_name)

  display(individuals)
  display(families)

  #user story 1
  areIndividualDatesBeforeCurrentDate(individuals,id_indices)
  areFamilyDatesBeforeCurrentDate(families, family_indices)

  #user story 2
  areBirthdaysBeforeMarriages(individuals, families, family_indices)

  #user story 3
  birth_before_death(individuals, id_indices)

  #user story 4
  marriage_before_divorce(families, family_indices)

  #user story 5
  marriageBeforeDeath(individuals,families)

  #user story 6
  divorceBeforeDeath(individuals, families)

  #user story 7
  unique_ids(filename)

  #user story 8
  unique_families(filename)

sprint1acceptancetest(filename)