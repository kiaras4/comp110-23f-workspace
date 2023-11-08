"""EX06 - Dictionary."""

__author__ = "730675328"


def invert(invert_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the given dictionary."""
    new_dict: dict[str, str] = {}
    for item in invert_dict:
        if invert_dict[item] not in new_dict:
            new_dict[invert_dict[item]] = item
        else:
            raise KeyError("No duplicates in inverted dictionary.")
    return new_dict


def favorite_color(fav_dict: dict[str, str]) -> str:
    """Determines the color that appears the most."""
    empty_dict: dict[str, int] = {}
    for key in fav_dict:
        if fav_dict[key] in empty_dict:
            empty_dict[fav_dict[key]] += 1
        else:
            empty_dict[fav_dict[key]] = 1
    fav_color: str = ""
    count: int = 0
    for key in empty_dict:
        if empty_dict[key] > count:
            fav_color = key
            count = empty_dict[key]
    return fav_color


def count(count_list: list[str]) -> dict[str, int]:
    """Counts number of times item appears in list."""
    empty_dict: dict[str, int] = {}
    for item in count_list:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1
    return empty_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Creates new dictionary organizing based on first letter."""
    for item in words:
        item.lower()
    letter_dict: dict[str, list[str]] = {}
    for item in words:
        letter = item.lower()[0]
        if letter not in letter_dict and item.lower()[0] == letter:
            letter_dict[letter] = []
            letter_dict[letter].append(item)
        else:
            letter_dict[letter].append(item)
    return letter_dict


def update_attendance(attendance_log: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]:
    """Updating attendance log."""
    if day in attendance_log:
        if name not in attendance_log[day]:
            attendance_log[day].append(name)
    else:
        attendance_log[day] = []
        attendance_log[day].append(name)
    return attendance_log


test_alphabetizer: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
print(alphabetizer(test_alphabetizer))