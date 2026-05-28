import time

def main():
    print("Welcome to the mixed fraction converter!\n Turn mixed fractions into improper fractions!")
    time.sleep(0.3)
    print("This is a work in progress, please report any bugs you find")
    print("")
    
    mixed_whole = int(input("Please input the whole: "))
    mixed_numirator = int(input("Please input the numirator: "))
    mixed_denominator = int(input("Please input the denominator: "))
    
    improper_nurmirator = str(mixed_whole * mixed_denominator + mixed_numirator)
    print(improper_nurmirator + "/" + str(mixed_denominator))
    
main()