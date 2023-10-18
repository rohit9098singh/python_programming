#here we are renaming the folders that we have created in the previous program
import os
import os
for i in range(0,5):
    os.rename(f"date/tutorial{i+1}",f"date/tutorial {i+1}") #there should source,destination

'''import os

# Renaming the folders
for i in range(0, 5):
    source = f"date/day{i+1}"
    destination = f"date/tutorial{i+1}"
    if os.path.exists(source):
        os.rename(source, destination)
    else:
        print(f"The source directory {source} does not exist.")

# Listing the folders in the 'date' directory
folders = os.listdir("date")
print(folders)
'''
