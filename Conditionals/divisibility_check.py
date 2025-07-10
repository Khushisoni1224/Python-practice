# File: divisibility_check.py
# Check divisibility by 5 and/or 10
# Sample Input: 20
# Sample Output: The number is divisible by both 5 and 10

num = int(input("Enter a number: "))
if num % 5 == 0 and num % 10 == 0:
    print("The number is divisible by both 5 and 10")
elif num % 5 == 0:
    print("The number is divisible by 5")
elif num % 10 == 0:
    print("The number is divisible by 10")
else:
    print("The number is not divisible by 5 or 10")