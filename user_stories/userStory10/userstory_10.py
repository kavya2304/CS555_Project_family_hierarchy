# User Story 10

from datetime import datetime
from dateutil.relativedelta import relativedelta

def marriage_after_14(individuals, families):
    legal_marriage_age = 14
    all_legal_marriages = True

    for index, row in families.iterrows():
        if row['married'] == row['married']:
            marriage_time = datetime.strptime(row['married'], " %d %b %Y")

            #error check if husband in individuals does not exist
            if row['Husband ID'] in individuals['id'].values and row['Wife ID'] in individuals['id'].values: 
                husband_birth = individuals.loc[individuals['id'] == row['Husband ID'], 'birthday'].iloc[0]
                husband_birth_time = datetime.strptime(husband_birth, " %d %b %Y")
                husband_marriage_age = relativedelta(marriage_time, husband_birth_time).years

                wife_birth = individuals.loc[individuals['id'] == row['Wife ID'], 'birthday'].iloc[0]
                wife_birth_time = datetime.strptime(wife_birth, " %d %b %Y")
                wife_marriage_age = relativedelta(marriage_time, wife_birth_time).years

                if husband_marriage_age < legal_marriage_age:
                    print("ERROR: FAMILY: US10: Input Line #" + str(row['index']) + ": "+ row['id'] + ": Husband (" + row['Husband ID'] + ") married before the age of 14")
                    all_legal_marriages = False
                if wife_marriage_age < legal_marriage_age:
                    print("ERROR: FAMILY: US10: Input Line #" + str(row['index']) + ": " + row['id'] + ": Wife (" + row['Wife ID'] + ") married before the age of 14")
                    all_legal_marriages = False

    #if all_legal_marriages:
        #print("US10: File has all marriages after 14.")

    return all_legal_marriages
