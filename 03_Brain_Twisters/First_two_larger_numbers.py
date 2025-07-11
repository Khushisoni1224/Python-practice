#File : Finding the first two larger numbers

#sample Inputs :
#Enter the first number :10
#Enter the second number :25
#Enter the third number :40
#Enter the fourth number :35

#Sample Outputs :
#The first largest number is : 40
#The second largest number is :35


num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))
num4=int(input("Enter the fourth number :"))

#Initialize first and second
first=num1
second=float('-inf')

#Compare num2 
if num2>first :
    second=first
    first=num2
else:
    second=num2

#Compare num3
if num3>first :
    second=first
    first=num3
elif num3>second:
    second=num3

#Compare num4
if num4 >first :
    second=first
    first=num4
elif num4>second :
    second=num4

print(f"The first largest number is : {first}")
print(f"The second largest number is :{second}")
