from collections import deque

queue =deque()

while True:
      print("queue",queue)
      print("1-enque")
      print("2-deque")
      print("3-exit")

      choice=input("enter the choice")
      
      if choice == '1':
            value=input("enter the to imput")
            print("enque value:",queue.append(value))

      elif choice == '2':
            print("deque",queue.popleft())

      elif choice =='3':
            print("exiting")
            break
      else:
            print("invaild")
