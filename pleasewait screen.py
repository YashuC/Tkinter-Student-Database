import os
import  tkinter
from tkinter import *
screen = Tk()

def centrewindow(w, h):
	ws = screen.winfo_screenwidth()
	hs = screen.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) -(h/2)
	screen.geometry('%dx%d+%d+%d' % (w, h, x, y))
centrewindow(320, 200)


def openmain():
	screen.destroy()
	exec(open('E:\Desktop\GUI\Main.py').read())

screen.overrideredirect(True)
label = Label(screen, text='Please Wait...', font=('Arial Bold', 12))
label.pack()
label.configure(anchor=CENTER, pady=25)

#Animation For Please wait loading)
def st():
	pleasewait.destroy()
def nd():
	pleasewait1.destroy()
def rd():
	pleasewait2.destroy()
def th():
	pleasewait3.destroy()
def th4():
	pleasewait4.destroy()


#different frames of gif so that we can animate
image0 = PhotoImage(file= "plswait.gif", format='gif -index 0')
pleasewait = Label(screen, image=image0)
pleasewait.pack()
pleasewait.after(0, st)

image1 = PhotoImage(file= "plswait.gif", format='gif -index 1')
pleasewait1 = Label(screen, image=image1)
pleasewait1.pack()
pleasewait1.after(500, nd)

image2 = PhotoImage(file= "plswait.gif", format='gif -index 2')
pleasewait2 = Label(screen, image=image2)
pleasewait2.pack()
pleasewait2.after(1000, rd)

image3 = PhotoImage(file= "plswait.gif", format='gif -index 1')
pleasewait3 = Label(screen, image=image3)
pleasewait3.pack()
pleasewait3.after(1500, th)

image4 = PhotoImage(file= "plswait.gif", format='gif -index 1')
pleasewait4 = Label(screen, image=image4)
pleasewait4.pack()
pleasewait4.after(2000, th4)

screen.after(2000,openmain)
screen.mainloop()