import tkinter as tk
from tkinter import messagebox


def perform_calculation():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select an operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")
    operation_var.set("Select Operation")


# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Create widgets
operation_var = tk.StringVar()
operation_var.set("Select Operation")

operations_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
label1 = tk.Label(root, text="Enter first number:")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Enter second number:")
entry2 = tk.Entry(root)
calculate_button = tk.Button(root, text="Calculate", command=perform_calculation)
reset_button = tk.Button(root, text="Reset", command=reset)
result_label = tk.Label(root, text="Result: ")

# Layout widgets
label1.pack(pady=5)
entry1.pack(pady=5)
label2.pack(pady=5)
entry2.pack(pady=5)
operations_menu.pack(pady=5)
calculate_button.pack(pady=5)
reset_button.pack(pady=5)
result_label.pack(pady=10)

# Run the application
root.mainloop()
