

from tkinter import *
from PIL import Image,ImageTk
root = Tk()

root.minsize(768,455)
Heading = Label(text = "My New Album..")
Heading.pack()
image = Image.open("PHOTO1.JPG")
image1 = Image.open("PHOTO2.jpg")
image2 = Image.open("Photo3.jpg")
image3 = Image.open("Photo5.jpg")
image4 = Image.open("Phto4.jpg")

photo = ImageTk.PhotoImage(image)
photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)
photo3 = ImageTk.PhotoImage(image3)
photo4 = ImageTk.PhotoImage(image4)

image_label = Label(image = photo)
image_label1 = Label(image = photo1)
image_label2 = Label(image = photo2)
image_label3 = Label(image = photo3)
image_label4 = Label(image = photo4)

image_label.pack()
image_label1.pack()
image_label2.pack()
image_label3.pack()
image_label4.pack()

root.mainloop()