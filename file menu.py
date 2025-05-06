import tkinter as tk

# Function to exit the application
def exit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Minimal File Menu")
root.geometry("300x200")

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a File menu with only Exit option
file_menu = tk.Menu(menu_bar)
file_menu.add_command(label="Exit", command=exit_app)

# Add File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Attach menu bar to the window
root.config(menu=menu_bar)

root.mainloop()
