#Write a function frequency_counter(s) that takes a string and returns a dictionary with the count of each character.

def counter(s):
    f={}
    for char in s:
        if char in f:
             f[char]+=1
        else:
            f[char]=1

    return f



text = input("Enter a string: ")
result = counter(text)
print("Character frequencies:", result)
