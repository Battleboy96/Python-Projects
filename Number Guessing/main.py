import random
import time

# Create number to guess between 1 and 10
number = random.randint(1, 10)

# Get user input as guess
print("Guess a number between 1 and 10")
guess = int(input())

# Check if guess is correct
if guess == number:
    print("You guessed the number!")

else:
    print("Wrong guess, the number was", number)
    # Tell user how far off they were
    time.sleep(0.5) # Pause for visual appeal
    print("You were off by", abs(guess - number))

time.sleep(0.5)