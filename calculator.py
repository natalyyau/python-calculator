import tkinter as tk

class Calculator:
    #GUI window set up
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.GUI_setup()

    #GUI Button set up
    def GUI_setup(self):
        #Sets up the calculator display for the expression
        self.display = tk.Entry(self.root, font=("Arial", 24), bd=10, relief="sunken", justify="left")
        self.display.grid(row=0, column=0)

        #Creates the calculator buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1, column=0)

        self.button_texts = [
            ("(", 0, 0), (")", 0, 1), ("√", 0, 2), ("clear", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for text, row, col in self.button_texts:
            button = tk.Button(self.button_frame, text=text, width=5, height=2)
            button.grid(row=row, column=col, sticky="nsew")

    #Runs the calculator
    def run(self):
        self.root.mainloop()

calculate = Calculator()
calculate.run()

expression = ""
def add_to_expression(num):
    global expression
    expression = expression + str(num)
