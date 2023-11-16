"""File to define Fish class."""


class Fish:
    """Creates Fish class."""

    age: int

    def __init__(self, age: int = 0):
        """Fish with ages."""
        self.age = age
        return None
    
    def one_day(self):
        """Method for one day at a time."""
        self.age += 1
        return None