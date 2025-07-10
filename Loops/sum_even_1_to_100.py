# File: sum_even_1_to_100.py
# Find sum of all even numbers from 1 to 100
# Sample Output: 2550

i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print("Sum of even numbers:", sum)