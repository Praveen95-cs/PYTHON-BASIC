# file opening and reading

file=open("just_read.txt","r")
value=file.readlines()
print(value)
file.close()

fil=open("just_read.txt","w")
fil.write("\n hello world praveen is a good boy")
print("completed")

fil.close()

fi=open("just_read.txt","a")
fi.write("hello 9999999900000")
print("completed")

fi.close()
