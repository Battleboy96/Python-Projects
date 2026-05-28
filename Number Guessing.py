import random
import time


number = random.randint(1, 10)


print("Guess a number between 1 and 10")
guess = int(input())


if guess == number:
    print("You guessed the number!")

else:
    print("Wrong guess, the number was", number)

    time.sleep(0.5)
    print("You were off by", abs(guess - number))

input("Press enter to exit")
