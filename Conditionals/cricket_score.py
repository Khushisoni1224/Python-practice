# File: cricket_score.py
# Classify cricket score performance
# Sample Input: 120
# Sample Output: Excellent Performance

score = int(input("Enter the score of cricket player: "))
if score < 50:
    print("Poor Performance")
elif score >= 50 and score <= 100:
    print("Good Performance")
elif score > 100:
    print("Excellent Performance")
else:
    print("Enter a valid score")