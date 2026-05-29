import time

# Disclaimer
print("This is a work in progress, please report any bugs you find")
print("")
time.sleep(0.3)

# Program loop
def main():
    def check_int(type):
        while True:
            try:
                variable = int(input(f"Please input the {type}: "))
                return variable
            except ValueError:
                print("Please input a number")
            
    # Create Mixed to Improper function
    def M2I():
        mixed_whole = check_int("whole number")
        mixed_numirator = check_int("numirator")
        mixed_denominator = check_int("denominator")

        improper_numerator = str(mixed_whole * mixed_denominator + mixed_numirator)
        print(f"{improper_numerator}/{mixed_denominator}")
        input("Press enter to continue...")

    # Create Improper to Mixed function
    def I2M():
        improper_numerator = check_int("numirator")
        improper_denominator = check_int("denominator")

        quotient, remainder = divmod(improper_numerator, improper_denominator)
        if remainder == 0:
            print(quotient)
        else:
            print(f"{quotient} and {remainder}/{improper_denominator}")
        input("Press enter to continue...")

    # Mode Select
    while True:
        try:
            mode = int(input("Please select a mode:\n1: Mixed to Improper\n2: Improper to Mixed\n3: Exit\n"))

        except ValueError:
            print("Please input a number")

        if mode == 1:
            M2I()
        if mode == 2:
            I2M()
        if mode == 3:
            print("Exiting...")
            time.sleep(0.3)
            exit(0)
main()