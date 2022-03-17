import tkinter as tk
window = tk.Tk()

window.title('hello')
window.geometry("250x230")
window.config(bg = "purple")


#box
box = tk.Label(
    window,
    text = "hello tkinter",
    bg = 'black',
    fg = 'pink'
)

box.pack(
    ipadx=50,
    ipady=50,
    padx=50,
    pady=50
)





window.mainloop()