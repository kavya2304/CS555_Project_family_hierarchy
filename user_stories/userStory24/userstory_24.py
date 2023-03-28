# User Story 24

def unique_families(families):
    family_ids = families[['Husband ID', 'Wife ID']]
    check_duplicated = list(family_ids.duplicated())

    return_string = ""
    for i in range(len(check_duplicated)):
        if (check_duplicated[i]):
            return_string += ("ERROR: FAMILY: US24: " + families.loc[i].at['id'] + " is not a unique ID with a unique spouse.\n")
    if return_string != "":
        print(return_string[:-1])
    
    all_unique = not any(check_duplicated)
    if all_unique:
        print("US24: File has all unique families.")

    return all_unique
