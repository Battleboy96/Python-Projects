import sys
import time as t
import random as rand

var1 = 1
var2 = var1 + 1
var3 = var2 * 2
print(var3 + rand.randint(1, 10))

rand_wait = rand.randint(1, 5)
print(f"Waiting for {rand_wait} seconds...")
t.sleep(rand_wait)
print("Done waiting!")

if var3 == rand.randint(5, 14):
    print("Spontaneous combination!")
    sys.exit(0)
    
else:
    print("No spontaneous combination this time.")