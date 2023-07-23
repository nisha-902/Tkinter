from tkinter import *
import tkinter.messagebox as msg


def getdollar():
    print(f"{slider1.get()} amount is credited")
    msg.showinfo("amount credited", f"{slider1.get()} amount is credited")


root = Tk()
root.geometry("433x433")
root.title("slider")

# slider = Scale(root, from_=0, to=100)
# slider.pack()
label = Label(root, text="how many dollar you want?")
label.pack()

slider1 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
slider1.pack()
slider1.set(23)

button = Button(root, text="Get Dollar", command=getdollar)
button.pack()

root.mainloop()
