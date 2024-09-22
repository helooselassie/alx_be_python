#!/usr/bin/env python3

# Prompt user for input
number = int(input("Enter a number to see its multiplication table: "))

# For loop to generate and print the multiplication table
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

