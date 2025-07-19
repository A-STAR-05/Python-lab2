#with library functions
a=[]
n=int(input("Enter number of elements"))
for i in range(0,n):
    a.append(int(input(f"enter {i+1}th element")))
print(f'The max is {max(a)},minimum is {min(a)}')
a.sort()
print(f'Sorted is {a}')
print(f"Non duplicated list is {list(set(a))}")