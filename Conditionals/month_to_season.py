# File: month_to_season.py
# Convert month number to season
# Sample Input: 3
# Sample Output: Spring

month = int(input("Enter the month number (1-12): "))
if month > 12:
    print("Enter a valid month")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
elif 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")