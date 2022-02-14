# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/simeo/Documents/MITx CS Class/words.txt"

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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #Checks if set of letters in the secret word is a subset of the set of letters guessed
    return set(list(secretWord)).issubset(set(lettersGuessed))



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ' '.join([secretWord[i] if secretWord[i] in lettersGuessed else '_' for i in range(len(secretWord))])


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join(sorted(set('abcdefghijklmnopqrstuvwxyz') - set(lettersGuessed)))


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
    #Welcome messages
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-----------') #insert line break

    #Saving important information
    s = secretWord
    lettersGuessed = []
    mistakesMade = 8

    #Start the guessing game
    while mistakesMade > 0:
        #Check if the word has been found, finishing the game early
        if isWordGuessed(secretWord, lettersGuessed):
            return print('Congratulations, you won!')

        #Announce how many rounds are left
        print('You have ' + str(mistakesMade) + ' guesses left.')
        #Display possible letters to guess
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        #Collect a guess
        guess = input('Please guess a letter: ')
        #Check if guess is a duplicate, and if so start again
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
            print('-----------') #insert line break
            continue
        lettersGuessed.append(guess)
        #Check whether guess was correct
        if guess in list(secretWord):
            print('Good Guess: ' + str(getGuessedWord(secretWord, lettersGuessed))) #Congratulate and restart the guessing round
            print('-----------') #insert line break
        elif guess not in list(secretWord):
            print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            print('-----------') #insert line break
            mistakesMade += -1                                                      #Increment mistake counter and restart round
    #Check if all attempts have failed, and inform player of loss
    if mistakesMade == 0:
        return print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
