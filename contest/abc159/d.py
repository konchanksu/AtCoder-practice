from collections import Counter

n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
b = sum((v - 1) * v // 2 for v in count.values())
for i in a:
    print(b + 1 - count[i])
