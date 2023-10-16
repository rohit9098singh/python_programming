
my_tuple = (1, 2, 3, 4, 3, 2, 1)


count_of_3 = my_tuple.count(3)
print(f"Count of 3 in the tuple: {count_of_3}")


index_of_4 = my_tuple.index(4)
print(f"Index of 4 in the tuple: {index_of_4}")


length_of_tuple = len(my_tuple)
print(f"Length of the tuple: {length_of_tuple}")


sliced_tuple = my_tuple[2:5]
print(f"Sliced tuple: {sliced_tuple}")


new_tuple = my_tuple + (5, 6, 7)
print(f"Concatenated tuple: {new_tuple}")


min_value = min(my_tuple)
max_value = max(my_tuple)
print(f"Minimum value in the tuple: {min_value}")
print(f"Maximum value in the tuple: {max_value}")


sorted_tuple = sorted(my_tuple)
print(f"Sorted tuple: {sorted_tuple}")


my_list = list(my_tuple)
print(f"Converted list: {my_list}")

converted_tuple = tuple(my_list)
print(f"Converted tuple: {converted_tuple}")