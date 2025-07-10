# File: odd_even_size.py
# Classify number as even/odd and small/large
# Sample Input: 22
# Sample Output: Even and Large

num = int(input("Enter the number: "))
if num % 2 == 0 and num < 20:
    print("Even and Small")
elif num % 2 != 0 and num < 20:
    print("Odd and Small")
elif num % 2 == 0 and num >= 20:
    print("Even and Large")
elif num % 2 != 0 and num >= 20:
    print("Odd and Large")
