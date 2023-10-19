#OPENING FILE IN READING MODE 
f=open('myfile1.txt','r')#f=open('myfile.txt') even if a write like this then also it works because defaultl mode is read only
text=f.read()
print(text)
f.close()

#OPENING FILE IN WRITING MODE
f=open('myfile1.txt2','w')
f.write("hello and welcome to my codding platflorm this is vs code")
f.close()

#OPENING FILE IN BINARY MODE
f=open('myfile1.txt','rb')#opens file in binary form only and used to open pdf,images,videos,jpj files etc
text3=f.read()
print(text3)

#APPEND MODE 
f=open('myfile1.txt2','a')
f.write("\nhello and welcome to my codding platflorm this is vs code")
f.close()

#  THERE IS ANOTHER METHOD TO USE THE FILE IO AND IF WE USE ALL THAT THEN WE DONT HAVE TO USE THE CLOSE STATEMENT
#  AND THAT IS A WITH STATEMENT

with open('myfile1.txt2','a') as f:
    f.write("are u making use of me is yes please tell me dont do  that.........")

# readline()    