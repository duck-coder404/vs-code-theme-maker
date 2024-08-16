import json
import tkinter as tk

with open(
    "/home/duck/Downloads/theme maker/settings.json", mode="r", encoding="utf-8") as read_file:
    all_sittings = json.load(read_file)

window = tk.Tk()
window.title("VS Code theme maker")

message = tk.Label(window, text="test")
message.pack()

window.mainloop()