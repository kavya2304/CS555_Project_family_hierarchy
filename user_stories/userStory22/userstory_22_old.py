from collections import Counter
from datetime import date
from dateutil.relativedelta import relativedelta
import os
import pandas as pd

individuals = []
individuals_id_and_name = []
families = []

allowed_tags = {
    0 : ['INDI','FAM','HEAD','TRLR','NOTE'],
    1 : ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV'],
    2 : ['DATE']
}

def save_ind_data(filename):
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
        person = {}
        if indices.index(i) != len(indices)-1:
            for j in range(i,indices[indices.index(i)+1]):
                line = lines[j]
                level = line[0]
                if 'INDI' in line.split() and level == '0':
                    person['id'] = line.split()[1].replace('@','')
                if 'NAME' in line.split():
                    person['name'] = line.split('NAME')[1].replace('\n','')
                    individuals_id_and_name[person['id']] = person['name']
                if 'SEX' in line.split() and level == '1':
                    person['gender'] = line.split()[2]
                if 'BIRT' in line.split():
                    person['birthday'] =  lines[j+1].split('DATE')[1].replace('\n','')
                if 'DEAT' in line.split():
                    is_dead = True
                    person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'FAMC' in line.split():
                    person['child'] = line.split()[2].replace('@','')
                if 'FAMS' in line.split():
                    person['spouse'] = line.split()[2].replace('@','')
        else:
            for j in range(i,len(lines)-1):
                line = lines[j]
                level = line[0]
                if 'INDI' in line.split() and level == '0':
                    person['id'] = line.split()[1].replace('@','')
                if 'NAME' in line.split():
                    person['name'] = line.split('NAME')[1].replace('\n','')
                    individuals_id_and_name[person['id']] = person['name']
                if 'SEX' in line.split() and level == '1':
                    person['gender'] = line.split()[2]
                if 'BIRT' in line.split():
                    person['birthday'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'DEAT' in line.split():
                    is_dead = True
                    person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'FAMC' in line.split():
                    person['child'] = line.split()[2].replace('@','')
                if 'FAMS' in line.split():
                    person['spouse'] = line.split()[2].replace('@','')

        if is_dead:
            person['age'] = relativedelta(pd.to_datetime(person['death'],infer_datetime_format=True), pd.to_datetime(person['birthday'],infer_datetime_format=True)).years
        else:
            today = date.today()
            person['age'] = relativedelta(today, pd.to_datetime(person['birthday'],infer_datetime_format=True)).years

        individuals.append(person)
    
    f.close()

    return (individuals,individuals_id_and_name)

def save_family_data(filename, individuals_id_and_name):
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
        family = {}
        if indices.index(i) != len(indices)-1:
            for j in range(i,indices[indices.index(i)+1]):
                line = lines[j]
                level = line[0]
                if 'FAM' in line.split() and level == '0':
                    family['id'] = line.split()[1].replace('@','')
                if 'MARR' in line.split():
                    family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'DIV' in line.split():
                    family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'HUSB' in line.split():
                    family['Husband ID'] = line.split()[2].replace('@','')
                    family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
                if 'WIFE' in line.split():
                    family['Wife ID'] = line.split()[2].replace('@','')
                    family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
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
                if 'MARR' in line.split():
                    family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'DIV' in line.split():
                    family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'HUSB' in line.split():
                    family['Husband ID'] = line.split()[2].replace('@','')
                    family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
                if 'WIFE' in line.split():
                    family['Wife ID'] = line.split()[2].replace('@','')
                    family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
                if 'CHIL' in line.split():
                    if 'children' in family: 
                        family['children'].append(line.split()[2].replace('@',''))
                    else:
                        family['children'] = []
                        family['children'].append(line.split()[2].replace('@',''))

        families.append(family)

    f.close()

    return families


def file_parser(ged_filename):
    (individuals, individuals_id_and_name) = save_ind_data(ged_filename)
    families = save_family_data(ged_filename, individuals_id_and_name)
    individuals = pd.DataFrame(individuals)
    families = pd.DataFrame(families)
    return (individuals, families)

def output_data(individuals, families, ged_filename):
    output_excel = ged_filename.strip('.ged') + '.xlsx'
    with pd.ExcelWriter(output_excel) as writer:
        individuals.to_excel(writer, sheet_name="Individuals")
        families.sort_values(by = ['id']).to_excel(writer, sheet_name="Families")
    return output_excel



# Sort the list of IDs and check for duplicates
def check_id(id_list):
    c1 = Counter(id_list)
    c2 = Counter(set(id_list))
    diff = c1-c2
    diff_list = sorted(set(diff.elements()))
    
    return_string = ""
    for x in diff_list:
        return_string += ("ID " + x + " is not a unique ID.\n")
    if return_string != "":
        print(return_string[:-1])

    return len(diff_list) == 0

def unique_ids(ged_filename):
    #(individuals,individuals_id_and_name) = createIndDataframe(filename)
    #families = createFamilyDataframe(filename, individuals_id_and_name)
    individuals, families = file_parser(ged_filename)
    xls_filename = output_data(individuals, families, ged_filename)

    individuals = pd.read_excel(io=xls_filename, sheet_name='Individuals')
    individual_id_list = sorted(list(individuals['id']))
    families = pd.read_excel(io=xls_filename, sheet_name='Families')
    family_id_list = sorted(list(families['id']))

    has_unique_individuals = check_id(individual_id_list)
    has_unique_families = check_id(family_id_list)
    all_unique = has_unique_individuals and has_unique_families

    if all_unique:
        print("File has all unique IDs.")
    
    return all_unique

#filename = os.path.abspath(os.path.dirname(__file__)) + '/../test_data.xlsx'
#filename = os.path.abspath(os.path.dirname(__file__)) + '/../testcases/userstory_7/uniqueIDsTestData1.xlsx'
#unique_ids(filename)