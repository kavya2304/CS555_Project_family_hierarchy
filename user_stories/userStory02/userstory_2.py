# User Story 2

from datetime import datetime

def compareDates(date_one, date_two):
  return datetime.strptime(date_one," %d %b %Y") > datetime.strptime(date_two," %d %b %Y")

def areBirthdaysBeforeMarriages(individuals_dataframe, families_dataframe, family_id_indices):
  for index, row in families_dataframe.iterrows():
    marriage_date = row['married']
    husband_birthday = individuals_dataframe.loc[individuals_dataframe['id'] == row['Husband ID'], 'birthday'].iloc[0]
    wife_birthday = individuals_dataframe.loc[individuals_dataframe['id'] == row['Wife ID'], 'birthday'].iloc[0]

    if compareDates(marriage_date, husband_birthday) == False:
      print("ERROR: FAMILY: US02: " + str(family_id_indices[row['id']]) + ": " + row['id'] + " Husband's birth date" + husband_birthday + " after marriage date" + marriage_date)
    
    if compareDates(marriage_date, wife_birthday) == False:
      print("ERROR: FAMILY: US02: " + str(family_id_indices[row['id']]) + ": " + row['id'] + " Wife's birth date" + wife_birthday + " after marriage date" + marriage_date)

#(individuals,individuals_id_and_name) = createIndDataframe("/content/birthdayBeforeMarriageTestData1.ged")
#families = createFamilyDataframe("/content/birthdayBeforeMarriageTestData1.ged", individuals_id_and_name)
#areBirthdaysBeforeMarriages(individuals,families,getFamilyIndices("/content/birthdayBeforeMarriageTestData1.ged"))