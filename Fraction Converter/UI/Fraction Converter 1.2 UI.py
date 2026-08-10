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
root.geometry("400x400")

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

NumeratorFrame = ttk.Frame(SimplifyFrame)
NumeratorFrame.pack(pady=10, padx=10)
SimplifyNumeratorHint = ft.HintLabel("Numerator", NumeratorFrame)
SimplifyNumeratorInput = ttk.Entry(NumeratorFrame)
SimplifyNumeratorInput.pack()

DenominatorFrame = ttk.Frame(SimplifyFrame)
DenominatorFrame.pack(pady=10, padx=10)
SimplifyDenominatorHint = ft.HintLabel("Denominator", DenominatorFrame)
SimplifyDenominatorInput = ttk.Entry(DenominatorFrame)
SimplifyDenominatorInput.pack()

def OnButtonClickSimplify():
    Numerator = int(SimplifyNumeratorInput.get())
    Denominator = int(SimplifyDenominatorInput.get())

    Result = ft.Simplify(Numerator, Denominator, ShowMessage=True)
    if Result == ValueError:
        messagebox.showwarning("Error", f"This fraction is already in its simplest form! {Numerator}/{Denominator}")
    else:
        SimplifiedOutput.config(text=str(Result))

ButtonSimplify = ttk.Button(SimplifyFrame, text="Simplify", command=OnButtonClickSimplify)
ButtonSimplify.pack(pady=10)

SimplifiedOutput = ttk.Label(SimplifyFrame, text="0", font=("Arial", 12), foreground="black", justify="center")
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

ItMNumeratorFrame = ttk.Frame(ImproperMixedFrame)
ItMNumeratorFrame.pack(pady=10, padx=10)
ItMImproperNumeratorInput = ttk.Entry(ItMNumeratorFrame)
ItMImproperNumeratorInput.pack()
NumeratorHint = ft.HintLabel("Numerator", ItMNumeratorFrame)

ItMDenominatorFrame = ttk.Frame(ImproperMixedFrame)
ItMDenominatorFrame.pack(pady=5, padx=10)
ItMImproperDenominatorInput = ttk.Entry(ItMDenominatorFrame)
ItMImproperDenominatorInput.pack()
DenominatorHint = ft.HintLabel("Denominator", ItMDenominatorFrame)

def OnButtonClickItM():
    ImproperNumerator = ItMImproperNumeratorInput.get()
    ImproperDenominator = ItMImproperDenominatorInput.get()

    Result = ft.ImproperToMixed(ImproperNumerator, ImproperDenominator)
    MixedOutput.config(text=str(Result))

ConvertButton = ttk.Button(ImproperMixedFrame, text="Convert Improper to Mixed", command=OnButtonClickItM)
ConvertButton.pack(pady=20)

MixedOutput = ttk.Label(ImproperMixedFrame, text="0", font=("Arial", 12), foreground="black", justify="center")
MixedOutput.pack(pady=10)

# Mixed to Improper Conversion Frame
MixedImproperFrame = ttk.Frame(IMConversionFrame)

MtIWholeFrame = ttk.Frame(MixedImproperFrame)
MtIWholeFrame.pack(pady=50, padx=10, side="left", anchor="n")
MtIWholeInput = ttk.Entry(MtIWholeFrame)
MtIWholeInput.pack()
MtIWholeHint = ft.HintLabel("Whole Number", MtIWholeFrame)
MtIWholeHint.pack(pady=5)

MtINumeratorFrame = ttk.Frame(MixedImproperFrame)
MtINumeratorFrame.pack(pady=10, padx=10)
MtINumeratorInput = ttk.Entry(MtINumeratorFrame)
MtINumeratorInput.pack()
MtINumeratorHint = ft.HintLabel("Numerator", MtINumeratorFrame)

