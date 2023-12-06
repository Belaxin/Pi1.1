from tkinter import  *
import time
import random
canvas = Canvas(width=300,height=600)
canvas.pack()
santa = PhotoImage(file='./santa.png')
santa_object = canvas.create_image(150,100,image = santa)

canvas.mainloop()