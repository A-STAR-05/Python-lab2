li=[]
for i in range(int(input('ENTER RANGE OF YR LIST'))):
    li.append(int(input(f'enter {i+1}th elemnt')))
print("List :",li)
li=set(li)
print("Set",li)
li=list(li)
li.sort()
print("Sorted List :",li)
