fact=int(input("enter the factorail value:.."))
rs=1
for i in range(1,fact+1):
    rs*=i

print(f"the factorail of {fact} is ..{rs}")