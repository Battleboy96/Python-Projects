import math
import fractions

def CheckInt(type, AllowZero=True):
    while True:
        try:
            Variable = int(input(f"Please input the {type}: "))

            if not AllowZero and Variable == 0:
                print("Error: This number cannot be zero.")
                continue

            return Variable
        except ValueError:
            print("Please input a number")

def SignFlip(Denominator, Numerator):
    if Denominator < 0:
        Denominator *= -1
        Numerator *= -1
    return Denominator, Numerator

# Create Mixed to Improper function
def MixedToImproper():
    MixedWhole = CheckInt("whole number")
    MixedNumerator = CheckInt("Numerator")
    MixedDenominator = CheckInt("Denominator", AllowZero=False)

    IsNegative = (MixedWhole < 0) or (MixedNumerator < 0) or (MixedDenominator < 0)

    AbsWhole = abs(MixedWhole)
    AbsNumerator = abs(MixedNumerator)
    AbsDenominator = abs(MixedDenominator)

    ImproperNumerator = AbsWhole * AbsDenominator + AbsNumerator
    
    if IsNegative == True:
        print(f"-{ImproperNumerator}/{AbsDenominator}")
    else:
        print(f"{ImproperNumerator}/{AbsDenominator}")

    input("Press enter to continue...")

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