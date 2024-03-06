import turtle
t = turtle.Turtle()
turtle.delay(0)
def n_Uhlonik(n,dlzka):
    for i in range(n//4):
        t.fd(dlzka)
        t.lt(360/n)

def obluk(d):
    for i in range(9):
        t.fd(d)
        t.left(10)

def lupen(d):
    for j in range(2):
            obluk(d)
            t.left(90)
def Kvet(d,pocet):
    for k in range(pocet):
        lupen(d)
        t.left(360/pocet)


Kvet(20,50)

turtle.mainloop()