digit=0
alphabet=0
space=0
special_character=0

mystring= input("Enter your string: ")
    

for char in mystring: 
 if char.isdigit():
        digit += 1
 elif char.isalpha():
        alphabet += 1
 elif char.isspace():
        space += 1
 else:
    special_character += 1
    
print(f"the enterd array as a follow\n{mystring}")
print(f"the number of alphnabet in the enterd array is\n{alphabet}")
print(f"the number of digit in the enterd array is\n{digit}")
print(f"the number of spaces in the enterd array is\n{space}")
print(f"the number of special_character in the enterd array is\n{special_character}")