MtIDenominatorFrame = ttk.Frame(MixedImproperFrame)
MtIDenominatorFrame.pack(pady=5, padx=10)
MtIDenominatorInput = ttk.Entry(MtIDenominatorFrame)
MtIDenominatorInput.pack()
MtIDenominatorHint = ft.HintLabel("Denominator", MtIDenominatorFrame)
MtIDenominatorHint.pack(pady=5)

def OnButtonClickMtI():
    MixedWhole = MtIWholeInput.get()
    MixedNumerator = MtINumeratorInput.get()
    MixedDenominator = MtIDenominatorInput.get()

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
DecimalHint = ft.HintLabel("Decimal", DecimalFrame)
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

FtDNumiratorFrame = ttk.Frame(FractionDecimalFrame)
FtDNumiratorFrame.pack(pady=5, padx=10)
FtDNumiratorHint = ft.HintLabel("Numerator", FtDNumiratorFrame)
FtDNumiratorHint.pack(pady=5)
FtDNumiratorInput = ttk.Entry(FtDNumiratorFrame)
FtDNumiratorInput.pack()

FtDDenominatorFrame = ttk.Frame(FractionDecimalFrame)
FtDDenominatorFrame.pack(pady=5, padx=10)
FtDDenominatorHint = ft.HintLabel("Denominator", FtDDenominatorFrame)
FtDDenominatorHint.pack(pady=5)
FtDDenominatorInput = ttk.Entry(FtDDenominatorFrame)
FtDDenominatorInput.pack()

def OnButtonClickFtD():
    Numerator = int(FtDNumiratorInput.get())
    Denominator = int(FtDDenominatorInput.get())
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

AddEquationFrame = ttk.Frame(AdditionFrame)
AddEquationFrame.pack(pady=10, padx=10, anchor="center")

# Create Fraction 1 Frame
AddFraction1Frame = ttk.Frame(AddEquationFrame)
AddFraction1Frame.pack(pady=10, padx=10, side="left", anchor="w")

# Create Numerator 1 Frame
AddNumerator1Frame = ttk.Frame(AddFraction1Frame)
AddNumerator1Frame.pack(padx=10, pady=10, )
AddNumerator1Hint = ft.HintLabel("Numerator 1:", AddNumerator1Frame)
AddNumerator1Hint.pack(padx=5, pady=5, side="top")
AddNumerator1Input = ttk.Entry(AddNumerator1Frame)
AddNumerator1Input.pack(side="top", padx=5)

# Create Denominator 1 Frame
AddDenominator1Frame = ttk.Frame(AddFraction1Frame)
AddDenominator1Frame.pack(padx=10, pady=10, )
AddDenominator1Hint = ft.HintLabel("Denominator 1:", AddDenominator1Frame)
AddDenominator1Hint.pack(padx=5, pady=5, side="top")
AddDenominator1Input = ttk.Entry(AddDenominator1Frame)
AddDenominator1Input.pack(side="top", padx=5)

PlusSign = ttk.Label(AddEquationFrame, text="+", font=("Arial", 14, "bold"))
PlusSign.pack(pady=10, padx=10, side="left", anchor="center")

# Create Fraction 2 Frame
AddFraction2Frame = ttk.Frame(AddEquationFrame)
AddFraction2Frame.pack(pady=10, side="left", anchor="e")

# Create Numerator 2 Frame
AddNumerator2Frame = ttk.Frame(AddFraction2Frame)
AddNumerator2Frame.pack(pady=10, padx=10, )
AddNumerator2Hint = ft.HintLabel("Numerator 2:", AddNumerator2Frame)
AddNumerator2Hint.pack(padx=5, pady=5, side="top")
AddNumerator2Input = ttk.Entry(AddNumerator2Frame)
AddNumerator2Input.pack(side="top", padx=5)

# Create Denominator 2 Frame
AddDenominator2Frame = ttk.Frame(AddFraction2Frame)
AddDenominator2Frame.pack(pady=10, padx=10, )
AddDenominator2Hint = ft.HintLabel("Denominator 2:", AddDenominator2Frame)
AddDenominator2Hint.pack(padx=5, pady=5, side="top")
AddDenominator2Input = ttk.Entry(AddDenominator2Frame)
AddDenominator2Input.pack(side="top", padx=5)

