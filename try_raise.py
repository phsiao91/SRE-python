class AgeException(Exception): pass


try:
    age = int(input("Enter your age, need to be over 18: "))
    if age < 18:
        raise AgeException
    years = int(input("Enter years of experience: "))
    res = years / age
except ValueError:
    print("Not an integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
except AgeException:
    print("You are too young to work here.")
else:
    print(f"You have been coding for {res*100}% of your life")
finally:
    print("The try block has finished")

print("Program finished")