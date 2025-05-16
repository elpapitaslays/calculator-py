import tkinter as tk

def click(value):
    current = entry.get()
    entry.set(current + str(value))

def clear():
    entry.set("")

def calculate():
    try:
        result = eval(entry.get())
        entry.set(str(result))
    except Exception:
        entry.set("Error")

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

entry = tk.StringVar()

input_field = tk.Entry(root, textvariable=entry, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
input_field.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

for text, row, col, *span in buttons:
    colspan = span[0] if span else 1
    action = calculate if text == '=' else (clear if text == 'C' else lambda x=text: click(x))
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 16), command=action)
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

root.mainloop()