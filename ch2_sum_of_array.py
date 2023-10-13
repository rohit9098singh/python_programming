try:
    size=int(input("enter the size of an array :"))
except ValueError as e:
    print(e)
    exit(1)

rohit=[]
for i in range(size):
    value=int(input(f"enter the array element at location {i+1} :"))
    rohit.append(value)
sum=0
for i in rohit:
    sum += i
print("the sum of all the values in the given values is as ",sum)                