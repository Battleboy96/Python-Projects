import math
import fractions

def CheckInt(EntryField, AllowZero=True):
    Variable = int(EntryField)
    if not AllowZero and Variable == 0:
        raise ValueError
    else:
        return Variable

def SignFlip(Denominator, Numerator):
    if Denominator < 0:
        Denominator *= -1
        Numerator *= -1
    return Denominator, Numerator

# Create Mixed to Improper function
def MixedToImproper(MixedWhole, MixedNumerator, MixedDenominator):
    MixedWholeInt = CheckInt(MixedWhole)
    MixedNumeratorInt = CheckInt(MixedNumerator)
    MixedDenominatorInt = CheckInt(MixedDenominator, AllowZero=False)

    IsNegative = (MixedWholeInt < 0) or (MixedNumeratorInt < 0) or (MixedDenominatorInt < 0)

    AbsWhole = abs(MixedWholeInt)
    AbsNumerator = abs(MixedNumeratorInt)
    AbsDenominator = abs(MixedDenominatorInt)

    ImproperNumerator = AbsWhole * AbsDenominator + AbsNumerator
    
    if IsNegative == True:
        return(f"-{ImproperNumerator}/{AbsDenominator}")
    else:
        return(f"{ImproperNumerator}/{AbsDenominator}")

# Create Improper to Mixed function
def ImproperToMixed(ImproperNumerator, ImproperDenominator):
    ImproperNumeratorInt = CheckInt(ImproperNumerator)
    ImproperDenominatorInt = CheckInt(ImproperDenominator, AllowZero=False)

    if (ImproperNumeratorInt < 0) != (ImproperDenominatorInt < 0):
        IsNegative = True
    else:
        IsNegative = False

    AbsNumerator = abs(ImproperNumeratorInt)
    AbsDenominator = abs(ImproperDenominatorInt)
    Quotient, Remainder = divmod(AbsNumerator, AbsDenominator)
    if Remainder == 0:
        if IsNegative:
            return(f"-{Quotient}")

        else:
            return(Quotient)

    else:
        if IsNegative == True:
            return(f"-{Quotient} and {Remainder}/{AbsDenominator}")
        else:
            return(f"{Quotient} and {Remainder}/{AbsDenominator}")

# Create Simplify function
def Simplify(Numerator, Denominator, ShowMessage=True):
    Denominator, Numerator = SignFlip(Denominator, Numerator)

    CommonDivisor = math.gcd(Numerator, Denominator)
    SimplifiedNumerator = Numerator // CommonDivisor
    SimplifiedDenominator = Denominator // CommonDivisor

    if SimplifiedDenominator == 1:
        return(f"{SimplifiedNumerator}")

    elif CommonDivisor == 1:
        if ShowMessage:
            return ValueError
        else:
            return(f"{Numerator}/{Denominator}")

    else:
        return(f"{SimplifiedNumerator}/{SimplifiedDenominator}")

# Create Fraction to Decimal function
def FractionToDecimal(Numerator, Denominator):
    Numerator = CheckInt(Numerator)
    Denominator = CheckInt(Denominator, AllowZero=False)
    Denominator, Numerator = SignFlip(Denominator, Numerator)
    
    if Denominator == 0:
        return ValueError

    Decimal = Numerator / Denominator
    return(f"{round(Decimal, 4)}")

# Create Decimal to Fraction function
def DecimalToFraction(Decimal):
    while True:
        try:
            ConvertedFraction = fractions.Fraction(Decimal)
            Numerator = ConvertedFraction.numerator
            Denominator = ConvertedFraction.denominator

        except ValueError:
            return ValueError

        return(f"{Numerator}/{Denominator}")

# Create addition function
def Addition(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator):
    FirstNumerator = CheckInt(FirstNumerator)
    FirstDenominator = CheckInt(FirstDenominator, AllowZero=False)
    SecondNumerator = CheckInt(SecondNumerator)
    SecondDenominator = CheckInt(SecondDenominator, AllowZero=False)

    if FirstDenominator == SecondDenominator:
        ResultNumerator = FirstNumerator + SecondNumerator
        return Simplify(ResultNumerator, FirstDenominator, ShowMessage=False)
    else:
        CommonDenominator = math.lcm(FirstDenominator, SecondDenominator)
        CommonFirstNumerator = FirstNumerator * (CommonDenominator // FirstDenominator)
        CommonSecondNumerator = SecondNumerator * (CommonDenominator // SecondDenominator)
        FinalNumerator = CommonFirstNumerator + CommonSecondNumerator
        return Simplify(FinalNumerator, CommonDenominator, ShowMessage=False)

# Create Subtraction function
def Subtraction(FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator):
    FirstNumerator = CheckInt(FirstNumerator)
    FirstDenominator = CheckInt(FirstDenominator, AllowZero=False)
    SecondNumerator = CheckInt(SecondNumerator)
    SecondDenominator = CheckInt(SecondDenominator, AllowZero=False)

    if FirstDenominator == SecondDenominator:
        ResultNumerator = FirstNumerator - SecondNumerator
        return Simplify(ResultNumerator, FirstDenominator, ShowMessage=False)
    else:
        CommonDenominator = math.lcm(FirstDenominator, SecondDenominator)
        CommonFirstNumerator = FirstNumerator * (CommonDenominator // FirstDenominator)
        CommonSecondNumerator = SecondNumerator * (CommonDenominator // SecondDenominator)
        FinalNumerator = CommonFirstNumerator - CommonSecondNumerator
        return Simplify(FinalNumerator, CommonDenominator, ShowMessage=False)

# Create Multiplication function
def Multiplication():
    FirstNumerator = CheckInt("First numerator")
    FirstDenominator = CheckInt("First denominator", AllowZero=False)
    SecondNumerator = CheckInt("Second numerator")
    SecondDenominator = CheckInt("Second denominator", AllowZero=False)
    FinalDenominator = FirstDenominator * SecondDenominator
    FinalNumerator = FirstNumerator * SecondNumerator
    Simplify(FinalNumerator, FinalDenominator, ShowMessage=False)
    input("Press enter to continue...")

# Create Division function
def Division():
    FirstNumerator = CheckInt("First numerator")
    FirstDenominator = CheckInt("First denominator", AllowZero=False)
    SecondNumerator = CheckInt("Second numerator")
    SecondDenominator = CheckInt("Second denominator", AllowZero=False)
    FinalDenominator = FirstDenominator * SecondNumerator
    FinalNumerator = FirstNumerator * SecondDenominator
    Simplify(FinalNumerator, FinalDenominator, ShowMessage=False)
    input("Press enter to continue...")

# Frame Switch Function
def SwitchFrames(Frame1, Frame2):
    if Frame1.winfo_viewable():
        Frame1.pack_forget()
        Frame2.pack(pady=10, padx=10, fill="both", expand=True)
    elif Frame2.winfo_viewable():
        Frame2.pack_forget()
        Frame1.pack(pady=10, padx=10, fill="both", expand=True)
        
# Menu Button
def MenuButton(MenuName, MainMenuFrame):
    MainMenuFrame.pack_forget()
    MenuName.pack(pady=20, padx=10, fill="both", expand=True)