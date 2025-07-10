# File: greeting_by_time.py
# Time-based greeting
# Sample Input: 14
# Sample Output: GOOD AFTERNOON!!

hour = int(input("Enter the time (hour in 24hr format): "))
if hour > 24:
    print("Please enter a valid time")
elif hour >= 5 and hour < 12:
    print("GOOD MORNING!!")
elif hour >= 12 and hour < 17:
    print("GOOD AFTERNOON!!")
elif hour >= 17 and hour < 21:
    print("GOOD EVENING!!")
else:
    print("It's sleep time!!")
