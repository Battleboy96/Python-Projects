import time
import math

# Disclaimer
print("This is a work in progress, please report any bugs you find")
print("")
time.sleep(0.3)

# Program loop
def main():
    def CheckInt(type, AllowZero=True):
        while True:
            try:
                variable = int(input(f"Please input the {type}: "))

                if not AllowZero and variable == 0:
                    print("Error: This number cannot be zero.")
                    continue # Loops back to try again without crashing or exiting!

                return variable
            except ValueError:
                print("Please input a number")

    def SignFlip(denominator, numerator):
        if denominator < 0:
            denominator *= -1
            numerator *= -1
        return denominator, numerator

    # Create Mixed to Improper function
    def MixedToImproper():
        MixedWhole = CheckInt("whole number")
        MixedNumerator = CheckInt("numerator")
        MixedDenominator = CheckInt("denominator", AllowZero=False)
        
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
        ImproperNumerator = CheckInt("numerator")
        ImproperDenominator = CheckInt("denominator", AllowZero=False)

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
        numerator = CheckInt("numerator")
        denominator = CheckInt("denominator", AllowZero=False)
        denominator, numerator = SignFlip(denominator, numerator)

        common_divisor = math.gcd(numerator, denominator)
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor

        if simplified_denominator == 1:
            print(f"{simplified_numerator}")

        elif common_divisor == 1:
            print("This fraction is already in its simplest form!")
            print(f"{numerator}/{denominator}")

        else:
            print(f"{simplified_numerator}/{simplified_denominator}")

        input("Press enter to continue...")

    def FractionToDecimal():
        numerator = CheckInt("numerator")
        denominator = CheckInt("denominator", AllowZero=False)
        denominator, numerator = SignFlip(denominator, numerator)
        
        if denominator == 0:
            print("Error: Denominator cannot be zero.")
            input("Press enter to continue...")
            return
        decimal = numerator / denominator
        print(f"{round(decimal, 4)}")

    # Mode Select
    while True:
        try:
            mode = int(input("Please select a mode:\n1: Mixed to Improper\n2: Improper to Mixed\n3: Simplify\n4: Fraction to Decimal\n5: Exit\n"))
            if mode < 1 or mode > 5:
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
            print("Exiting...")
            time.sleep(0.3)
            exit(0)
main()