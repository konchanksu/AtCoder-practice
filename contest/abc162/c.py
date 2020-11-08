# from fractions import gcd
from math import gcd
k = int(input())

ans = 0

for i in range(1, k + 1):
    for j in range(i + 1, k + 1):
        ans += gcd(i, j)
        for t in range(j + 1, k + 1):
            ans += gcd(gcd(i, j), t)

ans *= 6
ans += sum([i for i in range(1, k + 1)])
print(ans)
