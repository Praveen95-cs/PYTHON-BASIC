name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
dept = input("Enter department: ")

student = (name, roll, dept)

print("\nStudent Record:")
print("Name:", student[0])
print("Roll No:", student[1])
print("Department:", student[2])
