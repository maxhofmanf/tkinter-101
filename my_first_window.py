import tkinter as tk
import time
window = tk.Tk()
#code hier V


time.sleep(1)
window.title('my First Window')
window.geometry("50x50")
window.config(bg = "white")
print("6")
window.update()


time.sleep(1)
window.config(bg = "yellow")
window.geometry('100x100')
print("5")
window.update()

time.sleep(1)
window.config(bg = "orange")
window.geometry('150x150')
print("4")
window.update()

time.sleep(1)
window.config(bg = "red")
window.geometry('200x200')
print("3")
window.update()

time.sleep(1)
window.config(bg = "purple")
window.geometry('250x250')
print("2")
window.update()

time.sleep(1)
window.config(bg="black")
print("1")
window.update()


time.sleep(1)
window.destroy()
print("BOOM!")


window.mainloop()