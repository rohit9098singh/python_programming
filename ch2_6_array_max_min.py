
try:
    size=int(input("enter the size of an array :"))
except ValueError as e:
    print(e)
    exit(1)

array=[]
for i in range(size):
    values=input(f"enter the value at index {i+1} ")  
    array.append(values)
    
max_value=array[0]
min_value=array[0]
for arr in array:
    if(arr>max_value):
        max_value=arr
    if(arr<min_value):
        min_value=arr

print(f"the maximum value of the given array is :{max_value}")
print(f"the minimum value of the given array is {min_value}")        
