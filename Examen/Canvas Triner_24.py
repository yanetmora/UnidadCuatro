from tkinter import*
import random 
root = Tk()
canvas= Canvas(root,width = 300, height = 300)
canvas.pack()
def randomRects(num):
    for i in range(0,num):
        x1 = random.randrange(150)
        y1 = random.randrange(150)
        x2 = x1 + random.randrange(150)
        y2 = y1 + random.randrange(150)
        canvas.create_rectangle(x1,y1,x2,y2)

randomRects(150)
root.mainloop()
