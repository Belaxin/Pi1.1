import tkinter as tk

canvas = tk.Canvas(height=540, width=960)
canvas.pack()

def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def stvorce(x, y, pocet, dlzka, r=255 ,g=255 ,b=255):
    krok = 5
    for i in range(pocet):
        canvas.create_rectangle(x - dlzka // 2, y - dlzka // 2, x + dlzka // 2, y + dlzka // 2, fill=rgb(r, g, b))
        x += dlzka
        if r>=krok:
            r -= krok
        if g >= krok :
            g -= krok
        if b >= krok :
            b -= krok
y = 20
for i in range (5):
    stvorce(20,y,47,20,255,0,0)
    stvorce(20,y +20,47,20,0,255,0)
    stvorce(20,y +40,47,20,0,0,255)
    y +=60
canvas.mainloop()
