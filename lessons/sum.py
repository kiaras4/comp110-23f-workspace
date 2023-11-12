"""Summing the elements of a list using different loops."""

__author__ = "730675328"


def w_sum(wsum: list[float]) -> float:
    """Sum using while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(wsum):
        sum += wsum[idx]
        idx += 1
    return sum


def f_sum(fsum: list[float]) -> float:
    """Sum using for loop."""
    sum2: float = 0.0
    for item in fsum:
        sum2 += item
    return sum2


def f_range_sum(range_sum: list[float]) -> float:
    """Sum using for and range."""
    idx = 0
    sum3: float = 0.0
    for idx in range(0, len(range_sum)):
        sum3 += range_sum[idx]
    return sum3 