def OnButtonClickAddition():
    FirstNumerator = int(AddNumerator1Input.get())
    FirstDenominator = int(AddDenominator1Input.get())
    SecondNumerator = int(AddNumerator2Input.get())
    SecondDenominator = int(AddDenominator2Input.get())
    result = ft.Addition(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator)
    AddOutputLabel.config(text=str(result))

AddOutputLabel = ttk.Label(AdditionFrame, text="0", font=("Arial", 12))
AddOutputLabel.pack(pady=5, padx=5)

AddButton =ttk.Button(AdditionFrame, text="Add", command=OnButtonClickAddition)
AddButton.pack(pady=10, padx=10)

# Subraction Frame
SubtractionFrame = ttk.Frame(root)

ButtonBack = ttk.Button(SubtractionFrame, text="Back", command=lambda: BackCommand(SubtractionFrame, Arithmatic=True))
ButtonBack.pack(padx=10, side="top", anchor="nw")

SubEquationFrame = ttk.Frame(SubtractionFrame)
SubEquationFrame.pack(pady=10, padx=10, anchor="center")

# Create Fraction 1 Frame
SubFraction1Frame = ttk.Frame(SubEquationFrame)
SubFraction1Frame.pack(pady=10, padx=10, side="left", anchor="w")

# Create Numerator 1 Frame
SubNumerator1Frame = ttk.Frame(SubFraction1Frame)
SubNumerator1Frame.pack(padx=10, pady=10, )
SubNumerator1Hint = ft.HintLabel("Numerator 1:", SubNumerator1Frame)
SubNumerator1Hint.pack(padx=5, pady=5, side="top")
SubNumerator1Input = ttk.Entry(SubNumerator1Frame)
SubNumerator1Input.pack(side="top", padx=5)

# Create Denominator 1 Frame
SubDenominator1Frame = ttk.Frame(SubFraction1Frame)
SubDenominator1Frame.pack(padx=10, pady=10, )
SubDenominator1Hint = ft.HintLabel("Denominator 1:", SubDenominator1Frame)
SubDenominator1Hint.pack(padx=5, pady=5, side="top")
SubDenominator1Input = ttk.Entry(SubDenominator1Frame)
SubDenominator1Input.pack(side="top", padx=5)

MinusSign = ttk.Label(SubEquationFrame, text="-", font=("Arial", 14, "bold"))
MinusSign.pack(pady=10, padx=10, side="left", anchor="center")

# Create Fraction 2 Frame
SubFraction2Frame = ttk.Frame(SubEquationFrame)
SubFraction2Frame.pack(pady=10, side="left", anchor="e")

# Create Numerator 2 Frame
SubNumerator2Frame = ttk.Frame(SubFraction2Frame)
SubNumerator2Frame.pack(pady=10, padx=10, )
SubNumerator2Hint = ft.HintLabel("Numerator 2:", SubNumerator2Frame)
SubNumerator2Hint.pack(padx=5, pady=5, side="top")
SubNumerator2Input = ttk.Entry(SubNumerator2Frame)
SubNumerator2Input.pack(side="top", padx=5)

# Create Denominator 2 Frame
SubDenominator2Frame = ttk.Frame(SubFraction2Frame)
SubDenominator2Frame.pack(pady=10, padx=10, )
SubDenominator2Hint = ft.HintLabel("Denominator 2:", SubDenominator2Frame)
SubDenominator2Hint.pack(padx=5, pady=5, side="top")
SubDenominator2Input = ttk.Entry(SubDenominator2Frame)
SubDenominator2Input.pack(side="top", padx=5)

