# User Story 31

# List all living people over 30 who have never been married in a GEDCOM file
def list_living_single(individuals, families):
    living_over_30 = [(row['id'], row['age']) for index,row in individuals.iterrows() if (row['alive'] and row['age'] > 30)]
    single_people = [(row['id'], row['age']) for index,row in individuals.iterrows() if type(row['spouse']) is not list]

    living_single = [x for x in living_over_30 if x in single_people]

    print("US31: The list of living people that are single and over 30: " + str(living_single))
