from collections import Counter

n = int(input())
a = list(map(int, input().split()))

ans = n * (n-1) // 2

count = dict(Counter(a)).values()

for i in count:
    ans -= (i-1) * i // 2
print(ans)
