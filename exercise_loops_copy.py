import csv
import json
from pprint import pprint

employee_list = []
header = ["name", "email", "id"]

try:
    with open("./resources/employees.csv", "rt") as file:
        reader = csv.DictReader(file, header)
        for row in reader.reader:
            employee_list.append(row)
    pprint(employee_list)
except FileNotFoundError: print("File not found")

try:
    with open("./resources/employees.json", "rt") as file:
        data = file.read()
        employee_list = json.loads(data)
        print(data)
except FileNotFoundError: print("File not found")

# try:
#     with open("./resources/employees.csv", "rt") as file:
#         data = csv.reader(file)
#         employee_list = json.loads(data)
#         print(data)
# except FileNotFoundError: print("File not found11s")

# rows = []
# header = []
# try:
#     with open("./resources/employees.csv") as file:
#         data = csv.reader(file)
#         header = next(data)
#         # print(header)
#         for row in data:
#             rows.append(row)
# except FileNotFoundError: print("File not found")

# print(header)
# pprint(rows)

max_employees = 4
number_of_emplyees = 0
class NumberOfEmployees(Exception): pass
class AgeRestriction(Exception): pass

while True:
    try:
        number_of_emplyees = int(input("Enter how many employees to add: "))
        if number_of_emplyees > max_employees:
            raise NumberOfEmployees
            
        for i in range(number_of_emplyees):
            employee = {}
            while True:
                try:
                    age = int(input("Plase state your age: "))        
                    if age < 18:
                        raise AgeRestriction
                    first_name, last_name = input("please enter full name: ").split(" ")
                    birth_year = str(input("please enter your birth year: "))
                    email = (f"{first_name.lower()}.{last_name.lower()}{birth_year[2]}{birth_year[3]}@company.com")

                    employee["id"] = i + 1
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
        print(employee_list)
    except ValueError:
        print("Needs to be a number")
    except NumberOfEmployees:
        print(f"Cannot have more than {max_employees} employees")
    else: break


# try:
#     with open("./resources/exercise_loops_copy.txt", "x") as file:
#         print("file created")
#         try:
#             with open("./resources/exercise_loops_copy.txt", "at") as copy:
#                 copy.write(str(employee_list))
#         except FileNotFoundError: print("File not found!")
# except FileExistsError: print("File exists!")


# try:
#     with open("./resources/employees.csv","x") as file:
#         print("file created")
# except FileExistsError: print("Already exists!")

try:
    with open("./resources/employees.csv","wt") as file:
        # header = employee_list[0].keys()
        # csv_writer = csv.writer(file)
        # csv_writer.writerow(header)
        # for row in employee_list:
        #     row = []
        #     for item in header:
        #         row.append(item)
        #     csv_writer.writerow(row)
        # print("entered")
        # header = employee_list[0].keys()
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(employee_list)
except FileNotFoundError: print("File not Found")


try:
    with open("./resources/employees.json","wt+") as file:
        employee_json = json.dumps(employee_list,indent=2)
        file.write(employee_json)
except FileNotFoundError: print("not found")


