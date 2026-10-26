# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def eat(self):
        pass

# Child class: Lion
class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} the lion roars loudly.")

    def eat(self):
        print(f"{self.name} the lion eats fresh meat.")


# Child class: Elephant
class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} the elephant trumpets.")

    def eat(self):
        print(f"{self.name} the elephant eats grass and fruits.")


# Child class: Monkey
class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} the monkey chatters.")

    def eat(self):
        print(f"{self.name} the monkey eats bananas.")

# 
if __name__ == "__main__":
    zoo_animals = [
        Lion("Rheign"),
        Elephant("Leighann"),
        Monkey("Alwin")
    ]

    for animal in zoo_animals:
        animal.make_sound()
        animal.eat()
        print("-" * 40)