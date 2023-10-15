n = input("\nenter the size of an array: ")
array_size = int(n)
try:
    array_size = int(n)
except ValueError as e:
    print(e)
    print("your size is not in a valid datatype")
    exit(1)

my_array = []
for i in range(array_size):
    values = input(f"enter the array element at index {i+1}: ")
    my_array.append(values)
print("your enterd array is as follow",my_array)    

choice = int(input("enter your choice\n1: linear search\n2: binary search\n3: exit\n"))
match choice:
    case 1:
        search = input("Enter the array element that is to be searched: ")
        c = 1
        for i, element in enumerate(my_array):
            if search == element:
                print(f"The array element found at location: {i+1} and the element is: {search}")
                c = 1
                break
        else:
            print("The array element was not found in the array.")

    case 2:
        first = 0
        last = len(my_array) - 1
        search = input("Enter the element that is to be searched: ")
        while first <= last:
            middle = (first + last) // 2
            if my_array[middle] == search:
                print(f"Element found at location {middle + 1} and the element is {search}")
                break
            elif search < my_array[middle]:
                last = middle - 1
            else:
                first = middle + 1
        else:
            print("Element not found in the array.")
    case 3:
        exit(0)
    case _:
        print("Invalid choice")
