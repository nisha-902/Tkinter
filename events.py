from tkinter import *


def nisha(event):
    print(f"you clicked on the button at {event.x},{event.y}")


root = Tk()
root.geometry("500x500")
root.title("events")
myEvent = Button(root, text="click me")
myEvent.pack()
myEvent.bind('<Button-1>', nisha)
myEvent.bind('<Double-1>', quit)
root.mainloop()
