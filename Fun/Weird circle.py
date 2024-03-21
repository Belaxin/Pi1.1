# Priklad 18 - Platna
import tkinter as tk
import random
canvas = tk.Canvas(width=600,height=500)
canvas.pack()
x , y = 190, 130
r = 120
k = 6



for i in range((r//k)+15):
    for i in range(k):
        canvas.create_oval(x-r,y-r,x+r,y+r,outline="Gray")
        r -= 2
    r -= 2


canvas.mainloop()