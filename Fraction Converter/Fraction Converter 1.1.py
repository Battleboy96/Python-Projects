import time
import math
import fractions
import os

# Open Message
print("Fraction Converter 1.0 - By: Battleboy96")
print("Stable Release")
print("")
time.sleep(0.3)

# Program loop
def main():
    def CheckInt(type, AllowZero=True):
        while True:
            try:
                Variable = int(input(f"Please input the {type}: "))

                if not AllowZero and Variable == 0:
                    print("Error: This number cannot be zero.")
                    continue # Loops back to try again without crashing or exiting!

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
            print(f"{SimplifiedNumerator}")

        elif CommonDivisor == 1:
            if ShowMessage:
                print("This fraction is already in its simplest form!")
                print(f"{Numerator}/{Denominator}")

        else:
            print(f"{SimplifiedNumerator}/{SimplifiedDenominator}")
        input("Press enter to continue...")

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
        
    # Create arithmatic options menu
    def Arithmatic():

        
        ArithmaticMode = int(input("Please select an arithmatic mode:\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Return to main menu\n"))
        if ArithmaticMode == 1:
            Addition()
        if ArithmaticMode == 2:
            Subtraction()
        if ArithmaticMode == 3:
            Multiplication()
        if ArithmaticMode == 4:
            Division()

    # Mode Select
    while True:
        try:
            Mode = int(input("Please select a mode:\n1: Mixed to Improper\n2: Improper to Mixed\n3: Simplify\n4: Fraction to Decimal\n5: Decimal to Fraction\n6: Exit\n"))
            if Mode < 1 or Mode > 6:
                print("Please select a valid mode")
                continue
        except ValueError:
            print("Please input a number")
        input("Press enter to continue...")

        if mode == 1:
            MixedToImproper()
        if mode == 2:
            ImproperToMixed()
        if mode == 3:
            Numerator = CheckInt("Numerator")
            Denominator = CheckInt("Denominator", AllowZero=False)
            Simplify(Numerator, Denominator)
        if mode == 4:
            FractionToDecimal()
        if mode == 5:
            DecimalToFraction()
        if mode == 6:
            print("Exiting...")
            time.sleep(0.3)
            os.quit(0)
main()