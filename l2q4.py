li=[]
for i in range(int(input('ENTER RANGE OF YR LIST'))):
    li.append(int(input(f'enter {i+1}th elemnt')))
               
             
while True:
    choice=input('enter your choice press the numbers for \n1.push\n2.pop\n3.enQue\n4.deque \n5.Pressig anything other than1-4 to quit')
    if int(choice)==1:
       
        li.append(  int(input("You have chosen to push,enter the element")))
        print(li,"is the list after pushing your element")
    elif int(choice)==2:
        print('you have chose to pop ,',li.pop())
    elif int(choice)==3:
        li.append(input("You have chosen to enQue, enter the element"))
        print(li, "is the list after enQueuing your element")
    elif int(choice)==4:
        print("You have chosen to deQueue, the element removed is:", li.pop(0))
    else:
        break


