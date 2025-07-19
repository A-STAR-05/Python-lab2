#with library functions
a,b=[],[]
n=int(input("Enter number of elements"))
for i in range(0,n):
    a.append(int(input(f"enter {i+1}th element")))
#First lets remove the duplicate 
for i in a:
    if i not in b:
        b.append(i)

print(b)
#now this non duplicated list is sorted 
for i in range(0,len(b)):
    for j in range(0,len(b)-i-1):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
            
print(b)
#max min:
print(f"MAXIMUM {b[-1]},min {b[0]}")