num=int(input("enter the nmuber:"))

count=0

if num==0:
    count = 1
else:
    while num > 0:
          num = num // 10
          count+=1

print("number of the values in the text is",count)