from tkinter import *

# Create the main window
a = Tk()
a.title("Calculator")

# Entry widget for input
input = Entry(a, width=30, fg="green", font=("Arial", 16), borderwidth=2, relief="solid")
input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Initialize variables
operation = None
first_number = None

# Button colors
number_button_color = "#3498DB"  # Blue
symbol_button_color = "#E74C3C"  # Red
ac_button_color = "#E67E22"      # Orange
equal_button_color = "#2ECC71"   # Green
text_color = "#FFFFFF"           # White

# Button command functions
def click(num):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(num))

def set_operation(op):
    global first_number, operation
    first_number = float(input.get())
    operation = op
    input.delete(0, END)

def clear():
    input.delete(0, END)
    global first_number, operation
    first_number = None
    operation = None

def equal():
    second_number = float(input.get())
    input.delete(0, END)
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            result = "Error"
        else:
            result = first_number / second_number
    elif operation == "%":
        result = first_number % second_number
    elif operation == "^":
        result = first_number ** second_number
    else:
        result = "Error"
    input.insert(0, result)

def add_decimal():
    current = input.get()
    if "." not in current:
        input.insert(END, ".")

# Button creation (numbers)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    Button(a, text=text, padx=30, pady=20, fg=text_color, bg=number_button_color, font=("Arial", 16),
           command=lambda text=text: click(text)).grid(row=row, column=col, padx=5, pady=5)

# Button creation (operators and additional)
Button(a, text="+", padx=30, pady=20, fg=text_color, bg=symbol_button_color, font=("Arial", 16),
       command=lambda: set_operation("+")).grid(row=1, column=3, padx=5, pady=5)
Button(a, text="-", padx=30, pady=20, fg=text_color, bg=symbol_button_color, font=("Arial", 16),
       command=lambda: set_operation("-")).grid(row=2, column=3, padx=5, pady=5)
Button(a, text="*", padx=30, pady=20, fg=text_color, bg=symbol_button_color, font=("Arial", 16),
       command=lambda: set_operation("*")).grid(row=3, column=3, padx=5, pady=5)
Button(a, text="/", padx=30, pady=20, fg=text_color, bg=symbol_button_color, font=("Arial", 16),
       command=lambda: set_operation("/")).grid(row=4, column=3, padx=5, pady=5)

# Additional buttons (AC, =, and .)
Button(a, text="AC", padx=20, pady=20, fg=text_color, bg=ac_button_color, font=("Arial", 16),
       command=clear).grid(row=4, column=0, padx=5, pady=5)
Button(a, text=".", padx=30, pady=20, fg=text_color, bg=number_button_color, font=("Arial", 16),
       command=add_decimal).grid(row=4, column=2, padx=5, pady=5)
Button(a, text="=", padx=80, pady=20, fg=text_color, bg=equal_button_color, font=("Arial", 16),
       command=equal).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Operator buttons
Button(a, text="^", padx=30, pady=20, fg=text_color, bg=symbol_button_color, font=("Arial", 16),
       command=lambda: set_operation("^")).grid(row=5, column=2, padx=5, pady=5)
Button(a, text="%", padx=22, pady=20, fg=text_color, bg=symbol_button_color, font=("Arial", 16),
       command=lambda: set_operation("%")).grid(row=5, column=3, padx=5, pady=5)

# Run the main loop
a.mainloop()