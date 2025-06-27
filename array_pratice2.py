import array

arr=array.array('i')

for i in range (5):
    value=int(input("enter the value to be added"))
    arr.append(value)


for i in range (5):
    print(arr[i]**2)


