import tkinter as tk


def calculate_sum():
    number = entry.get()

    # Check if the number is 9 digits long
    if len(number) != 9:
        result_label.config(text="Error: The number must be 9 digits long.")
        return

    # Convert the number to a list of digits
    digits = list(number)

    # Add up the digits in the number
    total_sum = sum(int(digit) for digit in digits)

    # Update the result label
    result_label.config(text="The sum of the digits is {}".format(total_sum))


# Create the main window
window = tk.Tk()
window.title("Sum of Digits")
window.geometry("300x150")

# Create the input label and entry
input_label = tk.Label(window, text="Enter a 9-digit number:")
input_label.pack()

entry = tk.Entry(window)
entry.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_sum)
calculate_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
