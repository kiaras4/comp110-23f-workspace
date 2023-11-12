"""Combining two lists into a dictionary.""" 

__author__ = "730675328"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Combining two lists."""
    idx: int = 0
    new_dict: dict[str, int] = {}
    if len(list1) != len(list2) or len(list1) == 0 or len(list2) == 0:
        return new_dict
    while idx < len(list1):
        new_dict[list1[idx]] = list2[idx]
        idx += 1
    
    return new_dict
