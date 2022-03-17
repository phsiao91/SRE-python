
class RangeError(Exception): pass
class HighRangeError(Exception): pass

def my_function(low = None, high = None, input_type = int):
    while True:
        try:
            num = input_type(input(f"please enter a {input_type}: "))
            if isinstance(low, input_type) and low > num:
                raise RangeError
            if isinstance(high, input_type) and high < num:
                raise HighRangeError
            return num
        except ValueError:
            print("Not a number")
        except RangeError:
            print(f"Needs to be more than {low}")
        except HighRangeError:
            print(f"Needs to be lesser than {high}")



if __name__ == "__main__":
    # value = my_function()
    # print(value)

    num1 = my_function(1,100)
    print(num1)

    num2 = my_function(20)
    print(num2)

    num3 = my_function(input_type=float)
    print(num3)