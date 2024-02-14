import turtle
import random

t = turtle.Turtle()
t.speed(0)

def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"
def square(dlzka):
    for i in range(4):
        t.left(90)
        t.fd(dlzka)

def vtipne():
    t.setheading(180)
    t.penup()
    t.setposition(-300,-300)
    t.pendown()
    for i in range(55):
        t.fd(5)
        t.right(5)
    t.setheading(90)
    t.fd(200)
    for i in range(18):
        t.fd(10)
        t.right(10)
    t.fd(200)
    t.setheading(90)
    for i in range(55):
        t.fd(5)
        t.right(5)



def sachovnica(size,color1,color2):
    for j in range(1,9):
        for i in range(8):
            t.fillcolor(color1)
            t.begin_fill()
            t.fd(size)
            square(size)
            t.end_fill()
            color2, color1 = color1, color2
        color2 , color1 = color1, color2
        t.penup()
        t.setposition(0 ,j*-size)
        t.pendown()

sachovnica(20,"red","blue")
vtipne()
turtle.mainloop()