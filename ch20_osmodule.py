import os
print(os.name)         #OUTPUT--->nt thats the name of the windows os.......
#print(dir(os))

#cwd is the current working directory...
print(os.getcwd())  

#this function helps you to chageg the name of the directory means the location...     
os.chdir('\my codes\python')
print(os.getcwd())       

#this will help you to make new file or folder into the directory
os.mkdir('my boring life')

#this will help us to remove the folder that we have made
os.rmdir('my boring life')
