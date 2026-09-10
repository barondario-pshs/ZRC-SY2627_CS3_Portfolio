class Hero:
    """Represents an RPG Hero with a name, health points, and combat abilities."""

    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp  # Bonus feature: Track max health

    def take_damage(self, amount: int) -> None:
        """Reduces health by amount, ensuring it never drops below 0."""
        self.hp = max(0, self.hp - amount)
        print(f"{self.name} takes {amount} damage! HP left: {self.hp}")

    def heal(self, amount: int) -> None:
        """Bonus feature: Restores health up to the maximum capacity."""
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} heals for {amount}! HP left: {self.hp}")

    def is_alive(self) -> bool:
        """Bonus feature: Returns True if the hero has health remaining."""
        return self.hp > 0

    def __str__(self) -> str:
        """Bonus feature: Custom string representation for easy printing."""
        status = "Alive" if self.is_alive() else "Defeated"
        return f"Hero -> Name: {self.name} | HP: {self.hp}/{self.max_hp} | Status: {status}"


# Step 3 — Instantiate two heroes and try them out.
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(arthur.hp)     # Expected: 90
print(morgana.hp)    # Expected: 100


# Bonus Features
print("\n--- Testing Bonus Features ---")
arthur.heal(5)       # Heals Arthur back up
print(arthur)        # Uses __str__ for clean details
print(f"Is Arthur alive? {arthur.is_alive()}")