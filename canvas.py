from tkinter import *
root = Tk()
height = 544
width = 655
root.geometry(f"{width}x{height}")
root.title("Canvas_widget")
canvas = Canvas(root, width=width, height=height, bg="black")
canvas.pack(anchor="nw")
canvas.create_line(0, 0, 655, 544, fill="white")
canvas.create_line(0, 544, 655, 0, fill="white")
canvas.create_rectangle(20, 100, 600, 500, fill="white")
canvas.create_text(320, 270, text="nisha", fill="red")
canvas.create_oval(344, 200, 300, 350)

root.mainloop()
