from tkinter import *


def skill():
    statusVar.set("busy")
    statusBar.update()
    import time
    time.sleep(2)
    statusVar.set("ready")


root = Tk()
root.title("Status Bar")
root.geometry("433x344")
statusVar = StringVar()
statusVar.set("ready")
statusBar = Label(root, textvariable=statusVar, relief=SUNKEN, anchor="w")
statusBar.pack(side=BOTTOM, fill=X)

button = Button(root, text="click me", command=skill)
button.pack()
root.mainloop()
