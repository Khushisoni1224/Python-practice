# File: pyramid_pattern.py
# Print center-aligned pyramid of stars
# Sample Input: 4
# Sample Output:
#    *
#   ***
#  *****
# *******

rows = int(input("Enter the number of rows: "))
i = 1
while i <= rows:
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
    i += 1