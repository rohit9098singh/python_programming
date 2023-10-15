def personal_details(name='rohit',age=20,location='unknown'):
    print(f"NAME :{name}\nAGE :{age}\nLOCATION :{location}")

print("example 1")
personal_details('ram',12,'banglore')
print()

print("example 2")
personal_details('',12,'jharkhand')
print()

print("example 3")
personal_details()

# THEREFORE THE DEFAULT ARGUMENT BASICALLY SAYS THAT IF WE PROVIDE A PARAMETER IN FUNCTION THEN IT IS OK ITS PRIORITY WILL BE
#HIGHER BUT IF WE DONT PROVIDE ANY PARAMETER THAN IT WILL TAKE THE INPUT FROM THE DECLARATION PART IF WE HAVE PROVIDED THERE
# AND IF IN THE DECALRATION PART ALSO IF WE DONT PROVIDE THEN PART REMAINS BLANK FOR THEN ARGUMENT IN THE OUTPUT

#NOTE--->that if your are ommiting the first argument during the function call then it is compulsory to pass the rest  of the 
#element with the tag