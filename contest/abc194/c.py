from collections import Counter

n = int(input())
a = list(map(int, input().split()))
ans = 0

c = Counter(a)
for i in range(-200, 201):
    for j in range(i, 201):
        if not c.get(i) or not c.get(j):
            continue
        ans += c[i] * c[j] * (i - j) ** 2
print(ans)


