try:
    size=int(input("enter the size of an array :"))
except ValueError as e:
    print(e)
    exit(1)

rohit=[]
for i in range(size):
    value=int(input(f"enter the array element at location {i+1} :"))
    rohit.append(value)

sorted_array=sorted(rohit)
print("our original array is :",rohit)
print("your sorted array is as folow",sorted_array)    