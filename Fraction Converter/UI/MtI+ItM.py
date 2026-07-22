import tkinter as tk
from tkinter import ttk
import FractionTools as ft

root = tk.Tk()
root.title("Fraction Converter")
root.geometry("400x350")

IMConversionFrame = ttk.Frame(root)
IMConversionFrame.pack(fill="both", expand=True)


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