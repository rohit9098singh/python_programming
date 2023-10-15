inventary=[]

def add_item(item):
    inventary.append(item)

def remove_item(item):
    if item in inventary:
        inventary.remove(item)
    else:
        print("elemnt not present in the list")

def display_inventary():
    if not inventary:
        print("List is empty")

    else:
        print("inventary is")
        for i, item in enumerate(inventary, start=1):
            print(f"{i}. {item}")           
    
add_item("Apple")
add_item("Banana")
add_item("Milk")
add_item("Bread")

print("\nInitial Inventory:")
display_inventary()

remove_item("Apple")
remove_item("Banana")
remove_item("Milk")
remove_item("Bread")


print("\nInventory after removal:")
display_inventary()
