import tkinter

canvas = tkinter.Canvas(width=1000, height=600)
canvas.pack()


def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


prikazy = open('cv.txt', 'r')
prikazy_data = prikazy.readlines()
prikazy.seek(0)

for i in range(len(prikazy_data) // 2):
    suradnice = prikazy.readline().split()
    farby = prikazy.readline().split()

    x1, y1, x2, y2 = suradnice[1], suradnice[2], suradnice[3], suradnice[4]
    color = rgb(int(farby[0]), int(farby[1]), int(farby[2]))

    if suradnice[0] == 'r':
        print("stvorec")
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    if suradnice[0] == 'o':
        print("oval")
        canvas.create_oval(x1, y1, x2, y2, fill=color)

canvas.mainloop()
prikazy.close()
