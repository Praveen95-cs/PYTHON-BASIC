
def add(list1):
    num=int(input("\n enter the no of task you want to add::"))
    for i in range(num):
        value=input("\n Enter Task :")
        list1.append(value)
    
print("\n Successfull add item")


def remove(list1):
    word=input("\n enter the value you want to remove:")
    list1.remove(word)
print("\n Successfully removed the elements")

def view(list1):
    print("\n TO DO LIST- ITEMS")
    if not list:
        print("\n no data...")
    else:
        for i, wr in enumerate(list1, start=1):
            print(f"{i}. {wr}")
print("\n successfully view all the items")


list1=[]

while True:

    print("1-View TO DO LIST")
    print("2- ADD LIST")
    print("3-REMOVE LIST")
    print("4-exit")

    choose=int(input(" enter your choice: "))

    if choose == 1:
        view(list1)
    elif choose ==2:
        add(list1)
    elif choose == 3:
        remove(list1)
    elif choose == 4:
        print("Exiting...")
        break
    else:
        print("Invalid Option")