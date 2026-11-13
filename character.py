# Object-oriented game simulator
# Based on game_simulator_v1.py by Turid Torheim, NMBU, 2026
# Extended for Deliverable 3, INF201


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Base damage dealt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # _hp indicates a private attribute
        self.hp_max = hp_max
        self.damage = damage

    # ---------- Properties ----------
    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property: True if the character has more than 0 HP."""
        return self._hp > 0

    # ---------- Methods ----------
    def take_damage(self, amount: int) -> int:
        """
        Reduce own HP by amount. HP never goes below 0.

        Returns:
            int: The damage actually taken
        """
        amount = max(amount, 0)
        old_hp = self._hp
        self._hp = max(self._hp - amount, 0)
        return old_hp - self._hp

    def heal(self, amount: int) -> int:
        """
        Increase own HP by amount. HP never goes above hp_max.
        A dead character cannot be healed.

        Returns:
            int: The HP actually restored
        """
        if not self.is_alive:
            return 0
        amount = max(amount, 0)
        old_hp = self._hp
        self._hp = min(self._hp + amount, self.hp_max)
        return self._hp - old_hp

    def attack(self, target: "Character") -> int:
        """
        Attack target: the target's take_damage() method handles its own HP.

        Returns:
            int: The damage actually taken by the target
        """
        return target.take_damage(self.damage)

    def introduce(self) -> None:
        """Prints a string that introduces the character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<{type(self).__name__} name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return (f"{type(self).__name__}: {self.name} with {self.hp}/{self.hp_max} HP "
                f"and {self.damage} base damage")