import os
import random
from clear import clear
from between import between
from include_numeric import include_numeric

def main():
  clear()
  length = None
  password = ''
  include = [
    [64, 91],
    [96, 123]
  ]
  include_numeric(include)
  min_char = 48
  max_char = 122
  while type(length) is not int:
    try:
      length = int(input('Enter password length : '))
    except:
      print('You entered the wrong value!')
  clear()
  password_length = 0
  while password_length < length:
    char = random.randint(min_char, max_char)
    while not between(char, include):
      char = random.randint(min_char, max_char)
    password += chr(char)
    password_length += 1
  file = open('password.txt', 'w')
  file.write(password)
  file.close()
  print('Your password saved in password.txt')



main()

