import time

# Program loop
while True:
    def main():

        # Create Mixed to Improper function
        def M2I():
            while True:
                try:
                    mixed_whole = int(input("Please input the whole: "))
                    break
                except ValueError:
                    print("Please input a number")
                    
            while True:
                try:
                    mixed_numirator = int(input("Please input the numirator: "))
                    break
                except ValueError:
                    print("Please input a number")

            while True:
                try:
                    mixed_denominator = int(input("Please input the denominator: "))
                    break
                except ValueError:
                    print("Please input a number")

            improper_nurmirator = str(mixed_whole * mixed_denominator + mixed_numirator)
            print(improper_nurmirator + "/" + str(mixed_denominator))
            input("Press enter to continue...")

        # Create Improper to Mixed function
        def I2M():
            while True:
                try:
                    improper_nurmirator = int(input("Please input the numirator: "))
                    break
                except ValueError:
                    print("Please input a number")
            while True:
                try:
                    improper_denominator = int(input("Please input the denominator: "))
                    break
                except ValueError:
                    print("Please input a number")

            quotient, remainder = divmod(improper_nurmirator, improper_denominator)
            if remainder == 0:
                print(quotient)
            else:
                print(quotient, "and", remainder, "/", improper_denominator)
            input("Press enter to continue...")

        # Mode Select
        print("This is a work in progress, please report any bugs you find")
        print("")
        time.sleep(0.3)
    
        chosen = False
        while chosen == False:
            while True:
                try:
                    mode = int(input("Please select a mode:\n1: Mixed to Improper\n2: Improper to Mixed\n3: Exit\n"))
                    chosen = True
                    break
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