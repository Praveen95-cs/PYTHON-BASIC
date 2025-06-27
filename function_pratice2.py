#Write a function is_prime(n) that checks whether a number is prime and returns True or False.

def isprime(nu):
    for i in range(1,nu):
        count=0
        if nu%i==0:
            count+=1
        
    if count==1:
        print("True")
    else:
        print("False")

num=int(input("enter the number to check prime:"))

isprime(num)

