# File : Type of number (Positive / Negative / Zero)

#Sample Input : Enter a number:-2
#Sample Output : -2 is a Negative Number 

#Sample Input : Enter a number:5
#Sample Output : 5 is a Positive Number 

num=int(input("Enter a number:"))

if num == 0 :
    print(f"{num} is Zero !")
elif num > 0 :
    print(f"{num} is a Positive Number ")
elif num < 0 :
    print(f"{num} is a Negative Number ")
else :
    print("Enter a valid number ")