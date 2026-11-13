# Items (weapons) for the object-oriented game simulator
# INF201, NMBU, 2026

from dice import Dice


class Weapon:
    """Represents a weapon whose damage is decided by a dice roll."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): Name of the weapon
            damage_dice (Dice): The dice rolled to decide damage
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's damage dice and return the damage."""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Representation of weapon object"""
        return f"Weapon(name={self.name!r}, damage_dice={self.damage_dice!r})"