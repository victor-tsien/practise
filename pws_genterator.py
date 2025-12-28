import tkinter as tk
from tkinter import ttk, font
import random
import string


class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("密码生成器")
        self.geometry("350x200")
        self.config(bg='lightgray')

        self.label = ttk.Label(self, text="密码长度:", font=('Arial', 12), background='lightgray')
        self.label.pack(pady=20)

        self.length_var = tk.IntVar()
        self.length_entry = ttk.Entry(self, textvariable=self.length_var, font=('Arial', 12), width=10)
        self.length_entry.pack()

        self.generate_button = ttk.Button(self, text="生成密码", command=self.generate_password)
        self.generate_button.pack(pady=20)

        self.password_label = ttk.Label(self, text="", font=('Arial', 12, 'bold'), background='lightgray')
        self.password_label.pack()

    def generate_password(self):
        length = self.length_var.get()
        if length < 6:
            self.password_label.config(text="密码长度至少为6", foreground='red')
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        self.password_label.config(text=password, foreground='black')


if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
