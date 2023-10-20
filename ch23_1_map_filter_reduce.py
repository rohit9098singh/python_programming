def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

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

# Applying map function to the array
variable = list(map(factorial, array)) 
print("Results of mapping factorial function over the array:")
print(variable)
 
#=======or=============
 

#========USING THE FILTER NOW==========
def filter_function(a):
    return a>35
print("just here we are performing the filter operation and letting you know the output")
new_new_array=list(filter(filter_function,array))# first argument is the function name and the second is the itterable object from where it  has to be done
print(new_new_array)