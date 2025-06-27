#How can you dynamically delete a temperature value given by the user?

import array

arr=array.array('f',[])
sum=0.0
num=int(input("enter the number of elements"))
for i in range(num):
    value=float(input(f"enter the value of {i+1}:"))
    arr.append(value)

rem=int(input("enter the value to remove:"))
arr.remove(rem)
print("finally array is:",arr)