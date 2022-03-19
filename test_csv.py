import csv
import json
from pprint import pprint


rows = []
header = []


try:
    with open("./resources/drinks.csv") as file:
        data = csv.reader(file)
        header = next(data)
        # print(header)
        for row in data:
            rows.append(row)
except FileNotFoundError: print("File not found")

print(header)
pprint(rows)

# new_drink = input("enter a drink: "), input("temp: "), input("price: ")

# rows.append(new_drink)

# try:
#     with open("./resources/drinks.csv", "wt") as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerow(header)
#         csv_writer.writerows(rows)
# except FileNotFoundError: print("not found")


drink_list = []

for row in rows:
    drink = {}
    for i in range(len(header)):
        drink[header[i]] = row[i]
    drink_list.append(drink)

pprint(drink_list)


json_format = json.dumps(drink_list)

print((json_format))


try:
    with open("./resources/drinks.json","wt") as file:
        file.write(json_format)
except FileNotFoundError: print("not found")