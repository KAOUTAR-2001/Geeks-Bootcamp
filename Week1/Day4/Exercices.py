# Exercice
# Exercice1
# Base Pets class
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        """Make all pets walk"""
        for animal in self.animals:
            print(animal.walk())

# Base Cat class
class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

# Bengal Cat breed
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Chartreux Cat breed
class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Siamese Cat breed (New class)
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Creating cat instances
bengal_cat = Bengal("Tiger", 3)
chartreux_cat = Chartreux("Misty", 5)
siamese_cat = Siamese("Luna", 2)
# Creating a list of Sara's cats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Creating Sara's pets instance
sara_pets = Pets(all_cats)

# Taking all cats for a walk
sara_pets.walk()

# Exercice2

# Dog class definition
class Dog:
    def __init__(self, name, age, weight):
        """Initialize the dog with name, age, and weight."""
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        """Returns a string indicating that the dog is barking."""
        return f"{self.name} is barking!"

    def run_speed(self):
        """Calculates and returns the dog's running speed."""
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        """Determines the winner in a fight based on (run speed x weight)."""
        my_power = self.run_speed() * self.weight
        opponent_power = other_dog.run_speed() * other_dog.weight

        if my_power > opponent_power:
            return f" {self.name} wins the fight against {other_dog.name}!"
        elif my_power < opponent_power:
            return f" {other_dog.name} wins the fight against {self.name}!"
        else:
            return " It's a tie! Both dogs are equally strong."

# Creating three Dog instances
dog1 = Dog("pokie", 5, 20)
dog2 = Dog("Bolt", 3, 25)
dog3 = Dog("Max", 4, 18)

# Testing the dogs
print(dog1.bark())  # Rex barking
print(f"{dog1.name}'s speed: {dog1.run_speed():.2f}")

print(dog2.bark())  # Bolt barking
print(f"{dog2.name}'s speed: {dog2.run_speed():.2f}")

print(dog3.bark())  # Max barking
print(f"{dog3.name}'s speed: {dog3.run_speed():.2f}")

# Fighting between dogs
print(dog1.fight(dog2))  # pokie vs Bolt
print(dog2.fight(dog3))  # Bolt vs Max
print(dog3.fight(dog1))  # Max vs Rex

# Exercice3
# dog.py

class Dog:
    def __init__(self, name, age, weight):
        """Initialize the dog with name, age, and weight."""
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        """Returns a string indicating that the dog is barking."""
        return f"{self.name} is barking!"

    def run_speed(self):
        """Calculates and returns the dog's running speed."""
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        """Determines the winner in a fight based on (run speed x weight)."""
        my_power = self.run_speed() * self.weight
        opponent_power = other_dog.run_speed() * other_dog.weight

        if my_power > opponent_power:
            return f" {self.name} wins the fight against {other_dog.name}!"
        elif my_power < opponent_power:
            return f" {other_dog.name} wins the fight against {self.name}!"
        else:
            return " It's a tie! Both dogs are equally strong."

import random
from dog import PetDog  # Importing Dog class

# PetDog class that inherits from Dog
class PetDog(Dog):
    def __init__(self, name, age, weight):
        """Initialize the PetDog with additional attribute 'trained'"""
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        """Makes the dog bark and sets trained to True."""
        print(self.bark())  # Calls the inherited bark method
        self.trained = True
        print(f" {self.name} is now trained!")

    def play(self, *dog_names):
        """Prints that the dogs are playing together."""
        dogs_playing = ", ".join(dog_names)
        print(f" {self.name}, {dogs_playing} all play together!")

    def do_a_trick(self):
        """Performs a random trick if the dog is trained."""
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f" {self.name} is not trained yet. Train the dog first!")

# Creating PetDog instances
dog1 = PetDog("Buddy", 4, 22)
dog2 = PetDog("Rocky", 3, 18)
dog3 = PetDog("Charlie", 5, 25)

# Training the first dog
dog1.train()

# Playing with multiple dogs
dog1.play(dog2.name, dog3.name, "Max")

# Performing tricks
dog1.do_a_trick()
dog2.do_a_trick()  # This dog is not trained yet

# Exercices 4
# create family class

class Family:
    def __init__(self, last_name, members):
        """Initialize a family with a last name and a list of members."""
        self.last_name = last_name
        self.members = members  # List of dictionaries

    def born(self, **kwargs):
        """Add a child to the family with provided details."""
        self.members.append(kwargs)
        print(f" Congratulations! A new baby {kwargs['name']} is born into the {self.last_name} family!")

    def is_18(self, name):
        """Check if a family member is over 18 years old."""
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return False  # If member not found

    def family_presentation(self):
        """Print the family's last name and all member's details."""
        print(f"\n The {self.last_name} Family:")
        for member in self.members:
            print(f" - {member['name']}, {member['age']} years old, {member['gender']}, Child: {member['is_child']}")

