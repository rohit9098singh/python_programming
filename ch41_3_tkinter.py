from tkinter import *
root=Tk()
root.geometry("355x432")
def func():
    print("hello everyone this a function which will be called when the button will be clicked")
    a=int(input("enter a number of your choice to find the square of it :"))
    print("the square of the entered number is as follow",a*a)

frame=Frame(root,borderwidth=6,bg="grey",relief=SOLID)
frame.pack(side=LEFT,anchor="nw")
b1=Button(frame,fg="black",text="clickMe") # fg=foreground
b1.pack(side="left",padx=10)
b2=Button(frame,fg="black",text="clickMe",command=func) #command function basically takes the function name onlt and execute it whenever the button is cliced
b2.pack(side="left",padx=10)
b3=Button(frame,fg="black",text="clickMe") 
b3.pack(side="left",padx=10)
b4=Button(frame,fg="black",text="clickMe") 
b4.pack(side="left",padx=10)
b5=Button(frame,fg="black",text="clickMe") 
b5.pack(side="left",padx=10)
root.mainloop()