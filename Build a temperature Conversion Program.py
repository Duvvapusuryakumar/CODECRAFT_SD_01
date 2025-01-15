import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temp_value = float(entry_temperature.get())
        unit = selected_unit.get()

        if unit == "Celsius":
            fahrenheit = celsius_to_fahrenheit(temp_value)
            kelvin = celsius_to_kelvin(temp_value)
            result.set(f"{temp_value} °C = {fahrenheit:.2f} °F, {kelvin:.2f} K")

        elif unit == "Fahrenheit":
            celsius = fahrenheit_to_celsius(temp_value)
            kelvin = fahrenheit_to_kelvin(temp_value)
            result.set(f"{temp_value} °F = {celsius:.2f} °C, {kelvin:.2f} K")

        elif unit == "Kelvin":
            celsius = kelvin_to_celsius(temp_value)
            fahrenheit = kelvin_to_fahrenheit(temp_value)
            result.set(f"{temp_value} K = {celsius:.2f} °C, {fahrenheit:.2f} °F")

        else:
            messagebox.showerror("Error", "Please select a valid unit.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value for the temperature.")

def create_gui():
    global entry_temperature, selected_unit, result

    root = tk.Tk()
    root.title("Temperature Converter")

    # Input frame
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Enter Temperature:").grid(row=0, column=0, padx=5, pady=5)
    entry_temperature = tk.Entry(input_frame, width=10)
    entry_temperature.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Select Unit:").grid(row=1, column=0, padx=5, pady=5)
    selected_unit = tk.StringVar(value="Celsius")
    tk.OptionMenu(input_frame, selected_unit, "Celsius", "Fahrenheit", "Kelvin").grid(row=1, column=1, padx=5, pady=5)

    # Convert button
    tk.Button(root, text="Convert", command=convert_temperature).pack(pady=10)

    # Result label
    result = tk.StringVar()
    tk.Label(root, textvariable=result, font=("Arial", 14)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
