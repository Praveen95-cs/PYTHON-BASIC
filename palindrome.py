num = int(input("enter the number:"))
first=num
rev=0

while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

if first==rev:
    print("the number is palindrome")
else:
    print("it is not a parlindrome.")
