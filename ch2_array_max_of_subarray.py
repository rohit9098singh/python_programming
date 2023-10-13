def max_subarray_sum(array):
    max_sofar=array[0]
    max_ending=array[0]

    for i in range(1,len.array):  
      max_ending=max(array[i],max_ending+array[i])  
      max_sofar=max(max_sofar,max_ending)
    return max_sofar    
try:
    size=int(input("enter the size of an array :"))
except ValueError as e:
    print(e)
    exit(1)

array=[]
for i in range(size):
    values=input(f"enter the value at indexe {i+1} ")  
    array.append(values)

max_sum = max_subarray_sum(array)
print(f"The maximum sum of a subarray is: {max_sum}")    