# import math/ o = 2 * math.pi * r
# import math as Matika/o = 2 * Matika.pi * r
# from math import */ o = 2 * pi * r
import time
from math import pi, radians
import random
# Viac sposobov na import
from tkinter import *

r = 10
o = 2 * pi * r
print(round(o, 2))
# round sa pouziva na zaokruhlenie

cislo = random.randrange(0, 10)
cislo2 = random.randint(1, 5)
farba = random.choice(("red", "green", "blue"))
print(cislo2)


while True:
    x1 = random.randrange(0, 1080)
    y1 = random.randrange(0, 1080)
    x2 = random.randrange(0, 1080)
    y2 = random.randrange(0, 1080)
    canvas = Canvas(width=1000,height=1000)
    canvas.pack()
    canvas.create_line(x1,y1 ,x2,y2)
    time.sleep(1)
    canvas.mainloop()
