n=int(input("enter the size of an array of your choice\n"))
try:
    array_size=n
except ValueError :
    
    print("the value you have provided is not a valid parameter please enter integer value please")
    exit(1) 
print(f"You entered an array size of {array_size}") 


my_array=[]

for i in range(array_size):
    values=input(f"enter the array element  {i+1} ")
    my_array.append(values)

#printing your array now 
print("array",my_array)    


