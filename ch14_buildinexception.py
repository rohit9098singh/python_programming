# 1. ZeroDivisionError
try:
    result = 10 / 0
except ArithmeticError as e:
    print(f"ZeroDivisionError: {e}")

# 2. IndexError
my_list = [1, 2, 3]
try:
    value = my_list[3]
    print(value)
except IndexError as e:
    print(f"IndexError: {e}")


# 4. TypeError
try:
    sum_result = '1' + 2
except TypeError as e:
    print(f"TypeError: {e}")

# 5. ValueError
try:
    num = int('string')
except ValueError as e:
    print(f"ValueError: {e}")

# 6. KeyError
my_dict = {'a': 1, 'b': 2, 'c': 3}
try:
    value = my_dict['d']
except KeyError as e:
    print(f"KeyError: {e}")

