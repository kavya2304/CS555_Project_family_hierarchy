# User Story 33

def listOrphans(individuals, families):
    orphans = []
    for index, row in individuals.iterrows():
        if row['age'] < 18:
            if hasDeadParents(row['id'],individuals,families):
                orphans.append((row['id'], row['age']))
    if len(orphans) > 0:
        print('US33: List of Orphans:')
        print(orphans) 

def hasDeadParents(child_id, individuals, families):
    deadparents = False
    for index, row in families.iterrows():
        # row['children'] != 'nan' does not work because it can be a list, so to check if entry is not empty check if it's a list
        if type(row['children']) is list and (child_id in row['children']):
            husband_id = row['Husband ID']
            wife_id = row['Wife ID']
            deadparents = not individuals[individuals['id']==husband_id].squeeze()['alive'] and not individuals[individuals['id']==wife_id].squeeze()['alive']
    return deadparents
