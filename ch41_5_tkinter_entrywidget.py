from tkinter import *

root = Tk()
root.geometry("400x300")

def getvalues():
   name.get()
   gender.get()
   location.get()
   payment_mode.get()
   food_service.get()
   #with open("record.txt","w") as f:

Label(root, text="HERE WE GONNA SEE HOW THE CHECKBOX WORKS AT HERE", font=("Helvetica", 16, "bold"), relief=FLAT).grid(row=0, column=1)


l1 = Label(root, text="Name").grid(row=1, column=0)
l2 = Label(root, text="Gender").grid(row=2, column=0)
l3 = Label(root, text="Location").grid(row=3, column=0)
l4 = Label(root, text="Payment Mode").grid(row=4, column=0)

name = StringVar()
gender = StringVar()
location = StringVar()
payment_mode = StringVar()
food_service = IntVar()  # because it is a checkbox whose expected answer will be either 0 or 1

# ENTRY WIDGETS
entry_name = Entry(root, textvariable=name).grid(row=1, column=1)
entry_gender = Entry(root, textvariable=gender).grid(row=2, column=1)
entry_location = Entry(root, textvariable=location).grid(row=3, column=1)
entry_payment_mode = Entry(root, textvariable=payment_mode).grid(row=4, column=1)

# CHECKBOX
food_service_checkbox = Checkbutton(root, text="Food Service", variable=food_service).grid(row=5, column=1)

#creating button 
Button(text="submit_it",command=getvalues).grid(row=6,column=1)

root.mainloop()

