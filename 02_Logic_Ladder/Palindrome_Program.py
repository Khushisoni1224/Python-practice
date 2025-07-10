# File : Palindrome Program

#Sample Input :
#Enter a number :121
#Enter a String : madam

#Sample Output :
#121 number is not a palindrome !
#madam is a Palindrome !

num=int(input("Enter a number :"))
string=input("Enter a String : ")

#to reverse the string we can use slice operator
reverse_num = str(num)[::-1]
reverse_string=string[::-1]

if (reverse_num == num ):
    print(f"{num} number is a palindrome !")
else :
    print(f"{num} number is not a palindrome !")

if (reverse_string == string) :
    print(f"{string} is a Palindrome !")
else:
    print(f"{string} is not a Palindrome !")