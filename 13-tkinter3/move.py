import random
import time
from tkinter import *
canvas = Canvas(height=500,width=1000)
canvas.pack()

square = canvas.create_rectangle(0,0,10,10,fill="hot pink")
canvas.update()

for i in range(490):
    canvas.move(square,2,1) # square je objekt, move ho posunie o 110 a 110 takze x a y je 120
    time.sleep(0.)
    farba = random.choice(("green","red","yellow","purple"))
    canvas.itemconfig(square,fill=farba)
    canvas.after(1,canvas.update())
# canvas.delete(square)

canvas.mainloop()