# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

secretWord = chooseWord(wordlist).lower()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if(len(secretWord) == 1):
        return secretWord in lettersGuessed
    else:
        inWord = True
        for letter in secretWord:
            if(letter not in lettersGuessed):
                inWord = False
                break
        return inWord



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    newWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            newWord += letter
        else:
            newWord += '_ '
    return newWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_returned = alphabet[:]
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet_returned = alphabet_returned.replace(letter, '')
    return alphabet_returned
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakes = 0
    numberOfGuesses = 8
    lettersGuessed = []
    correct = 0
    availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    ended = False
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %s letters long.' % (len(secretWord)))
    print('------------')
    while not ended:
        availableLetters = getAvailableLetters(lettersGuessed)
        print('You have %s guesses left.' % (numberOfGuesses - mistakes))
        print('Available letters: '+ availableLetters)
        letter = (input('Please guess a letter: ').strip()).lower()
        if letter in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(letter)
            if isWordGuessed(letter, secretWord):
                correct += 1
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            else:
                mistakes += 1
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
        
        print('------------')
        if numberOfGuesses - mistakes == 0:
            print('Sorry, you ran out of guesses. The word was else.')
            ended = True
        elif getGuessedWord(secretWord, lettersGuessed).find('_') == -1:
            print('Congratulations, you won!')
            ended = True
            
print(secretWord)
hangman(secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
