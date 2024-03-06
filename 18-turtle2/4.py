import turtle
turtle.delay(0)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

t2.penup()
t2.setposition(100,0)
t2.pendown()

t1.penup()
t1.setposition(-100,0)
t1.pendown()

t3.penup()
t3.setposition(0,-100)
t3.pendown()

t4.penup()
t4.setposition(0,100)
t4.pendown()


fractionNum = 8
for j in range(fractionNum+1):
    t1.left(360//fractionNum)
    t2.left(360//fractionNum)
    t3.left(360//fractionNum)
    t4.left(360//fractionNum)
    t5.left(360//fractionNum)
    for i in range(4):
        t1.fd(50)
        t2.fd(50)
        t3.fd(50)
        t4.fd(50)
        t5.fd(175)
        t1.left(90)
        t2.left(90)
        t3.left(90)
        t4.left(90)
        t5.left(90)

turtle.mainloop()