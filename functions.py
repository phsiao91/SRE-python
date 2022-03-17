

def say_hello():
    print("Hello World!")

say_hello()


def greetings(name:str = "World", message:str = "Hello") -> str:
    return f"{message}, {name}"


print(greetings("Python", "Greetings"))
print(greetings())
print(greetings(message = "Good Morning"))
print(greetings("Functions"))


def add_numbers(*args):
    return args


def iterate(*args):
    total = 0
    for arg in args:
        total += arg
    return f"Sum of {args} = {total}"

print(add_numbers(1,2,3,4,5,6,7))
print(add_numbers(1,2,3))
print(add_numbers(1))
print(add_numbers())
print(add_numbers(2,4))

print(iterate(1,2,3,4,5,6,7))
print(iterate(1,2,3))
print(iterate(1))
print(iterate())
print(iterate(2,4))


def print_args(**kwargs):
    return kwargs


print(print_args(a=1, b=2, c=3))
print(print_args(x=10, y=20))
print(print_args())

def itereate_args(**kwargs):
    output = ""
    for key, value in kwargs.items():
        output += f"{key} = {value}\n"
    return output[:-1]

print(itereate_args(a=1, b=2, c=3))
print(itereate_args(x=10, y=20))
print(itereate_args())


print(True,1,2,3,4,[1,2,3], "Hello", None, sep = " -> ", end="\n\n")
print("good bye!")


def loop():
    t = 0
    while True:
        print(t)
        if t == 10:
            return t
        t += 1

print(loop())



def add_total(*nums, cb):
    total = 0
    for num in nums: total += num
    cb(total)


def pretty_print(val):
    print(f"****{val}****")


add_total(1,2,3, cb=print)
add_total(1,2,5,6, cb=pretty_print)
add_total(1,2,3, cb=pretty_print)