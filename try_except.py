
try:
    num = int(input("Enter an intteger: "))
    div = 10 / num
    # print(div)
except ValueError:
    print("You did not enter an integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"The result is\n{div}")
finally:
    print("The Try Block has ended")

print("Program finished")