# User Story 38

from datetime import datetime

def listUpComingBirthdays(individuals):
    today = datetime.today()
    birthdayList = []
    for index, row in individuals.iterrows():
        if str(row['birthday']) != 'nan':
            birthday = datetime.strptime(row['birthday']," %d %b %Y")
            birthDate = datetime(today.year, birthday.month, birthday.day)
            if abs((today-birthDate).days) <= 30:
                birthdayList.append((row['id'],row['age']))
    print("US38: List of Upcoming Birthdays:")
    print(birthdayList)
