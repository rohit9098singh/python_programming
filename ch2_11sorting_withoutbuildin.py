try:
    size=int(input("enter the size of an array :"))
except ValueError as e:
    print(e)
    exit(1)

rohit=[]
for i in range(size):
    value=int(input(f"enter the array element at location {i+1} :"))
    rohit.append(value)

for i in range(len(rohit)):
    for j in range(0,len(rohit)-i-1):
        if(rohit[j]>rohit[j+1]):
            rohit[i],rohit[i+1]=rohit[i+1],rohit[i]

print("the sorted array is as follow",rohit)               