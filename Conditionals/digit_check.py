# Folder: 01_conditionals
# File: digit_check.py
# Program to check if number is single, double, or triple digit
# Sample Input: 45
# Sample Output: The number is double digit.

a = int(input("Enter a number: "))
print(a)
if a < 10:
    print("The given number is a single digit.")
elif a >= 10 and a < 100:
    print("The number is double digit.")
elif a >= 100 and a < 1000:
    print("The number is of three digits.")
else:
    print("Enter a valid number.")