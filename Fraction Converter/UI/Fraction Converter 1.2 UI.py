import tkinter as tk
from tkinter import ttk
import FractionTools as ft

def BackCommand(CurrentFrame):
    CurrentFrame.pack_forget()
    MainMenuFrame.pack(fill="both", expand=True)

root = tk.Tk()
root.title("Fraction Converter")
root.geometry("400x350")

# Create Frames for each screen
MainMenuFrame = ttk.Frame(root)
SimplifyFrame = ttk.Frame(root)

# Pack the Main Menu Frame
MainMenuFrame.pack(fill="both", expand=True)

WelcomeLabel = ttk.Label(MainMenuFrame, text="Welcome to the Fraction Converter!", font=("Arial", 14, "bold"))
WelcomeLabel.pack(pady=20)

# Add the Menu Buttons
OptionSimplify = ttk.Button(MainMenuFrame, text="1. Simplify Fraction", command=lambda: [MainMenuFrame.pack_forget(), SimplifyFrame.pack(fill="both", expand=True)])
OptionSimplify.pack(fill="x", pady=5, ipady=10)

OptionArithmetic = ttk.Button(MainMenuFrame, text="2. Arithmetic Operations")
OptionArithmetic.pack(fill="x", pady=5, ipady=10)

OptionConversion = ttk.Button(MainMenuFrame, text="3. Decimal / Fraction Conversion")
OptionConversion.pack(fill="x", pady=5, ipady=10)

OptionMixed = ttk.Button(MainMenuFrame, text="4. Mixed / Improper Conversion")
OptionMixed.pack(fill="x", pady=5, ipady=10)

# Add the Simplify Frame
ButtonBack = ttk.Button(SimplifyFrame, text="Back", command=lambda: BackCommand(SimplifyFrame))
ButtonBack.pack(padx=10, side="top", anchor="nw")

NumeratorInput = ttk.Entry(SimplifyFrame)
NumeratorInput.pack(pady=10)
DenominatorInput = ttk.Entry(SimplifyFrame)
DenominatorInput.pack(pady=10)

def OnButtonClickSimplify():
    Numerator = int(NumeratorInput.get())
    Denominator = int(DenominatorInput.get())

    Result = ft.Simplify(Numerator, Denominator, ShowMessage=True)
    SimplifiedOutput.config(text=str(Result))

ButtonSimplify = ttk.Button(SimplifyFrame, text="Simplify", command=OnButtonClickSimplify)
ButtonSimplify.pack(pady=10)

SimplifiedOutput = ttk.Label(SimplifyFrame, text="", font=("Arial", 12), foreground="black", justify="center")
SimplifiedOutput.pack(pady=10)


root.mainloop()