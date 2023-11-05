with open('myfile5.txt', 'w') as f:
    f.write("This is a sample file used for the seek() demonstration.")

# Reading the file
with open('myfile5.txt', 'r') as f:
    print(f.read())  # This will print the entire content of the file

# Reading the file after seek
with open('myfile5.txt', 'r') as f:
    print(f.read(10))  # This will print the first 10 characters of the file
    f.seek(5)  # Move the file pointer to the 6th character (byte) yaha se agar hum read karange to vo 6 character se print karne lagega 5th ko skip marega
    print("you have seeked till the point",f.tell()) 
    print(f.read())  # This will print the content of the file from the 6th character onwards

#--> CREATING A NEW FILE HERE
with open('myfile5.txt2', 'w') as f:
    f.write("HELLO EVERYONE 123456")
    f.truncate(5) # means mere file me kitne character hai mereko nhi malum iske baadh usme sirf 5 he bytes hone chaheye

with open('myfile5.txt2 ', 'r') as f:
    print(f.read()) 