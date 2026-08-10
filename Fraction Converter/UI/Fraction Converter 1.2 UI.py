import tkinter as tk
from tkinter import ttk
import FractionTools as ft
from tkinter import messagebox

def BackCommand(CurrentFrame, Arithmatic=False):
    if not Arithmatic:
        CurrentFrame.pack_forget()
        MainMenuFrame.pack(fill="both", expand=True)
    if Arithmatic:
        CurrentFrame.pack_forget()
        ArithmaticFrame.pack(fill="both", expand=True)

root = tk.Tk()
root.title("Fraction Converter")
root.geometry("400x350")

# Pack the Main Menu Frame
MainMenuFrame = ttk.Frame(root)
MainMenuFrame.pack(fill="both", expand=True)

WelcomeLabel = ttk.Label(MainMenuFrame, text="Welcome to the Fraction Converter!", font=("Arial", 14, "bold"))
WelcomeLabel.pack(pady=20)

# Add the Menu Buttons
OptionSimplify = ttk.Button(MainMenuFrame, text="1. Simplify Fraction", command=lambda: ft.MenuButton(SimplifyFrame, MainMenuFrame))
OptionSimplify.pack(fill="x", pady=5, ipady=10)

OptionArithmetic = ttk.Button(MainMenuFrame, text="2. Arithmetic Operations", command=lambda: ft.MenuButton(ArithmaticFrame, MainMenuFrame))
OptionArithmetic.pack(fill="x", pady=5, ipady=10)

OptionConversion = ttk.Button(MainMenuFrame, text="3. Decimal / Fraction Conversion", command=lambda: ft.MenuButton(DFConversionFrame, MainMenuFrame))
OptionConversion.pack(fill="x", pady=5, ipady=10)

OptionMixed = ttk.Button(MainMenuFrame, text="4. Mixed / Improper Conversion", command=lambda: ft.MenuButton(IMConversionFrame, MainMenuFrame))
OptionMixed.pack(fill="x", pady=5, ipady=10)

# Add the Simplify Frame
SimplifyFrame = ttk.Frame(root)

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

# Arithmatic Operations Frame
ArithmaticFrame = ttk.Frame(root)

WelcomeLabel = ttk.Label(ArithmaticFrame, text="Arithmatic Options", font=("Arial", 14, "bold"))
WelcomeLabel.pack(pady=20)

ButtonBack = ttk.Button(ArithmaticFrame, text="Back", command=lambda: BackCommand(ArithmaticFrame))
ButtonBack.pack(padx=10, side="top", anchor="nw")

Addition = ttk.Button(ArithmaticFrame, text="1. Addition", command=lambda: ft.MenuButton(AdditionFrame, ArithmaticFrame))
Addition.pack(fill="x", pady=5, ipady=10)

Subtraction = ttk.Button(ArithmaticFrame, text="2. Subtraction", command=lambda: ft.MenuButton(SubtractionFrame, ArithmaticFrame))
Subtraction.pack(fill="x", pady=5, ipady=10)

Division = ttk.Button(ArithmaticFrame, text="3. Division", command=lambda: ft.MenuButton(DivisionFrame, ArithmaticFrame))
Division.pack(fill="x", pady=5, ipady=10)

Multiplication = ttk.Button(ArithmaticFrame, text="4. Multiplication", command=lambda: ft.MenuButton(MultiplicationFrame, ArithmaticFrame))
Multiplication.pack(fill="x", pady=5, ipady=10)

# Addition Frame
AdditionFrame = ttk.Frame(root)

ButtonBack = ttk.Button(AdditionFrame, text="Back", command=lambda: BackCommand(AdditionFrame, Arithmatic=True))
ButtonBack.pack(padx=10, side="top", anchor="nw")

EquationFrame = ttk.Frame(AdditionFrame)
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

PlusSign = ttk.Label(EquationFrame, text="+", font=("Arial", 14, "bold"))
PlusSign.pack(pady=10, padx=10, side="left", anchor="center")

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

def OnButtonClickAddition():
    FirstNumerator = int(Numerator1Input.get())
    FirstDenominator = int(Denominator1Input.get())
    SecondNumerator = int(Numerator2Input.get())
    SecondDenominator = int(Denominator2Input.get())
    result = ft.Addition(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator)
    OutputLabel.config(text=str(result))

OutputLabel = ttk.Label(AdditionFrame, text="0", font=("Arial", 12))
OutputLabel.pack(pady=5, padx=5)

AddButton =ttk.Button(AdditionFrame, text="Add", command=OnButtonClickAddition)
AddButton.pack(pady=10, padx=10)

# Subraction Frame
SubtractionFrame = ttk.Frame(root)

ButtonBack = ttk.Button(SubtractionFrame, text="Back", command=lambda: BackCommand(SubtractionFrame, Arithmatic=True))
ButtonBack.pack(padx=10, side="top", anchor="nw")

EquationFrame = ttk.Frame(SubtractionFrame)
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

MinusSign = ttk.Label(EquationFrame, text="-", font=("Arial", 14, "bold"))
MinusSign.pack(pady=10, padx=10, side="left", anchor="center")

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

def OnButtonClickSubtraction():
    FirstNumerator = int(Numerator1Input.get())
    FirstDenominator = int(Denominator1Input.get())
    SecondNumerator = int(Numerator2Input.get())
    SecondDenominator = int(Denominator2Input.get())
    result = ft.Subtraction(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator)
    OutputLabel.config(text=str(result))

OutputLabel = ttk.Label(SubtractionFrame, text="0", font=("Arial", 12))
OutputLabel.pack(pady=5, padx=5)

SubtractButton =ttk.Button(SubtractionFrame, text="Subtract", command=OnButtonClickSubtraction)
SubtractButton.pack(pady=10, padx=10)

# Division Frame
DivisionFrame = ttk.Frame(root)

ButtonBack = ttk.Button(DivisionFrame, text="Back", command=lambda: BackCommand(DivisionFrame, Arithmatic=True))
ButtonBack.pack(padx=10, side="top", anchor="nw")

EquationFrame = ttk.Frame(DivisionFrame)
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

DivisionSign = ttk.Label(EquationFrame, text="÷", font=("Arial", 14, "bold"))
DivisionSign.pack(pady=10, padx=10, side="left", anchor="center")

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

def OnButtonClickDivision():
    FirstNumerator = int(Numerator1Input.get())
    FirstDenominator = int(Denominator1Input.get())
    SecondNumerator = int(Numerator2Input.get())
    SecondDenominator = int(Denominator2Input.get())
    result = ft.Division(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator)
    OutputLabel.config(text=str(result))

OutputLabel = ttk.Label(DivisionFrame, text="0", font=("Arial", 12))
OutputLabel.pack(pady=5, padx=5)

DivideButton =ttk.Button(DivisionFrame, text="Divide", command=OnButtonClickDivision)
DivideButton.pack(pady=10, padx=10)
root.mainloop()