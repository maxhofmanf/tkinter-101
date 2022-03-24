import tkinter as tk
window = tk.Tk()
counter = tk.IntVar(0)
count=0
def Click1():
    global count
    count += 1
    counter.set(count)
    background()
def Click2():
    global count
    count -=1
    counter.set(count)
    background()
box1 = tk.Label(
    window,
    textvariable= counter
)
def background():
    if counter.get() > 0 :
        window['bg']= 'green'
    elif counter.get() < 0:
        window['bg']='red'
    else:
        window['bg']='gray'

btn1= tk.Button(text='+' ,bg="white", fg="black", padx = 30 , pady = 10, command= Click1)
btn2= tk.Button(text='-' ,bg="white", fg="black", padx = 30 , pady = 10, command= Click2)
btn1.pack()
box1.pack()
btn2.pack()
window.mainloop()
