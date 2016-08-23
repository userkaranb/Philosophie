from copy import copy
from PasswordScorer import PasswordScorer

def LoadDictionary():
  file = open('dictionary.txt', 'r')
  return [x.strip() for x in file.readlines()]


LoadDictionary()