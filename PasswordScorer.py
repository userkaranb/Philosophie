
class PasswordScorer(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def DisplayPasswordScoreAndStrength(self, password):
        score, strength = self.GetPasswordStrength(password)
        print 'Password {0} is {1}. It has a score of {2}'.format(password, strength, score)

    def GetPasswordStrength(self, password):
        newPassword = self.ReplaceWordsWithACharacter(password)
        score = PasswordScorer.CalculateScore(newPassword)
        return score, PasswordScorer.DetermineStrengthOfPasswordBucket(score)

    @staticmethod
    def CalculateScore(password):
        numberOfCharacterTypes = PasswordScorer.GetNumberOfCharacterTypes(password)
        return len(password) * numberOfCharacterTypes

    @staticmethod
    def DetermineStrengthOfPasswordBucket(score):
        if score <= 10:
            return 'Unacceptable'
        elif score > 10 and score < 50:
            return 'Weak'
        else:
            return 'Strong'

    def ReplaceWordsWithACharacter(self, password):
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
        password = self.ReplaceAllInstancesOfWords(wordsToReplace, password)
        return password

    def ReplaceAllInstancesOfWords(self, wordsToReplaceIndices, password):
        for startIndex, endIndex in wordsToReplaceIndices:
            startIndex = max(0, startIndex)
            endIndex = min(len(password) - 1, endIndex)
            if password[startIndex:endIndex + 1].lower() in self.dictionary:
                password = password[0:startIndex] + 'x' + password[endIndex + 1:]
        return password

    @staticmethod
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
