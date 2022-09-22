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
      if (line.split(tag,1)[1])[1:] is not '':
        arguments = (line.split(tag,1)[1])[1:]
      else:
        arguments = '\n'
    valid = 'N'
    if tag in allowed_tags[int(level)]:
      valid = 'Y'
    
    print('--> ' + line)
    print('<-- ' + level + '|' + tag + 
          '|' + valid + '|' + arguments)