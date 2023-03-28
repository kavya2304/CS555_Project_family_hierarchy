# User Story 3

import math
from datetime import datetime

def compareDates(date_one, date_two):
    return datetime.strptime(date_one," %d %b %Y") > datetime.strptime(date_two," %d %b %Y")

def birth_before_death(individuals_dataframe, id_indices):
    df = individuals_dataframe
    for row in df.itertuples(index=False):
        if not type(row.death) == float or not math.isnan(row.death):
            if compareDates(row.birthday, row.death):
                print("ERROR: INDIVIDUAL: US03: " + str(id_indices[row.id]) + ": " + row.id + ": " + "Died " + row.death + " before born " + row.birthday)

#(individuals,individuals_id_and_name) = createIndDataframe("test_data.ged")
#birth_before_death(individuals,getIDIndices("test_data.ged"))
