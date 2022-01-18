import tkinter as tk
import tkinter.font as font
import random


window = tk.Tk()
window.title("Knight-Knaves-Horses")
window.geometry("900x900")
items = {0: "Knights", 1: "Knaves", 2: "Horses"}
myfont = font.Font(family="Arial", size=20)


def change_text():

    myitems = ["Knights", "Knaves", "Horses"]
    newtext = random.choice(myitems)
    btn["text"] = newtext


btn = tk.Button(
    master=window,
    text=items[0],
    command=change_text,
    highlightbackground="#3E4149",
    # fg="#5799ef",
    fg="magenta",
    bg="gray",
    width="40",
    height="5",
    font=myfont,
    activebackground="#686868",
)

btn.place(x=150, y=50)


window.mainloop()
