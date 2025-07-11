#File Count the Vowels in a String

#Sample Input :
#Enter the string of Letters :abioueab

#Sample Output :
#Count of the vowels in the letters a is 1 
#The letter b is a Consonant ! 
#Count of the vowels in the letters i is 2 
#Count of the vowels in the letters o is 3 
#Count of the vowels in the letters u is 4 
#Count of the vowels in the letters e is 5 
#Count of the vowels in the letters a is 6 
#The letter b is a Consonant ! 
#Count : 6


letter=input("Enter the string of Letters :")
letters=letter
vowels=('a','e','i','o','u')
count = 0

for letters in letters :
    if letters in vowels:
        count=count+1
        print(f"Count of the vowels in the letters {letters} is {count} ")
    else :
        print(f"The letter {letters} is a Consonant ! ")
print(f"Count : {count}")
    
    

  
    
    
    
    
    