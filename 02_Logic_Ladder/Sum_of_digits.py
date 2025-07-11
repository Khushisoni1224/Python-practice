# File : Sum Of the digits 

#Sample Input :
#Enter a number :1234

#Sample Outputs :
#The total of the number 4 is 4
#The total of the number 3 is 7
#The total of the number 2 is 9
#The total of the number 1 is 10


num=int(input("Enter a number :"))
original = num
total = 0

while num > 0 :
    digit = num % 10 #reverse the number 
    total = total + digit
    num = num // 10
    print(f"The total of the number {digit} is {total}")
    