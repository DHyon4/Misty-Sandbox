# print("hello world this is Misty")
a = 1
b = 2
# print(a + b)
# print("Eddie is the man lets go to Korea")
food = ["ramen", "soda", "breastmilk", "ramen"]
# print(f"{food[2]} is fucking delicious")
# for food_item in food:
#     if food_item == "ramen":
#         print("spicy butthole")
#     else:
#         print("not spicy")

drinks = ["water"]
for drink in drinks:
    print(drink)
# n=11
# while n>10:
#     print(f"Are You Motherfucking Ready Football {n}")
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

nfl = {
    "afc": {
        "north": ["Ravens", "Steelers", "Browns", "Bengals"],
        "south": ["Texans", "Titans", "Colts", "Jaguars"],
        "east": ["Patriots", "Jets", "Dolphins", "Bills"],
        "west": ["Raiders", "Chiefs", "Chargers", "Broncos"],
    },
    "nfc": {
        "north": ["Packers", "Vikings", "Bears", "Lions"],
        "south": ["Saints", "Falcons", "Buccaneers", "Panthers"],
        "east": ["Eagles", "Giants", "Redskins", "WowBoys"],
        "west": ["49ers", "Seahawks", "Rams", "Cardinals"],
    },
}
print(nfl["afc"]["north"][1])
print(nfl)
