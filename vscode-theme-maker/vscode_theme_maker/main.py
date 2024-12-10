def render_tabs(all_sittings, window):
    pass

    def items_selected(event):
        pass


#        # get all selected indices
#        selected_indices = listbox.curselection()
#        # get selected items
#        selected_values = ",".join([listbox.get(i) for i in selected_indices])
#        print(selected_values)
#
#    listbox.bind("<<ListboxSelect>>", items_selected)
#
#    window.mainloop()


def create_window(width: int = 800, height: int = 500):
    pass


#    window = tk.Tk()
#    window.attributes("-topmost", 1)  # remove later pls
#    window.title("VS Code theme maker")
#    width = 800
#    height = 500
#    screen_width = window.winfo_screenwidth()  # get the screen dimensions
#    screen_height = window.winfo_screenheight()
#    center_x = int(screen_width / 2 - width / 2)  # calculate the center point
#    center_y = int(screen_height / 2 - height / 2)
#    window.geometry(f"{width}x{height}+{center_x}+{center_y}")
#    return window


def main():
    import sys
    import PyQt6
    import PySide6.QtCore
    PyQt6 
    sys
    # Prints PySide6 version
    print(PySide6.__version__)

    # Prints the Qt version used to compile PySide6
    print(PySide6.QtCore.__version__)
    import json

    all_sittings = json.load(open("settings.json"))

    window = create_window()

    render_tabs(all_sittings, window)


main()
