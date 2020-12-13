from math import sqrt, ceil
def prime(n):
    if n == 2:
        return True
    for i in range(2, ceil(sqrt(n) + 0.0001)):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(n, 2 * 10 ** 5):
    if prime(i):
        print(i)
        break

