
my_dict = {}


my_dict["name"] = "John Doe"
my_dict["age"] = 30
my_dict["job"] = "Engineer"


print("Initial Dictionary:")
print(my_dict)

print("\nAccessing Elements:")
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict.get('age')}")


print("\nChecking Key Existence:")
if "age" in my_dict:
    print("Age key exists in the dictionary.")


print("\nModifying Elements:")
my_dict["age"] = 31
print("Modified Dictionary:")
print(my_dict)


print("\nRemoving Elements:")
removed_item = my_dict.pop("job")
print(f"Removed Item: {removed_item}")
print("Updated Dictionary:")
print(my_dict)

print("=====================================")
print("\nDictionary Keys, Values, and Items:")
print(f"Keys: {my_dict.keys()}")
print(f"Values: {my_dict.values()}")
print(f"Items: {my_dict.items()}")

new_dict = {"location": "New York", "education": "Masters"}
my_dict.update(new_dict)
print("\nMerged Dictionary:")
print(my_dict)

# Clearing the dictionary
my_dict.clear()
print("\nCleared Dictionary:")
print(my_dict)
