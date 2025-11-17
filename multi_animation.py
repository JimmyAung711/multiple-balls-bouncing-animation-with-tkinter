from tkinter import *
import time
from balls import Ball

window = Tk()

canvas = Canvas(window,width=500,height=500)
canvas.pack()

volleyball = Ball(canvas,0,0,100,1,1,'orange')
baseball = Ball(canvas,0,0,100,2,1,'grey')
golf = Ball(canvas,0,0,100,1,3,'light yellow')

while True:
          volleyball.move()
          baseball.move()
          golf.move()
          window.update()
          time.sleep(0.01)
          
window.mainloop()