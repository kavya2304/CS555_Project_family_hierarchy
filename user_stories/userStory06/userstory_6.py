# User Story 6

from datetime import datetime

def greaterDate(first_date, second_date):
    return datetime.strptime(first_date, " %d %b %Y") > datetime.strptime(second_date, " %d %b %Y")

def divorceBeforeDeath(individuals, families):
    for index, row in families.iterrows():
        divorceDate = row['divorced']

        husband_death = individuals.loc[individuals['id'] == row['Husband ID'], 'death'].iloc[0]
        wife_death = individuals.loc[individuals['id'] == row['Wife ID'], 'death'].iloc[0]

        if str(husband_death) != 'nan' and str(divorceDate) != 'nan':
          if greaterDate(str(husband_death), str(divorceDate)) == False:
              print("ERROR: US06: Input Line #: " + str(row['index']) + ": Husband " + row['Husband ID'] + " death date before divorce.")

        if str(wife_death) != 'nan' and str(divorceDate) != 'nan':
          if greaterDate(str(wife_death), str(divorceDate)) == False:
              print("ERROR: US06: Input Line #: " + str(row['index']) + ": Wife " + row['Wife ID'] + " death date before divorce.")
