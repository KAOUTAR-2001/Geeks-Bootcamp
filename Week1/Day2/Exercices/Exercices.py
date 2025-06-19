#11111

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))

print(result_dict)

#222222

# Initialize an empty dictionary for family members
family = {}

# Ask the user how many family members they want to add
num_members = int(input("How many family members? "))

# Collect family members' names and ages
for _ in range(num_members):
    name = input("Enter name: ").strip().capitalize()  # Capitalize the name for better formatting
    age = int(input("Enter age: "))
    family[name] = age  # Add the member to the dictionary

# Initialize total cost
total_cost = 0

print("\n Ticket Prices \n")

# Define ticket pricing and calculate total cost
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    total_cost += price
    print(f"{name} has to pay ${price}")

# Print total cost for the family
print(f"\n Total cost for the family: ${total_cost}")

#3
# 1 Create the brand dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 2 Change the number of stores to 2
brand["number_stores"] = 2

# 3 Print who Zara's clients are using type_of_clothes
print(f"Zara serves customers in categories: {', '.join(brand['type_of_clothes'])}")

# 4 Add country of creation
brand["country_creation"] = "Spain"

# 5 Check if international_competitors exists and add 'Desigual'
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6 Delete the creation_date key
del brand["creation_date"]

# 7 Print the last international competitor
print(f"Last international competitor: {brand['international_competitors'][-1]}")

# 8 Print major colors in the US
print(f"Major colors in the US: {brand['major_color']['US']}")

# 9 Print the number of key-value pairs in the dictionary
print(f"Total key-value pairs: {len(brand)}")

# 10 Print all the keys of the dictionary
print(f"Keys: {list(brand.keys())}")

# 11 Create another dictionary called more_on_zara
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# 12 Add more_on_zara information to the brand dictionary
brand.update(more_on_zara)

# 13Print the updated number of stores
print(f"Updated number of stores: {brand['number_stores']}")

#3333

def describe_city(city, country="Unknown Country"):
    print(f"{city} is in {country}.")

# Call the function
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

#4444

import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print(" Success! You guessed the number correctly!")
    else:
        print(f" Fail! Your number: {user_number}, Random number: {random_number}")


num = int(input("Enter a number between 1 and 100: "))
compare_numbers(num)

#5555

def make_shirt(size="Large", message="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{message}'.")

# Call with default values
make_shirt()
make_shirt("Medium")
make_shirt("Small", "Hello World!")

# Using keyword arguments
make_shirt(size="XL", message="Python Rocks!")

#6666

import random

def get_random_temp(season):
    if season == "winter":
        return random.uniform(-10, 16)
    elif season == "spring":
        return random.uniform(5, 22)
    elif season == "summer":
        return random.uniform(20, 40)
    elif season == "autumn":
        return random.uniform(10, 25)
    else:
        return random.uniform(-10, 40)

def main():
    season = input("Enter the season (winter, spring, summer, autumn): ").lower()
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp:.1f} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp < 23:
        print("Mild weather today.")
    elif temp < 32:
        print("It's warm outside!")
    else:
        print("It's really hot! Stay hydrated.")

main()

#7777

def star_wars_quiz():
    data = [
        {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
        {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
        {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
        {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
        {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
        {"question": "What species is Chewbacca?", "answer": "Wookiee"}
    ]

    correct = 0
    wrong_answers = []

    for item in data:
        user_answer = input(item["question"] + " ").strip()
        if user_answer.lower() == item["answer"].lower():
            correct += 1
        else:
            wrong_answers.append((item["question"], user_answer, item["answer"]))

    print(f"\nYou got {correct}/{len(data)} correct!")

    if wrong_answers:
        print("\nHere are the questions you got wrong:")
        for question, user_ans, correct_ans in wrong_answers:
            print(f" {question}\n   Your answer: {user_ans}\n   Correct answer: {correct_ans}")

star_wars_quiz()