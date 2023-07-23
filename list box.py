from tkinter import *


def add():
    global i
    print(f"{i}")
    lb.insert(ACTIVE, f"{i}")
    i = i+1


i = 0
root = Tk()
root.title("list box")
root.geometry("433x433")

lb = Listbox(root)
lb.pack()
lb.insert(END, "Welcome to SkillBout")

button = Button(root, text="add data", command=add)
button.pack()
root.mainloop()
