# User Story 19

def isChildInFamily(person_id, families):
    childinfamily = False
    for index, row in families.iterrows():
        if str(row['children']) != 'nan' and person_id in row['children']:
            childinfamily = True
    return childinfamily

def no_cousins_marriage(individuals, families):
    for index, row in families.iterrows():
        wife_id = row['Wife ID']
        husband_id = row['Husband ID']
        if husband_id in getFirstCousins(wife_id,individuals,families):
            print("ERROR: FAMILY: US19: Line Index # " + str(row['index']) + ": Family " + row['id'] + " is a marriage between first cousins!")
                
def getFirstCousins(person_id, individuals_dataframe, families_dataframe):
    cousins = []
    for index, row in families_dataframe.iterrows():
        husband_id = row['Husband ID']
        wife_id = row['Wife ID']
        if str(row['children']) != 'nan':
            if person_id in row['children']:
                cousins.extend(getNiblings(husband_id,individuals_dataframe, families_dataframe))
                cousins.extend(getNiblings(wife_id,individuals_dataframe, families_dataframe))
    return cousins

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
