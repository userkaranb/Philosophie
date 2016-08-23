from copy import copy
from PasswordScorer import PasswordScorer

def LoadDictionary():
  file = open('dictionary.txt', 'r')
  return [x.strip() for x in file.readlines()]

def RunTests():
    firstTest = 'password1'
    secondTest = 'goat m4n'
    thirdTest = 's0_0per 5n4k3'
    fourthTest = 'abcde fghijk lo1xbz!'
    scorer = PasswordScorer(set(LoadDictionary()))

    scorer.DisplayPasswordScoreAndStrength(firstTest)
    scorer.DisplayPasswordScoreAndStrength(secondTest)
    scorer.DisplayPasswordScoreAndStrength(thirdTest)
    scorer.DisplayPasswordScoreAndStrength(fourthTest)

RunTests()
LoadDictionary()