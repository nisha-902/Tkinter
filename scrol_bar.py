from tkinter import *
root = Tk()
root.title("Scroll Bar")
root.geometry("433x324")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# list box
# lb = Listbox(root, yscrollcommand=scrollbar.set)
# lb.pack(fill="both", padx=22)
# for i in range(500):
#     lb.insert(END, f"item{i}")
# scrollbar.config(command=lb.yview)

# String
lb = Listbox(root)
lb.pack(fill=BOTH)
text = Text(lb, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)
root.mainloop()
