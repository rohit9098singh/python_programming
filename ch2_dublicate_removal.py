try:
  size=int(input("enter the size of an array :"))
except ValueError as e:
  print(e)
  exit(1)


my_array=[]
for i in range(size):
  value=input(f"enter the value at index {i+1} :")
  my_array.append(value)  

print("your array is ",my_array) 

def removingdublicate(dublicate):
 removed_dublicate=[] 
 for i in my_array:
  if i  not in removed_dublicate:
    removed_dublicate.append(i)
 return removed_dublicate  

print("array after removal of the dublicates are as follow")
print(removingdublicate(my_array)) 


 