def OnButtonClickSubtraction():
    FirstNumerator = int(SubNumerator1Input.get())
    FirstDenominator = int(SubDenominator1Input.get())
    SecondNumerator = int(SubNumerator2Input.get())
    SecondDenominator = int(SubDenominator2Input.get())
    result = ft.Subtraction(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator)
    SubOutputLabel.config(text=str(result))

SubOutputLabel = ttk.Label(SubtractionFrame, text="0", font=("Arial", 12))
SubOutputLabel.pack(pady=5, padx=5)

SubtractButton =ttk.Button(SubtractionFrame, text="Subtract", command=OnButtonClickSubtraction)
SubtractButton.pack(pady=10, padx=10)

# Division Frame
DivisionFrame = ttk.Frame(root)

ButtonBack = ttk.Button(DivisionFrame, text="Back", command=lambda: BackCommand(DivisionFrame, Arithmatic=True))
ButtonBack.pack(padx=10, side="top", anchor="nw")

DivEquationFrame = ttk.Frame(DivisionFrame)
DivEquationFrame.pack(pady=10, padx=10, anchor="center")

# Create Fraction 1 Frame
DivFraction1Frame = ttk.Frame(DivEquationFrame)
DivFraction1Frame.pack(pady=10, padx=10, side="left", anchor="w")

# Create Numerator 1 Frame
DivNumerator1Frame = ttk.Frame(DivFraction1Frame)
DivNumerator1Frame.pack(padx=10, pady=10, )
DivNumerator1Hint = ft.HintLabel("Numerator 1:", DivNumerator1Frame)
DivNumerator1Hint.pack(padx=5, pady=5, side="top")
DivNumerator1Input = ttk.Entry(DivNumerator1Frame)
DivNumerator1Input.pack(side="top", padx=5)

# Create Denominator 1 Frame
DivDenominator1Frame = ttk.Frame(DivFraction1Frame)
DivDenominator1Frame.pack(padx=10, pady=10, )
DivDenominator1Hint = ft.HintLabel("Denominator 1:", DivDenominator1Frame)
DivDenominator1Hint.pack(padx=5, pady=5, side="top")
DivDenominator1Input = ttk.Entry(DivDenominator1Frame)
DivDenominator1Input.pack(side="top", padx=5)

DivisionSign = ttk.Label(DivEquationFrame, text="÷", font=("Arial", 14, "bold"))
DivisionSign.pack(pady=10, padx=10, side="left", anchor="center")

# Create Fraction 2 Frame
DivFraction2Frame = ttk.Frame(DivEquationFrame)
DivFraction2Frame.pack(pady=10, side="left", anchor="e")

# Create Numerator 2 Frame
DivNumerator2Frame = ttk.Frame(DivFraction2Frame)
DivNumerator2Frame.pack(pady=10, padx=10, )
DivNumerator2Hint = ft.HintLabel("Numerator 2:", DivNumerator2Frame)
DivNumerator2Hint.pack(padx=5, pady=5, side="top")
DivNumerator2Input = ttk.Entry(DivNumerator2Frame)
DivNumerator2Input.pack(side="top", padx=5)

# Create Denominator 2 Frame
DivDenominator2Frame = ttk.Frame(DivFraction2Frame)
DivDenominator2Frame.pack(pady=10, padx=10, )
DivDenominator2Hint = ft.HintLabel("Denominator 2:", DivDenominator2Frame)
DivDenominator2Hint.pack(padx=5, pady=5, side="top")
DivDenominator2Input = ttk.Entry(DivDenominator2Frame)
DivDenominator2Input.pack(side="top", padx=5)

def OnButtonClickDivision():
    FirstNumerator = int(DivNumerator1Input.get())
    FirstDenominator = int(DivDenominator1Input.get())
    SecondNumerator = int(DivNumerator2Input.get())
    SecondDenominator = int(DivDenominator2Input.get())
    result = ft.Division(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator)
    DivOutputLabel.config(text=str(result))

