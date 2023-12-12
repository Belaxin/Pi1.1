from tkinter import *
import random

canvas = Canvas(width=1000,height=500)
canvas.pack()
while True:
    x = random.randint(0, 1000)
    y = random.randint(0, 500)
    canvas.create_line(0, 0, x, y)
    canvas.create_line(1000, 0, x, y)
    canvas.create_line(1000, 500, x, y)
    canvas.create_line(0, 500, x, y)
    canvas.update()
zz
canvas.mainloop()