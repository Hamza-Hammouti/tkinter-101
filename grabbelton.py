import tkinter
import random

window = tkinter.Tk()

window.title("Grabbelton")

window.geometry("250x250")

items = ["banaan", "autotje", "openhaard", "cadeaubon", "horloge", "laptop", "bekertje", "televisie", "matras", "snoepzak"]

def grabbelen():
    left = len(items)
    if left <= 11 and left > 0:
        gegrabbeld = (random.choice(items))
        items.remove(gegrabbeld)
    else:
        print("Je hebt geen items meer over")
        
    if left <= 9 and left > 0:
        gewonnen = tkinter.Label(window, text = "Je hebt een " + "".join(gegrabbeld) + " gegrabbeld!").grid(row=3, padx=25, pady= 10)
    
    status = tkinter.Label(window, text = "Er zijn nog " + str(left) + " items in de grabbelton.").grid(row=1, padx=25, pady= 10)

knop = tkinter.Button(window, text ="Grabbelen", command = grabbelen).grid(row=2, padx=30, pady= 10)
# -------------------------------

grabbelen()

window.mainloop()