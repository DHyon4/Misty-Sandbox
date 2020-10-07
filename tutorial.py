# print("Hello world! This is Misty")

# Text type: str
from abc import ABC

my_string = "hello"

# Numeric Types: int, float, complex

my_int = 12345
my_float = 0.1

# Sequence Types: list, tuple, range

my_list_of_strings = ["John", "Paul", "George", "Ringo"]
my_list_of_ints = [1_000_000_000_000_000_000_000_000_000_000, 2, 3, 4]

# Mapping Types: dict

my_dict = {
    "key": "value",
    "afc": {},
    "nfc": {},
    "thing": "category",
    "apple": "fruit"
}

leads = {
    "123-45-6789": "John Smith"
}

# Set Types: set, frozenset

my_set = {"Giannis Antetokounmpo", "Giannis Antetokounmpo", "Giannis Antetokounmpo"}
# print(my_set)

# Boolean Type: bool

# Binary Types: bytes, bytearray, memoryview

quarterbacks = ["Tom Brady", "Derek Carr", "Drew Brees", "Cam Newton", "Teddy Bridgewater"]
cities = ["New York", "Seoul", "Chicago", "Paris", "Milan", "Rio de Janeiro"]
nba_mvps = ["Giannis Antetokounmpo", "Giannis Antetokounmpo", "James Harden", "Russell Westbrook", "Stephen Curry",
            "Stephen Curry", "Kevin Durant", "LeBron James", "LeBron James", "Derrick Rose", "LeBron James",
            "LeBron James", "Kobe Bryant"]
nba_mvps_set = set(nba_mvps)
# print(nba_mvps_set)

phone_directory = {
    "123-45-6789": {"name": "John Smith",
                    "state": "NY"},
    "123-45-6780": {"name": "John Smith",
                    "state": "TX"},
}

# phone_directory = {
#     "John Smith": "Texas",
#     "John Smith": "New York"
# }
#
# phone_directory_deduped = {
#     "John Smith1": "Texas",
#     "John Smith2": "New York"
# }

# dannys_name = "danny"
# print(dannys_name * 5)

# print(len(quarterbacks))

# for i in range(len(cities)):
#     city = cities[i]
#     print(f"{i}: {city}")


# for city in cities:
#     print(city)

a = 1
b = 2
# print(a + b)
# print("Eddie is the man, lets go to Korea")
food = ["ramen", "soda", "milk", "ramen"]


# print(f"{food[2]} is delicious")
# for food_item in food:
#     if food_item == "ramen":
#         print("spicy")
#     else:
#         print("not spicy")

# drinks = ["water"]
# for drink in drinks:
#     print(drink)
# n=11
# while n>10:
#     print(f"Are You Ready For Some Football {n}")
#     n=n+15

# fruit_and_vegetables = {
#     "apple": "fruit",
#     "banana": "fruit",
#     "orange": "fruit",
#     "cucumber": "vegetable",
#     "spinach": "vegetable",
# }
# # print(fruit_and_vegetables["apple"])
# # print(fruit_and_vegetables.values())
# for green, green_type in fruit_and_vegetables.items():
#     # print(green, green_type )
#     print(f"{green} is a {green_type}")

def say_whatever(thing_to_print):
    print(thing_to_print)


# for i in range(10):
#     say_whatever("Danny Hyon")


# Classes

class Animal(ABC):
    def __init__(self, has_tail, noise):
        self.has_tail = has_tail
        self.noise = noise

    def make_noise(self):
        print(self.noise)


class Cat(Animal):
    def __init__(self, has_tail=True, noise="meow"):
        super().__init__(has_tail, noise)


class Dog(Animal):
    def __init__(self, has_tail=True, noise="woof"):
        super().__init__(has_tail, noise)


class Huskie(Dog):
    def __init__(self):
        super().__init__()


my_cat = Cat()
my_cat.make_noise()

my_dog = Dog()
my_dog.make_noise()

my_huskie = Huskie()
my_huskie.make_noise()
