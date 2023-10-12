n=input("enter the size of an array :")
try:
 my_array=int(n)
except ValueError as e:
  print(e)
  print("you have entered an wrong datatype value please enter a correct value" )
  exit(1)

hold=[]
for i in range(my_array):
  no=input(f"enter the value at index :{i+1} :")
  hold.append(no)
    
print("----------your enterd array is as follow---------")
print("the array is :",hold)

print("printing the array in a reverse order.........")
for i in range(my_array - 1, -1, -1):
    print(hold[i])
    
#OR WE CAN ALSO USE THIS METHOD TO ITTERATE THE LOOP 
#print("array element in reverse order is as follow :")
#for i in  reversed(hold):
  #print(i)    