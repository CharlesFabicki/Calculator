import tkinter as tk
import math


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Calculator")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        display_frame = tk.Frame(self.root)
        display_frame.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Display entry field
        display_entry = tk.Entry(display_frame, textvariable=self.result_var, font=("Helvetica", 30), bd=10,
                                 insertwidth=1, justify='right')
        display_entry.pack(fill="both", expand=True)

        # Layout for digit buttons
        digit_buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 1)
        ]

        # Layout for operation buttons
        operation_buttons = [
            ('/', 1, 3), ('%', 1, 4),
            ('*', 2, 3), ('√', 2, 4),
            ('-', 3, 3), ('^', 3, 4),
            ('+', 4, 3), ('(', 4, 4), (')', 4, 5),
            ('C', 4, 0), ('=', 4, 2),
            ('π', 1, 5), ('𝑒', 2, 5), ('ln', 3, 5)
        ]

        # Create digit buttons
        for (text, row, col) in digit_buttons:
            button = tk.Button(self.root, text=text, font=("Helvetica", 16), height=2, width=5,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        # Create operation buttons
        for (text, row, col) in operation_buttons:
            button = tk.Button(self.root, text=text, font=("Helvetica", 16), height=2, width=5,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        # Clear button
        if button_text == 'C':
            self.result_var.set('')
        # Evaluate button
        elif button_text == '=':
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        # Square root button
        elif button_text == '√':
            try:
                result = str(math.sqrt(eval(current_text)))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        # Percentage button
        elif button_text == '%':
            try:
                result = str(eval(current_text) / 100)
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        # Power button
        elif button_text == '^':
            self.result_var.set(current_text + "**")
        # π (pi) button
        elif button_text == 'π':
            self.result_var.set(current_text + str(math.pi))
        # 𝑒 (Euler's number) button
        elif button_text == '𝑒':
            self.result_var.set(current_text + str(math.e))
        # Natural logarithm button
        elif button_text == 'ln':
            try:
                result = str(math.log(eval(current_text)))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        # Other buttons (digits and operators)
        else:
            self.result_var.set(current_text + button_text)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
