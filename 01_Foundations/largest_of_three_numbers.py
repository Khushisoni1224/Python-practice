# File: Largest Of Three numbers 

# Sample Inputs
#Enter first number :22
#Enter second number :11
#Enter third number :77

# Sample outputs
#Third Number 77 is the largest of the three numbers 


num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
num3=int(input("Enter third number :"))

if num1>=num2 and num1>=num3 :
    print(f"First Number {num1} is the largest of the three numbers  ")
elif num2>=num1 and num2>=num3:
    print(f"Second Number {num2} is the largest of the three numbers ")
elif num3>=num1 and num3>=num2 :
    print(f"Third Number {num3} is the largest of the three numbers ")
else :
    print("Enter valid numbers ")
