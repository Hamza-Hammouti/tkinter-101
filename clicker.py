from ctypes.wintypes import INT
import tkinter

window = tkinter.Tk()
window.title("Clicker")
window.geometry("250x180")
window.configure(bg="grey")

number = 0

def upanddown(aantal):
    global number, button2
    number += aantal
    if number >= 1:
        window.configure(bg="green")
    elif number <= -1:
        window.configure(bg="red")
    elif number == 0:
        window.configure(bg="grey")

    button2 = tkinter.Label(window, text = number, width="30").grid(row=1, column=0, padx=15, pady=15)

button1 = tkinter.Button(window, text ="Up", width="30", command=lambda: [upanddown(1)]).grid(row=0, column=0, padx=15, pady=15)
button2 = tkinter.Label(window, text = number, width="30").grid(row=1, column=0, padx=15, pady=15)
button3 = tkinter.Button(window, text ="Down", width="30", command=lambda: [upanddown(-1)]).grid(row=2, column=0, padx=15, pady=15)

# -------------------------------

window.mainloop()