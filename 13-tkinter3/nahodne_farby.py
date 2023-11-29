from tkinter import *
import random
canvas = Canvas(width=1000, height=1000)
canvas.pack()
meno = "Tomas"
priezvisko = "Matis"
vek = 255
print ("Volam sa", meno, priezvisko, "a mam", vek,"rokov")
print (f"Volam sa {meno} {priezvisko} a mam {vek:02x} rokov")  # vek :02x , 02 je pocet cifier a x prevedie do hex





x = 0
y= 100
while True:
    x = x+1
    if random.randint(1,2)==2:
        y=y+5
    else:
        y=y-5
    if y<0:
        y= 500
    if y>1000:
        y= 500
    if x>1000:
        x = 0
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    print(farba)
    canvas.create_rectangle(x,y,x+30,y+30,fill=farba)
    canvas.update()
canvas.mainloop()