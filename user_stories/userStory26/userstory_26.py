# User Story 26

def hasCorrespondingEntries(individuals_dataframe, family_dataframe):
  for index, row in individuals_dataframe.iterrows():
    if str(row['child']) != 'nan':
      children = family_dataframe.loc[family_dataframe['id'] == row['child'], 'children'].iloc[0]
      if row['id'] != row['id']:
        print("ERROR: INDIVIDUAL: US26: Input Line # " + str(row['index']) + ": " + row['id'] + " not in Family " +  row['child'] + " as a child.")
      elif row['id'] not in children:
        print("ERROR: INDIVIDUAL: US26: " + str(row['index']) + ": " + row['id'] + " not in Family " +  row['child'] + " as a child.")
    if str(row['spouse']) != 'nan':

      for family_id in row['spouse']:
        husband_id = family_dataframe.loc[family_dataframe['id'] == family_id, 'Husband ID'].iloc[0]
        wife_id = family_dataframe.loc[family_dataframe['id'] == family_id, 'Wife ID'].iloc[0]
        if row['id'] != husband_id and row['id'] != wife_id:
          print("ERROR: INDIVIDUAL: US26: " + str(row['index']) + ": " + row['id'] + " not in Family " +  family_id + " as a spouse.")


  for index, row in family_dataframe.iterrows():
    if row['Husband ID'] == row['Husband ID'] and row['Husband ID'] not in individuals_dataframe['id'].values:
      print("ERROR: FAMILY: US26: Input Line # " + str(row['index']) + " Husband " + row['Husband ID'] + " not in table of individuals")
    if row['Wife ID'] == row['Wife ID'] and row['Wife ID'] not in individuals_dataframe['id'].values:
      print("ERROR: FAMILY: US26: Input Line # " + str(row['index']) + " Wife " + row['Wife ID'] + " not in table of individuals")  
    if str(row['children']) != 'nan':
      for child in row['children']:
        if child not in individuals_dataframe['id'].values:
           print("ERROR: FAMILY: US26: Child " + child + " not in table of individuals")

