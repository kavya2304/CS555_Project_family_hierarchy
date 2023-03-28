import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import user_stories.userStory41.userstory_41 as userstory_41
import user_stories.userStory42.userstory_42 as userstory_42

individuals = []
individuals_id_and_name = []
families = []

allowed_tags = {
    0 : ['INDI','FAM','HEAD','TRLR','NOTE'],
    1 : ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV'],
    2 : ['DATE']
}


def parse_gedcom(filename):
    f = open(filename, "r")
    for line in f:
        level = line[0]
        tag = ''
        arguments = ''
        if 'INDI' in line.split():
            tag = 'INDI'
            arguments = line.split()[1] + '\n'
        elif 'FAM' in line.split():
            tag = 'FAM'
            arguments = line.split()[1] + '\n'
        else:
            tag = line.split()[1]
        if (line.split(tag,1)[1])[1:] != '':
            arguments = (line.split(tag,1)[1])[1:]
        else:
            arguments = '\n'
            valid = 'N'
        if tag in allowed_tags[int(level)]:
            valid = 'Y'
        
        print('--> ' + line)
        print('<-- ' + level + '|' + tag + 
            '|' + valid + '|' + arguments)
    f.close()
  
def createIndDataframe(filename):
  individuals = []
  individuals_id_and_name = {}
  f = open(filename, "r")
  lines = f.readlines()

  indices = []
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'INDI' in line.split() and level == '0':
      indices.append(i)

  for i in indices:
    is_dead = False
    person = {
    }
    if indices.index(i) != len(indices)-1:
      for j in range(i,indices[indices.index(i)+1]):
        line = lines[j]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
          person['id'] = line.split()[1].replace('@','')
          person['index'] = i
        if 'NAME' in line.split():
          person['name'] = line.split('NAME')[1].replace('\n','')
          individuals_id_and_name[person['id']] = person['name']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          userstory_42.reject_illegitimate_dates(lines[j+1].split('DATE')[1].replace('\n',''),j+1)
          birthdate = userstory_41.include_partial_dates(lines[j+1].split('DATE')[1].replace('\n',''),j+1)
          person['birthday'] =  birthdate
        if 'DEAT' in line.split():
          is_dead = True
          userstory_42.reject_illegitimate_dates(lines[j+1].split('DATE')[1].replace('\n',''),j+1)
          deathdate = userstory_41.include_partial_dates(lines[j+1].split('DATE')[1].replace('\n',''),j+1)
          person['death'] = deathdate
        if 'FAMC' in line.split():
          person['child'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          if 'spouse' in person.keys():
              person['spouse'].append(line.split()[2].replace('@',''))
          else :
              person['spouse'] = [line.split()[2].replace('@','')]
    else:
      for j in range(i,len(lines)-1):
        line = lines[j]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
          person['id'] = line.split()[1].replace('@','')
          person['index'] = i
        if 'NAME' in line.split():
          person['name'] = line.split('NAME')[1].replace('\n','')
          individuals_id_and_name[person['id']] = person['name']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          userstory_42.reject_illegitimate_dates(lines[j+1].split('DATE')[1].replace('\n',''),j+1)
          birthdate = userstory_41.include_partial_dates(lines[j+1].split('DATE')[1].replace('\n',''),j+1)
          person['birthday'] = birthdate
        if 'DEAT' in line.split():
          is_dead = True
          userstory_42.reject_illegitimate_dates(lines[j+1].split('DATE')[1].replace('\n',''),j+1)
          deathdate = userstory_41.include_partial_dates(lines[j+1].split('DATE')[1].replace('\n',''),j+1)
          person['death'] = deathdate
        if 'FAMC' in line.split():
          person['child'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          if 'spouse' in person.keys():
              person['spouse'].append(line.split()[2].replace('@',''))
          else :
              person['spouse'] = [line.split()[2].replace('@','')]

    if is_dead:
       person['alive'] = False
       person['age'] = relativedelta(datetime.strptime(person['death']," %d %b %Y"),datetime.strptime(person['birthday']," %d %b %Y")).years
    else:
      person['alive'] = True
      today = date.today()
      person['age'] = relativedelta(today, datetime.strptime(person['birthday']," %d %b %Y")).years


    individuals.append(person)

  f.close()
      
  return (pd.DataFrame(individuals),individuals_id_and_name)

def createFamilyDataframe(filename, individuals_id_and_name):
  families = []
  f = open(filename, "r")
  lines = f.readlines()

  indices = []
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'FAM' in line.split() and level == '0':
      indices.append(i)
  
  for i in indices:
    family = {
    }
    if indices.index(i) != len(indices)-1:
      for j in range(i,indices[indices.index(i)+1]):
        line = lines[j]
        level = line[0]
        if 'FAM' in line.split() and level == '0':
          family['id'] = line.split()[1].replace('@','')
          family['index'] = i
        if 'MARR' in line.split():
          family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
          family['are divorced'] = False
        if 'DIV' in line.split():
          family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
          family['are divorced'] = True
        if 'HUSB' in line.split():
          family['Husband ID'] = line.split()[2].replace('@','')
          try:
            family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
          except KeyError:
            family['Husband Name'] = 'nan'
        if 'WIFE' in line.split():
          family['Wife ID'] = line.split()[2].replace('@','')
          try:
            family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
          except KeyError:
            family['Wife Name'] = 'nan'
        if 'CHIL' in line.split():
          if 'children' in family: 
            family['children'].append(line.split()[2].replace('@',''))
          else:
            family['children'] = []
            family['children'].append(line.split()[2].replace('@',''))
    else:
      for j in range(i,len(lines)-1):
        line = lines[j]
        level = line[0]
        if 'FAM' in line.split() and level == '0':
          family['id'] = line.split()[1].replace('@','')
          family['index'] = i
        if 'MARR' in line.split():
          family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
          family['are divorced'] = False
        if 'DIV' in line.split():
          family['are divorced'] = True
          family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'HUSB' in line.split():
          family['Husband ID'] = line.split()[2].replace('@','')
          try:
            family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
          except KeyError:
            family['Husband Name'] = 'nan'
        if 'WIFE' in line.split():
          family['Wife ID'] = line.split()[2].replace('@','')
          try:
            family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
          except KeyError:
            family['Wife Name'] = 'nan'
        if 'CHIL' in line.split():
          if 'children' in family: 
            family['children'].append(line.split()[2].replace('@',''))
          else:
            family['children'] = []
            family['children'].append(line.split()[2].replace('@',''))

    families.append(family)

  f.close()

  return pd.DataFrame(families)

def getIDIndices(filename):
  indices = {}
  f = open(filename, "r")
  lines = f.readlines()
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'INDI' in line.split() and level == '0':
      indices[line.split()[1].replace('@','')] = i
  f.close()
  return indices

def getFamilyIndices(filename):
  indices = {}
  f = open(filename, "r")
  lines = f.readlines()
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'FAM' in line.split() and level == '0':
      indices[line.split()[1].replace('@','')] = i
  f.close()
  return indices

def file_parser(filename):
    (individuals, individuals_id_and_name) = createIndDataframe(filename)
    families = createFamilyDataframe(filename, individuals_id_and_name)
    individuals = pd.DataFrame(individuals)
    families = pd.DataFrame(families)
    return (individuals, families)

def output_data(individuals, families, filename):
    output_excel = filename.strip('.ged') + '.xlsx'
    with pd.ExcelWriter(output_excel) as writer:
        individuals.to_excel(writer, sheet_name="Individuals")
        families.sort_values(by = ['id']).to_excel(writer, sheet_name="Families")