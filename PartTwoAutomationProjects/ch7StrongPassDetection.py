import re

def strongPassDetect(password):
  passStrong = True

  #password is at least 8 char long
  if len(password) < 8:
    passStrong = False

  #password contains at least 1 digit
  passRegex = re.compile(r'\d')
  if passRegex.search(password) == None:
    passStrong = False
  
  #password contains at least 1 uppercase
  passRegex = re.compile(r'[A-Z]')
  if passRegex.search(password) == None:
    passStrong = False

  #password contains at least 1 lowercase
  passRegex = re.compile(r'[a-z]')
  if passRegex.search(password) == None:
    passStrong = False
  
  return passStrong

strongPassDetect('B4B4GANOOSHv')