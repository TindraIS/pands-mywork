'''
-----------------------------------------------------------------
Name: lab3.1.5.randomfruit.py
Description: Prints out a random fruit 
Author: Irina Simoes
Date created: 15/02/2024
-----------------------------------------------------------------
'''
import random

fruits = ('Apple', 'Pear', 'Orange', 'Pineapple')
#print(len(fruits))

generator = random.randint(0,len(fruits)-1)

fruit = fruits[generator]

print(f'A random fruit: {fruit}')
