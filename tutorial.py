# print("Hello world! This is Misty")

# Text type: str

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
    "thing": "category",
    "apple": "fruit"
}

leads = {
    "123-45-6789": "John Smith"
}


# Set Types: set, frozenset

my_set = {"Giannis Antetokounmpo", "Giannis Antetokounmpo", "Giannis Antetokounmpo"}
print(my_set)

# Boolean Type: bool

# Binary Types: bytes, bytearray, memoryview

quarterbacks = ["Tom Brady", "Derek Carr", "Drew Brees", "Cam Newton", "Teddy Bridgewater"]
cities = ["New York", "Seoul", "Chicago", "Paris", "Milan", "Rio de Janeiro"]
nba_mvps = ["Giannis Antetokounmpo", "Giannis Antetokounmpo", "James Harden", "Russell Westbrook", "Stephen Curry", "Stephen Curry", "Kevin Durant", "LeBron James", "LeBron James", "Derrick Rose", "LeBron James", "LeBron James", "Kobe Bryant"]
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
