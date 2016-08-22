from copy import copy

def GetPasswordStrength(password):
    newPassword = ReplaceLongestSubstringWithASingleCharacter(password)
    numberOfCharacterTypes = GetNumberOfCharacterTypes(newPassword)
    return len(newPassword) * numberOfCharacterTypes

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
