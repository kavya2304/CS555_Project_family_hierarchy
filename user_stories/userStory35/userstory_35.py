# User Story 35

from datetime import datetime
import math

def listRecentBirths(individuals):
    current = datetime.now()
    recentBirthsList = []
    for index, row in individuals.iterrows():
        if not type(row.birthday) == float or not math.isnan(row.birthday):
            birthday = datetime.strptime(row.birthday, " %d %b %Y")
            if (current.year - birthday.year == 0):
                if ((current - birthday).days < 30):
                    recentBirthsList.append((row['id'],row['age']))
    print("US35: List of recent births: " + str(recentBirthsList))
    