import string
import random

num=int(input("enter the length:"))
chaaracter=string.ascii_letters + string.digits + string.punctuation
rs=''.join(random.choices(chaaracter, k=num))

print(rs)