import sys
from copy import copy
from PasswordScorer import PasswordScorer

def LoadDictionary(inputFile):
  file = open(inputFile, 'r')
  return [x.strip() for x in file.readlines()]

def main(dictionary):
    waitForQuit = False
    scorer = PasswordScorer(dictionary)
    while not waitForQuit:
        password = raw_input('Enter a password here to receive a score. Type "quit" to exit: ').lower().replace("\"", '')
        if password == 'quit':
            waitForQuit = True
        else:
            scorer.DisplayPasswordScoreAndStrength(password)

if __name__ == "__main__":
    dictionary = None
    if len(sys.argv[1:]) > 0:
        dictionary = LoadDictionary(sys.argv[1:][0])
    else:
        dictionary = LoadDictionary('dictionary.txt')

    main(dictionary)