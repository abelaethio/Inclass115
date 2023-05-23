import tkinter as tk
from tkinter import ttk

# Importing the necessary modules for creating a GUI application using tkinter.

def on_select(event):
    # Function to handle the selection event of the combobox.

    # Create an item object that obtains the value of the selected item.
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

# Creating a function that will be triggered when an item is selected in the combobox.

root = tk.Tk()
root.title("Abel")
# Creating the root window and setting its title.

items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
# Defining a list of items for the combobox.

combo_box = ttk.Combobox(root, values=items)
# Creating a combobox object and associating it with the root window, using the defined items as the values.

combo_box.bind("<<ComboboxSelected>>", on_select)
# Binding the selection event of the combobox to the on_select function.

combo_box.pack()
# Displaying the combobox on the screen using the pack geometry manager.

root.mainloop()
# Starting the main event loop to keep the root window visible and responsive.
