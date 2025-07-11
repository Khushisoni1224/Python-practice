
#Sample Input :
#Enter a number :123

#Sample Output :
#The number 123 is now reversed to 3 
#The number 123 is now reversed to 32 
#The number 123 is now reversed to 321 

num=int(input("Enter a number :"))
original=num
reverse=0

 #extract digits from the number until there are no digits left.
while num > 0 : 
    digit = num % 10 # to reverse a number we should first extract last digit of the number 
    reverse = reverse * 10 + digit
#Initially: reverse = 0, digit = 3 ⇒ reverse = 0*10 + 3 = 3
#Next: digit = 2 ⇒ reverse = 3*10 + 2 = 32
#Next: digit = 1 ⇒ reverse = 32*10 + 1 = 321
    num = num // 10 # To go to next adjacent earlier digit
    print(f"The number {original} is now reversed to {reverse} ")