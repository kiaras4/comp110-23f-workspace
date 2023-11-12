"""Defines point class."""
from __future__ import annotations

__author__ = "730675328"


class Point:
    """Point class."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method to scale point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Method to return new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Method to return point in readable manner."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Magic method for multiplication."""
        new_x = self.x * factor
        new_y = self.y * factor
        new_point: Point = Point(new_x, new_y)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Magic method for addition."""
        new_x = self.x + factor
        new_y = self.y + factor
        new_point: Point = Point(new_x, new_y)
        return new_point