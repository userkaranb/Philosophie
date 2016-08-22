
def GetPasswordStrength(password):
    newPassword = ReplaceLongestSubstringWithASingleCharacter(password)
    # Count number of characters in new substring
    # Calculate score
    # Display to user

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
    password.replace(longestSubstring, 'x')
    return password