# File: temperature_check.py
# Classify temperature into freezing, cold, warm, or hot
# Sample Input: 27
# Sample Output: WARM

temperature = float(input("Enter the temperature: "))
print(temperature)
if temperature < 0:
    print("Freezing")
elif temperature >= 0 and temperature < 15:
    print("COLD")
elif temperature >= 15 and temperature < 30:
    print("WARM")
elif temperature >= 30:
    print("HOT")