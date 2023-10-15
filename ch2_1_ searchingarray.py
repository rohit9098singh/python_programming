n=input("enter the size of an array :")
array_size=int(n)
try:
   array_size=int(n)
except ValueError as e:
   print(e)
   print("your size is not in a valid datatype") 
   exit(1)  
my_array=[]
for i in range(array_size):
   values=input(f"enter the the array elememt at index :{i+1} : ")
   my_array.append(values)

print("==========your enterd array is as follow============")
print("array is",my_array)
search = input("Enter the array element that is to be searched: ")

#found = False
c=1

for i, element in enumerate(my_array):
    if search == element:
        print(f"The array element found at location: {i+1} and the element is: {search}")
        #found = True
        c=1
        break

#if not found:
    else:
     print("The array element was not found in the array.")



