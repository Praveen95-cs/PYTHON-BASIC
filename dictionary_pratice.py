name={}

no=int(input("enter the no of student:"))

for i in range(no):
    studentname=input(f"\n enter the name of the student{i+1}::")
    reg_no=int(input("enter the reg no:"))
    maths=int(input("enter the maths mark:"))
    science=int(input("enter the science mark:"))
    cse=int(input("enter the cse mark:"))
    print("mark is more than 100")
    
    if maths > 100 or science > 100 or cse > 100:
       print("one of the mark is greater than 100...!")
       break

    name[studentname] = {
        "reg_no":reg_no,
        "maths":maths,
        "science":science,
        "cse":cse
        }
    
for studentname in name:
    print(f"Name of the student:",name[studentname])

    total=name[studentname]["maths"]+name[studentname]["science"]+name[studentname]["cse"]
    print(f"total mark =>> ",total)

    cutt_off=name[studentname]["maths"]/2+name[studentname]["science"]/2+name[studentname]["cse"]
    print(f"Cutt_off mark",cutt_off)



