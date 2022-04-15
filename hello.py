import tkinter

window = tkinter.Tk()

window.title("Hello")

window.geometry("150x100")

window.config(bg="grey")

# -------------------------------

box1 = tkinter.Label(
    window,
    text="Hello tkinter!",
    bg="black",
    fg="white"
)

box1.pack(
    ipadx=15,
    ipady=15,
    expand=True
)

window.mainloop()