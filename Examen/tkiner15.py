from tkinter import*
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title","Did you know that the World just blew up?")

answer = tkinter.messagebox.askquestion("Question 1","Are you human?")

if answer =="Yes":
    tkinter.mesagebox.showinfo("Congrats","Thank god!it's good to know another human is out there.")

if answer == "no":
    tkinter.messagebox.showinfo("Alien","You are a 100% confirmed Alien")

root.mainloop()

                              
     
