#Write a program that takes 10 integer inputs and stores them in an array. Then print only even numbers
import array

arr=array.array('i',[])

num=int(input("enter the number of elements"))
for i in  range(num):
    value=int(input(f"enter the value of {i+1}:"))
    arr.append(value)

print("\n even values are")
for i in range(num):
    if(arr[i]%2==0):
        print(arr[i])
