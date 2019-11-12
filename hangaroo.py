from function1 import isWordGuessed
from function2 import getGuessedWord
from function3 import getAvailableLetters
secretWord = 0
def Hangaroo(secretWord):
    print("Input secret Word")
    secretWord = input()
    secretWord = secretWord.lower()
    secretWord = list(secretWord)
    print("You have 6 chances to guess the word right")
    mistakesMade = 0
    lettersGuessed = []
    while mistakesMade < 6:
        print("\n Input letter")
        x = list(input())
        lettersGuessed.extend(x)
        print("These are the available letters left")
        getAvailableLetters(lettersGuessed)
        if len(x) > 1:
            print("Only 1 letter is allowed")
            return Hangaroo(secretWord)
        getGuessedWord(secretWord,lettersGuessed)
        if isWordGuessed(secretWord,lettersGuessed) == True:
            print("\n You are correct")
        else:
            mistakesMade = mistakesMade + 1
        if all(el in lettersGuessed  for el in secretWord) == True:
            print("Congratulations you Guessed the word!!!")
            return
    
    if mistakesMade == 6:
        print("\n Sorry you lost, Hangaroo will now be Hanged ")
        print("------\n     i\n     O \n  /  I  \  \n    / \ ")
    
   