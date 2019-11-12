secretWord = "cat"
lettersGuessed = ['B','t','o','C','d']
def getAvailableLetters(lettersGuessed):
    zz = [x.lower() for x in lettersGuessed]
    yy = "abcdefghijklmnopqrstuvwxyz"
    d = list(yy)
    h = set(d)
    p = set(zz)
    g = h - p
    f = list(g)
    b = sorted(f)
    print(b)
    