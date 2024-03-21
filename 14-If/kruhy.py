import tkinter as tk
import random

width = 600
height = 400
canvas = tk.Canvas(width=width, height=height)
canvas.pack()
radius = 10
spacing = radius + radius // 2
x = spacing + radius
y = spacing + radius
xx = x

color = ""
for i in range(height // (spacing + 2 * radius)):   # stlpce
    if y == height // 2:
        color = "red"
    for g in range(width // (2*radius)): # riadky
        if x == width//2:
            color = "red"
            print("true")
        else:
            color = "white"
        canvas.create_oval(x-radius,y-radius,x+radius,y+radius,fill=color)
        x += radius + spacing

    y += radius+spacing
    x = xx
canvas.mainloop()
