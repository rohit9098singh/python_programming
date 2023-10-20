factorial =lambda n: 1 if n==0 else n*factorial(n-1)
try:
    a = int(input("Enter the number of elements whose factorial you want to calculate: "))
except ValueError as e:
    print(e)
    exit()

array = []
for i in range(a):
    value = int(input(f"Enter the element at index {i+1}: "))
    array.append(factorial(value))
print("Factorials of the elements are:")
print(array)

variable = list(map(factorial, array))
print("Results of mapping factorial function over the array using lambda:")
print(variable)

print("Performing the filter operation using a lambda function:")
filter_lambda = lambda x: x > 35
new_new_array = list(filter(filter_lambda, array))
print(new_new_array)