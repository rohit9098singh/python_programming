import os
# TO KNOW HOW MANY FOLDERS DO WE HAVE IN THE DATE FOLDERS
folders=os.listdir("date")   
print(folders) 
for folder in folders:
    print(os.listdir(f"date/{folder}"))
'''try:
    with open('date{subfolder.md', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the path and file name.")
except Exception as e:
    print(f"An error occurred: {e}")'''