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

OptionMixed = ttk.Button(MainMenuFrame, text="4. Mixed / Improper Conversion", command=lambda: [MainMenuFrame.pack_forget(), IMConversionFrame.pack(fill="both", expand=True)])
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

# Add the Mixed to Improper Frame
IMConversionFrame = ttk.Frame(root)

ButtonBack = ttk.Button(IMConversionFrame, text="Back", command=lambda: BackCommand(IMConversionFrame))
ButtonBack.pack(padx=10, side="top", anchor="nw")

ImproperMixedFrame = ttk.Frame(IMConversionFrame)
ImproperMixedFrame.pack(pady=20, padx=10, fill="both", expand=True)

WholeFrame = ttk.Frame(ImproperMixedFrame)
WholeFrame.pack(pady=70, padx=10, side="left", anchor="n")
WholeInput = ttk.Entry(WholeFrame)
WholeInput.pack()
WholeHint = ttk.Label(WholeFrame, text="Whole Number", foreground="grey", font=("Arial", 10, "italic"))
WholeHint.pack(pady=5)

NumeratorFrame = ttk.Frame(ImproperMixedFrame)
NumeratorFrame.pack(pady=30, padx=10)
MixedNumeratorInput = ttk.Entry(NumeratorFrame)
MixedNumeratorInput.pack()
NumeratorHint = ttk.Label(NumeratorFrame, text="Numerator", foreground="grey", font=("Arial", 10, "italic"))
NumeratorHint.pack(pady=5)

DenominatorFrame = ttk.Frame(ImproperMixedFrame)
DenominatorFrame.pack(pady=5, padx=10)
MixedDenominatorInput = ttk.Entry(DenominatorFrame)
MixedDenominatorInput.pack()
DenominatorHint = ttk.Label(DenominatorFrame, text="Denominator", foreground="grey", font=("Arial", 10, "italic"))
DenominatorHint.pack(pady=5)

def OnButtonClickMtI():
    MixedWhole = WholeInput.get()
    MixedNumerator = MixedNumeratorInput.get()
    MixedDenominator = MixedDenominatorInput.get()

    Result = ft.MixedToImproper(MixedWhole, MixedNumerator, MixedDenominator)
    ImproperOutput.config(text=str(Result))

ConvertButton = ttk.Button(ImproperMixedFrame, text="Convert Mixed to Improper", command=OnButtonClickMtI)
ConvertButton.pack(pady=20)

ImproperOutput = ttk.Label(ImproperMixedFrame, text="0", font=("Arial", 12), foreground="black", justify="center")
ImproperOutput.pack(pady=10)
root.mainloop()