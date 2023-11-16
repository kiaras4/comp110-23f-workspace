"""File to define River class."""

__author__ = "730675328"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Creates River class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks surviving bears and fish."""
        surviving_bears: list[Bear] = []
        surviving_fish: list[Fish] = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish
        return None

    def bears_eating(self):
        """Method for when a bear eats."""
        for animals in self.bears:
            if len(self.fish) >= 5:
                animals.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks for bears who went too long without food."""
        surviving_bears: list[Bear] = []
        for animal in self.bears:
            if animal.hunger_score >= 0:
                surviving_bears.append(animal)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Repopulation of fish."""
        add: int = (len(self.fish) // 2) * 4
        for x in range(0, add):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulation of bears."""
        add: int = len(self.bears) // 2
        for x in range(0, add):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """To see the day and number of fish and bears."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """One week in river ecosystem."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
        return None
    
    def remove_fish(self, amount: int):
        """Removes specified number of fish starting from the frontmost fish."""
        x: int = 0
        while x < amount:
            self.fish.pop(0)
            x += 1