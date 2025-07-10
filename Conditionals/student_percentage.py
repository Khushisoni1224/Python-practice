# File: student_percentage.py
# Classify student's result by percentage
# Sample Input: 67
# Sample Output: The student passed with First Class.

per = int(input("Enter the percentage scored by student: "))
print(per, "%")
if per >= 75:
    print("The student passed with Distinction.")
elif per > 60 and per < 75:
    print("The student passed with First Class.")
elif per > 50 and per < 60:
    print("The student passed with Second Class.")
elif per < 50:
    print("The student has failed.")
else:
    print("Better luck next time!!")