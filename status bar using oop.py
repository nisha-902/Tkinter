from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("544x544")
        self.title("status bar")

    def status(self):
        self.var = StringVar()
        self.var = set("ready")
        self.sbar = Label(self, relief=SUNKEN)
        self.sbar.pack(side=BOTTOM, fill=X)

    def skill(self):
        print("data")

    def createbutton(self, input):
        Button(self, text=input, command=self.skill).pack()


if __name__ == '__main__':
    obj = GUI()
    obj.status()
    obj.createbutton("click me")

    obj.mainloop()
