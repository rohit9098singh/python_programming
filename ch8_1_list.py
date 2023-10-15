'''orderd collection of data items they store multiple items in a single varible'''
# create a list
my_list = [1, 2, 3, 4, 5]


my_list.append(6)
print("List after appending 6:", my_list)

my_list.extend([7, 8, 9])
print("List after extending with [7, 8, 9]:", my_list)

my_list.insert(3, 10)
print("List after inserting 10 at index 3:", my_list)

my_list.remove(5)
print("List after removing 5:", my_list)

popped_element = my_list.pop()  # we can also remove an specifed element by putting its index inside pop(here)...
print("Popped element:", popped_element)
print("List after popping the last element:", my_list)

my_list.clear()
print("List after clearing:", my_list)

new_list = [2, 3, 1, 5, 4, 3, 2]

index_of_3 = new_list.index(3)
print("Index of the first occurrence of 3:", index_of_3)

count_of_2 = new_list.count(2)
print("Count of 2 in the list:", count_of_2)

new_list.sort()
print("List after sorting:", new_list)

new_list.reverse()
print("List after reversing:", new_list)

copied_list = new_list.copy()
print("Copied list:", copied_list)

sliced_list = new_list[2:5]
print("Sliced list:", sliced_list)
