employee_list = []
max_employees = 4
number_of_emplyees = 0

class NumberOfEmployees(Exception): pass
class AgeRestriction(Exception): pass

while True:
    try:
        number_of_emplyees = int(input("Enter how many employees to add: "))
        if number_of_emplyees > max_employees:
            raise NumberOfEmployees

        counter = 1
        while counter <= number_of_emplyees:
            employee = {}
            while True:
                try:
                    age = int(input("Plase state your age: "))        
                    if age < 18:
                        raise AgeRestriction
                    first_name, last_name = input("please enter full name: ").split(" ")
                    birth_year = str(input("please enter your birth year: "))
                    email = (f"{first_name.lower()}.{last_name.lower()}{birth_year[2]}{birth_year[3]}@company.com")

                    employee["id"] = counter
                    employee["name"] = first_name
                    employee["email"] = email

                    employee_list.append(employee)
                except ValueError:
                    print("Must be a number")
                except AgeRestriction:
                    print("Must be 18 years or older")
                    break
                else:
                    break
            counter += 1
            print(employee_list)
    except ValueError:
        print("Needs to be a number")
    except NumberOfEmployees:
        print(f"Cannot have more than {max_employees} employees")
    else: break

    
