import tkinter as tk
import math

#creates the calculator window
root = tk.Tk()
root.title("Calculator")

expression = ""

def add_to_expression(num):
    global expression
    expression = expression + str(num)
    display.delete(0, tk.END)  # Clear the current content in the display
    display.insert(tk.END, expression) #Updates the display to the new expression

def evaluate_expression():
    global expression
    try:
        result = eval(expression.replace("÷", "/").replace("×", "*").replace("^", "**")) 
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = str(result)  # Updates expression to the result
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

def clear_expression():
    global expression
    expression = ""
    display.delete(0, tk.END)

#Sets up the calculator display for the expression
display = tk.Entry(root, font=("Arial", 24), bd=10, relief="sunken", justify="left")
display.grid(row=0, column=0)

#Creates the calculator buttons
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0)

button_texts = [
        ("(", 0, 0), (")", 0, 1), ("^", 0, 2), ("clear", 0, 3),
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

for text, row, col in button_texts:
    if text == "clear":
        button = tk.Button(button_frame, text=text, width=5, height=2, command=clear_expression)
    elif text == "=":
        button = tk.Button(button_frame, text=text, width=5, height=2, command=evaluate_expression)
    else:
        button = tk.Button(button_frame, text=text, width=5, height=2, command=lambda num=text: add_to_expression(num))
    button.grid(row=row, column=col, sticky="nsew")

root.mainloop()
