import turtle

farba1, farba2 = "tomato", "tan"
t = turtle.Turtle()


def kosostvorec(velkost, farba):
    t.fillcolor(farba)
    t.begin_fill()
    for i in range(2):
        t.fd(velkost)
        t.left(45)
        t.fd(velkost)
        t.left(135)
    t.end_fill()


def utvar(velkost):
    global farba1
    global farba2
    for i in range(8):
        kosostvorec(velkost, farba1)
        farba1, farba2 = farba2, farba1
        t.left(45)


utvar(100)


turtle.mainloop()
