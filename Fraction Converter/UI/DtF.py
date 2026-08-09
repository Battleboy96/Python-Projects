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
    Decimal = float(DecimalInput.get())
    Result = ft.DecimalToFraction(Decimal)
    if Result == ValueError:
        messagebox.showerror("Error", "Please input a valid decimal number")
    else:
        FractionOutput.config(text=str(Result))

ButtonFrame = ttk.Frame(DecimalFractionFrame)
ButtonFrame.pack(pady=10)
ConvertDtFButton = ttk.Button(ButtonFrame, text="Convert", command=OnButtonClickDtF)
ConvertDtFButton.pack()

OutputFrame = ttk.Frame(DecimalFractionFrame)
OutputFrame.pack(pady=20, padx=10, fill="both", expand=True)
FractionOutput = ttk.Label(OutputFrame, text="0/0", font=("Arial", 12))
FractionOutput.pack()

# Fraction to Decimal Conversion Frame
FractionDecimalFrame = ttk.Frame(DFConversionFrame)

NumiratorFrame = ttk.Frame(FractionDecimalFrame)
NumiratorFrame.pack(pady=5, padx=10)
NumiratorHint = ttk.Label(NumiratorFrame, text="Numerator", foreground="grey", font=("Arial", 10, "italic"))
NumiratorHint.pack(pady=5)
NumiratorInput = ttk.Entry(NumiratorFrame)
NumiratorInput.pack()

DenominatorFrame = ttk.Frame(FractionDecimalFrame)
DenominatorFrame.pack(pady=5, padx=10)
DenominatorHint = ttk.Label(DenominatorFrame, text="Denominator", foreground="grey", font=("Arial", 10, "italic"))
DenominatorHint.pack(pady=5)
DenominatorInput = ttk.Entry(DenominatorFrame)
DenominatorInput.pack()

def OnButtonClickFtD():
    Numerator = int(NumiratorInput.get())
    Denominator = int(DenominatorInput.get())
    Result = ft.FractionToDecimal(Numerator, Denominator)
    if Result == ValueError:
        messagebox.showerror("Error", "Denominator cannot be zero")
    else:
        DecimalOutput.config(text=str(Result))

ButtonFrame = ttk.Frame(FractionDecimalFrame)
ButtonFrame.pack(pady=10)
ConvertFtDButton = ttk.Button(ButtonFrame, text="Convert", command=OnButtonClickFtD)
ConvertFtDButton.pack()

OutputFrame = ttk.Frame(FractionDecimalFrame)
OutputFrame.pack(pady=10, padx=10, fill="both", expand=True)
DecimalOutput = ttk.Label(OutputFrame, text="0.0", font=("Arial", 12))
DecimalOutput.pack()

root.mainloop()
