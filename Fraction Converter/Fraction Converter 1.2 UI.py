import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Fraction Converter")
root.geometry("400x350")

# Create the Main Menu
main_menu_frame = ttk.Frame(root)
main_menu_frame.pack(fill="both", expand=True)

label = ttk.Label(main_menu_frame, text="Welcome to the Fraction Converter!", font=("Arial", 14, "bold"))
label.pack(pady=20)

# Add the Menu Buttons
btn_simplify = ttk.Button(main_menu_frame, text="1. Simplify Fraction")
btn_simplify.pack(fill="x", pady=5, ipady=10)

btn_arithmetic = ttk.Button(main_menu_frame, text="2. Arithmetic Operations")
btn_arithmetic.pack(fill="x", pady=5, ipady=10)

btn_conversion = ttk.Button(main_menu_frame, text="3. Decimal / Fraction Conversion")
btn_conversion.pack(fill="x", pady=5, ipady=10)

btn_mixed = ttk.Button(main_menu_frame, text="4. Mixed / Improper Conversion")
btn_mixed.pack(fill="x", pady=5, ipady=10)

root.mainloop()