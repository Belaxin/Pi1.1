from tkinter import  *
import time
import random
height= 600
width = 600
posun = 10

canvas = Canvas(width=width,height=height)
canvas.pack()
santa = PhotoImage(file='./santa.png')

santa_y = 64
santa_y2 = height-64
santa_x = width//2

santa_object = canvas.create_image(santa_x,santa_y,image = santa)
santa_object2 = canvas.create_image(santa_x+128,santa_y,image = santa)
santa_object3 = canvas.create_image(width / 2 - 128, santa_y2, image=santa)
while True:



    for i in range((height-110)//posun):
        # jump santa
        canvas.move(santa_object, 0, posun)
        canvas.update()
        time.sleep(0.01)
        # teleport santa
        canvas.update()
        time.sleep(0.01)
        canvas.move(santa_object2, 0, posun)
        santa_y = santa_y + posun
        print(santa_y)

        if santa_y > height - 64:
            canvas.delete(santa_object2)
            santa_y = 64
            santa_object2 = canvas.create_image(width / 2 + 128, santa_y, image=santa)

        # teleport reverse
        canvas.update()
        time.sleep(0.01)
        canvas.move(santa_object3, 0, -posun)
        santa_y2 = santa_y2 - posun
        print(f"santa je na {santa_y2}")

        if santa_y2 < 64:
           canvas.delete(santa_object3)
           santa_y2 = height - 50
           santa_object3 = canvas.create_image(width / 2 - 128, santa_y2, image=santa)

    for i in range((height-110)//posun):
        #jump santa
        canvas.move(santa_object, 0, -posun)
        canvas.update()
        time.sleep(0.01)
        # teleport santa
        canvas.update()
        time.sleep(0.01)
        canvas.move(santa_object2, 0, posun)
        santa_y = santa_y + posun
        print(santa_y)

        if santa_y > height - 64:
            canvas.delete(santa_object2)
            santa_y = 64
            santa_object2 = canvas.create_image(width / 2 + 128, santa_y, image=santa)

        # teleport reverse
        canvas.update()
        time.sleep(0.01)
        canvas.move(santa_object3, 0, -posun)
        santa_y2 = santa_y2 - posun
        print(f"santa je na {santa_y2}")

        if santa_y2 < 64:
            canvas.delete(santa_object3)
            santa_y2 = height - 50
            santa_object3 = canvas.create_image(width / 2 - 128, santa_y2, image=santa)