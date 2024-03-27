import turtle
import random

t = turtle.Turtle()


def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


###################
def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.left(90)


def stvorce(dlzka, krok):
    for i in range(dlzka // krok):
        farba = rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.fillcolor(farba)
        t.begin_fill()
        stvorec(dlzka)
        t.end_fill()
        t.fd(krok // 2)
        t.left(90)
        t.fd(krok // 2)
        t.right(90)
        dlzka -= krok


t.pu()
stvorce(200, 25)

turtle.mainloop()
