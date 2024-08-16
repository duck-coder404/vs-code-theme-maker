import json
import tkinter as tk

window = tk.Tk()
window.title("VS Code theme maker")
window.mainloop()

with open("/home/duck/Downloads/theme maker/settings.json", mode="r", encoding="utf-8") as read_file:
    all_sittings = json.load(read_file)



for i in all_sittings["workbench.colorCustomizations"]:
    print(i)