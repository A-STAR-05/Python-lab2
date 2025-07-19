import random as rand
li = []
prime = []

for i in range(10):
    li.append(rand.randint(1, 10))

for index in range(0, 10, 2):  
    num = li[index]
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)

print("List of random numbers:", li)
print("List of prime numbers at even indices:", prime)
                
    

    
