secretWord = "cat"
lettersGuessed = ['t','o','c','d']
def getGuessedWord(secretWord,lettersGuessed):
    x = list(secretWord)
   
    for i in x:               
        if i in lettersGuessed:
            
            print(i, end = '')
        else:
            print('_',end = '')
        
        
