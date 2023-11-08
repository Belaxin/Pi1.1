# import math/ o = 2 * math.pi * r
# import math as Matika/o = 2 * Matika.pi * r
# from math import */ o = 2 * pi * r
from math import pi, radians
import random
# Viac sposobov na import
from tkinter import  *

r = 10
o = 2 * pi * r
print(round(o, 2))
# round sa pouziva na zaokruhlenie

cislo = random.randrange(0, 10)
cislo2 = random.randint(1,5)
farba = random.choice(("red", "green", "blue"))
print(cislo2)

top = Tk()
top.geometry("1080x1080")


canvas = canvas()
while True:
    x = random.randrange(0, 1080)
    y = random.randrange(0, 1080)
    canvas