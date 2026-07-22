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
def ImproperToMixed():
    ImproperNumerator = CheckInt("Numerator")
    ImproperDenominator = CheckInt("Denominator", AllowZero=False)

    if (ImproperNumerator < 0) != (ImproperDenominator < 0):
        IsNegative = True
    else:
        IsNegative = False

    AbsNumerator = abs(ImproperNumerator)
    AbsDenominator = abs(ImproperDenominator)
    Quotient, Remainder = divmod(AbsNumerator, AbsDenominator)
    if Remainder == 0:
        if IsNegative:
            print(f"-{Quotient}")

        else:
            print(Quotient)

    else:
        if IsNegative == True:
            print(f"-{Quotient} and {Remainder}/{AbsDenominator}")
        else:
            print(f"{Quotient} and {Remainder}/{AbsDenominator}")
    input("Press enter to continue...")

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
            return(f"This fraction is already in its simplest form!\n{Numerator}/{Denominator}")
        else:
            return(f"{Numerator}/{Denominator}")

    else:
        return(f"{SimplifiedNumerator}/{SimplifiedDenominator}")

# Create Fraction to Decimal function
def FractionToDecimal():
    Numerator = CheckInt("Numerator")
    Denominator = CheckInt("Denominator", AllowZero=False)
    Denominator, Numerator = SignFlip(Denominator, Numerator)
    
    if Denominator == 0:
        print("Error: Denominator cannot be zero.")
        input("Press enter to continue...")
        return
    decimal = Numerator / Denominator
    print(f"{round(decimal, 4)}")
    input("Press enter to continue...")

# Create Decimal to Fraction function
def DecimalToFraction():
    while True:
        Decimal = input("Please input a decimal number: ")
        
        try:
            ConvertedFraction = fractions.Fraction(Decimal)
            Numerator = ConvertedFraction.numerator
            Denominator = ConvertedFraction.denominator

        except ValueError:
            print("Please input a valid decimal number")
            continue

        print(f"{Numerator}/{Denominator}")
        input("Press enter to continue...")
        return

# Create addition function
def Addition():
    FirstNumerator = CheckInt("First numerator")
    FirstDenominator = CheckInt("First denominator", AllowZero=False)
    SecondNumerator = CheckInt("Second numerator")
    SecondDenominator = CheckInt("Second denominator", AllowZero=False)

    if FirstDenominator == SecondDenominator:
        ResultNumerator = FirstNumerator + SecondNumerator
        Simplify(ResultNumerator, FirstDenominator, ShowMessage=False)
    else:
        CommonDenominator = math.lcm(FirstDenominator, SecondDenominator)
        CommonFirstNumerator = FirstNumerator * (CommonDenominator // FirstDenominator)
        CommonSecondNumerator = SecondNumerator * (CommonDenominator // SecondDenominator)
        FinalNumerator = CommonFirstNumerator + CommonSecondNumerator
        Simplify(FinalNumerator, CommonDenominator, ShowMessage=False)
    input("Press enter to continue...")

# Create Subtraction function
def Subtraction():
    FirstNumerator = CheckInt("First numerator")
    FirstDenominator = CheckInt("First denominator", AllowZero=False)
    SecondNumerator = CheckInt("Second numerator")
    SecondDenominator = CheckInt("Second denominator", AllowZero=False)

    if FirstDenominator == SecondDenominator:
        ResultNumerator = FirstNumerator - SecondNumerator
        Simplify(ResultNumerator, FirstDenominator, ShowMessage=False)
    else:
        CommonDenominator = math.lcm(FirstDenominator, SecondDenominator)
        CommonFirstNumerator = FirstNumerator * (CommonDenominator // FirstDenominator)
        CommonSecondNumerator = SecondNumerator * (CommonDenominator // SecondDenominator)
        FinalNumerator = CommonFirstNumerator - CommonSecondNumerator
        Simplify(FinalNumerator, CommonDenominator, ShowMessage=False)
    input("Press enter to continue...")

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