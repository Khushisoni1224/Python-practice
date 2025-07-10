#File : Prime Number between a range 

#Sample Output :
#Prime Numbers Between 1 to 50 
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 

print("Prime Numbers Between 1 to 50 ")

for number in range (2,51):
    is_prime=True
    
    for i in range (2,number):
        if number % i ==0 :
            is_prime=False
            break
    if is_prime :
        print(number , end=" ")