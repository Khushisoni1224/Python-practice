#File : Even or Odd Number
# Enter a number :5
#5 is an ODD Number 
#----------------------------
#Enter a number :12
#12 is an EVEN Number 

num=int(input("Enter a number :"))

if num % 2 ==0:
    print(f"{num} is an EVEN Number ")
elif num%2 != 0 :
    print(f"{num} is an ODD Number ")
else :
    print("Enter a valid number ")