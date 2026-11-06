# 1. Questions & Answers
# a. What is duck typing, as explained in the video?
# Duck typing is a concept of polymorphism without inheritance, where an object's
# suitability is determined by the presence of specific methods and behaviors rather than its explicit inheritance hierarchy.

# b. What did the Car class need to have so it could work inside the same loop as Dog and
# Cat, even if it does not inherit from the Animal class?
# The Car class needed to implement the same method signature as Dog and Cat so it could be 
# processed within the same loop without needing to inherit from the Animal class.

# 2.
# a. Create three classes: Car, Boat, and Drone with a move() method
class Car:
    def move(self):
        print("The car drives on the road.")  #

class Boat:
    def move(self):
        print("The boat sails on water.")  #

class Drone:
    def move(self):
        print("The drone flies in the sky.")  #[cite: 2]

# b. Function named start_trip(vehicle) that calls vehicle.move()[cite: 2]
def start_trip(vehicle):
    vehicle.move()  #[cite: 2]

# c. Create one object of each class[cite: 2]
my_car = Car()
my_boat = Boat()
my_drone = Drone()

# d. Call the start_trip() method for each object[cite: 2]
start_trip(my_car)
start_trip(my_boat)
start_trip(my_drone)