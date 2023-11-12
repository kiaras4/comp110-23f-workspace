"""Practice quiz question with lists."""

__author__ = "730675328"


def odd_and_even(list1: list[int]) -> list[int]:
    empty_list: list[int] = []
    idx: int = 0
    while idx < len(list1):
        if idx % 2 == 0 and list1[idx] % 2 != 0:
            empty_list.append(list1[idx])
        idx += 1
    
    return empty_list