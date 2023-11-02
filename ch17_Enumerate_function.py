new_list=['banana','mango','tamarind','oats','apple']
for i,j in enumerate(new_list):
    print(f"the element present at index: {i} is {j}")

print("========using another loop and printing in different way==========")
for i,j in enumerate(new_list,start=1):#end function is not supported in enummerator we will have to explicitly use 
                                       #if to itterate over the list as per our start and end
     if 1 <= i <= 2:
       print(f"the element present at the index: {i} is {j}")    