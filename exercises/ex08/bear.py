"""File to define Bear class."""


class Bear:
    """Creates Bear class."""

    age: int
    hunger_score: int

    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Bears with age and hunger_score."""
        self.age = age
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """Method for one day at a time."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Method for when a bear eats."""
        self.hunger_score += num_fish
        return None