# Priklad 18 - Platna
import tkinter as tk
import random

canvas = tk.Canvas(width=600, height=500)
canvas.pack()
r = 120
k = 6
x, y = r + 60, r + 10

for i in range((r // k) - 15):
    for i in range(k):
        canvas.create_oval(x - r, y - r, x + r, y + r, outline="black")
        r -= 3
    canvas.create_oval(x - r, y - r, x + r, y + r, outline="gray")
    if r < 15 + 6 * 3:
        print(r, "break")
        break
    r -= 3
    print(r, "inside")

print(r)

canvas.mainloop()
