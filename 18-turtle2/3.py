import turtle
import random
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
def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def Kvet(d,pocet,r,g,b):
    for k in range(pocet):
        t.pencolor("Black")
        t.fillcolor(rgb(r,g,b))
        t.begin_fill()
        lupen(d)
        t.end_fill()
        t.left(360/pocet)
        if rCan == True:
            r-=255//pocet
        if gCan == True:
            g-=255//pocet
        if bCan == True:
            b-=255//pocet

for i in range(40):
    r,g,b = random.choice((0,255)),random.choice((0,255)),random.choice((0,255))
    if r==255:
        rCan = True
    else:
        rCan = False
    if g==255:
        gCan = True
    else:
        gCan = False
    if b==255:
        bCan = True
    else:
        bCan = False
    Kvet(5,10,r,g,b)
    t.penup()
    t.setposition(random.randint(50,250),random.randint(50,250))
    t.pendown()


turtle.mainloop()