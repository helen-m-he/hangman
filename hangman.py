
# -----------------------------------
# Helper code -- from MITx: 6.00.1x

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

# Load the list of words into the variable wordlist so that it can be accessed from anywhere in the program
wordlist = loadWords()

# Returns T if the user has correctly guessed the ENTIRE word, F if not
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        # if there is even 1 character in the secret word that hasn't been guessed, return False
        if char not in lettersGuessed:
            return False
    # Otherwise, return True
    return True

# Returns secretWord w the guessed letters appearing + the remaining as blanks
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    # Initialize ans as empty string
    ans = ''

    # For  each letter in secretWord, check to see if it has been guessed. If yes, add that letter to ans. If no, add a blank + space
    for i in range(len(secretWord)): # iterate thru each character in secretWord
        # if that character in secretWord HAS been guessed, add that letter to ans
        if secretWord[i] in lettersGuessed:
            ans += secretWord[i]
        # if not, just add a blank
        else:
            ans += '_ '
        ###print(ans)

    return ans #ans is a string


#Returns the letters the users hasn't guessed yet
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    # Shortcut to get a string of all the lowercase letters
    import string
    alphabet = string.ascii_lowercase #'abcdefghijklmnopqrstuvwxyz'

    # Initialize available as empty string
    available = ''

    # Iterate through all letters in the ALPHABET
    for letter in alphabet:
        # if that letter in the alphabet has NOT been guessed, then it's still available
        if letter not in lettersGuessed:
            available += letter

    return available


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
    # Start the game
    print("Welcome to the game, Hangman!")

    # Tell user how many letters are in the secret word
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

    # Initialize necessary stuff
    lettersGuessed = []
    guessesLeft = 8


    # GO THROUGH THE ROUNDS:

    # Keep going till user runs out of guesses OR guesses correctly
    while guessesLeft > 0:
        print("-------------")

        # Tell user how many guesses they have left
        print("You have " + str(guessesLeft) + " guesses left.")

        # Tell user which letters they haven't guessed yet
        print("Available letters: " + getAvailableLetters(lettersGuessed))

        # Ask user to guess
        guess = input("Please guess a letter: ").lower() # !!! use .lower() to convert user input to lowercase
            # (assume user obeys + only submits 1 character (A-Z) per round, so don't need to code any error msgs)

        # CHECK THIS GUESS:
        # If user guesses a letter they already guessed
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        # Else if user guesses correctly
        elif guess in secretWord:
            lettersGuessed.append(guess) # Add this guess to list of lettersGuessed (MUST DO THIS BEFORE THE BELOW LINE, so "getGuessedWord" returns most updated version)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        # If user guesses INcorrectly
        else:
            lettersGuessed.append(guess)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1 # !! they only lose a guess if they guess INcorrectly

        # End the game if they guess the word right
        right = isWordGuessed(secretWord, lettersGuessed)
        if right:
            break

    # If, by the time the game ends (aka the "while" loop is over)...
    if right: #... if they got the word right
        print("-------------")
        print("Congratulations, you won!")
    else:       #... if they still haven't gotten the word right
        print("-------------")
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
