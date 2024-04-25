import tkinter as tk

def facto(number):
    if number == 0:
        return 1
    else:
        return number * facto(number-1)

def calculate_factorial():
    try:
        number = int(entry.get())
        factorial_result = facto(number)
        n_factorial_result = facto(number)
        result_label.config(text=f"{number}! = {factorial_result}\n{number}N = {n_factorial_result}")
    except ValueError:
        result_label.config(text="Please enter a valid integer.")

root = tk.Tk()
root.title("Factorial Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter the number whose factorial you want to calculate:")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

calculate_button = tk.Button(frame, text="Calculate", command=calculate_factorial)
calculate_button.grid(row=1, column=0, columnspan=2, pady=5)

result_label = tk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()