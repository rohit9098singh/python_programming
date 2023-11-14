from tkinter import *
root=Tk()
root.geometry("300x400")
f1=Frame(root,bg="blue",borderwidth=8,relief=FLAT)#relief=FLAT,relief=RAISED,relief=GROOVE,relief=SOLID
f1.pack(side="left",fill="y",anchor="sw") # fill kya karta hai fill karne me madat karta hai border sab ko
f2=Frame(root,bg="grey",borderwidth=6,relief=SOLID)
f2.pack(side="top",fill="x")
l1=Label(f1,text="python project")
l1.pack(pady=12)  # label ke andar likha hua text ko adjust karne me madat karta hai ye 
l2=Label(f2,text="vs code",font="helvictia 16 bold",fg="green")
l2.pack()

root.mainloop()