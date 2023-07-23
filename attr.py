from tkinter import *
root = Tk()
root.geometry("444x344")
root.title("nisha's GUI")
label = Label(text="i am am nisha\n"
                   "and ite my birthday\n"
                   "lets celebrate and dance!\n", bg="green", fg="white", padx=40, pady=40, font="TimesNewRoman 9 bold",
              borderwidth=4, relief=SUNKEN)

label.pack(side=LEFT, fill=Y, padx=34, pady=34)
root.mainloop()
