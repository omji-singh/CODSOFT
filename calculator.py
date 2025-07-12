import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.resizable(False, False)
        self.build_ui()

    def build_ui(self):
        frm = ttk.Frame(self, padding=10)
        frm.grid()

        ttk.Label(frm, text="First number:").grid(row=0, column=0, sticky="e")
        self.entry_num1 = ttk.Entry(frm, width=20)
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frm, text="Second number:").grid(row=1, column=0, sticky="e")
        self.entry_num2 = ttk.Entry(frm, width=20)
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frm, text="Operation:").grid(row=2, column=0, sticky="e")
        self.combo_op = ttk.Combobox(frm, values=["+", "-", "*", "/"], state="readonly", width=5)
        self.combo_op.current(0)
        self.combo_op.grid(row=2, column=1, sticky="w", pady=5)

        ttk.Button(frm, text="Calculate", command=self.calculate).grid(row=3, column=1, sticky="e", pady=10)

        self.result_label = ttk.Label(frm, text="Result: ")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

    def calculate(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            op = self.combo_op.get()

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero.")
                    return
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Invalid operation selected.")
                return

            self.result_label.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

if __name__ == "__main__":
    CalculatorApp().mainloop()
