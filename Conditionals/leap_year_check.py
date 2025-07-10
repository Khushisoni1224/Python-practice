# File: leap_year_check.py
# Determine if a year is leap, century, or normal year
# Sample Input: 2000
# Sample Output: It's a century and a leap year.

year = int(input("Enter the year: "))
print(year)
if year % 400 == 0:
    print("It's a century and a leap year.")
elif year % 4 == 0:
    print("It's a leap year.")
else:
    print("It's a normal year.")