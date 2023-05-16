
"""
def readFile(fileName):
    words = list()
    with open(fileName) as f:
        for line in f:
            line = line.strip("\n")
            words.append(line)
    return words #list
def removeWrongWords(word, wordsList):
    #word format will be a list like so [a,_,_,c,...]
    #got through words list remove inelifgble words 
    #for each word - check length, then look for matching letters
    length = len(word) 
    for element in wordsList:
        if length != len(element):
            wordsList.remove(element)
        
        else:
            for i in range(length):
                if word[i] != "_":
                    if word[i] != element[i]:
                        wordsList.remove[element]
                        break
    return wordsList

def lettersLeft(letter, lettersLeft):
    lettersLeft.remove(letter)
    return lettersLeft

def bestGuess(lettersLeft, wordsLeft): #do we count 2 or more occurances of letter
    letter_dict = {letter: 0 for letter in lettersLeft}
    for word in wordsLeft:
        for letter in word:
            if letter in lettersLeft:
                letter_dict[letter] = int(letter_dict[letter])+1
    bestGuess = max(letter_dict, key=letter_dict.get)
    print(bestGuess)
    return bestGuess

def main():
    wordList = readFile("usa.txt")
    again = "yes"
    lettersLeft = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                   "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while again != "no":
        word = list(input("enter the word. If letter is unknown replace with _: ")) #in the form abcd... _for unknown letter
        wordList = removeWrongWords(word, wordList)
        letter = bestGuess(lettersLeft, wordList)
        lettersLeft = lettersLeft(letter, lettersLeft)
        print("the best guess is", letter)
        again = input("do you want to guess another letter?")

main()

"""
def readFile(fileName):
    words = list()
    with open(fileName) as f:
        for line in f:
            line = line.strip("\n")
            words.append(line)
    return words #list

def removeWrongWords(word, wordsList):
    length = len(word) 
    newWordsList = []
    for element in wordsList:
        if length == len(element):
            valid = True
            for i in range(length):
                if word[i] != "_" and word[i] != element[i]:
                    valid = False
                    break
            if valid:
                newWordsList.append(element)
    return newWordsList

def lettersLeft(letter, lettersLeft):
    lettersLeft.remove(letter)

def bestGuess(lettersLeft, wordsLeft):
    letter_dict = {letter: 0 for letter in lettersLeft}
    for word in wordsLeft:
        for letter in word:
            if letter in lettersLeft:
                letter_dict[letter] += 1
    bestGuess = max(letter_dict, key=letter_dict.get)
    print(bestGuess)
    return bestGuess

def main():
    wordList = readFile("usa.txt")
    again = "yes"
    lettersLeft = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                   "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while again != "no":
        word = list(input("enter the word. If letter is unknown replace with _: ")) #in the form abcd... _for unknown letter
        wordList = removeWrongWords(word, wordList)
        letter = bestGuess(lettersLeft, wordList)
        lettersLeft.remove(letter)
        print("the best guess is", letter)
        again = input("do you want to guess another letter?")

main()
