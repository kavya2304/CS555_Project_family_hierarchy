# User Story 36

from datetime import datetime

def listRecentDeaths(individuals):
    today = datetime.today()
    deathList = []
    for index, row in individuals.iterrows():
        if str(row['death']) != 'nan':
            deathDate = datetime.strptime(row['death']," %d %b %Y")
            if today.year == deathDate.year and (today-deathDate).days <= 30:
                deathList.append((row['id'], row['age']))
    print("US36: List of Recent Deaths:")
    print(deathList)
