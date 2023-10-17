'''sets are the unordered collection of the data  items ,they also store multiple data items in a single variable,they are separated by a 
comma and enclosed within a curley bracket .
you cannot change the content of the sets once it is created.they do not contain duplicate values inside it '''
# Creating a set 
my_set = {1, 2, 3, 4, 4, 5, 5, 6}

print("Set elements:")
print(my_set)

# Adding elements to the set
my_set.add(7)
my_set.add(8)

# Printing the updated set
print("\nSet after adding elements:")
print(my_set)

# Removing elements from the set
my_set.remove(3)

# Printing the set after removing an element
print("\nSet after removing an element:")
print(my_set)

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
print("\nUnion of sets:")
print(set1 | set2)

# Intersection of sets
print("\nIntersection of sets:")
print(set1 & set2)

# Difference of sets
print("\nDifference of sets:")
print(set1 - set2)

#update method
print("====upadtaing one set with the another one===")
set1.update(set2)
print(set1)

#pop
print("=======performimg the pop operation at here======")
set3=set1.pop()
print(set3)

#del and clear
set2.clear()
print(set2)

#del(set1)

#print(set1)# will raise an erroe bz set 1 is deleted and it no longer exits


#checking of isdisjoint,issuperset,
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
