from tkinter import *
import random

width = 1000
height = 600
canvas = Canvas(width=width, height=height, bg="forest green")
canvas.pack()
# settings
x = 5
y = 5
d = 15
spacing = 5
xx = x
colors = ["blue", "magenta", "pink", "purple"]
for g in range((height - y) // (d * 2 + spacing)):

    for i in range((width - x) // (d * 2 + spacing)):
        # petals
        color = random.choice(colors)
        canvas.create_oval(x, y, x + 1 * d, y + 1 * d, fill=color)
        canvas.create_oval(x, y + 1 * d, x + 1 * d, y + 2 * d, fill=color)
        canvas.create_oval(x + d, y, x + 2 * d, y + 1 * d, fill=color)
        canvas.create_oval(x + d, y + 1 * d, x + 2 * d, y + 2 * d, fill=color)

        # core
        canvas.create_oval(x + d * 0.5, y + d * 0.5, x + d * 1.5, y + d * 1.5, fill="yellow")

        x = x + d * 2 + spacing
    x = xx
    y = y + d * 2 + spacing
canvas.mainloop()
