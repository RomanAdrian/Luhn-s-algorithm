from cs50 import get_int
import sys
from functools import reduce
import re

while True:
    cardnumber = get_int("What is your card number? \n")
    if cardnumber > 0:
        break
# American Express uses 15-digit numbers MasterCard uses 16-digit numbers Visa uses 13- and 16-digit numbers

sum_all = 0
cc = str(cardnumber) # turns int to a string

if len(cc) != 16 and len(cc) != 15 and len(cc) != 13:
    print("INVALID")

multiply_digits = list(map(lambda second: int(second) * 2, cc[-2::-2])) # [start:end:step]
filtered_multiply = list(filter(lambda x: x < 10, multiply_digits)) # if condition used implicitly
reduced_multiply = reduce(lambda a,b: int(a) + int(b), filtered_multiply)
check_doubles = list(map(lambda double: int(double) % 10 + int(double) // 10 if int(double) >= 10 else 0, multiply_digits)) # if it finds doubles it adds its product
reduced_doubles = reduce(lambda a,b: int(a) + int(b), check_doubles)
odd_digits = reduce(lambda a,b: int(a) + int(b), cc[::-2]) # iterates over the odd digits end to start

if sum_all + (reduced_multiply + reduced_doubles + odd_digits) % 10 == 0: # adds all digits
    if re.findall(r'3[47].*', cc):
        print("AMEX")
    elif re.findall(r'5[12345].*', cc):
        print("MASTERCARD")
    elif re.findall(r'4.*', cc):
        print("VISA")
    else:
        print("INVALID")
# American Express numbers start with 34 or 37 MasterCard numbers start with 51, 52, 53, 54, or 55 Visa numbers start with 4
