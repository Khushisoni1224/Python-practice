# File: marks_classification.py
# Classify marks into pass, grace, or fail
# Sample Input: 33
# Sample Output: Grace Marks

marks = float(input("Enter the marks: "))
if marks > 35:
    print("Pass")
elif marks >= 30 and marks <= 35:
    print("Grace Marks")
elif marks < 30:
    print("Fail")