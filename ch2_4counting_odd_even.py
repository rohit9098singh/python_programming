even = 0
odd = 0

try:
    n = int(input("Enter the size of an array: "))
except ValueError as e:
    print(e)
    print("Invalid data type entry. Please make a proper choice.")
    exit(1)
    
array = []

for i in range(n):
    value = int(input(f"Enter the value at index {i+1}: "))
    array.append(value)  # Append the value to the list

    if value % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"The number of even numbers in your array is: {even}")
print(f"The number of odd numbers in your array is: {odd}")
