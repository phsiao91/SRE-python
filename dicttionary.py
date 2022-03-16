

bio = {
    "name": input("Please enter your name: "),
    "age": int(input("Please enter your age: ")),
    "years coding": int(input("Please enter years of experience: "))
}

try:
    number_of_employees = int(input("How many employees to add: "))
    if number_of_employees > 10:
        raise Exception
except ValueError:
    print("Needs to be a number")
except Exception:
    print("Cannot have more than 10 employees")

first_three = tuple(input("Please enter your first three languages: ").split(" "))

favorite_three = input("Please enter your favorite three: ").split(" ")

favorite = set(first_three).intersection(favorite_three)

single_collection = [*first_three, *favorite_three]

language_set = set(single_collection)

bio.update({"languages": language_set})

bio["favorite"] = favorite

print(first_three)
print(favorite_three)
print(single_collection)
print(language_set)
print(bio)
