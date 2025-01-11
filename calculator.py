import tkinter as tk

class Calculator:
    #GUI window set up
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.grid_rowconfigure(0, weight=1)  # Make root window row expandable
        self.root.grid_columnconfigure(0, weight=1)  # Make root window column expandable
        self.GUI_setup()

    #GUI Button set up
    def GUI_setup(self):
        self.display = tk.Entry(self.root, font=("Arial", 24), bd=10, relief="sunken", justify="left")
        self.display.grid(row=0, column=0, sticky="nsew")

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1, column=0, sticky="nsew")

        self.button_texts = [
            ("(", 0, 0), (")", 0, 1), ("√", 0, 2), ("clear", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]
        for i in range(5):  # 5 rows
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 columns
            self.button_frame.grid_columnconfigure(i, weight=1)

        for text, row, col in self.button_texts:
            button = tk.Button(self.button_frame, text=text, width=5, height=2)
            button.grid(row=row, column=col, sticky="nsew")

    def run(self):
        self.root.mainloop()

calculate = Calculator()
calculate.run()


