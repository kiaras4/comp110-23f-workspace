"""EX04 - Utils."""

__author__ = "730675328"


def all(list1: list[int], num: int) -> bool:
    """Tests if the list is entirely comprised of the given integer."""
    idx = 0
    # loops through all indices
    while idx < len(list1):
        if len(list1) == 0:
            return False
        if num != list1[idx]:
            return False
        elif num == list1[idx] and idx < len(list1) - 1:
            idx += 1
        else:
            return True
        
    return False


def max(input: list[int]) -> int:
    """Determines max of given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    # initiates values
    idx = 1
    max1: int = input[0]
    list1 = input

    # loops through indices
    while idx < len(input):
        if list1[idx] > max1:
            max1 = list1[idx]
            idx += 1
        else:
            idx += 1

    return max1


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if given lists are equal."""
    idx = 0
    if len(list1) == 0 and len(list2) == 0:
        return True
    elif len(list1) == 0 or len(list2) == 0:
        return False
    if len(list1) != len(list2):
        return False
    # loops through indices
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        elif list1[idx] == list2[idx] and idx < len(list1) - 1:
            idx += 1
        else:
            return True
    
    return False