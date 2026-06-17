import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    bg="yellow",
    fg="black"
)
label.pack(fill="both", expand=True)

def update_time():
    string = strftime("%H:%M:%S %p\n%d/%m/%Y")
    label.config(text=string)
    label.after(1000, update_time)

update_time()

root.mainloop()