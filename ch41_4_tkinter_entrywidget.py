from tkinter import *

def getvalue():
    print(f"the value of the username is {username.get()}")
    print(f"the value of the password is {password.get()}")

def toggle_password():
    if show_password_var.get():
        pass_entry.config(show="")
    else:
        pass_entry.config(show="*")

root = Tk()
root.geometry("300x400")

username = StringVar()
password = StringVar()

username_label = Label(root, text="username")
password_label = Label(root, text="password")
username_label.grid()
password_label.grid(row=1)

user_entry = Entry(root, textvariable=username)
user_entry.grid(row=0, column=1)
pass_entry = Entry(root, textvariable=password, show="*")  
pass_entry.grid(row=1, column=1)

# Checkbutton to toggle password visibility
show_password_var = IntVar()
show_password_check = Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_check.grid(row=2, column=1)

Button(root, text="Submit", command=getvalue).grid()

root.mainloop()



#SUPPOSE IF I WANT TO PLACE THE ROW AT PASSWORD AT THE NINETH ROW WE CANNOT PLACE IT DIRECTLY WE WILL HAVE TO MAKE A DUMMY ROWS TO FILL THE REST AREA THEN 
#ONLY WE CAN INSERT  IT EXAMPLE GIVEN BELOW 
'''# Place a dummy widget (empty label) in previous rows to create them
for i in range(9):
    Label(root, text="").grid(row=i, column=0)

# Place the password label in row 9
password.grid(row=9)
'''
#variable class in tkinter is BooleanVar,DoubleVar,ntVar,StringVar