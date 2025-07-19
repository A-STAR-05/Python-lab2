tup1=(1,2,3,4,1,1,2,3,4,4,9,9,9,9,9,9,4)
print("Mean=",sum(tup1)/len(tup1))
tup=list(set((tup1)))
tup.sort()
print(tup)
#med
if len(tup) % 2 == 0:
    med = (tup[len(tup)//2 - 1] + tup[len(tup)//2]) / 2
else:
    med = tup[len(tup)//2]
print("Median=", med)
#Mode
tup1=list(tup1)
count=0;
for i in tup:
    if tup1.count(i) > count:
        count = tup1.count(i)
        mode = i
print("Mode=", mode)    
