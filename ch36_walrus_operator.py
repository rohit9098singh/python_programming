#NORMAL METHOD WITHOUT USING WALRUS OPERARTOR
'''foods =list()
while true:
    food=input("enter the name of the food that you want to enter at here........")
    foods.append(food)
print(foods)    '''

#WALRUS METHOD TO DO THE SAME ABOVE PROGRAMME
foods=list()  #creating a list with the list constructor
while(food := input("what food do you like :")) != "quit":
    foods.append(food)
print(foods)

