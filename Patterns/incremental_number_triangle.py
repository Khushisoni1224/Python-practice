# File: incremental_number_triangle.py
# Print triangle of incrementing numbers
# Sample Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1