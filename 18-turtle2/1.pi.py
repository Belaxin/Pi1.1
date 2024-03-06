import turtle
t = turtle.Turtle()
turtle.delay(0)
def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.lt(90)


def n_Uhlonik(n,dlzka):
    for i in range(n):
        t.fd(dlzka)
        t.lt(360/n)




t.penup()
t.setposition(0,-300)
t.pendown()

for n in range(3,16):
    n_Uhlonik(n,100)
    n+=1


turtle.mainloop()