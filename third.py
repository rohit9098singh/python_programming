# A LITTLE DIFFERENT WAY TO TAKE THE ARRRAY ENTER FROM THE USER
n=input("enter the size of an array of your choice :")
array_size=int(n)
print(f"your array size is {array_size}")
my_array=[0]*array_size
for i in range(array_size):
    values=input(f"enter the array eloemts of index {i+1} ")
    my_array[i]=values

print("your given array is as follow")
print("array",my_array)    
