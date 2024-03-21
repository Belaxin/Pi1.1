# Priklad 10 - Random Color kruhy
import tkinter as tk
import random

Width = 1000
Height = 800
canvas = tk.Canvas(width=Width, height=Height)
canvas.pack()


def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


amount = 20
layers = 10
size = 50
spacing = 5

for i in range(amount):
    x = random.randint(100, Width - 100)
    y = random.randint(100, Height - 100)
    for g in range(layers):
        canvas.create_oval(x - size, y - size, x + size, y + size,
                           fill=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        size -= spacing
    size = 50
canvas.mainloop()
