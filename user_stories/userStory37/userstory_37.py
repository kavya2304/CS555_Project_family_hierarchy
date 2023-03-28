# User Story 37

from datetime import date, datetime
import pandas as pd

def is_within_last_30_days(event_date):
    return (date.today() - datetime.strptime(event_date," %d %b %Y").date()).days <= 30 if pd.notna(event_date) else False
    
# List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days
# Assuming spouses mean they were married at one point and don't have to be together
def list_recent_survivors(individuals, families):
    recent_survivors = []
    for index, row in individuals.iterrows():
        if not row['alive']:
            if is_within_last_30_days(row['death']):
                living_spouses, living_descendants = [], []
                for family in row['spouse']:
                    family_row = families.loc[families['id'] == family]

                    # living_spouses and living_descendents lists are unsorted
                    gender_column_string = 'Husband ID' if row['gender'] != 'M' else 'Wife ID'
                    spouse_id = family_row.at[family_row.index[0], gender_column_string]

                    spouse_row = individuals.loc[individuals['id'] == spouse_id]
                    spouse_age = spouse_row.at[spouse_row.index[0], 'age']
                    spouse_alive = spouse_row.at[spouse_row.index[0], 'alive']
                    living_spouses.append((spouse_id, spouse_age)) if spouse_alive else None

                    children_list = family_row.at[family_row.index[0], 'children']
                    descendants_rows = individuals.loc[individuals['id'].isin(children_list) & individuals['alive'] == True]

                    for index, descendant in descendants_rows.iterrows():
                        living_descendants.append((descendant['id'], descendant['age']))

                new_recent_survivors = {
                    'name': (row['id'], row['age']),
                    'living spouses': living_spouses, 
                    'living descendants': living_descendants
                }
                recent_survivors.append(new_recent_survivors)

    print("US37: The list of all living spouses and descendants of people who died in the last 30 days: " + str(recent_survivors))
