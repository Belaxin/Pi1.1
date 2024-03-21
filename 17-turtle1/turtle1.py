import turtle
import random

t = turtle.Turtle()
t.speed(0)

def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"
def square(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.left(90)

for i in range(36):
    t.seth(random.randint(0,359))
    t.penup()
    t.fillcolor(rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    t.setposition(random.randint(-200,200),random.randint(-200,200))
    t.pendown()
    t.begin_fill()
    square(30)
    t.end_fill()



turtle.mainloop()