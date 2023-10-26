import re
import chars

def set_basic_symbols():
  is_include = None
  while is_include is None:
    is_include = input('Include basic symbols? ')
    if not re.search('(y|n|yes|no)', is_include):
      print('You entered the wrong option!')
      is_include = None
  if re.search('(y|yes)', is_include):
    chars.list.append([32, 48])
    chars.list.append([57, 65])
    chars.list.append([90, 97])
    chars.max = 97