import tkinter as tk
from tkinter import ttk
import math

# Functions from original code are temporary
def SignFlip(Denominator, Numerator):
    if Denominator < 0:
        Denominator *= -1
        Numerator *= -1
    return Denominator, Numerator

def Simplify(Numerator, Denominator, ShowMessage=True):
    Denominator, Numerator = SignFlip(Denominator, Numerator)

    CommonDivisor = math.gcd(Numerator, Denominator)
    SimplifiedNumerator = Numerator // CommonDivisor
    SimplifiedDenominator = Denominator // CommonDivisor

    if SimplifiedDenominator == 1:
        return(f"{SimplifiedNumerator}")

    elif CommonDivisor == 1:
        if ShowMessage:
            return(f"This fraction is already in its simplest form!\n{Numerator}/{Denominator}")
        else:
            return(f"{Numerator}/{Denominator}")

    else:
        return(f"{SimplifiedNumerator}/{SimplifiedDenominator}")

root = tk.Tk()
root.title("Fraction Converter")
root.geometry("400x350")

SimplifyFrame = ttk.Frame(root)
SimplifyFrame.pack(fill="both", expand=True)

NumeratorInput = ttk.Entry(SimplifyFrame)
NumeratorInput.pack(pady=10)
DenominatorInput = ttk.Entry(SimplifyFrame)
DenominatorInput.pack(pady=10)

Button = ttk.Button(SimplifyFrame, text="Simplify")
Button.pack(pady=10)

SimplifiedOutput = ttk.Label(SimplifyFrame, text="0", font=("Arial", 12), foreground="black")
SimplifiedOutput.pack(pady=10)

def OnButtonClick():
    Numerator = int(NumeratorInput.get())
    Denominator = int(DenominatorInput.get())
    
    # Pretend the function is defiened
    Result = Simplify(Numerator, Denominator, ShowMessage=True)
    SimplifiedOutput.config(text=str(Result))
    
Button.config(command=OnButtonClick)

root.mainloop()