# Don't ask what this does! I have no idea and can't be bothered to read it.
import sys
import time
import random

var1 = 1
var2 = var1 + 1
var3 = var2 * 2
print(var3 + random.randint(1, 10))

rand_wait = random.randint(1, 5)
print(f"Waiting for {rand_wait} seconds...")
time.sleep(rand_wait)
print("Done waiting!")

if var3 == random.randint(5, 14):
    print("Spontaneous combination!")
    sys.exit(0)
    
else:
    print("No spontaneous combination this time.")