#Write a function check_palindrome(word) that takes a string as input and returns True if the word is a palindrome (reads the same forward and backward), otherwise returns False.

def palindrome(str):
    text=str.lower()
    if(str==str[::-1]):
        print("the string is palindrome!")
    else:
         print("the string is not a palindrome!")  

str=input("enter the string:")
palindrome(str)