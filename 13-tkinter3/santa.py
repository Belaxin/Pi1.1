from tkinter import  *
import time
import random
height= 600
width = 600
posun = 10

canvas = Canvas(width=width,height=height)
canvas.pack()
santa = PhotoImage(file='./santa.png')

santa_y = 66
santa_x = width//2

santa_object = canvas.create_image(santa_x,santa_y,image = santa)
santa_object2 = canvas.create_image(santa_x+128,santa_y,image = santa)
while True:



    for i in range((height-110)//posun):
        canvas.move(santa_object, 0, posun)
        canvas.update()
        time.sleep(0.01)

        canvas.update()
        time.sleep(0.01)
        canvas.move(santa_object2, 0, posun)
        santa_y = santa_y + posun
        print(santa_y)

        if santa_y > height - 50:
            canvas.delete(santa_object2)
            santa_y = 66
            santa_object2 = canvas.create_image(width / 2 + 128, santa_y, image=santa)

    for i in range((height-110)//posun):
        canvas.move(santa_object, 0, -posun)
        canvas.update()
        time.sleep(0.01)

        canvas.update()
        time.sleep(0.01)
        canvas.move(santa_object2, 0, posun)
        santa_y = santa_y + posun
        print(santa_y)

        if santa_y > height - 50:
            canvas.delete(santa_object2)
            santa_y = 66
            santa_object2 = canvas.create_image(width / 2 + 128, santa_y, image=santa)
