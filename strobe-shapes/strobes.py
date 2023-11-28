from tkinter import *
import random


canvas = Canvas( width=1000, height=1000)
canvas.pack()
colors = ["green","blue","pink","cyan","black","white","magenta","orange"]
while True:
    canvas.create_arc(random.randint(0,1000),random.randint(0,1000),random.randint(0,1000),random.randint(0,1000),fill=color,start=random.randint(1,360),extent=random.randint(1,360))
    canvas.update()

canvas.mainloop()

