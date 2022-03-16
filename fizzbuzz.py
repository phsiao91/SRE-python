
num = int(input("Please enter a number: "))
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0
total = 0
i = 0


while i < num:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
        fizzbuzz_count += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else: 
        print(i)
        total += num

print(f"fizz count: {fizz_count}")
print(f"buzz count: {buzz_count}")
print(f"fizzbuzz count: {fizzbuzz_count}")
print(f"integer total: {total}")

