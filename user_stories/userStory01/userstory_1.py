# User Story 1

from datetime import datetime
from datetime import date

def isDateBeforeCurrentDate(event_date):
  return date.today() > event_date.date()

def areIndividualDatesBeforeCurrentDate(individuals_dataframe, id_indices):
  #birthdays
  for id in individuals_dataframe['id']:
    birthday_date = individuals_dataframe.loc[individuals_dataframe['id'] == id, 'birthday'].iloc[0]
    if isDateBeforeCurrentDate(datetime.strptime(birthday_date," %d %b %Y")) == False:
      print("ERROR: INDIVIDUAL: US01: " + str(id_indices[id]) + ": " + id + " Birthday" + birthday_date + " occurs in the future")

  #deaths
  is_alive = individuals_dataframe.loc[individuals_dataframe['id'] == id, 'alive'].iloc[0]
  if not is_alive:
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
