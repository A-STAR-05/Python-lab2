#merge a list an select and remove the common element
a=[1,2,3,4]
b,d=[2,3,4,7],[]
c=a+b
for i in c:
    if i  in b and i not in a or i not in b and i in a:

        d.append(i)
print("Merged list:", c)
print("Common elements:", d)