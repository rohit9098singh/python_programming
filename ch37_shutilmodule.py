import shutil
import os
shutil.copy("ch37_shutilmodule.py","ch37_2shutilmodule.py")
os.remove("ch37_2shutilmodule.py")  # we are using this to delete it because we dont have anything build in shutil module to delete files and folders
shutil.copytree("date","day1,day2")
#shutil.move("date","day1")
shutil.move("day1","day")