import json
import tkinter as tk

with open("/home/duck/Downloads/theme maker/settings.json") as read_file:
    all_sittings = json.load(read_file)

window = tk.Tk()
window.title("VS Code theme maker")

window_width = 300
window_height = 200

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# calculate the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

message = tk.Label(window, text="test")
message.pack()

window.mainloop()
