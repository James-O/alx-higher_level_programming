#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = 0

if number >= 0:
    lastnum = number % 10
else:
    lastnum = ((-number) % 10) * -1

display = f"Last digit of {number} is {lastnum}"

if lastnum == 0:
    print(f"{display} and is 0")
elif lastnum > 5 and lastnum % 10 != 0:
    print(f"{display} and is greater than 5")
else:
    print(f"{display} and is less than 6 and not 0")
