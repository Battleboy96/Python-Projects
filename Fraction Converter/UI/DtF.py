import tkinter as tk
from tkinter import ttk
import FractionTools as ft
from tkinter import messagebox

def BackCommand(arg):
    print("temp")

root = tk.Tk()
root.title("Fraction Converter")
root.geometry("400x350")

# Add the Decimal <-> Fraction Conversion Frame
DFConversionFrame = ttk.Frame(root)
DFConversionFrame.pack(pady=20, padx=10, fill="both", expand=True) # Temprary pack for testing purposes

ButtonBack = ttk.Button(DFConversionFrame, text="Back", command=lambda: BackCommand(DFConversionFrame))
ButtonBack.pack(padx=10, side="top", anchor="nw")

ButtonSwitch = ttk.Button(DFConversionFrame, text="Switch Conversion", command=lambda: ft.SwitchFrames(DecimalFractionFrame, FractionDecimalFrame))
ButtonSwitch.pack(pady=10, side="top", anchor="ne")

# Decimal to Fraction Conversion Frame
DecimalFractionFrame = ttk.Frame(DFConversionFrame)
DecimalFractionFrame.pack(pady=20, padx=10, fill="both", expand=True)

DecimalFrame = ttk.Frame(DecimalFractionFrame)
DecimalFrame.pack(pady=20, padx=10, fill="both", expand=True)
DecimalHint = ttk.Label(DecimalFrame, text="Decimal", foreground="grey", font=("Arial", 10, "italic"))
DecimalHint.pack(pady=5)
DecimalInput = ttk.Entry(DecimalFrame)
DecimalInput.pack()

def OnButtonClickDtF():
    Decimal = int(DecimalInput.get())
    Result = ft.DecimalToFraction(Decimal)
    if Result == ValueError:
        messagebox.showerror("Error", "Please input a valid decimal number")
    else:
        FractionOutput.config(text=str(Result)) # To be fixed next session
root.mainloop()
