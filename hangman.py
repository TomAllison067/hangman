import random

# Constants defining the file to read and the number of guesses we are allowed
FILE_NAME = "word_list.txt"
GUESSES_ALLOWED = 7


def read_file(file_name):
    """Reads each line from the file into a list of words"""
    list = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            list.append(line.strip("\n"))
    return list


def print_word(letters_to_guess, player_guesses):
    """Prints the word according to how many correct letters have been guessed.
        It checks whether each letter of the word is also in the set player_guesses, and prints the letter or * accordingly."""
    for letter in letters_to_guess:
        if letter in player_guesses:
            print(letter, end="")
        else:
            print("*", end="")
    print()

def check_victory(letters_to_guess, player_guesses):
    """Checks if the player has guessed each letter in the word or not, returning True if so."""
    for letter in letters_to_guess:
        if letter not in player_guesses:
            return False
    return True # If we get here, we have won.

def check_guess(guess, letters_to_guess):
    """Checks whether the player's guess is in the word and returns True if so, or False otherwise."""
    if guess in letters_to_guess:
        return True
    return False

def prompt_for_guess():
    """Prompts the user for input and returns the first letter of their guess."""
    guess = None
    while True:
        guess = input("Please enter your next guess: ")
        if len(guess) > 0: # Stops an error being thrown if the user enters no input
            break
    return guess[0].lower()


def play_game():
    # Read word list into a list of words
    words = read_file(FILE_NAME)

    # Pick a random word from this list
    word_to_guess = random.choice(words)

    # Convert this word to a list of characters
    letters_to_guess = [letter for letter in word_to_guess]

    # Initialise an empty set to store which letters the player has guessed
    player_guesses = set([])

    incorrect_guesses = 0
    victory = False

    while incorrect_guesses < GUESSES_ALLOWED and not victory:
        # Tell the player how many guesses they have left
        guesses_remaining = GUESSES_ALLOWED - incorrect_guesses
        print("You have {} guess(es) left.".format(guesses_remaining))

        # Show the word to the player
        print_word(letters_to_guess, player_guesses)

        # Wait for the player to enter an input. If they enter an empty input, prompt again.
        guess = prompt_for_guess()
        
        # Add guess to the player guess set
        player_guesses.add(guess)

        # Check whether the guess is correct or not, incrementing incorrect_guesses if not
        if not check_guess(guess, letters_to_guess):
            incorrect_guesses += 1

        # Check for victory
        victory = check_victory(letters_to_guess, player_guesses)
        
    if victory:
        print("Congratulations you win")
    else:
        print("The word was {}.".format(word_to_guess))
        print("You lose")


if __name__ == "__main__":
    play_game()
