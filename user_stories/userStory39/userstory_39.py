from datetime import date, datetime
import pandas as pd

def is_within_next_30_days(event_date):
    return 0 <= (datetime.strptime(event_date," %d %b %Y").date().replace(year=date.today().year) - date.today()).days <= 30 if pd.notna(event_date) else False

# List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
# Assuming they still have to still be married
# Assuming both couples have to be alive
def list_upcoming_anniversaries(individuals, families):
    upcoming_anniversaries = []
    for index, row in families.iterrows():
        if not row['are divorced']:
            if is_within_next_30_days(row['married']):
                husband_id = row['Husband ID']
                wife_id = row['Wife ID']

                husband_row = individuals.loc[individuals['id'] == husband_id]
                is_husband_alive = husband_row.at[husband_row.index[0], 'alive']

                wife_row = individuals.loc[individuals['id'] == wife_id]
                is_wife_alive = wife_row.at[wife_row.index[0], 'alive']

                upcoming_anniversaries.append((husband_id, wife_id)) if (is_husband_alive and is_wife_alive) else None

    print("US39: The list of all living couples with marriage anniversaries in the next 30 days: " + str(upcoming_anniversaries))
