import time
from tkinter import *
import random

# These are the window settings
width = 1000
height = 500
canvas = Canvas(width=width, height=height, bg="orchid", cursor="circle")
canvas.pack()

# these are the settings
x = 4
y = 4
d = 10
xx = x
yy = y
colors = ["blue", "pink", "red", "purple", "green", "brown", "yellow"]

while True:
    color = random.choice(colors)
    print(color)
    for i in range(height // (d * 11)):
        for g in range(width // (d * 31)):
            canvas.update()
            # Pismeno T
            canvas.create_rectangle(x, y, x + d, y + d, outline=color, fill="black")
            canvas.create_rectangle(x + d, y, x + 2 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 2 * d, y, x + 3 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 3 * d, y, x + 4 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 4 * d, y, x + 5 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 4 * d, y, x + 5 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 2 * d, y + 1 * d, x + 3 * d, y + 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 2 * d, y + 2 * d, x + 3 * d, y + 3 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 2 * d, y + 3 * d, x + 3 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 2 * d, y + 4 * d, x + 3 * d, y + 5 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 2 * d, y + 5 * d, x + 3 * d, y + 6 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 2 * d, y + 6 * d, x + 3 * d, y + 7 * d, outline=color, fill="black")

            # Pismeno O
            canvas.create_rectangle(x + 6 * d, y + 5 * d, x + 7 * d, y + 6 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 6 * d, y + 4 * d, x + 7 * d, y + 5 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 6 * d, y + 3 * d, x + 7 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 6 * d, y + 2 * d, x + 7 * d, y + 3 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 6 * d, y + 1 * d, x + 7 * d, y + 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 10 * d, y + 5 * d, x + 11 * d, y + 6 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 10 * d, y + 4 * d, x + 11 * d, y + 5 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 10 * d, y + 3 * d, x + 11 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 10 * d, y + 2 * d, x + 11 * d, y + 3 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 10 * d, y + 1 * d, x + 11 * d, y + 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 7 * d, y, x + 8 * d, y + d, outline=color, fill="black")
            canvas.create_rectangle(x + 8 * d, y, x + 9 * d, y + d, outline=color, fill="black")
            canvas.create_rectangle(x + 9 * d, y, x + 10 * d, y + d, outline=color, fill="black")
            canvas.create_rectangle(x + 7 * d, y + 6 * d, x + 8 * d, y + 7 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 8 * d, y + 6 * d, x + 9 * d, y + 7 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 9 * d, y + 6 * d, x + 10 * d, y + 7 * d, outline=color, fill="black")

            # pismeno M
            canvas.create_rectangle(x + 12 * d, y + 6 * d, x + 13 * d, y + 7 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 12 * d, y + 5 * d, x + 13 * d, y + 6 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 12 * d, y + 4 * d, x + 13 * d, y + 5 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 12 * d, y + 3 * d, x + 13 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 12 * d, y + 2 * d, x + 13 * d, y + 3 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 12 * d, y + 1 * d, x + 13 * d, y + 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 12 * d, y + 0 * d, x + 13 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 13 * d, y + 1 * d, x + 14 * d, y + 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 14 * d, y + 2 * d, x + 15 * d, y + 3 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 14 * d, y + 3 * d, x + 15 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 15 * d, y + 1 * d, x + 16 * d, y + 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 16 * d, y + 6 * d, x + 17 * d, y + 7 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 16 * d, y + 5 * d, x + 17 * d, y + 6 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 16 * d, y + 4 * d, x + 17 * d, y + 5 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 16 * d, y + 3 * d, x + 17 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 16 * d, y + 2 * d, x + 17 * d, y + 3 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 16 * d, y + 1 * d, x + 17 * d, y + 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 16 * d, y + 0 * d, x + 17 * d, y + 1 * d, outline=color, fill="black")

            # pismeno A
            canvas.create_rectangle(x + 18 * d, y + 6 * d, x + 19 * d, y + 7 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 18 * d, y + 5 * d, x + 19 * d, y + 6 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 18 * d, y + 4 * d, x + 19 * d, y + 5 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 18 * d, y + 3 * d, x + 19 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 18 * d, y + 2 * d, x + 19 * d, y + 3 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 18 * d, y + 1 * d, x + 19 * d, y + 2 * d, outline=color, fill="black")

            canvas.create_rectangle(x + 19 * d, y + 0 * d, x + 20 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 20 * d, y + 0 * d, x + 21 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 21 * d, y + 0 * d, x + 22 * d, y + 1 * d, outline=color, fill="black")

            canvas.create_rectangle(x + 22 * d, y + 6 * d, x + 23 * d, y + 7 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 22 * d, y + 5 * d, x + 23 * d, y + 6 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 22 * d, y + 4 * d, x + 23 * d, y + 5 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 22 * d, y + 3 * d, x + 23 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 22 * d, y + 2 * d, x + 23 * d, y + 3 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 22 * d, y + 1 * d, x + 23 * d, y + 2 * d, outline=color, fill="black")

            canvas.create_rectangle(x + 19 * d, y + 3 * d, x + 20 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 20 * d, y + 3 * d, x + 21 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 21 * d, y + 3 * d, x + 22 * d, y + 4 * d, outline=color, fill="black")

            canvas.create_rectangle(x + 20 * d, y - 1 * d, x + 21 * d, y - 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 21 * d, y - 2 * d, x + 22 * d, y - 3 * d, outline=color, fill="black")

            # pismeno S
            canvas.create_rectangle(x + 24 * d, y + 1 * d, x + 25 * d, y + 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 24 * d, y + 2 * d, x + 25 * d, y + 3 * d, outline=color, fill="black")

            canvas.create_rectangle(x + 28 * d, y + 4 * d, x + 29 * d, y + 5 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 28 * d, y + 5 * d, x + 29 * d, y + 6 * d, outline=color, fill="black")

            canvas.create_rectangle(x + 25 * d, y + 0 * d, x + 26 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 26 * d, y + 0 * d, x + 27 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 27 * d, y + 0 * d, x + 28 * d, y + 1 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 28 * d, y + 0 * d, x + 29 * d, y + 1 * d, outline=color, fill="black")

            canvas.create_rectangle(x + 25 * d, y + 3 * d, x + 26 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 26 * d, y + 3 * d, x + 27 * d, y + 4 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 27 * d, y + 3 * d, x + 28 * d, y + 4 * d, outline=color, fill="black")

            canvas.create_rectangle(x + 24 * d, y + 6 * d, x + 25 * d, y + 7 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 25 * d, y + 6 * d, x + 26 * d, y + 7 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 26 * d, y + 6 * d, x + 27 * d, y + 7 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 27 * d, y + 6 * d, x + 28 * d, y + 7 * d, outline=color, fill="black")

            canvas.create_rectangle(x + 26 * d, y - 1 * d, x + 27 * d, y - 2 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 27 * d, y - 2 * d, x + 28 * d, y - 3 * d, outline=color, fill="black")
            canvas.create_rectangle(x + 25 * d, y - 2 * d, x + 26 * d, y - 3 * d, outline=color, fill="black")
            # this makes the origin point go over one name and leave a space. I.e. 28*d is the length of a name and 2
            # is the space
            x = x + d * 31

        # this makes the origin point go down one line
        y = y + d * 11
        # this makes the origin point go back into the original x
        x = xx
    y = yy
