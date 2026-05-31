import time
import math

# Disclaimer
print("This is a work in progress, please report any bugs you find")
print("")
time.sleep(0.3)

# Program loop
def main():
    def CheckInt(type, allow_zero=True):
        while True:
            try:
                variable = int(input(f"Please input the {type}: "))

                if not allow_zero and variable == 0:
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
        mixed_whole = CheckInt("whole number")
        mixed_numerator = CheckInt("numerator")
        mixed_denominator = CheckInt("denominator", allow_zero=False)
        
        is_negative = (mixed_whole < 0) or (mixed_numerator < 0) or (mixed_denominator < 0)
        
        abs_whole = abs(mixed_whole)
        abs_numerator = abs(mixed_numerator)
        abs_denominator = abs(mixed_denominator)
        
        improper_numerator = abs_whole * abs_denominator + abs_numerator
        
        if is_negative == True:
            print(f"-{improper_numerator}/{abs_denominator}")
        else:
            print(f"{improper_numerator}/{abs_denominator}")

        input("Press enter to continue...")

    # Create Improper to Mixed function
    def ImproperToMixed():
        improper_numerator = CheckInt("numerator")
        improper_denominator = CheckInt("denominator", allow_zero=False)

        if (improper_numerator < 0) != (improper_denominator < 0):
            is_negative = True
        else:
            is_negative = False

        abs_numerator = abs(improper_numerator)
        abs_denominator = abs(improper_denominator)
        quotient, remainder = divmod(abs_numerator, abs_denominator)
        if remainder == 0:
            if is_negative:
                print(f"-{quotient}")

            else:
                print(quotient)

        else:
            if is_negative == True:
                print(f"-{quotient} and {remainder}/{abs_denominator}")
            else:
                print(f"{quotient} and {remainder}/{abs_denominator}")
        input("Press enter to continue...")

    # Create Simplify function
    def Simplify():
        numerator = CheckInt("numerator")
        denominator = CheckInt("denominator", allow_zero=False)
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
        denominator = CheckInt("denominator", allow_zero=False)
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