#Add 5 movie names from user input and print only those that start with the letter 'A'.

l=[]
n=int(input("enter the value of the iteration:"))

for i in range(n):
    value=input("enter the value to be inserted")
    l.append(value)

print("\n\n")
print(l)

for mn in l:
    if mn.startswith('A'):
        print(mn)
