from tkinter import *
import tkinter.messagebox as msg


def message():
    print("this is my new message")
    # a = msg.showinfo("Message", "welcome to SB")
    # print(a)
    value = msg.askquestion("Was your Experience good", "Rate us")
    if value == "yes":
        message1 = "great . happy to this this"
    else:
        message1 = "Tell us what went wrong"
    msg.showinfo("experience", message1)


def question():
    ans = msg.askretrycancel("Nisha, can you send me money", "no i can't")
    if ans:
        print("dont retry, its waste")
    else:
        print("Well Done")


root = Tk()
root.title("Message Box")
root.geometry('433x433')
mainMenu = Menu(root)
m1 = Menu(mainMenu, tearoff=0)
m1.add_command(label="Message", command=message)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="Message", menu=m1)

m2 = Menu(mainMenu, tearoff=0)
m2.add_command(label="Rate us", command=message)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="Rate", menu=m2)

m3 = Menu(mainMenu)
m3.add_command(label="Question", command=question)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="Question", menu=m3)
root.mainloop()
