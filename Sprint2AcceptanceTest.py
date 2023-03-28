import pandas as pd
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import gedcom_master
from user_stories import userstory_1,userstory_2,userstory_3,userstory_4,userstory_5,userstory_6,userstory_7,userstory_8,userstory_09,userstory_15,userstory_16,userstory_26,userstory_27,userstory_40,userstory_41,userstory_42
from user_stories import userstory_10,userstory_18, userstory_42


filename = 'Sprint2AcceptanceTest.ged'


def sprint2AcceptanceTest(filename):
  id_indices = gedcom_master.getIDIndices(filename)
  family_indices = gedcom_master.getFamilyIndices(filename)
  (individuals,individuals_id_and_name) = gedcom_master.createIndDataframe(filename)
  families = gedcom_master.createFamilyDataframe(filename, individuals_id_and_name)


  #user story 1
  userstory_1.areIndividualDatesBeforeCurrentDate(individuals,id_indices)
  userstory_1.areFamilyDatesBeforeCurrentDate(families, family_indices)

  #user story 2
  userstory_2.areBirthdaysBeforeMarriages(individuals, families, family_indices)

  #user story 3
  userstory_3.birth_before_death(individuals, id_indices)

  #user story 4
  userstory_4.marriage_before_divorce(families, family_indices)

  #user story 5
  userstory_5.marriageBeforeDeath(individuals,families)

  #user story 6
  userstory_6.divorceBeforeDeath(individuals, families)

  #user story 7
  userstory_7.unique_ids(individuals,families)

  #user story 8
  userstory_8.unique_families(families)

  #user story 9
  userstory_09.areBirthsBeforeParentDeaths(individuals,families)

  #user story 10
  userstory_10.marriage_after_14(individuals,families)

  #user story 18
  userstory_18.no_siblings_marriage(individuals,families)

  #user story 26
  userstory_26.hasCorrespondingEntries(individuals,families)

  #user story 27
  userstory_27.individual_ages(individuals)
  

  print(individuals)
  print(families)


sprint2AcceptanceTest(filename_one, filename_two)



