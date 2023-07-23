
from tkinter import *
from PIL import Image, ImageTk
import os
root = Tk()
root.geometry("600x500")
photo1 = PhotoImage(file="shinchan.png")
image = Image.open("fl.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label3 = Label(image=photo1)
label3.pack()
label.pack()
dirs = os.listdir()
label2 = Label(text=dirs)
label2.pack()
root.mainloop()
