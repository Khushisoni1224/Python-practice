# File : Multiplication Table
#Sample Input : 
#Enter the number for which you want to create a table : 5
#Sample Output :
"""
The Table of 5 is :
5 x 1 =  5
5 x 2 =  10
5 x 3 =  15
5 x 4 =  20
5 x 5 =  25
5 x 6 =  30
5 x 7 =  35
5 x 8 =  40
5 x 9 =  45
5 x 10 =  50
"""

number=int(input("Enter the number for which you want to create a table : "))
while number != 0 :
    print(f"The Table of {number} is :")
    for i in range (1,11):
        mul=number*i
        print(f"{number} x {i} = ", mul)
    break
       
