import turtle

t = turtle.Turtle()
t.speed(0)


def square(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.left(90)
def pyramid(layers, size):
    for g in range(layers):
        square(size+g*20)
        t.penup()
        t.fd(-10)
        t.right(90)
        t.fd(10)
        t.left(90)
        t.pendown()



def spiral(deg, exponent,color):
    t.color(color)
    for i in range(1000):
        t.fd(i**exponent)
        t.left(deg)


#pyramid(5, 10)
#t.penup()
#t.setposition(5,5)
#t.pendown()
spiral(179.5, 1.3,"black")
turtle.mainloop()
for j in range(4):
    for i in range(1, 5):
        square(10*i)
    t.left(90)



