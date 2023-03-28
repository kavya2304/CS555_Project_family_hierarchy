# User Story 20

def no_newphew_niece_marriage(individuals, families):
    for index, row in families.iterrows():
        wife_id = row['Wife ID']
        husband_id = row['Husband ID']
        if husband_id in getNiblings(wife_id,individuals,families):
            print("ERROR: FAMILY: US20: Line Index # " + str(row['index']) + ": Family " + row['id'] + " is a marriage between a nephew and an aunt!")
        if wife_id in getNiblings(husband_id,individuals,families):
            print("ERROR: FAMILY: US20: Line Index # " + str(row['index']) + ": Family " + row['id'] + " is a marriage between a niece and an uncle!")

def getNiblings(person_id, individuals_dataframe, families_dataframe):
    niblings = []
    for index, row in families_dataframe.iterrows():
        if str(row['children']) != 'nan':
            if person_id in row['children']:
                for child in row['children']:
                    if child != person_id:
                        niblings.extend(getChildren(child,individuals_dataframe, families_dataframe))
    return niblings

def getChildren(person_id, individuals_dataframe, families_dataframe):
    children = []
    spouse_type = ''
    if individuals_dataframe.loc[individuals_dataframe['id'] == person_id, 'gender'].iloc[0] == 'M':
        spouse_type = 'Husband ID'
    else:
        spouse_type = 'Wife ID'
    for index, row in families_dataframe.iterrows():
        if row[spouse_type] == person_id:
            if str(row['children']) != 'nan':
                for child in row['children']:
                    children.append(child)
    return children
