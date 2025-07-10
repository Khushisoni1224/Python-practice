# File: square_pattern.py
# Print square pattern of stars
# Sample Input: 3
# Sample Output:
# * * *
# * * *
# * * *

rows = int(input("Enter the number of rows: "))
i = 1
while i <= rows:
    print("* " * rows)
    i += 1