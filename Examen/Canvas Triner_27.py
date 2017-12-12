from tkinter import*
import random
import time
tk = Tk()
tk.title("Bounce!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 500, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id,245,100)
        start = [-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        print(pos)
        if pos[1]<= 0:
            self.y = 3
        if pos[3]>= self.canvas_height:
            self.y = -3
        if  pos[0]<= 0:
            self.x =3
        if pos[2]>=self.canvas_width:
            self.x = -3 
        

ball = Ball(canvas,'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    
