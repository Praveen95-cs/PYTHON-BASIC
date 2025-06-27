#Take a list of numbers and sort them in descending order.

l=[]
n=int(input("enter the value of the iteration:"))

for i in range(n):
    value=input(f"enter the value to be inserted:")
    l.append(value)

l.sort(reverse=True)
print("sorted list",l)

l.pop(2)
print(l)