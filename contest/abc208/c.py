n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [(i, j) for i, j in enumerate(a)]

d = {}

count = k % n
ans = k // n
for item in sorted(b, key=lambda x: x[1]):
    if count == 0:
        break
    d[item] = True
    count -= 1

for item in sorted(b):
    if item in d:
        print(ans + 1)
    else:
        print(ans)
