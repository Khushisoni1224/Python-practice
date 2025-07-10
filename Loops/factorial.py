# File: factorial.py
# Calculate factorial of a number using while loop
# Sample Input: 5
# Sample Output: 120

a = int(input("Enter a number: "))
fact = 1
i = 1
while i <= a:
    fact *= i
    i += 1
print("Factorial:", fact)
