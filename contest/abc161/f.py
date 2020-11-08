from collections import Counter

n = int(input()) 
times = 0

def make_divisors(n):
    divisors = [n]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors
    
times = len(make_divisors(n - 1))
a = make_divisors(n)

for i in a:
    tmp = n // i
    if tmp == 1:
        times += 1 
        continue
    while tmp % i == 0:
        tmp = tmp // i
    if tmp % i == 1:
        times += 1 
    
print(times if n != 2 else 1)
