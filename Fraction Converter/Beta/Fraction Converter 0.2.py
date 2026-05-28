import time

def main():

    # Create Mixed to Improper function
    def M2I():
        mixed_whole = int(input("Please input the whole: "))
        mixed_numirator = int(input("Please input the numirator: "))
        mixed_denominator = int(input("Please input the denominator: "))
    
        improper_nurmirator = str(mixed_whole * mixed_denominator + mixed_numirator)
        print(improper_nurmirator + "/" + str(mixed_denominator))

    def I2M():
        improper_nurmirator = int(input("Please input the numirator: "))
        improper_denominator = int(input("Please input the denominator: "))
        quotient, remainder = divmod(improper_nurmirator, improper_denominator)
        print(quotient, "and", remainder, "/", improper_denominator)
    
    print("Welcome to the mixed fraction converter (0.2)!\nTurn mixed fractions into improper fractions!")
    time.sleep(0.3)
    print("This is a work in progress, please report any bugs you find")
    print("")
    time.sleep(0.3)
    
    chosen = False
    while chosen == False:
        while True:
            try:
                mode = input("Please select a mode:\n1: Mixed to Improper\n2: Improper to Mixed\n")
                mode = int(mode)
                chosen = True
                break
            except ValueError:
                print("Please input a number")
    
        if mode == 1:
            M2I()
        if mode == 2:
            I2M()

main()