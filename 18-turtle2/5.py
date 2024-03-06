import turtle

turtles = []  # list, pole
pocet = 4

for i in range(pocet):
    t = turtle.Turtle()
    t.penup()
    t.setposition(i* 100, 0)
    t.pendown()
    turtles.append(t)


# for i in range(4):
#     for t in turtles:
#         t.forward(50)
#         t.left(90)

turtle.mainloop()