
stack=[]

while True:

    print("\n Current Stack",stack)
    print("1-append")
    print("2-poped")
    print("3-peek")
    print("4-Exit")

    choice =input("enter your choice:")

    if choice =='1':
       value=input("enter the value")
       stack.append(value)

    elif choice =='2':
       if stack:
        print("poped:",stack.pop())
       else:
        print("no values")

    elif choice =='3':
        if stack:
           print("peek:",stack[-1])
        else:
           print("no values")

    elif choice == '4':
          print("Exiting...")
          break

    else:
        print("Invalid operation")
