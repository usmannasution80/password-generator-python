import re

def include_numeric(include):
  is_include = None
  while is_include is None:
    is_include = input('Include numeric? ')
    if not re.search('(y|n|yes|no)', is_include):
      print('You entered the wrong option!')
      is_include = None
  if re.search('(y|yes)', is_include):
    include.append([47, 58])