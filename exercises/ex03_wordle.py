"""EX03 - Wordle."""

__author__ = "730675328"


def contains_char(secret: str, char1: str) -> bool:
    """Tests if the letter(char1) is anywhere in the secret word."""
    assert len(char1) == 1
    # initiates index variable
    idx: int = 0

    # loops through each index of secret, testing for the char1 letter
    while idx < len(secret):
        if secret[idx] == char1:
            return True
        elif secret[idx] != char1 and idx < len(secret) - 1:
            idx += 1
        else:
            return False
    # For when char1 is not found
    return False


def emojified(guess: str, secret: str) -> str:
    """Concatenates the green, yellow, and white boxes according to the letter."""
    assert len(guess) == len(secret)

    # Establishes the boxes used
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # Initializes the index
    idx: int = 0

    # Initializes the string for the colored boxes
    boxes = ""
    # Loops through each index
    while idx < len(secret):
        char1: str = str(guess[idx])

        # Tests if the letter is correct and in the correct location
        if str(secret[idx]) == str(guess[idx]):
            boxes += str(GREEN_BOX)         
        elif contains_char(secret, char1):
            boxes += str(YELLOW_BOX)
        else:
            boxes += str(WHITE_BOX)
        # Approaches exit condition
        idx += 1

    return boxes


def input_guess(length: int) -> str:
    """Allows player to input a guess and ensures it is the correct length."""
    guess: str = input(f"Enter a {length} character word: ")

    # loops until player inputs a guess of the correct length
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
        
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Initiates the variables, print statement, and the player's guess
    secret: str = "taylor"
    guess_count: int = 1
    length: int = len(secret)
    print(f"=== Turn {guess_count}/6 ===")
    guess: str = input_guess(length)

    # loops through the allowed turns while the guess is wrong
    while guess_count < 6 and secret != guess:
        print(emojified(guess, secret))
        guess_count += 1
        print(f"=== Turn {guess_count}/6 ===")
        guess = input_guess(length)

    # tests if all allowed guesses are wrong
    if guess_count >= length and secret != guess:
        print("X/6 - Sorry, try again tomorrow!")
    # this point = a correct guess within the allowed turns
    else:
        print(emojified(guess, secret))
        print(f"You won in {guess_count}/6 turns!")


if __name__ == "__main__":
    main()