"""EX01 - One Shot Wordle."""

__author__ = "730675328"

# Initializes the string used in the testing 
secret_word: str = "python"

# Initializes the user inputted guess
guess = str(input(f"What is your {len(secret_word)}-letter guess? "))

# Establishes the boxes used
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Initializes the main index
letter_idx: int = 0

# Initializes the string for the colored boxes
boxes = ""

# Testing if the guessed word is the correct length
while len(guess) != len(secret_word):
    guess = str(input(f"That was not {len(secret_word)} letters! Try again: "))

# Loops through each index
while letter_idx < len(secret_word):
    # Tests if the letter is correct and in the correct location
    if str(secret_word[letter_idx]) == str(guess[letter_idx]):
        boxes += str(GREEN_BOX)         
    else:
        # Initializes the index used for testing matching letters without changing main index
        separate_idx: int = 0
        """ Loops through the letters, testing if the letter 
        appears in the secret word and assigns appropriate box """
        while separate_idx < len(secret_word):
            if str(guess[letter_idx]) == str(secret_word[separate_idx]):
                separate_idx = len(secret_word)
                boxes += str(YELLOW_BOX)
            elif separate_idx == (len(secret_word) - 1):
                boxes += str(WHITE_BOX)
                # Advances the loop until exit condition is met
                separate_idx += 1
            else:
                separate_idx += 1
    # Approaches exit condition
    letter_idx += 1

print(boxes)

# Tests if the correct word is guessed or not
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!") 