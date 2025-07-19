import random as rand
rset=set()
for i in range(10):
    rset.add(rand.randint(1, 100))
print("Random set:", rset)
print("Sorted set:", sorted(rset))
print("AFTER REMOVING Maximum:", rset-set([max(rset)]))
print("AFTER REMOVING Minimum:", rset-set([min(rset)]))
