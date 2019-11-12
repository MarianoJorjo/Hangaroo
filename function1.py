secretWord = input()
lettersGuessed = ['c','a','t']
def isWordGuessed(secretWord,lettersGuessed):
    b = list(secretWord)
    for i in b:               
        if i in lettersGuessed:
            resultt = True
        else:
            resultt = False    
        return resultt   
            
    

