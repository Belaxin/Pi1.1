import tkinter as tk
canvas = tk.Canvas()
canvas.pack()

fbody = open('body.txt','r')
for riadok in fbody:
    medzera = riadok.find(' ')
    x = int(riadok[:medzera])
    y = int(riadok[medzera:])
    canvas.create_oval(x-10,y-10, x+10, y+10)

tk.mainloop()