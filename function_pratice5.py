#Write a function count_vowels(s) that takes a string and returns the number of vowels in it.

def countv(str1):
    count=0

    for n in str1:

       if 'a' or 'A' in str:
          count+=1
       elif 'e' or 'E' in str:
        count+=1
       elif 'i' or 'E' in str:
        count+=1 
       elif 'o' or 'O' in str:
         count+=1
       elif 'u' or 'U' in str:
         count+=1 

    return count

str1=input("enter the string:")
print("no of count:",countv(str1))



