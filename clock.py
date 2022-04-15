import tkinter as tk
import time as tm

window = tk.Tk()
window.title('Clock')
window.geometry("250x100")
window.config(bg="lightgrey")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

def time():
    current_time=tm.strftime('%H:%M:%S')
    clock_label=tk.Label(bg="lightgrey", fg="black",text=current_time,font=('Aerial 15 bold', 40))
    clock_label.grid(row=0,column=0)
    window.after(1000, time)

# -------------------------------

time()

window.mainloop()