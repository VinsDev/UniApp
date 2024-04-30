import tkinter as tk
from tkinter import ttk

class ErrorWindow:
    def __init__(self, parent, message):
        self.parent = parent
        self.parent.title("Error")
        
        # Configure the style
        self.style = ttk.Style()
        self.style.configure("Error.TLabel", foreground="red", font=("Arial", 12))
        self.style.configure("Error.TButton", background="#ffcccc", foreground="red", font=("Arial", 10, "bold"))
        
        # Frame for better organization
        self.frame = ttk.Frame(parent, style="Error.TFrame")
        self.frame.pack(padx=20, pady=10)
        
        # Error message label
        self.message_label = ttk.Label(self.frame, text=message, style="Error.TLabel")
        self.message_label.pack(pady=10)
        
        # OK button
        self.ok_button = ttk.Button(self.frame, text="OK", command=self.close_window, style="Error.TButton")
        self.ok_button.pack(pady=5)

    def close_window(self):
        self.parent.destroy()

    def center_window(self):
        # Calculate the position of the window relative to its parent
        x = self.parent.winfo_rootx() + (self.parent.winfo_width() - self.frame.winfo_reqwidth()) // 2
        y = self.parent.winfo_rooty() + (self.parent.winfo_height() - self.frame.winfo_reqheight()) // 2
        
        # Set the window position
        self.parent.geometry(f"+{x}+{y}")

def main():
    root = tk.Tk()
    app = ErrorWindow(root, "Incorrect username or password")
    root.mainloop()

if __name__ == "__main__":
    main()
