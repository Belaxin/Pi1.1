import tkinter

canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()
x1 = 20
y1 = 10
dlzka = 20
canvas.create_rectangle(x1, y1, x1 + dlzka, y1 + dlzka)
canvas.create_rectangle(x1 + dlzka, y1, x1 + dlzka*2, y1 + dlzka)
canvas.create_rectangle(x1 + dlzka*2, y1, x1 + dlzka*3, y1 + dlzka)

canvas.create_oval(x1 + dlzka, y1 + dlzka, x1 + dlzka*2, y1 + dlzka*2, fill="Red")
canvas.create_rectangle(40, 50, 60, 70)

canvas.create_rectangle(20, 70, 40, 90)
canvas.create_rectangle(40, 70, 60, 90)
canvas.create_rectangle(60, 70, 80, 90)



i = 0


def horizontal(x, y):
    for i in range(1, x + 1):
        canvas.create_rectangle(20 * x, y * 20, 40 * x, y * 20 + 20)
        print(20 * x, y * 20, 40 * x, y * 20 + 20)
        x+= 1


horizontal(2, 7)

canvas.mainloop()


# mainloop udrzi okno na obrazovke
