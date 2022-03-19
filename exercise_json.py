import json



drinks = []
try:
    with open("./resources/drinks.json","rt") as file:
        data = file.read()
        drinks = json.loads(data)
        print(type(drinks))
except FileNotFoundError: print("Not found")


print(drinks)