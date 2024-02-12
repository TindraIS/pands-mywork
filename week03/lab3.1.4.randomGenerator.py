'''
-----------------------------------------------------------------
Name: lab3.1.4.randomGenerator.py
Description: Prints out a random number between 1 and 10. 
Author: Irina Simoes
Date created: 12/02/2024
-----------------------------------------------------------------
'''
import random

range = input("Enter a range, eg. 1-10: ")
range_first = range.split("-")[0]
print(range_first)
range_second = range.split("-")[1]
print(range_second)

number = random.randint(int(range_first),int(range_second))
print("Here is a random number {}".format(number))