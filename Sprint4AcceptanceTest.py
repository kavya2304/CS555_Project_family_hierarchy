import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
from gedcom_helper import *

from user_stories.userStory01.userstory_1 import *
from user_stories.userStory02.userstory_2 import *
from user_stories.userStory03.userstory_3 import *
from user_stories.userStory04.userstory_4 import *
from user_stories.userStory05.userstory_5 import *
from user_stories.userStory06.userstory_6 import *
from user_stories.userStory22.userstory_22 import *
from user_stories.userStory24.userstory_24 import *
from user_stories.userStory09.userstory_09 import *
from user_stories.userStory26.userstory_26 import *
from user_stories.userStory27.userstory_27 import *
from user_stories.userStory40.userstory_40 import *
from user_stories.userStory41.userstory_41 import *
from user_stories.userStory42.userstory_42 import *
from user_stories.userStory10.userstory_10 import *
from user_stories.userStory18.userstory_18 import *
from user_stories.userStory28.userstory_28 import *
from user_stories.userStory29.userstory_29 import *
from user_stories.userStory12.userstory_12 import *
from user_stories.userStory17.userstory_17 import *
from user_stories.userStory19.userstory_19 import *
from user_stories.userStory20.userstory_20 import *
from user_stories.userStory30.userstory_30 import *
from user_stories.userStory31.userstory_31 import *
from user_stories.userStory32.userstory_32 import *
from user_stories.userStory33.userstory_33 import *
from user_stories.userStory36.userstory_36 import *
from user_stories.userStory38.userstory_38 import *
from user_stories.userStory34.userstory_34 import *
from user_stories.userStory35.userstory_35 import *
from user_stories.userStory37.userstory_37 import *
from user_stories.userStory39.userstory_39 import *

filename = 'Sprint4AcceptanceTest.ged'

def sprint4AcceptanceTest(filename):
    id_indices = getIDIndices(filename)
    family_indices = getFamilyIndices(filename)
    (individuals,individuals_id_and_name) = createIndDataframe(filename)
    families = createFamilyDataframe(filename, individuals_id_and_name)

    #user story 1
    areIndividualDatesBeforeCurrentDate(individuals,id_indices)
    areFamilyDatesBeforeCurrentDate(families, family_indices)

    #user story 2
    areBirthdaysBeforeMarriages(individuals, families, family_indices)

    #user story 3
    birth_before_death(individuals, id_indices)

    #user story 4
    marriage_before_divorce(families, family_indices)

    #user story 5
    marriageBeforeDeath(individuals,families)

    #user story 6
    divorceBeforeDeath(individuals, families)

    #user story 22
    unique_ids(individuals,families)

    #user story 24
    unique_families(families)

    #user story 9
    areBirthsBeforeParentDeaths(individuals,families, family_indices)

    #user story 26
    hasCorrespondingEntries(individuals,families)

    #user story 27
    individual_ages(individuals, id_indices)

    #user story 10
    marriage_after_14(individuals,families)

    #user story 18
    no_siblings_marriage(individuals,families)

    #user story 28
    listChildrenByAge(individuals,families)

    #user story 29
    getDeadPeople(individuals)

    #user story 12
    parents_not_too_old(individuals,families,family_indices)

    #user story 17
    no_marriages_to_descendants(individuals,families,family_indices)

    #user story 19
    no_cousins_marriage(individuals,families)

    #user story 20
    no_newphew_niece_marriage(individuals,families)

    #user story 30
    list_living_married(individuals,families)

    #user story 31
    list_living_single(individuals,families)

    #user story 32
    listMultipleBirths(individuals)

    #user story 33
    listOrphans(individuals,families)

    #user story 36
    listRecentDeaths(individuals)

    #user story 38
    listUpComingBirthdays(individuals)

    #user story 34
    large_age_difference(individuals, families)

    #user story 35
    listRecentBirths(individuals)

    #user story 37
    list_recent_survivors(individuals, families)

    #user story 39
    list_upcoming_anniversaries(individuals, families)

    print(individuals)
    print(families)

sprint4AcceptanceTest(filename)