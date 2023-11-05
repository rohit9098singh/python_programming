from functools import reduce

# Your number list
numbers = [1, 2, 3, 4, 5]

# Using reduce to get the sum of the numbers
result = reduce(lambda x, y: x + y, numbers)
print(result)


# reduce kya karega ke sabse pehle 1+2=3,then 3+3=6, then 6+4=10, then 10+5=15.
