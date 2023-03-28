# User Story 27

import math
    
def individual_ages(individuals_dataframe,id_indices):
    for index,row in individuals_dataframe.iterrows():
        name, age = row['name'], row["age"]
        if age < 0 or math.isnan(age):
            message = "ERROR: INDIVIDUAL: US27: " + str(id_indices[row['id']]) + ": " + row['id'] + " Name: " + name + " does not have a valid age."
            print(message)
        #else:
            #print("NAME:"+ name +",Age:" + str(age))
