import turtle
import random

t = turtle.Turtle()


def bodky(n, m):
    t.pu()
    t.fd(-200)
    t.left(90)
    t.fd(200)
    t.right(90)
    t.pd()
    for j in range(n):
        for i in range(m):
            t.dot(random.randint(20, 35), "salmon")
            t.pu()
            t.fd(30)
            t.pd()
        t.pu()
        t.right(90)
        t.fd(30)
        t.right(90)
        t.fd(m * 30)
        t.left(180)
        t.pd()


bodky(10, 15)

turtle.mainloop()
