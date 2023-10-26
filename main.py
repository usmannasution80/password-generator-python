import os
import random
import chars
from clear import clear
from between import between
from set_numeric import set_numeric
from set_basic_symbols import set_basic_symbols

def main():

  clear()

  length = None
  password = ''
  set_numeric()
  set_basic_symbols()

  while type(length) is not int:
    try:
      length = int(input('Enter password length : '))
    except:
      print('You entered the wrong value!')

  clear()

  password_length = 0

  while password_length < length:
    index = random.randint(0, len(chars.list) - 1)
    [min_char, max_char] = chars.list[index]
    char = random.randint(min_char, max_char)
    password += chr(char)
    password_length += 1

  file = open('password.txt', 'w')
  file.write(password)
  file.close()

  print('Your password saved in password.txt')



main()

