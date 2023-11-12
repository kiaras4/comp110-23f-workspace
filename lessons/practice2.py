
def mimic_letter(my_words: str, letter_idx: int) -> str:
    """outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return ("Index too high")
    # If we made it here, that means the letter_idx is valid
    return my_words[letter_idx]

my_words: str = "hello"
letter_idx: int = 1

print(mimic_letter(my_words, letter_idx))