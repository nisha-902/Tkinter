from tkinter import *
import tkinter.messagebox as msg


def skill():
    print(f"order Received")
    msg.showinfo("Developer info", f"i am a {var.get()}")


root = Tk()
root.geometry("344x344")
var = StringVar()
var.set("radio")
label = Label(root, text="Which Developer you are?", font="lucia 19 bold", justify=LEFT)
radio = Radiobutton(root, text="Python Developer", variable=var, value="Python Developer")
radio1 = Radiobutton(root, text="Java Developer", variable=var, value="Java Developer")
radio2 = Radiobutton(root, text="Angular Developer", variable=var, value="Angular Developer")
radio3 = Radiobutton(root, text="PHP Developer", variable=var, value="PHP Developer")
button = Button(root, text="click me", command=skill)
label.pack()
radio.pack(anchor="w")
radio1.pack(anchor="w")
radio2.pack(anchor="w")
radio3.pack(anchor="w")
button.pack()
root.mainloop()
