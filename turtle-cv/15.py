import math
import turtle

t = turtle.Turtle()


def square(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.left(90)


def Pytagoras(Prepona, uhol):
    # prepona
    t.fillcolor("Blue")
    t.begin_fill()
    square(Prepona)
    t.fd(Prepona)
    t.end_fill()
    # odvesna 1
    t.fillcolor("Red")
    t.begin_fill()
    t.right(180 - uhol)
    square(Prepona * (math.cos(math.radians(uhol))))
    t.fd(Prepona * (math.cos(math.radians(uhol))))
    t.end_fill()
    # odvesna 2
    t.fillcolor("Yellow")
    t.begin_fill()
    t.right(90)
    square(Prepona * (math.sin(math.radians(uhol))))
    t.end_fill()
    # vypocty
    sucet = (Prepona * (math.sin(math.radians(uhol)))) ** 2 + (Prepona * (math.cos(math.radians(uhol)))) ** 2
    print("Stvorec nad preponou: " + str(Prepona ** 2))
    print("Stvorec nad 1. odvesnou: " + str((Prepona * (math.sin(math.radians(uhol)))) ** 2))
    print("Stvorec nad 2. odvesnou: " + str((Prepona * (math.cos(math.radians(uhol)))) ** 2))
    print("Sucet:" + str(sucet))


Pytagoras(150, 17)

turtle.mainloop()
