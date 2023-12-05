import time
from tkinter import *

canvas = Canvas(height=800,width=800)
canvas.pack()
x = 400
y = 200
def fall(y):
    return y+100
while True :
    time.sleep(0.5)
    ptarmigan = PhotoImage(file='./ptarmigan.gif')
    photo = canvas.create_image(x,y, image = ptarmigan)
    y = fall(y)
    print(y)
    if y>800:
        y = 0
    canvas.update()

