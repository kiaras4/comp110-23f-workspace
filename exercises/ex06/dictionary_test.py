"""Dictionary tests."""

__author__ = "730675328"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count
from dictionary import alphabetizer
from dictionary import update_attendance


def test_invert_empty() -> None:
    """Tests if no dictionary is inputted."""
    test_invert: dict[str, str] = {}
    assert invert(test_invert) == {}


def test_invert_one_elem() -> None:
    """Tests functionality with one element."""
    test_invert: dict[str, str] = {"a": "z"}
    assert invert(test_invert) == {"z": "a"}


def test_invert_multiple_elem() -> None:
    """Test functionality with multiple elements."""
    test_invert: dict[str, str] = {"a": "z", "b": "y", "c": "d"}
    assert invert(test_invert) == {"z": "a", "y": "b", "d": "c"}


def test_favorite_color_empty() -> None:
    """Test for empty."""
    test_favorite_color: dict[str, str] = {}
    assert favorite_color(test_favorite_color) == ""


def test_favorite_color_use() -> None:
    """Tests use case."""
    test_favorite_color: dict[str, str] = {"Gayle": "blue", "Marc": "yellow", "David": "blue"}
    assert favorite_color(test_favorite_color) == "blue"


def test_favorite_color_use2() -> None:
    """Testing ties in favorite colors."""
    test_favorite_color: dict[str, str] = {"Gayle": "blue", "Mark": "blue", "David": "yellow", "Marc": "yellow"}
    assert favorite_color(test_favorite_color) == "yellow"


def test_count_empty() -> None:
    """Test empty input for count."""
    test_count_list: list[str] = []
    assert count(test_count_list) == {}
    

def test_count_use() -> None:
    """Tests one use case for count."""
    test_count_list: list[str] = ["red", "red", "blue", "yellow"]
    assert count(test_count_list) == {"red": 2, "blue": 1, "yellow": 1}


def test_count_use2() -> None:
    """Tests second use case with one input."""
    test_count_list: list[str] = ["red"]
    assert count(test_count_list) == {"red": 1}


def test_alphabetizer_empty() -> None:
    """Tests empty input for alphabetizer."""
    test_alphabetizer: list[str] = []
    assert alphabetizer(test_alphabetizer) == {}


def test_alphabetizer_use() -> None:
    """Tests use case."""
    test_alphabetizer: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(test_alphabetizer) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_use2() -> None:
    """Tests second use case."""
    test_alphabetizer: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    assert alphabetizer(test_alphabetizer) == {'P': ['Python'], 'p': ['party'], 's': ['sugar'], 'T': ['Turtle'], 't': ['table']}


def test_update_attendance_empty() -> None:
    """Tests empty edge case."""
    test_update_attendance: dict[str, list[str]] = {}
    day: str = ""
    name: str = ""
    assert update_attendance(test_update_attendance, day, name) == {"": [""]}


def test_update_attendance_add_1() -> None:
    """Tests use case."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Tuesday"
    name: str = "Vrinda"
    assert update_attendance(attendance_log, day, name) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_add_2() -> None:
    """Tests second use case."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Wednesday"
    name: str = "Kaleb"
    assert update_attendance(attendance_log, day, name) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa'], 'Wednesday': ['Kaleb']}