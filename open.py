
opened = False

try:
    file = open("./resources/text.txt")
    opened = True
    print(file.read())
except FileNotFoundError: print("File not found")
finally:
    if opened: file.close()



try:
    with open("./resources/text.txt","rt") as file:
        print(file.readline())
        print(file.read(5))
except FileNotFoundError: print("File not found")

try:
    with open("./resources/test.txt","x"):
        print("File created.")
except FileExistsError: print("File already exists.")

try:
    with open("./resources/test.txt","at") as file:
        file.write("\nwritten here new\n")
        file.writelines(['written','here','new'])
except FileNotFoundError: print("File not found.")

try:
    with open("./resources/test.txt","rt") as file:
        with open("./resources/copy.txt","wt") as copy:
            copy.write(file.read())
except FileNotFoundError: print("File not found.")
