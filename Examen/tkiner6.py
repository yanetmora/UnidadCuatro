from tkinter import *

root = Tk()


Button1= Button(None,text = "Click Me!",fg = "Blue",bg = "yellow")
Button1.pack()

Button2 = Button(None,text = "Hello!",fg = "Red")
Button2.pack(fill=X)

Button3 = Button(None,text = "Hello!",fg = "Purple")
Button3.pack(side=RIGHT,fill=Y)

Button4 = Button(None,text = "Hello!",fg = "Yellow")
Button4.pack()


                  
root.mainloop()
