#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
def status ():
    if (number % 10 > 5):
        return ("and is greater than 5")
    elif (number % 10 == 0): 
        return ("and is 0")
    elif (number % 10 < 6 and number % 10 != 0):
        return ("and is less than 6 and not 0") 

print("Last digit of", number, "is" , number % 10, status())

