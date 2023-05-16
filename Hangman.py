import random

def readFile(fileName):
    words = list()
    with open(fileName) as f:
        for line in f:
            line = line.strip("\n")
            words.append(line)
    return words

def pickRandomWord(words):
    r = random.randint(0, len(words))
    return words[r]

def drawHangman(strikes):
    if (strikes == 0):
        print("____________")
        print("   |/      ")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("  _|___")
    
    elif (strikes == 1):
        print("____________")
        print("   |/      |")
        print("   |      (_)")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("  _|___")      
    
    elif (strikes == 2):
        print("____________")
        print("   |/      |")
        print("   |      (_)")
        print("   |       |")
        print("   |       |")
        print("   |")
        print("   |")
        print("   |")
        print("  _|___")    
    
    elif (strikes == 3):
        print("____________")
        print("   |/      |")
        print("   |      (_)")
        print("   |      \\|")
        print("   |       |")
        print("   |")
        print("   |")
        print("   |")
        print("  _|___")     
    
    elif (strikes == 4):
        print("____________")
        print("   |/      |")
        print("   |      (_)")
        print("   |      \\|/")
        print("   |       |")
        print("   |")
        print("   |")
        print("   |")
        print("  _|___")      
    
    elif (strikes == 5):
        print("____________")
        print("   |/      |")
        print("   |      (_)")
        print("   |      \\|/")
        print("   |       |")
        print("   |      /")
        print("   |")
        print("   |")
        print("  _|___");     
    
    elif (strikes == 6):
        print("____________")
        print("   |/      |")
        print("   |      (_)")
        print("   |      \\|/")
        print("   |       |")
        print("   |      / \\")
        print("   |")
        print("   |")
        print("  _|___")      
    
def checkWin(word, numCorrect):
    return len(word) == numCorrect


def getLength(word):
    return len(word)

def checkLetter(word, letter):
    n=0
    for i in range(0, len(word)):
        if word[i] == letter:
            n+=1
    return n

def displayChar(lettersLeft, alphabet):
    for i in range(len(alphabet)):
        if alphabet[i] in lettersLeft:
            print(alphabet[i], end=" ")
        else:
            print("_", end=" ")
    print("")
    return 0

def letterPicked(character, lettersLeft):
    return character in lettersLeft

def displayWord(word, lettersGuessed):
    n=0
    print(word)
    for letter in word:
        if letter in lettersGuessed:
            n+=1
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    return n

def main():
    words = readFile("usa.txt")
    word = pickRandomWord(words)
    lettersGuessed = list()
    lettersLeft = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                   "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                   "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numCorrect = 0
    strike = 0
    drawHangman(0)
    print("")
    print("")
    numCorrect = displayWord(word, lettersGuessed)   

    while not (checkWin(word, numCorrect)):

        char = input("Enter a letter: ")

        while len(char) != 1:
            print("Incorrect length")
            char = input("Enter a letter: ")
            while letterPicked(char, lettersGuessed):
                print("Letter already guessed")
                char = input("Enter a letter: ")

        while letterPicked(char, lettersGuessed):
            print("Letter already guessed")
            char = input("Enter a letter: ")
            while len(char) != 1:
                print("Incorrect length")
                char = input("Enter a letter: ")
        lettersGuessed.append(char)
        lettersLeft.remove(char)
        if not char in word:
            strike+=1
        if strike ==6:
            drawHangman(strike)
            print("You lose! The word was", word)
            return 0
        else:
            drawHangman(strike)
            print("")
            print("")
            numCorrect = displayWord(word, lettersGuessed)
            displayChar(lettersLeft, alphabet)
    print("You win!")
main()