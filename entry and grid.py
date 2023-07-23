from tkinter import *


def getval():
    print(f"value of username is {userValue.get()}")
    print(f"value of password is {passValue.get()}")


root = Tk()
root.geometry("433x655")
# with pack
# label = Label(root, text="UserName")
# label.pack(side=LEFT, anchor="nw")
# userValue = StringVar()
# userEntry = Entry(root, textvariable=userValue, borderwidth=3, relief=SUNKEN)
# userEntry.pack(side=LEFT, anchor="nw")

# with grid
label = Label(root, text="UserName")
label1 = Label(root, text="Password")
label.grid(row=0)
label1.grid(row=1)

userValue = StringVar()
passValue = StringVar()
userEntry = Entry(root, textvariable=userValue, borderwidth=3, relief=SUNKEN)
userEntry.grid(row=0, column=1)
PassEntry = Entry(root, textvariable=passValue, borderwidth=3, relief=SUNKEN)
PassEntry.grid(row=1, column=1)

button = Button(root, text="Submit", command=getval)
button.grid()
root.mainloop()