DivOutputLabel = ttk.Label(DivisionFrame, text="0", font=("Arial", 12))
DivOutputLabel.pack(pady=5, padx=5)

DivideButton =ttk.Button(DivisionFrame, text="Divide", command=OnButtonClickDivision)
DivideButton.pack(pady=10, padx=10)

# Multiplication Frame
MultiplicationFrame = ttk.Frame(root)

ButtonBack = ttk.Button(MultiplicationFrame, text="Back", command=lambda: BackCommand(MultiplicationFrame, Arithmatic=True))
ButtonBack.pack(padx=10, side="top", anchor="nw")

MultEquationFrame = ttk.Frame(MultiplicationFrame)
MultEquationFrame.pack(pady=10, padx=10, anchor="center")

# Create Fraction 1 Frame
MultFraction1Frame = ttk.Frame(MultEquationFrame)
MultFraction1Frame.pack(pady=10, padx=10, side="left", anchor="w")

# Create Numerator 1 Frame
MultNumerator1Frame = ttk.Frame(MultFraction1Frame)
MultNumerator1Frame.pack(padx=10, pady=10, )
MultNumerator1Hint = ft.HintLabel("Numerator 1:", MultNumerator1Frame)
MultNumerator1Hint.pack(padx=5, pady=5, side="top")
MultNumerator1Input = ttk.Entry(MultNumerator1Frame)
MultNumerator1Input.pack(side="top", padx=5)

# Create Denominator 1 Frame
MultDenominator1Frame = ttk.Frame(MultFraction1Frame)
MultDenominator1Frame.pack(padx=10, pady=10, )
MultDenominator1Hint = ft.HintLabel("Denominator 1:", MultDenominator1Frame)
MultDenominator1Hint.pack(padx=5, pady=5, side="top")
MultDenominator1Input = ttk.Entry(MultDenominator1Frame)
MultDenominator1Input.pack(side="top", padx=5)

MultiplicationSign = ttk.Label(MultEquationFrame, text="x", font=("Arial", 14, "bold"))
MultiplicationSign.pack(pady=10, padx=10, side="left", anchor="center")

# Create Fraction 2 Frame
MultFraction2Frame = ttk.Frame(MultEquationFrame)
MultFraction2Frame.pack(pady=10, side="left", anchor="e")

# Create Numerator 2 Frame
MultNumerator2Frame = ttk.Frame(MultFraction2Frame)
MultNumerator2Frame.pack(pady=10, padx=10, )
MultNumerator2Hint = ft.HintLabel("Numerator 2:", MultNumerator2Frame)
MultNumerator2Hint.pack(padx=5, pady=5, side="top")
MultNumerator2Input = ttk.Entry(MultNumerator2Frame)
MultNumerator2Input.pack(side="top", padx=5)

# Create Denominator 2 Frame
MultDenominator2Frame = ttk.Frame(MultFraction2Frame)
MultDenominator2Frame.pack(pady=10, padx=10, )
MultDenominator2Hint = ft.HintLabel("Denominator 2:", MultDenominator2Frame)
MultDenominator2Hint.pack(padx=5, pady=5, side="top")
MultDenominator2Input = ttk.Entry(MultDenominator2Frame)
MultDenominator2Input.pack(side="top", padx=5)

def OnButtonClickMultiplication():
    FirstNumerator = int(MultNumerator1Input.get())
    FirstDenominator = int(MultDenominator1Input.get())
    SecondNumerator = int(MultNumerator2Input.get())
    SecondDenominator = int(MultDenominator2Input.get())
    result = ft.Multiplication(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator)
    MultOutputLabel.config(text=str(result))

MultOutputLabel = ttk.Label(MultiplicationFrame, text="0", font=("Arial", 12))
MultOutputLabel.pack(pady=5, padx=5)

MultiplyButton =ttk.Button(MultiplicationFrame, text="Multiply", command=OnButtonClickMultiplication)
MultiplyButton.pack(pady=10, padx=10)
root.mainloop()