#Write a function sum_even_numbers(lst) that takes a list of integers and returns the sum of all even numbers in the list.

def even(box):
    sum=0
    for i in box:
        if i%2==0:
            sum+=i

    return sum
    

box=[]
n=int(input("enter the no of elements:"))
for i in range(n):
    value=int(input(f"enter the no :{i+1} "))
    box.append(value)

print(f"Sum of values is ::",even(box))

