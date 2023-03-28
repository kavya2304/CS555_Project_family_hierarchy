# User Story 30

# List all living married people in a GEDCOM file
# Bug: Does not check if person is divorced
def list_living_married(individuals, families):
    living_people = [(row['id'], row['age']) for index,row in individuals.iterrows() if row['alive']]
    married_people = []
    for index, row in individuals.iterrows():
        if type(row['spouse']) is list:
            for family in row['spouse']:
                family_row = families.loc[families['id'] == family]
                family_divorced = family_row.at[family_row.index[0], 'are divorced']
                if not family_divorced:
                    married_people.append((row['id'], row['age']))
                    break
    living_married = [x for x in living_people if x in married_people]

    print("US30: The list of living people that are married: " + str(living_married))
