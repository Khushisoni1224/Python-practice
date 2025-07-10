# File: gcd_while_loop.py
# Find GCD of two numbers using while loop
# Sample Input: 24, 36
# Sample Output: 12

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
if a < b:
    small = a
else:
    small = b

i = 1
while i <= small:
    if a % i == 0 and b % i == 0:
        gcd = i
    i += 1
print("GCD is:", gcd)