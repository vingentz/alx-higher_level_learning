#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
k = number
check = 0
if (k < 0):
    k *= -1
    check = 1
    digit = k % 10
if (check):
    digit *= -1
    k *= -1
if (digit > 5):
    print("Last digit of %d is %d and is greater than 5" % (k, digit))
elif (digit == 0):
    print("Last digit of %d is %d and is 0" % (k, digit))
elif (digit < 6 and digit != 0):
    print(f"Last digit of {k:d} is {digit:d} and is less than 6 and not 0")
