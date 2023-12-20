import tkinter as tk
import random

# settings
canvas_width = 1000
canvas_height = 250
numberOfCircles = 100000
radius = 5
color = ""
canvas = tk.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

for i in range(numberOfCircles):
    x = random.randint(2 + radius, canvas_width - radius-2)
    y = random.randint(2 + radius, canvas_height - radius-2)
    if x < canvas_width // 2 and y >= canvas_height // 2:
        color = "red"
    elif x <= canvas_width // 2 and y < canvas_height // 2:
        color = "green"
    elif x > canvas_width // 2 and y <= canvas_height // 2:
        color = "blue"
    else:
        color = "yellow"
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, width=0)
    canvas.update()
canvas.mainloop()
