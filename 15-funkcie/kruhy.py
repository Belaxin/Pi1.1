import tkinter as tk

canvas = tk.Canvas(width=1000, height=800)
canvas.pack()


def kruh(x, y, r,farba):
    canvas.create_oval(x - r, y - r, x + r, y + r,fill=farba)

def kruhy_riadok(x, y, polomer , farba, pocet_riadkov):
    for j in range(pocet_riadkov):
        kruh(x, y, polomer, farba)
        x += 2*polomer+2
def kruhy_stvorec(x, y, pocet_stlpcov, polomer, farba):
    for i in range(pocet_stlpcov):
        kruhy_riadok(x, y, polomer, farba, pocet_stlpcov)
        y += 2*polomer+2



kruhy_stvorec(50,50, 20, 10, "red")
canvas.mainloop()
