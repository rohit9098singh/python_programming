import os
if(not os.path.exists("date")):
 os.mkdir('date')

  
# now i want ke date nam ka folder hai iske andar 1 se leke 100 din tak ka ek alag alag folders ban jae
for i in range(0,5):
    os.mkdir(f"date/day{i+1}") #IT WILL THROUGHA N ERROR BECAUSE DATA DIRECTORY IS ALREDY MADE AND WE ARE TRYING TO MAKE IT AGAIN
                               #TO RESOLVE THIS WE WILL HAVE TO USE A CHECK CONDITON ABOVE...... SEE     

