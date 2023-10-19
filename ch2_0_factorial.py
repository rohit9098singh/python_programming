'''def factorial(n):
   if(n==0):
      return 1
   else:
      return n*factorial(n-1)
try:
   a=int(input("enter the number of element whoes factorial you want to calculate......"))
except ValueError as e:
   print(e)

array=[]
for i in range(a):
   value=int(input(f"enter the element at index {i+1} :"))
   array.append(factorial(value))

print("the given list is___")
for i in array:
   print("=====your enterd array is =====\n",array)
      
print("factorial of the given list is.......")
for i,element in enumerate(array):
   print(f"the factorail of the given no at {i+1} is {element}")'''
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
