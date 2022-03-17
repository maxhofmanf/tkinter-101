from time import strftime
import tkinter as tk
from datetime import datetime
from tkinter import font

window = tk.Tk()
now = datetime.now()


currentTime = tk.StringVar( value = now.strftime("%H:%M:%S"))
# window setting

window.geometry("250x100")
window.title("clock")
window.config(bg = "black")
#clock

the_clock= tk.Label(
    window,       
    bg= 'black',
    fg='white',
    textvariable= currentTime , font="Times 50 bold"
)
the_clock.pack()
def update_clock():
    currentTime.set(strftime("%H:%M:%S"))
    the_clock.configure(textvariable= currentTime)
    window.after(80, update_clock)

update_clock()
window.mainloop()