'''
before enter game loop:
1 choose a word for the answer
2 guess counter to 6
3 make empty list for guesses

game loop:
1 get user input for guess and
2 add to list and
3 subtract from guesses
4 test guess against word
5 print guesses

stop when guess == word or guesses == 0
'''
import random
from colorama import Fore, Back, Style


def loadDiction():
    return open("words.txt").readlines()


def get_word(words, length):
    # select matches algorithm
    matches = []
    for i in range(len(words)):
        words[i] = words[i].rstrip()
        if len(words[i]) == length:
            matches += [words[i]]

    return random.choice(matches)


def checkAnswer(guess, word):
    #build colorful str
    global result
    result = ""
    for i in range(len(guess)):
        #green
        if guess[i] == word[i]:
            result += Back.GREEN + Fore.BLACK + guess[i] + Style.RESET_ALL
        #yellow
        elif guess[i] in word:
            result += Back.YELLOW + Fore.BLACK + guess[i] + Style.RESET_ALL
        #gray
        else:
            result += Back.WHITE + Fore.BLACK + guess[i] + Style.RESET_ALL\


def displayGuessed(guessed):
    for i in range(len(guessed)):
        print(guessed[i])


def wordle():
    words = loadDiction()
    word = get_word(words, 5)
    #print(word)
    guesses = 6
    guessed = []

    #fencepost
    guess = input("Enter 5 letter word: ").upper()
    while len(guess) != 5:
        guess = input("Enter 5 letter word: ").upper()

    checkAnswer(guess, word)
    guessed.append(result)
    guesses -= 1

    while guesses > 0 and guess != word:
        # print all guesses
        displayGuessed(guessed)

        guess = input("Enter 5 letter word: ").upper()
        while len(guess) != 5:
            guess = input("Enter 5 letter word: ").upper()
        checkAnswer(guess, word)
        guessed.append(result)
        guesses -= 1

    #you have won or you have died
    displayGuessed(guessed)

    if guess == word:
        print("You won!")
    else:
        print("You lost, the word was: " + word)


wordle()
