#Write a function find_max_min(lst) that takes a list of numbers and returns both the maximum and minimum values.
def max_min(lst1):

     m1 = lst1[0]
     m2 = lst1[0]

     for n in lst1:
        if m1 < n:
           m1 = lst1
        elif m2 > n:
             m2 = lst1   
        return m1,m2

nums=int(input("enter the number you want:.."))
lst1=[]
for i in range(nums):
    value=input("enter the value of list:")
    lst1.append(value)

print("max",max_min(lst1))

