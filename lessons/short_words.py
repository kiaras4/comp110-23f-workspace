"""Function that creates new list using the words of accepted length."""

__author__ = "730675328"


def short_words(input: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    idx: int = 0
    new_list: list[str] = []
    while idx < len(input):
        if len(input[idx]) < 5:
            new_list.append(input[idx])
            idx += 1
        else:
            print(f"{input[idx]} is too long.")
            idx += 1
    return new_list

my_list: list[str] = ["sun", "cloud", "sky"]
print(short_words(my_list))