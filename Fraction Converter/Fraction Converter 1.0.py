import time
import math
import fractions

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
    def Simplify():
        Numerator = CheckInt("Numerator")
        Denominator = CheckInt("Denominator", AllowZero=False)
        Denominator, Numerator = SignFlip(Denominator, Numerator)

        CommonDivisor = math.gcd(Numerator, Denominator)
        SimplifiedNumerator = Numerator // CommonDivisor
        SimplifiedDenominator = Denominator // CommonDivisor

        if SimplifiedDenominator == 1:
            print(f"{SimplifiedNumerator}")

        elif CommonDivisor == 1:
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

    # Mode Select
    while True:
        try:
            mode = int(input("Please select a mode:\n1: Mixed to Improper\n2: Improper to Mixed\n3: Simplify\n4: Fraction to Decimal\n5: Decimal to Fraction\n6: Exit\n"))
            if mode < 1 or mode > 6:
                print("Please select a valid mode")
                continue
        except ValueError:
            print("Please input a number")

        if mode == 1:
            MixedToImproper()
        if mode == 2:
            ImproperToMixed()
        if mode == 3:
            Simplify()
        if mode == 4:
            FractionToDecimal()
        if mode == 5:
            DecimalToFraction()
        if mode == 6:
            print("Exiting...")
            time.sleep(0.3)
            exit(0)
main()