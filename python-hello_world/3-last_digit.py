#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

last_digit = abs(number) % 10

if number < 0:
    print("Last digit of", number, "is", -abs(last_digit), end=" ")
elif number > 0:
    print("Last digit of", number, "is", last_digit, end=" ")
   
# message if something is wrong
if last_digit > 5 and number > 0:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")