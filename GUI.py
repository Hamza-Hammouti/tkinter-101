import tkinter

window = tkinter.Tk()

window.title("My First Window")

window.geometry("50x50")

def colorChange(i=5):
    if i >= 0:
        colors = ('red', 'blue', 'green', 'black', 'yellow', 'white')
        window.config(bg=colors[i])
        window.after(2000, colorChange, i-1)
        print(i+1)
    if i == 4:
        window.geometry("100x100")
    if i == 3:
        window.geometry("150x150")
    if i == 2:
        window.geometry("200x200")
    if i == 1:
        window.geometry("250x250")
    if i == 0:
        window.geometry("300x300")
        print("BOOM!")
        window.destroy()
        
# -------------------------------

colorChange()

window.mainloop()