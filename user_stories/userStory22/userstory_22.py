# User Story 22

# Sort the list of IDs and check for duplicates
def check_id(id_list, indi_or_fam):
    visited = set()
    diff_list = sorted({x for x in id_list if x in visited or (visited.add(x) or False)})

    return_string = ""
    for x in diff_list:
        return_string += ("ERROR: " + indi_or_fam.upper() + ": US22: " + x + " is not a unique " + indi_or_fam.capitalize() + " ID.\n")
    if return_string != "":
        print(return_string[:-1])

    return len(diff_list) == 0

def unique_ids(individuals, families):
    individual_id_list = sorted(list(individuals['id']))
    family_id_list = sorted(list(families['id']))

    has_unique_individuals = check_id(individual_id_list, "individual")
    has_unique_families = check_id(family_id_list, "family")
    all_unique = has_unique_individuals and has_unique_families

    if all_unique:
        print("US22: File has all unique IDs.")

    return all_unique
