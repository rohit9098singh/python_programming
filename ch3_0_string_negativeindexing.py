str1=input("enter the string of your choice :")
print("the length of the given string is :",len(str1))

# imagine the enterd string as a length of 5
#using negative indexing :print(str1[0:-2]) is written as same os--->print(str1[0:len(str1)-2]) which will be read as str1[0:3]
print(str1[0:-2])

# if we use one more parameter then it means to jump like str1[0:2:2] means it will print every 2nd elemnet of the string

print(str1[0:-2:2])