import tkinter as tk
from tkinter import ttk
from .error import ErrorWindow
from models.database import Database
import re
from cli.utils.utils import Utils

class LoginWindow:
    def __init__(self, parent, navigate):
        self.parent = parent
        self.navigate = navigate
        self.parent.title("GUI Uni App")
        self.parent.geometry("600x400")  # Set window size

        self.clear_content()
        # Add a label for the app name
        self.app_name_label = ttk.Label(parent, text="GUI Uni App", font=("Arial", 16, "bold"))
        self.app_name_label.pack(pady=10)

        # Create a frame for better organization
        self.frame = ttk.Frame(parent)
        self.frame.pack(pady=10)

        # Username label and entry
        self.username_label = ttk.Label(self.frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password label and entry
        self.password_label = ttk.Label(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Login button
        self.login_button = ttk.Button(parent, text="Login", command=self.login)
        self.login_button.pack(pady=5)

    def login(self):
        if not re.match(Utils.EMAIL_REGEX, self.username_entry.get()) or not re.match(Utils.PASSWORD_REGEX, self.password_entry.get()):
                error_message = "Incorrect username or password format"
                self.show_error(error_message)
        else:
            students = Database.read_objects_from_file()
            for student in students:
                if student.email == self.username_entry.get() and student.password == self.password_entry.get():
                    self.clear_content()
                    self.navigate('/subject-enrollment', student=student)
                    break
                else:
                    error_message = "Incorrect username or password"
                    self.show_error(error_message)


    def show(self):
        # Show the subject menu window
        self.parent.deiconify()

    def hide(self):
        # Hide the login window
        self.parent.withdraw()

    def clear_content(self):
        # Clear the content of the login window
        for widget in self.parent.winfo_children():
            widget.destroy()

    def show_error(self, message):
        # Show an error window with the provided message
        error_window = tk.Toplevel(self.parent)
        ErrorWindow(error_window, message)

def main():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
