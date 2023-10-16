inventory = ()

def Add_Element(item):
        global inventory  # Declare inventory as a global variable
        changed_inventory = list(inventory)
        changed_inventory.append(item)
        inventory=tuple(changed_inventory)
         

def Remove_element(item):
    global inventory
    new_inventory = list(inventory)
    if item in new_inventory:
        new_inventory.remove(item)
        inventory = tuple(new_inventory)
        print(f"Removed {item} from the inventory.")
    else:
        print("Item is not present in the inventory.")
product = int(input("Enter the number of elements you want to add to your inventory: "))
for i in range(product):
    to_add = input(f"Enter the product {i+1} to add to your inventory: ")
    Add_Element(to_add)

# Print the current inventory
print("Here are the items that are present in the inventory:")
print(inventory)

# Perform removal from inventory
item_to_remove = input("Enter the item you want to remove from the inventory: ")
Remove_element(item_to_remove)

# Print the updated inventory
print("Here is the updated inventory:")
print(inventory)
