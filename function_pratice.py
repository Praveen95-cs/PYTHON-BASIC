#Write a function calculate_square that accepts a number and returns its square.

no=int(input("enter the num"))

def square(n):
    square=n**2
    return square

print(f"Square of the {no} is ",square(no))