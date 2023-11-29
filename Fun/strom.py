from tkinter import *
import random
canvas = Canvas(width=1000,height=800)
canvas.pack()
while True:
    x = random.randint(200,800)
    x2 = random.randint(200,800)
    y = random.randint(400,800)
    canvas.create_line(200,600,800,600,width=20,fill="brown")
    canvas.create_line(x,600,x,y,fill="forest green")
    canvas.update()

