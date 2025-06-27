import array

arr=array.array('i',[1,2,2,4,2,6])

print(arr)
arr.append(7)
print(arr)
arr.remove(1)
print("removed value",arr)

arr.insert(2, 111)
print(arr)

print("counted value",arr.count(2))
print("sorted value",arr.sort())
