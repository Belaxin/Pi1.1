xx = yy = None
import random
import tkinter as tk

canvas = tk.Canvas(width=1000, height=800)
canvas.pack()
he = canvas.create_oval(0, 0, 0, 0)


def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


sex = canvas.create_oval(0, 0, 0, 0)
e, r = 500, 500
enemySpeed = 8
jumpscare = tk.PhotoImage(file="jumpscare.gif")


def click(event):
    global xx, yy, sex, e, r, he
    canvas.delete(he)
    canvas.delete(sex)
    x, y = event.x, event.y
    sex = canvas.create_oval(x - 15, y - 15, x + 15, y + 15,
                             fill=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             outline=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    if xx != None:
        canvas.create_line(xx, yy, x, y)
    xx, yy = x, y
    # enemy
    he = canvas.create_oval(e - 5, r - 5, e + 5, r + 5, fill="Brown")
    if xx > e:
        e += enemySpeed
    elif xx < e:
        e -= enemySpeed
    if yy > r:
        r += enemySpeed
    else:
        r -= enemySpeed


def hore(event):
    global xx, yy, sex, e, r, he
    canvas.delete(he)
    canvas.delete(sex)
    yy -= 10
    sex = canvas.create_oval(xx - 15, yy - 15, xx + 15, yy + 15,
                             fill=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             outline=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    # enemy
    he = canvas.create_oval(e - 5, r - 5, e + 5, r + 5, fill="Brown")
    if xx > e:
        e += enemySpeed
    elif xx < e:
        e -= enemySpeed
    if yy > r:
        r += enemySpeed
    else:
        r -= enemySpeed

    # collision detection
    if xx - 15 < e < xx + 15 and yy - 15 < r < yy + 15:
        print("rip")
        xx, yy = 100000, 1000000
        canvas.create_image(500, 400, image=jumpscare)


def lava(event):
    global xx, yy, sex, e, r, he
    canvas.delete(he)
    canvas.delete(sex)
    xx -= 10
    sex = canvas.create_oval(xx - 15, yy - 15, xx + 15, yy + 15,
                             fill=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             outline=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    # enemy
    he = canvas.create_oval(e - 5, r - 5, e + 5, r + 5, fill="Brown")
    if xx > e:
        e += enemySpeed
    elif xx < e:
        e -= enemySpeed
    if yy > r:
        r += enemySpeed
    else:
        r -= enemySpeed

    # collision detection
    if xx - 15 < e < xx + 15 and yy - 15 < r < yy + 15:
        print("rip")
        xx, yy = 100000, 1000000
        canvas.create_image(500, 400, image=jumpscare)


def dole(event):
    global xx, yy, sex, e, r, he
    canvas.delete(he)
    canvas.delete(sex)
    yy += 10
    sex = canvas.create_oval(xx - 15, yy - 15, xx + 15, yy + 15,
                             fill=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             outline=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    # enemy
    he = canvas.create_oval(e - 5, r - 5, e + 5, r + 5, fill="Brown")
    if xx > e:
        e += enemySpeed
    elif xx < e:
        e -= enemySpeed
    if yy > r:
        r += enemySpeed
    else:
        r -= enemySpeed

    # collision detection
    if xx - 15 < e < xx + 15 and yy - 15 < r < yy + 15:
        print("rip")
        xx, yy = 100000, 1000000
        canvas.create_image(500, 400, image=jumpscare)


def prava(event):
    global xx, yy, sex, e, r, he
    canvas.delete(he)
    canvas.delete(sex)
    xx += 10
    sex = canvas.create_oval(xx - 15, yy - 15, xx + 15, yy + 15,
                             fill=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             outline=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    # enemy
    he = canvas.create_oval(e - 5, r - 5, e + 5, r + 5, fill="Brown")
    if xx > e:
        e += enemySpeed
    elif xx < e:
        e -= enemySpeed
    if yy > r:
        r += enemySpeed
    else:
        r -= enemySpeed

    # collision detection
    if xx - 15 < e < xx + 15 and yy - 15 < r < yy + 15:
        print("rip")
        xx, yy = 100000, 1000000
        canvas.create_image(500, 400, image=jumpscare)


canvas.bind('<ButtonPress>', click)
canvas.bind_all('<w>', hore)
canvas.bind_all('<a>', lava)
canvas.bind_all('<s>', dole)
canvas.bind_all('<d>', prava)
canvas.mainloop()
