# File: Sum of all Numbers

# FOR Loop
#Sample Input : Enter a number : 3
#Sample Output : The sum all the numbers starting from 0 to 3 is 6

num=int(input("Enter a number : "))
sum=0
for i in range (0,num+1):
    sum=sum+i
    
print(f"The sum all the numbers starting from 0 to {num} is" , sum )

#-------------------------------------------------------

#WHILE Loop
#Sample Inputs :Enter a number : 7
#Sample Outputs : The sum all the numbers starting from 0 to 7 is:  28

number=int(input("Enter a number : "))
summation=0
j=0
while j in range (0,number+1):
    summation=summation+j
    j=j+1
print(f"The sum all the numbers starting from 0 to {number} is: ",summation)



    