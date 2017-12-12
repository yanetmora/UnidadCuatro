from tkinter import*
import random 
root = Tk()
canvas= Canvas(root,width = 300, height = 300)
canvas.pack()

canvas.create_text(150,150,text="This is my first GUI TEXT AND IT IS AWESOME!",fill="White",font=("Times",30))

randomRects(150)
root.mainloop()
