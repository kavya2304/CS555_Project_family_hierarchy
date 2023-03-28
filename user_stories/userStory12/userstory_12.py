# User Story 12

import math
    
def parents_not_too_old(individuals,families,family_id_indices):
    message="Parents are not too old"
    for index, row in families.iterrows():
        if not type(row.children)==float or not math.isnan(row.children):
            age_of_mother=individuals.loc[individuals['id']==row['Wife ID'],'age'].iloc[0]
            age_of_father=individuals.loc[individuals['id']==row['Husband ID'],'age'].iloc[0]
            for child in row.children:
                age_of_child=individuals.loc[individuals['id']==child,'age'].iloc[0]
                if (age_of_mother-age_of_child)>=60 or (age_of_father-age_of_child)>=80:                     
                        message="ERROR: FAMILY: US12: " + str(family_id_indices[row['id']]) + ": " + row['id'] + " Age of child: " + str(age_of_child) + " Age of mother: " + str(age_of_mother)+ " Age of Father: "+ str(age_of_father)
                        print(message)     
    return message

#(individuals,individuals_id_and_name) = createIndDataframe("test_data.ged")
#families = createFamilyDataframe("test_data.ged", individuals_id_and_name)
#parents_not_too_old(individuals,families,getFamilyIndices("test_data.ged"))
