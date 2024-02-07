# Priklad 17 - Nemecka vlajka
import tkinter as tk
import random

canvas = tk.Canvas(width=600, height=500)
canvas.pack()
resolution = 5000
size = 35000 / resolution

for i in range(resolution):
    y = random.randint(100, 400)
    x = random.randint(100, 500)
    if 200 > y >= 100:
        color = "Black"
    elif 300 > y >= 200:
        color = "Red"
    else:
        color = "Gold"
    canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline="")

canvas.mainloop()
