from tkinter import *


def skill():
    print("this is a skill function")


root = Tk()
root.geometry("455x544")
root.title("Menu And Submenu")

# non dropdown
# myMenu = Menu(root)
# myMenu.add_command(label="File", command=skill)
# myMenu.add_command(label="exit", command=quit)

# dropdown
mainMenu = Menu(root)
m1 = Menu(mainMenu, tearoff=0)
m1.add_command(label="create", command=skill)
m1.add_command(label="save", command=skill)
m1.add_command(label="save as", command=skill)
m1.add_separator()
m1.add_command(label="print", command=skill)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainMenu, tearoff=0)
m2.add_command(label="cut", command=skill)
m2.add_command(label="copy", command=skill)
m2.add_command(label="paste", command=skill)

root.config(menu=mainMenu)
mainMenu.add_cascade(label="Edit", menu=m2)

# root.config(menu=myMenu)
root.mainloop()
