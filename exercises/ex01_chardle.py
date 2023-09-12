"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "73067532"

searched_word = str(input("Enter a 5-character word: "))

if len(searched_word) != 5:
    #warns user that lenth of the word must be 5 characters
    print("Error: Word must contain 5 characters")
    exit()

character = str(input("Enter a single character: "))

if len(character) != 1:
    #warns the user that their input must be 1 character
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + searched_word) 

#initializes the counter
count_char = 0

#searches for character at index 0
if searched_word[0] == character:
    print(character + " found at index " + str(0))
    #counts frequency of character 
    count_char = count_char + 1
#searches for character at index 1
if searched_word[1] == character:
    print(character + " found at index " + str(1))
    count_char = count_char + 1
#searches for character at index 2
if searched_word[2] == character:
    print(character + " found at index " + str(2))
    count_char = count_char + 1
#searches for character at index 3
if searched_word[3] == character:
    print(character + " found at index " + str(3))
    count_char = count_char + 1
#searches for character at index 4
if searched_word[4] == character:
    print(character + " found at index " + str(4))
    count_char = count_char + 1

#tests the frequency of the character
if count_char == 1:
    #uses "instance" for one instance of the character
    print(str(count_char) + " instance of " + character + " found in " + searched_word)
else:
    #uses "instances" for frequencies not equal to one
     print(str(count_char) + " instances of " + character + " found in " + searched_word)