from copy import copy

def GetPasswordStrength(password):
    newPassword = ReplaceLongestSubstringWithASingleCharacter(password)
    numberOfCharacterTypes = GetNumberOfCharacterTypes(newPassword)
    return DetermineStrengthOfPasswordBucket(len(newPassword) * numberOfCharacterTypes)

def DetermineStrengthOfPasswordBucket(score):
    if score <= 10:
        return 'Unacceptable'
    elif score > 10 and score < 50:
        return 'Weak'
    else:
        return 'Strong'

def GetLongestSubstring(password):
    counter = 0
    currentStartIndex = 0
    currentEndIndex = 0
    longestSubstringStartIndex = 0
    longestSubstringEndIndex = 0
    while counter < len(password):
        if password[counter].isalpha():
            currentEndIndex = counter
        else:
            if currentEndIndex - currentStartIndex > longestSubstringEndIndex - longestSubstringStartIndex:
                longestSubstringStartIndex = currentStartIndex
                longestSubstringEndIndex = currentEndIndex
            currentStartIndex = counter + 1
            currentEndIndex = counter + 1
        counter += 1
    if currentEndIndex - currentStartIndex > longestSubstringEndIndex - longestSubstringStartIndex:
                longestSubstringStartIndex = currentStartIndex
                longestSubstringEndIndex = currentEndIndex
    return password[longestSubstringStartIndex:longestSubstringEndIndex+1]

def ReplaceLongestSubstringWithASingleCharacter(password):
    longestSubstring = GetLongestSubstring(password)
    passCopy = copy(password)
    passCopy = passCopy.replace(longestSubstring, 'x')
    return passCopy

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
    print 'Strength of Password {0} is {1}'.format(firstTest, GetPasswordStrength(firstTest))
    print 'Strength of Password {0} is {1}'.format(secondTest, GetPasswordStrength(secondTest))
    print 'Strength of Password {0} is {1}'.format(thirdTest, GetPasswordStrength(thirdTest))

RunTests()