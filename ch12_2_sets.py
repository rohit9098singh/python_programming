cities={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","mumbai","inida","delhi"}

print("doing union operation")
print(cities|cities2)
cities3=cities.union(cities2)
print(cities3)

print()
print("==============doing intersection operation================")
print(cities&cities2)
cities3=cities.intersection(cities2)

print()
print("=============update operation=============================")
cities.update(cities2)
print(cities)

print()
print("===============performing symetric_difference and symetricdiffence update=============")
# dono me same same jo hai usko eleminate kar ke do rest of the element in both the sets ho usko print karedga
'''set_A = {1, 2, 3, 4, 5}
set_B = {3, 4, 5, 6, 7}

sym_diff = set_A ^ set_B
print(sym_diff)  # Output: {1, 2, 6, 7}'''
cities3=cities^cities2
print(cities3)
cities3=cities.symmetric_difference(cities2)
print(cities3)
cities.symmetric_difference_update(cities2)
print(cities)

print()
print("==================difference and difference update==========================")
#element which is present in set 1 but not in set 2
'''set_A = {1, 2, 3, 4, 5}
set_B = {3, 4, 5, 6, 7}

diff = set_A - set_B
print(diff)  # Output: {1, 2}
'''
cities3=cities-cities2
print(cities3)
cities3=cities.difference(cities2)
print(cities3)
cities.difference_update(cities2)
print(cities)


