from tkinter import*

root = Tk()

def printName(event):
    print('Hello there Avinash')

button1 = Button(root,text = "Click Me")
button1.bind("<Button-1>",printName)

button1.pack()

root.mainloop()
