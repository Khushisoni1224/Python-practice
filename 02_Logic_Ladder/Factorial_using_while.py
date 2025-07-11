# File : Factorial Problem

#Sample Input :
#Enter a number :5

#sample Output :
#Factorial of 5 at iteration 1 is 1
#Factorial of 5 at iteration 2 is 2
#Factorial of 5 at iteration 3 is 6
#Factorial of 5 at iteration 4 is 24
#Factorial of 5 at iteration 5 is 120
#
#Factorial of 5 is 120


num=int(input("Enter a number :"))
fact=1

for i in range (1,num+1):
    fact=fact*i
    print(f"Factorial of {num} at iteration {i} is {fact}")
print(" ")
print(f"Factorial of {num} is {fact}")
    