import random
import string

def loadwords():
    file = open('/Users/abhismacbook/Documents/python/projects/hangman/words.txt','r')
    line = file.read()
    wordlist = line.split()
    return wordlist

def iswordGuessed(secretword,lettersguessed):
    for i in secretword:
        if i not in lettersguessed:
            return False
    return True

def availableLetters(secretword,lettersguessed):
    alphabets = list(string.ascii_lowercase)
    for i in lettersguessed:
        if i in secretword:
            alphabets.remove(i)
    return ''.join(alphabets)

def chooseword(wordlist):
    secretword = random.choice(wordlist)
    return secretword

def getGuessedWord(secretword,lettersguessed):
    ans = ''
    s=[]
    for i in lettersguessed:
        if i in secretword:
            s.append(i)
    for i in secretword:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans
    

def hangman(secretword):    
    global lettersguessed
    lettersguessed = []
    mistakeMade = 0

    print("welcome to hangman")
    print("-----------")
    
    while 8-mistakeMade > 0:
        print(f'You have {8-mistakeMade} guesses left')
        print(f'available letters are: \n',availableLetters(secretword,lettersguessed))
        print(f'word so far: ',getGuessedWord(secretword,lettersguessed))
        guess = str(input("Guess the letter: ")).lower()
        if guess in secretword and guess not in lettersguessed:
            lettersguessed.append(guess)
            print('you guessed the right letter!')
        elif guess in lettersguessed:
            print('you have already guessed this letter')
        else:
            lettersguessed.append(guess)
            mistakeMade += 1
        if 8-mistakeMade == 0:
            print('Out of guesses, the secret word was: ', secretword)
            break
        if iswordGuessed(secretword,lettersguessed):
            print("You won. The secret words is: ",secretword)
            break

wordlist = loadwords()
secretword = chooseword(wordlist)
hangman(secretword)