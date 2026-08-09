import tkinter as tk
from tkinter import ttk
import FractionTools as ft
from tkinter import messagebox

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
OptionSimplify = ttk.Button(MainMenuFrame, text="1. Simplify Fraction", command=lambda: ft.MenuButton(SimplifyFrame, MainMenuFrame))
OptionSimplify.pack(fill="x", pady=5, ipady=10)

OptionArithmetic = ttk.Button(MainMenuFrame, text="2. Arithmetic Operations")
OptionArithmetic.pack(fill="x", pady=5, ipady=10)

OptionConversion = ttk.Button(MainMenuFrame, text="3. Decimal / Fraction Conversion", command=lambda: ft.MenuButton(DFConversionFrame, MainMenuFrame))
OptionConversion.pack(fill="x", pady=5, ipady=10)

OptionMixed = ttk.Button(MainMenuFrame, text="4. Mixed / Improper Conversion", command=lambda: ft.MenuButton(IMConversionFrame, MainMenuFrame))
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
    if Result == ValueError:
        messagebox.showwarning("Error", f"This fraction is already in its simplest form! {Numerator}/{Denominator}")
    else:
        SimplifiedOutput.config(text=str(Result))

ButtonSimplify = ttk.Button(SimplifyFrame, text="Simplify", command=OnButtonClickSimplify)
ButtonSimplify.pack(pady=10)

SimplifiedOutput = ttk.Label(SimplifyFrame, text="", font=("Arial", 12), foreground="black", justify="center")
SimplifiedOutput.pack(pady=10)

# Add the Mixed <-> Improper Frame
IMConversionFrame = ttk.Frame(root)

ButtonBack = ttk.Button(IMConversionFrame, text="Back", command=lambda: BackCommand(IMConversionFrame))
ButtonBack.pack(padx=10, side="top", anchor="nw")

ButtonSwitch = ttk.Button(IMConversionFrame, text="Switch Conversion", command=lambda: ft.SwitchFrames(MixedImproperFrame, ImproperMixedFrame))
ButtonSwitch.pack(pady=10, side="top", anchor="ne")

# Improper to Mixed Conversion Frame
ImproperMixedFrame = ttk.Frame(IMConversionFrame)
ImproperMixedFrame.pack(pady=20, padx=10, fill="both", expand=True)

NumeratorFrame = ttk.Frame(ImproperMixedFrame)
NumeratorFrame.pack(pady=10, padx=10)
ImproperNumeratorInput = ttk.Entry(NumeratorFrame)
ImproperNumeratorInput.pack()
NumeratorHint = ttk.Label(NumeratorFrame, text="Numerator", foreground="grey", font=("Arial", 10, "italic"))
NumeratorHint.pack(pady=5)

DenominatorFrame = ttk.Frame(ImproperMixedFrame)
DenominatorFrame.pack(pady=5, padx=10)
ImproperDenominatorInput = ttk.Entry(DenominatorFrame)
ImproperDenominatorInput.pack()
DenominatorHint = ttk.Label(DenominatorFrame, text="Denominator", foreground="grey", font=("Arial", 10, "italic"))
DenominatorHint.pack(pady=5)

def OnButtonClickItM():
    ImproperNumerator = ImproperNumeratorInput.get()
    ImproperDenominator = ImproperDenominatorInput.get()

    Result = ft.ImproperToMixed(ImproperNumerator, ImproperDenominator)
    MixedOutput.config(text=str(Result))

ConvertButton = ttk.Button(ImproperMixedFrame, text="Convert Improper to Mixed", command=OnButtonClickItM)
ConvertButton.pack(pady=20)

MixedOutput = ttk.Label(ImproperMixedFrame, text="0", font=("Arial", 12), foreground="black", justify="center")
MixedOutput.pack(pady=10)

# Mixed to Improper Conversion Frame
MixedImproperFrame = ttk.Frame(IMConversionFrame)

WholeFrame = ttk.Frame(MixedImproperFrame)
WholeFrame.pack(pady=50, padx=10, side="left", anchor="n")
WholeInput = ttk.Entry(WholeFrame)
WholeInput.pack()
WholeHint = ttk.Label(WholeFrame, text="Whole Number", foreground="grey", font=("Arial", 10, "italic"))
WholeHint.pack(pady=5)

NumeratorFrame = ttk.Frame(MixedImproperFrame)
NumeratorFrame.pack(pady=10, padx=10)
MixedNumeratorInput = ttk.Entry(NumeratorFrame)
MixedNumeratorInput.pack()
NumeratorHint = ttk.Label(NumeratorFrame, text="Numerator", foreground="grey", font=("Arial", 10, "italic"))
NumeratorHint.pack(pady=5)

DenominatorFrame = ttk.Frame(MixedImproperFrame)
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

ConvertButton = ttk.Button(MixedImproperFrame, text="Convert Mixed to Improper", command=OnButtonClickMtI)
ConvertButton.pack(pady=20)

ImproperOutput = ttk.Label(MixedImproperFrame, text="0", font=("Arial", 12), foreground="black", justify="center")
ImproperOutput.pack(pady=10)

MtIConversionFrame = ttk.Frame(IMConversionFrame)

ImproperNumeratorFrame = ttk.Frame(MtIConversionFrame)
ImproperNumeratorFrame.pack(pady=10)

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