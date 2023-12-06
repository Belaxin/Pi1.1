import time
from tkinter import *
import random
height = 600
width = 1000
canvas = Canvas(width=width,height=height,bg ="forest green")
canvas.pack()
x = 3
y = 3
d = 90
xx =x
pocet = (width-2)//(d+5)
stvrtina = d//4
# // celociselne delenie
# napr 7 // 3 = 2z
for g in range((height-2)//(d+d//2)):
    for i in range(pocet):
            colors =random.choice( ["blue", "red", "purple", "light sea green", "snow4", "pink"])

            canvas.create_rectangle(x,y+d//2,x+1*d,y+1*d+d//2,fill=colors)
            canvas.create_polygon(x,y+d//2,x+d//2,y,x+1*d,y+d//2,fill="crimson",outline="black")
            canvas.create_rectangle(x+stvrtina,y+3*stvrtina,x+stvrtina*3,y+stvrtina*5,fill="sky blue")
            canvas.create_line(x+d//2,y+stvrtina*3,x+d//2,y+stvrtina*5)
            canvas.create_line(x+stvrtina,y+d,x+stvrtina*3,y+d)

            x = x+5+d
    y = y+d+d//2
    x =xx
#   canvas.create_rectangle(x,y+d//2,x+1*d,y+1*d+d//2,fill=colors,outline=colors)
canvas.mainloop()

while True:

    canvas.create_line(random.randint(0,1000),random.randint(0,1000),random.randint(0,1000),random.randint(0,1000))
    if random.randint(1,2)==1:
        x=x+10
    else:
        x=x-10
    if random.randint(1,2)==1:
        y=y+10
    else:
        y=y-10

    if x<0:
        x=100
    if y<0:
        y=100
    myRectangle = canvas.create_rectangle(x,y,x+1*d,y+1*d,fill="light sea green")
    myLine1 =canvas.create_line(x,y,x+1*d,y+1*d)
    myLine2 =canvas.create_line(x+1*d,y,x,y+1*d)
    canvas.update()
    canvas.delete(myRectangle,myLine1,myLine2)