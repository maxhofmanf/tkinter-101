import tkinter as tk
import random
window = tk.Tk()
window['bg'] = 'white'
grabbelton= ['een telefoon','bril','een laptop','een auto','miljoen euro', 'mc donalds hamburger','een broodje kaas','ps5', 'nintendo switch', 'schimmel']
stat = True

prijs = ''
result = tk.StringVar('')
leftover = tk.StringVar('')

def Click():
    global stat, y, prijs,result, leftover
    ran = random.randrange(0,len(grabbelton))
    if stat == True:
        prijs = grabbelton[ran]
        result.set('Gefeliciteerd, je hebt een '+prijs+' gegrabbeld!')
        grabbelton.remove(prijs)
        if len(grabbelton) >0:
            leftover.set('er zijn nog '+str(len(grabbelton))+ ' items in de ton')
        else:
            leftover.set('de grabbelton is leeg')


box = tk.Label(
    window,
    text = 'klik op de knop om te grabbelen',
    bg = 'white'
)

box2 = tk.Label(
    window,
    textvariable= result
)
box3 = tk.Label(
    window,
    textvariable= leftover
)




button = tk.Button(text='Grabbelen' ,bg="white", fg="black", padx = 50 , pady = 20, command= Click)
box.pack()
button.pack(pady = 40, padx = 40)
box2.pack()
box3.pack()
window.mainloop()
