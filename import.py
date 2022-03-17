import module
from function_except import my_function
import random
import timeit


print(module.reading(name="Example"))
print(module.c)

num = my_function()
print(f"you entered {num}")


print("import directory")

print(random.random())
print(random.randint(1,10))
print(random.sample([1,2,3,4,5],3))


statement = """for i in range(1,1000):
    print(i)"""

print(timeit.timeit(stmt=statement, number=2))


if __name__ == "__main__":
    print(dir())