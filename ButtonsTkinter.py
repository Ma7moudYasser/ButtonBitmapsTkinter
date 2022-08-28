from tkinter import *

top = Tk()
top.geometry('500x500')

B1 = Button(top, text = 'error', bitmap = 'error')
B1.pack()

B2 = Button(top, text = 'hourglass', bitmap = 'hourglass')
B2.pack()

B3 = Button(top, text = 'info', bitmap = 'info')
B3.pack()

B4 = Button(top, text = 'warning', bitmap = 'warning')
B4.pack()

B5 = Button(top, text = 'question', bitmap = 'question')
B5.pack()

B6 = Button(top, text = 'gray12', bitmap = 'gray12')
B6.pack()

B7 = Button(top, text = 'gray25', bitmap = 'gray25')
B7.pack()

top.mainloop()
