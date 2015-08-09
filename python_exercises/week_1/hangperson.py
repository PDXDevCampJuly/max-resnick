#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import choice

words = ["test"]
numWrong = 0
listedWord = [None]
guesses = []


# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
    global listedWord
    global numWrong

    # Greet the user
    print("Let's play a game of hangperson!")

    # Randomly select a word from the list of words
    listedWord = list(choice(words))
    # Make the randomly selected word into a list object
    # Make another list the same length as the word, but with
    # '_' instead of letters. This will track the user's progress.
    # Use the variable name currentState
    currentState = []
    currentState.extend("_" * len(listedWord))

    # Print the initial state of the game
    printHangperson(currentState)

    # Start the game! Loop until the user either wins or loses
    while currentState != listedWord and numWrong < 6:
        currentState = updateState(userGuess(), currentState)
        printHangperson(currentState)

    # Determine if the user won or lost, and then tell them accordingly
    if currentState == listedWord and numWrong < 6:
        print("Congrags you managed to not be hung.")

    elif currentState != listedWord or numWrong >= 6:
        print("Oh noooooos you've been hung.")


# This helpful function prompts the user for a guess,
# accepting only single letters.
# DO NOT CHANGE
#
# returns a letter
def userGuess():
    global guesses
    guess = ""
    while not guess:
        guess = input("Guess a letter in the word! (Say 'exit'" +
                      "to stop playing) >>")
        if guess == 'exit':
            print("Too hard for ye eh?")
            exit()
        elif guess in guesses:
            print("\n\033[91m",
                  "Error: You've already guessed \
                  the letter {} try again.".format(str(guess).upper),
                  "\033[0m")
        elif guess not in guesses:
            guesses.append(guess)
        else:
            print("An unknown error hase occured.")
    return guess


# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
    global numWrong
    global guesses
    # First, determine if the letter guessed is in the word.
    # If it isn't, tell the user and update the numWrong var
    # If it is, congratulate them and update the state of the game.
    #     To update the state, make sure to replace ALL the '_' with
    #     the guessed letter.
    if guess in guesses:
        return ValueError
    elif (guess in listedWord) and (guess not in guesses):
        guesses.append(guess)
        for i, char in enumerate(listedWord):
            if char == guess:
                currentState[i] = guess
    else:
        numWrong += 1
    return currentState


# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
    person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
    print()

    if numWrong > 0:
        print(person[0])

    if numWrong > 1:
        print(person[numWrong-1])

    print("\n\n")

    for i in state:
        print(i, end=" ")

    print("\n")

# This line runs the program on import of the module
hangperson()
