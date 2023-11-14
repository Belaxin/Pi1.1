import time
from tkinter import *
import random

canvas = Canvas(width=375, height=150, bg="orchid", cursor="circle")
canvas.pack()

x = 40
y = 40
d = 10
colors = ["blue", "pink", "red", "purple", "green", "brown", "yellow"]

while True:
    time.sleep(0.5)
    canvas.update()
    # Pismeno T
    canvas.create_rectangle(x, y, x + d, y + d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + d, y, x + 2 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 2 * d, y, x + 3 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 3 * d, y, x + 4 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 4 * d, y, x + 5 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 4 * d, y, x + 5 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 2 * d, y + 1 * d, x + 3 * d, y + 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 2 * d, y + 2 * d, x + 3 * d, y + 3 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 2 * d, y + 3 * d, x + 3 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 2 * d, y + 4 * d, x + 3 * d, y + 5 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 2 * d, y + 5 * d, x + 3 * d, y + 6 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 2 * d, y + 6 * d, x + 3 * d, y + 7 * d, outline=random.choice(colors), fill="black")

    # Pismeno O
    canvas.create_rectangle(x + 6 * d, y + 5 * d, x + 7 * d, y + 6 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 6 * d, y + 4 * d, x + 7 * d, y + 5 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 6 * d, y + 3 * d, x + 7 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 6 * d, y + 2 * d, x + 7 * d, y + 3 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 6 * d, y + 1 * d, x + 7 * d, y + 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 10 * d, y + 5 * d, x + 11 * d, y + 6 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 10 * d, y + 4 * d, x + 11 * d, y + 5 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 10 * d, y + 3 * d, x + 11 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 10 * d, y + 2 * d, x + 11 * d, y + 3 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 10 * d, y + 1 * d, x + 11 * d, y + 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 7 * d, y, x + 8 * d, y + d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 8 * d, y, x + 9 * d, y + d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 9 * d, y, x + 10 * d, y + d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 7 * d, y + 6 * d, x + 8 * d, y + 7 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 8 * d, y + 6 * d, x + 9 * d, y + 7 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 9 * d, y + 6 * d, x + 10 * d, y + 7 * d, outline=random.choice(colors), fill="black")

    # pismeno M
    canvas.create_rectangle(x + 12 * d, y + 6 * d, x + 13 * d, y + 7 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 12 * d, y + 5 * d, x + 13 * d, y + 6 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 12 * d, y + 4 * d, x + 13 * d, y + 5 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 12 * d, y + 3 * d, x + 13 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 12 * d, y + 2 * d, x + 13 * d, y + 3 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 12 * d, y + 1 * d, x + 13 * d, y + 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 12 * d, y + 0 * d, x + 13 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 13 * d, y + 1 * d, x + 14 * d, y + 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 14 * d, y + 2 * d, x + 15 * d, y + 3 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 14 * d, y + 3 * d, x + 15 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 15 * d, y + 1 * d, x + 16 * d, y + 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 16 * d, y + 6 * d, x + 17 * d, y + 7 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 16 * d, y + 5 * d, x + 17 * d, y + 6 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 16 * d, y + 4 * d, x + 17 * d, y + 5 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 16 * d, y + 3 * d, x + 17 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 16 * d, y + 2 * d, x + 17 * d, y + 3 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 16 * d, y + 1 * d, x + 17 * d, y + 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 16 * d, y + 0 * d, x + 17 * d, y + 1 * d, outline=random.choice(colors), fill="black")

    # pismeno A
    canvas.create_rectangle(x + 18 * d, y + 6 * d, x + 19 * d, y + 7 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 18 * d, y + 5 * d, x + 19 * d, y + 6 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 18 * d, y + 4 * d, x + 19 * d, y + 5 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 18 * d, y + 3 * d, x + 19 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 18 * d, y + 2 * d, x + 19 * d, y + 3 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 18 * d, y + 1 * d, x + 19 * d, y + 2 * d, outline=random.choice(colors), fill="black")

    canvas.create_rectangle(x + 19 * d, y + 0 * d, x + 20 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 20 * d, y + 0 * d, x + 21 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 21 * d, y + 0 * d, x + 22 * d, y + 1 * d, outline=random.choice(colors), fill="black")

    canvas.create_rectangle(x + 22 * d, y + 6 * d, x + 23 * d, y + 7 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 22 * d, y + 5 * d, x + 23 * d, y + 6 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 22 * d, y + 4 * d, x + 23 * d, y + 5 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 22 * d, y + 3 * d, x + 23 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 22 * d, y + 2 * d, x + 23 * d, y + 3 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 22 * d, y + 1 * d, x + 23 * d, y + 2 * d, outline=random.choice(colors), fill="black")

    canvas.create_rectangle(x + 19 * d, y + 3 * d, x + 20 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 20 * d, y + 3 * d, x + 21 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 21 * d, y + 3 * d, x + 22 * d, y + 4 * d, outline=random.choice(colors), fill="black")

    canvas.create_rectangle(x + 20 * d, y - 1 * d, x + 21 * d, y - 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 21 * d, y - 2 * d, x + 22 * d, y - 3 * d, outline=random.choice(colors), fill="black")

    # pismeno S
    canvas.create_rectangle(x + 24 * d, y + 1 * d, x + 25 * d, y + 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 24 * d, y + 2 * d, x + 25 * d, y + 3 * d, outline=random.choice(colors), fill="black")

    canvas.create_rectangle(x + 28 * d, y + 4 * d, x + 29 * d, y + 5 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 28 * d, y + 5 * d, x + 29 * d, y + 6 * d, outline=random.choice(colors), fill="black")

    canvas.create_rectangle(x + 25 * d, y + 0 * d, x + 26 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 26 * d, y + 0 * d, x + 27 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 27 * d, y + 0 * d, x + 28 * d, y + 1 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 28 * d, y + 0 * d, x + 29 * d, y + 1 * d, outline=random.choice(colors), fill="black")

    canvas.create_rectangle(x + 25 * d, y + 3 * d, x + 26 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 26 * d, y + 3 * d, x + 27 * d, y + 4 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 27 * d, y + 3 * d, x + 28 * d, y + 4 * d, outline=random.choice(colors), fill="black")

    canvas.create_rectangle(x + 24 * d, y + 6 * d, x + 25 * d, y + 7 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 25 * d, y + 6 * d, x + 26 * d, y + 7 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 26 * d, y + 6 * d, x + 27 * d, y + 7 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 27 * d, y + 6 * d, x + 28 * d, y + 7 * d, outline=random.choice(colors), fill="black")

    canvas.create_rectangle(x + 26 * d, y - 1 * d, x + 27 * d, y - 2 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 27 * d, y - 2 * d, x + 28 * d, y - 3 * d, outline=random.choice(colors), fill="black")
    canvas.create_rectangle(x + 25 * d, y - 2 * d, x + 26 * d, y - 3 * d, outline=random.choice(colors), fill="black")
