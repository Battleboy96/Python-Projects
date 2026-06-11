import random
import time
import int_checker

def main():
    ErrorMessage = "Oops! You're gonna need to use a number next time! XP"
    MinNumber = int_checker.conv_input("Enter a minimum number: ", ErrorMessage)
    MaxNumber = int_checker.conv_input("Enter a minimum number: ", ErrorMessage)
    UsrGuess = int_checker.conv_input("Now guess!", ErrorMessage)
    if UsrGuess == random.randinit(MinNumber, MaxNumber):
        print("Oh ho! That's correct!")
        time.sleep(0.5)
    else:
        print("Oops! That's wrong!")
        time.sleep(0.5)
