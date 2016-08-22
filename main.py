from copy import copy

def GetPasswordStrength(password):
    newPassword = ReplaceWordsWithACharacter(password)
    score = CalculateScore(newPassword)
    return DetermineStrengthOfPasswordBucket(score)

def CalculateScore(password):
    numberOfCharacterTypes = GetNumberOfCharacterTypes(password)
    return len(password) * numberOfCharacterTypes

def DetermineStrengthOfPasswordBucket(score):
    if score <= 10:
        return 'Unacceptable'
    elif score > 10 and score < 50:
        return 'Weak'
    else:
        return 'Strong'

def ReplaceWordsWithACharacter(password):
    counter = 0
    currentStartIndex = 0
    currentEndIndex = 0
    wordsToReplace = []
    while counter < len(password):
        if password[counter].isalpha():
            currentEndIndex = counter
        else:
            if currentEndIndex > currentStartIndex:
                wordsToReplace.insert(0, (currentStartIndex, currentEndIndex))
            currentStartIndex = counter + 1
            currentEndIndex = counter + 1
        counter += 1
    if currentStartIndex != currentEndIndex:
        wordsToReplace.insert(0, (currentStartIndex, currentEndIndex))
    password = ReplaceAllInstancesOfWords(wordsToReplace, password)
    return password

def ReplaceAllInstancesOfWords(wordsToReplaceIndices, password):
    for startIndex, endIndex in wordsToReplaceIndices:
        startIndex = max(0, startIndex)
        endIndex = min(len(password) - 1, endIndex)
        password = password[0:startIndex] + 'x' + password[endIndex + 1:]
    return password


def GetNumberOfCharacterTypes(password):
    types = set()
    for c in password:
        if c.isalpha():
            types.update(['string'])
        elif c.isdigit():
            types.update(['digit'])
        elif c.isspace():
            types.update(['space'])
        else:
            types.update(['other'])
    return len(types)


def RunTests():
    firstTest = 'password1'
    secondTest = 'goat m4n'
    thirdTest = 's0_0per 5n4k3'
    fourthTest = 'abcde fghijk lo1xbz!'

    print 'Strength of Password {0} is {1} and Score is {2}'.format(firstTest, GetPasswordStrength(firstTest),
     CalculateScore(ReplaceWordsWithACharacter(firstTest)))
    print 'Strength of Password {0} is {1} and Score is {2}'.format(secondTest, GetPasswordStrength(secondTest),
     CalculateScore(ReplaceWordsWithACharacter(secondTest)))
    print 'Strength of Password {0} is {1} and Score is {2}'.format(thirdTest, GetPasswordStrength(thirdTest),
     CalculateScore(ReplaceWordsWithACharacter(thirdTest)))
    print 'Strength of Password {0} is {1} and Score is {2}'.format(fourthTest, GetPasswordStrength(fourthTest),
     CalculateScore(ReplaceWordsWithACharacter(fourthTest)))

RunTests()