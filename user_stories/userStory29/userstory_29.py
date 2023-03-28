# User Story 29

def getDeadPeople(individuals_dataframe):
    print("US29: List of dead people")
    deadPeople = [(row['id'], row['age']) for index, row in individuals_dataframe.iterrows() if not row['alive']]
    print(deadPeople)
