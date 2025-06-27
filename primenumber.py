num=int(input("enter the value:")) 
count=0

for i in range(1,num):
    if num%i==0:
        count+=1
    
if count == 1:
    print("the number is prime")

else:
    print("the number is not prime")