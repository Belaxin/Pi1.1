import tkinter as tk
canvas = tk.Canvas(width = 1000, height =1000)
canvas.pack()

#Pismeno T
canvas.create_line(100,300, 100,100, 40, 100, 160,100,fill="blue",width = 9)

#Pismeno O
canvas.create_oval(150, 100, 250,300,width = 5,outline = "yellow")

#pismeno M

canvas.create_line(300,300, 300,100,    350,200 , 400,100, 400,300, fill="red", width =2)

#pismeno a

canvas.create_line(450,300, 500, 100, 550, 300,fill="orange", width=20)
canvas.create_line(475,225, 525, 225,fill = "orange", width=20)
canvas.create_line(510, 60, 560, 20,fill=  "orange", width=10)

#pismeno s

canvas.create_arc(600, 100, 700, 200 ,style = tk.ARC, width = 3, outline = "pink")

canvas.create_arc(600, 200, 700, 100, start = 90,style = tk.ARC, width = 3, outline = "pink")
canvas.create_arc(700,100,600,200, start = 180,style = tk.ARC, width = 3, outline = "pink" )
canvas.create_arc(600,200,700,300 ,style = tk.ARC, width = 3, outline = "pink")
canvas.create_arc(700,300, 600, 200, start = 270,style = tk.ARC, width = 3, outline = "pink")
canvas.create_arc(600, 300, 700, 200, start = 180,style = tk.ARC, width = 3, outline = "pink")

canvas.create_line(600,30,650,60,700,30,width=3,fill="pink")


#pismeno M
canvas.create_line(50, 600, 50, 400, 100, 500, 150, 400, 150 ,600, width = 25, fill= "purple" )

#pismeno A
canvas.create_line(200,600, 250, 400, 300,600, width= 15,fill ="green")
canvas.create_line(225,525, 280,525,width = 15, fill ="green")


#pismeno T

canvas.create_line(350, 600, 350,400,fill="cyan", width = 8)
canvas.create_line(290,400, 410,400,fill ="cyan", width = 8)

# pismeno i

canvas.create_line(425, 600, 425, 400, width = 5, fill ="brown")
canvas.create_oval (420, 385, 430, 375, fill = "brown",)


#pismeno s

canvas.create_arc(475, 400, 575, 500 ,style = tk.ARC, width = 40, outline = "grey")
canvas.create_arc(475, 400, 575, 500, start = 90,style = tk.ARC, width = 40, outline = "grey")
canvas.create_arc(575,400,475,500, start = 180,style = tk.ARC, width = 40, outline = "grey" )
canvas.create_arc(475, 500, 575, 600 ,style = tk.ARC, width = 40, outline = "grey")
canvas.create_arc(575, 600, 475, 500, start = 270,style = tk.ARC, width = 40, outline = "grey")
canvas.create_arc(475,500, 575, 600, start = 180,style = tk.ARC, width =40 , outline = "grey")


canvas.mainloop()
