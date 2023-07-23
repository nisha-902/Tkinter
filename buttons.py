from tkinter import *


def nisha():
    print("button pressed")


root = Tk()
root.geometry("544x455")
frame = Frame(root, relief=SUNKEN)
frame.pack(side=LEFT, anchor='nw')
button1 = Button(frame, text="press ok", command=nisha)
button1.pack(side=TOP)
button2 = Button(frame, text="press ok", command=nisha)
button2.pack()
button3 = Button(frame, text="press ok", command=nisha)
button3.pack()

root.mainloop()
