#How would you calculate the average of all values stored in a float array?

import array

arr=array.array('f',[])
sum=0.0
num=int(input("enter the number of elements"))
for i in range(num):
    value=float(input(f"enter the value of {i+1}:"))
    arr.append(value)
    sum=sum+value

    avg=sum/num


print("average of the above sequence:",avg)
