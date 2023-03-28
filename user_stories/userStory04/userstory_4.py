# User Story 4

from datetime import datetime

def marriage_before_divorce(families_dataframe, family_id_indices):
    df2 = families_dataframe
    for row in df2.itertuples(index=False):
        if not type(row.married) == float and not type(row.divorced) == float:
            marr = row.married
            divv = row.divorced
            if datetime.strptime(marr," %d %b %Y") > datetime.strptime(divv," %d %b %Y"):    
                message = "ERROR: FAMILY: US04: " + str(family_id_indices[row.id]) +" :"+ row.id + ": Divorced date " + str(divv) + ", Before Marriage date " + str(marr) + " , therefore it is not valid."
                print(message)       
                
#(individuals,individuals_id_and_name) = createIndDataframe("test_data.ged")
#families = createFamilyDataframe("test_data.ged", individuals_id_and_name)
#marriage_before_divorce(families,getFamilyIndices("test_data.ged"))