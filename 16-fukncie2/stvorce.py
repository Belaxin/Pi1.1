import tkinter as tk

canvas = tk.Canvas(height=540, width=960)
canvas.pack()


def stvorce(x, y, pocet, dlzka):
    for i in range(pocet):
        canvas.create_rectangle(x - dlzka // 2, y - dlzka // 2, x + dlzka // 2, y + dlzka // 2)
        x += dlzka


stvorce(20, 20, 10, 30)
canvas.mainloop()
