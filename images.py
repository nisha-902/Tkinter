from tkinter import *
from PIL import Image, ImageTk
nisha_root = Tk()
nisha_root.geometry("800x500")
# pic = PhotoImage(file="shinchan.png")
image = Image.open("fl.jpg")
pic = ImageTk.PhotoImage(image)
skill_label = Label(image=pic)
skill_label.pack()
nisha_root.mainloop()
