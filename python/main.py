import json
import tkinter as tk
from tkinter import ttk

all_sittings = json.load(open("/home/duck/Downloads/theme maker/settings.json"))

window = tk.Tk()
window.attributes("-topmost", 1)  # remove later pls
window.title("VS Code theme maker")
window_width = 800
window_height = 500
screen_width = window.winfo_screenwidth()  # get the screen dimension
screen_height = window.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)  # calculate the center point
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


options = tk.Variable(value=list(all_sittings.keys()))
listbox = tk.Listbox(window, listvariable=options, height=6)
listbox.pack(expand=True, fill=tk.BOTH)


def items_selected(event):
    # get all selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_values = ",".join([listbox.get(i) for i in selected_indices])
    print(selected_values)


listbox.bind("<<ListboxSelect>>", items_selected)

window.mainloop()
