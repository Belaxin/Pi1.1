from tkinter import *

canvas = Canvas(height=400,width=800)
canvas.pack()

ptarmigan = PhotoImage(file='./ptarmigan.gif')
canvas.create_image(400,200, image = ptarmigan)
canvas.mainloop()