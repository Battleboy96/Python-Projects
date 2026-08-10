import tkinter as tk
from tkinter import ttk
import FractionTools as ft

def BackCommand(arg, Arithmatic=False):
    print("temp")

# Create Multiplication Frame
MultiplicationFrame = tk.Tk()
MultiplicationFrame.title("Multiplication Menu")
MultiplicationFrame.geometry("400x350")

ButtonBack = ttk.Button(MultiplicationFrame, text="Back", command=lambda: BackCommand(MultiplicationFrame, Arithmatic=True))
ButtonBack.pack(padx=10, side="top", anchor="nw")

EquationFrame = ttk.Frame(MultiplicationFrame)
EquationFrame.pack(pady=10, padx=10, anchor="center")

# Create Fraction 1 Frame
Fraction1Frame = ttk.Frame(EquationFrame)
Fraction1Frame.pack(pady=10, padx=10, side="left", anchor="w")

# Create Numerator 1 Frame
Numerator1Frame = ttk.Frame(Fraction1Frame)
Numerator1Frame.pack(padx=10, pady=10, )
Numerator1Hint = ttk.Label(Numerator1Frame, text="Numerator 1:", font=("Arial", 10, "italic"), foreground="grey")
Numerator1Hint.pack(padx=5, pady=5, side="top")
Numerator1Input = ttk.Entry(Numerator1Frame)
Numerator1Input.pack(side="top", padx=5)

# Create Denominator 1 Frame
Denominator1Frame = ttk.Frame(Fraction1Frame)
Denominator1Frame.pack(padx=10, pady=10, )
Denominator1Hint = ttk.Label(Denominator1Frame, text="Denominator 1:", font=("Arial", 10, "italic"), foreground="grey")
Denominator1Hint.pack(padx=5, pady=5, side="top")
Denominator1Input = ttk.Entry(Denominator1Frame)
Denominator1Input.pack(side="top", padx=5)

MultiplicationSign = ttk.Label(EquationFrame, text="x", font=("Arial", 14, "bold"))
MultiplicationSign.pack(pady=10, padx=10, side="left", anchor="center")

# Create Fraction 2 Frame
Fraction2Frame = ttk.Frame(EquationFrame)
Fraction2Frame.pack(pady=10, side="left", anchor="e")

# Create Numerator 2 Frame
Numerator2Frame = ttk.Frame(Fraction2Frame)
Numerator2Frame.pack(pady=10, padx=10, )
Numerator2Hint = ttk.Label(Numerator2Frame, text="Numerator 2:", font=("Arial", 10, "italic"), foreground="grey")
Numerator2Hint.pack(padx=5, pady=5, side="top")
Numerator2Input = ttk.Entry(Numerator2Frame)
Numerator2Input.pack(side="top", padx=5)

# Create Denominator 2 Frame
Denominator2Frame = ttk.Frame(Fraction2Frame)
Denominator2Frame.pack(pady=10, padx=10, )
Denominator2Hint = ttk.Label(Denominator2Frame, text="Denominator 2:", font=("Arial", 10, "italic"), foreground="grey")
Denominator2Hint.pack(padx=5, pady=5, side="top")
Denominator2Input = ttk.Entry(Denominator2Frame)
Denominator2Input.pack(side="top", padx=5)

def OnButtonClickMultiplication():
    FirstNumerator = int(Numerator1Input.get())
    FirstDenominator = int(Denominator1Input.get())
    SecondNumerator = int(Numerator2Input.get())
    SecondDenominator = int(Denominator2Input.get())
    result = ft.Multiplication(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator)
    OutputLabel.config(text=str(result))

OutputLabel = ttk.Label(MultiplicationFrame, text="0", font=("Arial", 12))
OutputLabel.pack(pady=5, padx=5)

MultiplyButton =ttk.Button(MultiplicationFrame, text="Multiply", command=OnButtonClickMultiplication)
MultiplyButton.pack(pady=10, padx=10)

MultiplicationFrame.mainloop()