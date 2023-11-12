"""Test my zip function."""

__author__ = "730675328"

from lessons.zip import zip


def test_empty_list() -> None:
    """Zip([]) should return empty dictionary."""
    assert zip([], []) == {}


def test_one_element_lists() -> None:
    """Use case with one item lists."""
    test_list1: list[str] = ["Happy"]
    test_list2: list[int] = [1]
    assert zip(test_list1, test_list2) == {"Happy": 1}


def test_longer_lists() -> None:
    """Testing with longer lists."""
    test_list1: list[str] = ["Happy", "Tuesday", "Yall"]
    test_list2: list[int] = [1, 2, 3]
    assert zip(test_list1, test_list2) == {"Happy": 1, "Tuesday": 2, "Yall": 3}