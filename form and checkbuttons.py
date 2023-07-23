from tkinter import *


# creating function for button
def click():
    print(f"{nameValue.get(), phoneValue.get(), paymentModeValue.get(), emergencyValue.get(), foodServiceValue.get()}\n")
    with open("record.txt", "a") as f:
        f.write(f"{nameValue.get(), phoneValue.get(), paymentModeValue.get(), emergencyValue.get(), foodServiceValue.get()}")


root = Tk()
root.geometry("544x455")
root.title("my Gui")


# label for text
label1 = Label(root, text="Name")
label1.grid(row=0)
label2 = Label(root, text="Phone")
label2.grid(row=1)
label3 = Label(root, text="Emergency Contact")
label3.grid(row=2)
label4 = Label(root, text="Payment Mode")
label4.grid(row=3)

# assigning values for variables
nameValue = StringVar()
phoneValue = IntVar()
emergencyValue = IntVar()
paymentModeValue = StringVar()
foodServiceValue = IntVar()

# creating entries
nameEntry = Entry(root, textvariable=nameValue, relief=SUNKEN, borderwidth=3)
phoneEntry = Entry(root, textvariable=phoneValue, relief=SUNKEN, borderwidth=3)
emergencyEntry = Entry(root, textvariable=emergencyValue, relief=SUNKEN, borderwidth=3)
paymentModeEntry = Entry(root, textvariable=paymentModeValue, relief=SUNKEN, borderwidth=3)

# packing entries
nameEntry.grid(row=0, column=2)
phoneEntry.grid(row=1, column=2)
emergencyEntry.grid(row=2, column=2)
paymentModeEntry.grid(row=3, column=2)

# creating check buttons
foodService = Checkbutton(text="do you want food?", variable=foodServiceValue)
foodService.grid(row=5, column=2)

# creating submit button
button = Button(text="click me", command=click)
button.grid(column=2)
root.mainloop()
