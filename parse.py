
employee_list = []

class NumberOfEmployees(Exception): pass
class AgeRestriction(Exception): pass


# first_name, last_name = input("please enter full name: ").split(" ")

# birth_year = str(input("please enter your birth year: "))

# number_of_employees = None

while True:
    try:
        number_of_employees = int(input("How many employees to add: "))
        if number_of_employees >= 10:
            raise NumberOfEmployees
        
        first_name, last_name = input("please enter full name: ").split(" ")
        birth_year = str(input("please enter your birth year: "))
        
    except ValueError:
        print("Needs to be a number")
    except NumberOfEmployees:
        print("Cannot have more than 10 employees")
    else: break

while True:
    try:
        age = int(input("Plase state your age: "))
        if age < 18:
            raise AgeRestriction
        first_name, last_name = input("please enter full name: ").split(" ")
        birth_year = str(input("please enter your birth year: "))
        
    except ValueError:
        print("Needs to be a number")
    except AgeRestriction:
        print("Cannot be less than 18 years of age")
        break
    else: break




# print(number_of_employees)
# print(birth_year[2])

print(f"First Name: {first_name.capitalize()}\nLast Name: {last_name.capitalize()}\nAge: {age}\nEmail: {first_name.lower()}.{last_name.lower()}{birth_year[2]}{birth_year[3]}@company.com")

# employee = {
#     "name": first_name,
#     "age": age,
#     "employees": number_of_employees,
# }

# print(employee)

# num = int(input("Enter a number: "))

# print("Number is even") if num % 2 == 0 else print("Number is odd")