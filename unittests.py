from PasswordScorer import PasswordScorer
import inspect

def PrintFunctionHeader(functionName):
    print '\n---TEST: {0}---'.format(functionName)

def RunTests():
    VerifyBasicScores()
    VerifyEmptyStringExample()
    VerifyComplexExample()
    VerifyReplaceWordsWithACharacter()
    VerifyReplaceAllInstancesOfWords()
    VerifyCharacterTypeCount()
    VerifyDetermineStrengthOfPasswordBucket()

def VerifyBasicScores():
    PrintFunctionHeader(inspect.stack()[0][3])
    firstTest = 'password1'
    secondTest = 'goat m4n'
    thirdTest = 's0_0per 5n4k3'
    fourthTest = 'abcde fghijk lo1xbz!'
    scorer = PasswordScorer(set(['password', 'goat', 'per', 'abcde', 'fghijk', 'lo', 'xbz']))

    score1, _ = scorer.GetPasswordStrength(firstTest)
    AssertEqualScores(firstTest, 4, score1)

    score2, _ = scorer.GetPasswordStrength(secondTest)
    AssertEqualScores(secondTest, 15, score2)

    score3, _ = scorer.GetPasswordStrength(thirdTest)
    AssertEqualScores(thirdTest, 44, score3)

    score4, _ = scorer.GetPasswordStrength(fourthTest)
    AssertEqualScores(fourthTest, 32, score4)

def VerifyEmptyStringExample():
    PrintFunctionHeader(inspect.stack()[0][3])
    password = ''
    scorer = PasswordScorer(set(['password', 'goat', 'per', 'abcde', 'fghijk', 'lo', 'xbz']))
    score, _ = scorer.GetPasswordStrength(password)
    AssertEqualScores(password, 0, score)

def VerifyComplexExample():
    PrintFunctionHeader(inspect.stack()[0][3])
    password = 'ThisIs A Longer! More, complex Password'
    scorer = PasswordScorer(set(['this', 'a', 'longer', 'more', 'complex', 'password', 'somethingelse']))
    score, _ = scorer.GetPasswordStrength(password)
    AssertEqualScores(password, 54, score)

def VerifyReplaceWordsWithACharacter():
    PrintFunctionHeader(inspect.stack()[0][3])
    password = 'ThisIs A Longer! More, complex Password'
    scorer = PasswordScorer(set(['this', 'a', 'ax', 'longer', 'more', 'complex', 'password', 'somethingelse']))
    newPassword = scorer.ReplaceWordsWithACharacter(password)
    AssertEqualScores(password, 'ThisIs A x! x, x x', newPassword)

    password = '12password34'
    newPassword = scorer.ReplaceWordsWithACharacter(password)
    AssertEqualScores(password, '12x34', newPassword)

    password = 'A!Password'
    newPassword = scorer.ReplaceWordsWithACharacter(password)
    AssertEqualScores(password, 'A!x', newPassword)

    password = 'Ax!Password'
    newPassword = scorer.ReplaceWordsWithACharacter(password)
    AssertEqualScores(password, 'x!x', newPassword)

def VerifyReplaceAllInstancesOfWords():
    PrintFunctionHeader(inspect.stack()[0][3])
    password = 'A!Password!With!Characters!To!Replace!'
    scorer = PasswordScorer(set(['a', 'password', 'with', 'characters', 'to', 'replace']))
    indicesToReplace = [(30,36), (27, 28), (16, 25), (11,14), (2,9)]
    newPassword = scorer.ReplaceAllInstancesOfWords(indicesToReplace, password)
    AssertEqualScores(password, 'A!x!x!x!x!x!', newPassword)

def VerifyCharacterTypeCount():
    PrintFunctionHeader(inspect.stack()[0][3])
    password = 'x!x!x! x1234'
    characterTypes = PasswordScorer.GetNumberOfCharacterTypes(password)
    AssertEqualScores(password, 4, characterTypes)

    password = '1'
    characterTypes = PasswordScorer.GetNumberOfCharacterTypes(password)
    AssertEqualScores(password, 1, characterTypes)

    password = 'abc def x'
    characterTypes = PasswordScorer.GetNumberOfCharacterTypes(password)
    AssertEqualScores(password, 2, characterTypes)

    password = '??@?@#?@#?@#$?@$%?@$'
    characterTypes = PasswordScorer.GetNumberOfCharacterTypes(password)
    AssertEqualScores(password, 1, characterTypes)

def VerifyDetermineStrengthOfPasswordBucket():
    PrintFunctionHeader(inspect.stack()[0][3])
    score = 10
    bucket = PasswordScorer.DetermineStrengthOfPasswordBucket(score)
    AssertEqualScores(score, 'Unacceptable', bucket)
    score = 11
    bucket = PasswordScorer.DetermineStrengthOfPasswordBucket(score)
    AssertEqualScores(score, 'Weak', bucket)
    score = 115
    bucket = PasswordScorer.DetermineStrengthOfPasswordBucket(score)
    AssertEqualScores(score, 'Strong', bucket)

def AssertEqualScores(password, expectedResult, actualResult):
    if expectedResult == actualResult:
        print 'Success for {0}. Both Values equal {1}'.format(password, expectedResult)
    else:
        print 'Password {0} had varying results. Expected: {1}. Actual {2}'.format(password,
         expectedResult, actualResult)

RunTests()