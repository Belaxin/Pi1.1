import time
import  tkinter as tk

canvas = tk.Canvas(height=600,width=800)
canvas.pack()
x = 400
y = 100
speed =(100 - float(input("enter the speed")))/500

print(speed)
while True:
    ptarmigan = tk.PhotoImage(file='./ptarmigan.gif')
    photo = canvas.create_image(x,y, image = ptarmigan)
    for i in range(400//10):
        time.sleep(speed)
        canvas.move(photo, 0,10 )
        canvas.update()
    for i in range(400//10):
        time.sleep(speed)
        canvas.move(photo, 0 , -10)
        canvas.update()