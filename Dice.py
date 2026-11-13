# Dice class for the object-oriented game simulator
# INF201, NMBU, 2026

import random


class Dice:
    """Represents an n-sided dice (n >= 2)."""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice

        Args:
            sides (int): Number of sides on the dice (default = 6, must be >= 2)

        Raises:
            ValueError: If sides is less than 2
        """
        if sides < 2:
            raise ValueError(f"A dice must have at least 2 sides, got {sides}")
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a random integer between 1 and sides."""
        return random.randint(1, self.sides)

    def __call__(self) -> int:
        """Make the dice callable, so d20() is the same as d20.roll()."""
        return self.roll()

    def __repr__(self) -> str:
        """Representation of dice object, e.g. Dice(sides=6)"""
        return f"Dice(sides={self.sides})"