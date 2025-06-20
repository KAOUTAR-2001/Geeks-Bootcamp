#OOP
#Ex1

# Class definition
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Function to find the oldest cat
def find_oldest_cat(cats):
    return max(cats, key=lambda cat: cat.age)

# Creating 3 cat objects
cat1 = Cat("MIMI", 11)
cat2 = Cat("KATY", 9)
cat3 = Cat("FIFI", 2)

# Storing them in a list
cats = [cat1, cat2, cat3]

# Finding and printing the oldest cat
oldest = find_oldest_cat(cats)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

##################################################################

#Ex2
# Class definition
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Creating dog objects
lilyas_dog = Dog("Pokie", 50)
amals_dog = Dog("tagger", 20)

# Printing dog details
print(f"lilyas dog: {lilyas_dog.name}, {lilyas_dog.height}cm")
lilyas_dog.bark()
amals_dog.jump()

print(f"amals dog: {amals_dog.name}, {amals_dog.height}cm")
amals_dog.bark()
amals_dog.jump()

# Checking which dog is bigger
bigger_dog = lilyas_dog if lilyas_dog.height > amals_dog.height else amals_dog
print(f"The bigger dog is {bigger_dog.name}.")

############################################################

#Ex3

# Class definition
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Creating an object
stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and shes buying a stairway to heaven"
])

# Printing song lyrics
stairway.sing_me_a_song()

##########################################################

#Ex4
# Class definition
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        return grouped_animals

    def get_groups(self):
        groups = self.sort_animals()
        for key, group in groups.items():
            print(f"{key}: {group}")

# Creating a zoo object
new_york_zoo = Zoo("New York Zoo")

# Adding animals
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Lion")
new_york_zoo.add_animal("Zebra")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")

# Displaying animals
new_york_zoo.get_animals()

# Selling an animal
new_york_zoo.sell_animal("Lion")
print("\nAfter selling Lion:")
new_york_zoo.get_animals()

# Sorting and grouping animals
print("\nGrouped Animals:")
new_york_zoo.get_groups()